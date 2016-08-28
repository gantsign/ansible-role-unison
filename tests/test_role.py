from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_unison(Sudo, Command, File):
    with Sudo('vagrant'):
        # Clean up any previous runs
        Command('rm /vagrant/home/included/test1')
        Command('rm /vagrant/home/included/excluded/test2')
        Command('rm /vagrant/home/includeme')
        Command('rm /vagrant/home/excludeme')

        # Setup test directories and files
        assert Command('mkdir -p /home/vagrant/included/excluded').rc == 0
        assert Command('touch /home/vagrant/included/test1').rc == 0
        assert Command('touch /home/vagrant/included/excluded/test2').rc == 0
        assert Command('touch /home/vagrant/includeme').rc == 0
        assert Command('touch /home/vagrant/excludeme').rc == 0

    # Run Unison
    # Note: have to run sudo with `--set-home` or Unison will
    # attempt to write its log file to `/root`.
    cmd = Command('sudo --user vagrant --set-home unison vagrant')
    assert cmd.rc == 0

    with Sudo('vagrant'):
        # Verify
        assert File('/vagrant/home/included/test1').is_file
        assert not File('/vagrant/home/included/excluded/test2').exists
        assert File('/vagrant/home/includeme').is_file
        assert not File('/vagrant/home/excludeme').exists

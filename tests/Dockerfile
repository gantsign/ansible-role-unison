FROM ubuntu:16.04

# Update apt
RUN apt-get -qq update

# Install sudo
RUN apt-get -qq -y install sudo
RUN sudo -V

# Install ansible
RUN apt-get -qq -y install ansible

# Configure test user
RUN useradd --home /home/vagrant vagrant
RUN bash -c "echo 'vagrant ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/vagrant"
RUN mkdir -p /home/vagrant/.ansible/tmp
RUN chown root:root /home
RUN chmod 'u=rwx,go=rx' /home
RUN chown -R vagrant:vagrant /home/vagrant
RUN chmod -R 'u=rwx,go=rx' /home/vagrant
RUN mkdir -p /vagrant
RUN chown -R vagrant:vagrant /vagrant
RUN chmod -R 'u=rwx,go=rx' /vagrant

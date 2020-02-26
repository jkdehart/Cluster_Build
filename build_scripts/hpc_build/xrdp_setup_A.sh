rpm -Uvh "https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm"
yum update

yum -y install xrdp tigervnc-server
systemctl start xrdpreb
systemctl enable xrdp

firewall-cmd --permanent --add-port=3389/tcp
firewall-cmd --reload

chcon --type=bin_t /usr/sbin/xrdp
chcon --type=bin_t /usr/sbin/xrdp-sesman

# creates user
sudo useradd sshtunnel -m -d /home/sshtunnel -s /bin/true

echo "SET USER PASSWORD"
sudo passwd sshtunnel

echo "Add these lines to the end of /etc/ssh/ssh_config file:"

echo '
Match User sshtunnel
    AllowTcpForwarding yes
    X11Forwarding no
    AllowAgentForwarding no
    ForceCommand /bin/false
'

# read -p "Press enter to continue"
printf "%s " "Press enter to continue"
read ans


sudo vim /etc/ssh/ssh_config



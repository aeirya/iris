from util.config_reader import read_config
import subprocess

def connect_as_server(config):
    ssh_port, user, ip, local_port = config['ssh-port'], config['relay-user'], config['relay-ip'], config['local-port']
    relay_port = 12000 # todo: fetch the port from relay server
    
    cmd = f'ssh -p {ssh_port} -f -N -R {relay_port}:localhost:{local_port} {user}@{ip}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate()


config = read_config('ssh.config')
connect_as_server(config)
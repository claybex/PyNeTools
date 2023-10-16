import paramiko, getpass, os

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Output ---') 
        print('\n'.join(line.strip() for line in output))
    
ip = os.environ["IP"]
port = '22'
cmd = 'ls -la'
user = 'max'
passwd = getpass.getpass()

ssh_command(ip, port, user, passwd, cmd)


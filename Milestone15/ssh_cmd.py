


import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    x = False
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user,password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output :
        print('--- Output ---')
        for line in output:
            print(line.strip())

#passwdfeld = tk.Entry(root, textvariable=passwdfeld_wert, show="*")

if __name__ == '__main__' :
    import getpass
    #user = getpass.getuser()
    user = input('Username: ')
    #password = getpass.getpass()
    password = input('Password: ')

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)

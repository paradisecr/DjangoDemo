import paramiko


if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("server_ip", 22, "user_name", "passwd")
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.read())
    ssh.close()

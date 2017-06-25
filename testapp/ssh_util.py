import paramiko


if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("127.0.0.1", 22, "caorui", "457964183")
    stdin, stdout, stderr = ssh.exec_command("ls")
    print(stdout.read())
    ssh.close()

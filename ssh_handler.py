import paramiko


class ssh_login:
    def __init__(self, server_host: str, server_username: str, server_pass: str, command):
        self.server_host = server_host
        self.server_username = server_username
        self.server_pass = server_pass
        self.command = command
        self.result_data = {}

    def run(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh_client.connect(hostname=self.server_host, port=22,
                               username=self.server_username, password=self.server_pass)
        except paramiko.AuthenticationException:
            print("incrrect username or password")
        except paramiko.SSHException as ssh_ex:
            print(f"ssh connection error: {ssh_ex}")

        _, stdout, stderr = ssh_client.exec_command(command=self.command)
        # print(stdout.readline())
        # print(stderr.readline())
        if stderr.readline() == "":
            aaa = stdout.readline().replace("\n", "")
            print(type(aaa))
            return (aaa)
        else:
            raise RuntimeError("couldn not get status")


if __name__ == "__main__":
    command = ""
    instance = ssh_login("host", "hoge", "hoge", command)
    instance.run()

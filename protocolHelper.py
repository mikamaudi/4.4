class Protocol:

    @staticmethod
    def get_msg(thesocket):
        data = b''
        while not b'\r\n\r\n' in data:
            data += thesocket.recv(1024)

        msg_parts = data.split(b"\r\n\r\n")
        headers = msg_parts[0].decode().split("\r\n")
        cmd = headers[0]

        # if all message read...
        for header in headers[1:]:
            if "Content-Length:" in header:
                length = int(header.split(" ")[1])
                while len(msg_parts[1]) < length:
                    msg_parts[1] += thesocket.recv(length - len(msg_parts[1]))


        #return results:
        return cmd, headers[1:], msg_parts[1] #cmd(first header), headers, data

    def check_msg(data: str):
        # GET <url> HTTP/1.1
        cmd_parts = data.split(" ")
        if len(cmd_parts) == 3 and cmd_parts[0] == "GET" and cmd_parts[2] == "HTTP/1.1":
            return True, cmd_parts[1], "GET"
        return False, None, None



class Message:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.text = ""

    def append_text(self):
        append_str = input("请输入你想要加入的一行文本:\n")
        self.text += append_str

    def to_string(self):
        message = "From:" + self.sender + '\n' + "To:" + self.receiver + '\n' + self.text
        print(message)


if __name__ == '__main__':
    sender = input("请输入发送人的姓名:\n")
    receiver = input("请输入收信人的姓名:\n")
    message = Message(sender=sender, receiver=receiver)
    message.append_text()
    message.to_string()

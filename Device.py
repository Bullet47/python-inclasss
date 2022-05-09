class Device:

    def __init__(self):
        self.Address = ""
        self.ESSID = ""
        self.Mode = ""
        self.Channel = ""
        self.Signal = ""
        self.Quality = ""
        self.Encryption = ""


if __name__ == '__main__':
    list_device = []  # 创建一个对象列表
    filename = "scan.txt"
    i = 1  # 第几个cell
    nl = 0  # 第几行
    with open(filename) as f:
        for line in f.readlines():
            if not line.isspace():  # 忽略空行
                list_line_space = line.split(" ")
                list_line_colon = line.split(":")
                if nl == 0:
                    device = Device()  # 声明一个Device对象
                    device.Address = list_line_space[4][:-1]  # list_line_space[4]是一个字符串，然后再对这个字符串[:-1]
                elif nl == 1:
                    device.ESSID = list_line_colon[1][1:-1]  # list_line_colon[1]是一个字符串，然后再对字符串取[1:-1]
                elif nl == 2:
                    device.Mode = list_line_colon[1].split(" ")[1]
                    device.Channel = list_line_colon[2][1:-1]
                elif nl == 3:
                    device.Signal = list_line_colon[1].split(" ")[1] + " " + list_line_colon[1].split(" ")[2]
                    device.Quality = list_line_colon[2][1:-1]
                elif nl == 4:
                    device.Encryption = list_line_colon[1][1:-1]
                    i += 1
                    list_device.append(device)
                nl = (nl + 1) % 5

        print("Address            ESSID                Mode    Channel  Signal    Quality  Encryption")
        for device in list_device:
            print('{:<19}{:<21}{:<8}{:<9}{:<10}{:<9}'.format(device.Address, device.ESSID, device.Mode,
                                                             device.Channel, device.Signal, device.Quality),
                  end="")
            print(device.Encryption)

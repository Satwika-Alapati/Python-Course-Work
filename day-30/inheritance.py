class whatsappsV1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp-v1 {self.name}!")
    def messaging(self):
        print("You can send messages")

class whatsappsV2:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp-v2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

satwika=whatsappsV1('sajid')
satwika.messaging()

akki=whatsappsV2('mahesh')
akki.messaging()
akki.calls()
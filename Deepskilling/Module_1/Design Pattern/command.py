class Light:
    def turn_on(self):
        print("Light ON")
    def turn_off(self):
        print("Light OFF")

class LightOnCommand:
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turn_on()

class LightOffCommand:
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def set_command(self, command):
        self.command = command
    def press_button(self):
        self.command.execute()
light = Light()

remote = RemoteControl()
remote.set_command(LightOnCommand(light))
remote.press_button()
remote.set_command(LightOffCommand(light))
remote.press_button()
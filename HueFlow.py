from phue import Bridge

b = Bridge('192.168.1.10')
# If the app is not registered and the button is not pressed, press the button and call connect()
# (this only needs to be run a single time)
b.connect()
# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()
# Get a dictionary with the light id as the key
lights = b.get_light_objects('id')

blue = [25, 46920]
blueHigh = [255, 46920]
yello = [255, 12750]
green = [255, 25500]
purple = [255, 56100]


def huey(huey):
    lights_list = b.get_light_objects('list')
    for light in lights_list:
        light.on = True
        light.brightness = huey[0]
        light.hue = huey[1]
        light.transitiontime = 5


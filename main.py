def on_bluetooth_connected():
    basic.show_string("D")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_forever():
    bluetooth.uart_write_number(input.temperature() * 1000 + input.light_level())
    basic.pause(2000)
basic.forever(on_forever)

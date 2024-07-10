bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showString("D")
})
basic.forever(function on_forever() {
    bluetooth.uartWriteNumber(input.temperature() * 1000 + input.lightLevel())
    basic.pause(2000)
})

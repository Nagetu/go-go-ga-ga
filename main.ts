basic.showString("python begins")
basic.showLeds(`
    . . # # .
    . # . . #
    . . # # .
    . # . . #
    . . # # .
    `)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Snake)
})

basic.show_string("python begins")
basic.show_leds("""
    . . # # .
    . # . . #
    . . # # .
    . # . . #
    . . # # .
    """)

def on_forever():
    basic.show_icon(IconNames.SNAKE)
basic.forever(on_forever)

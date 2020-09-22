def on_button_pressed_a():
    global Teller
    if True:
        music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
        basic.show_leds("""
            . # . # .
            . . . . .
            # . . . #
            # . . . #
            . # # # .
            """)
        basic.pause(1000)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    Teller += 1
    basic.show_string("" + str((Teller)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Teller
    if True:
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
        basic.show_leds("""
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            # . . . #
            """)
        basic.pause(1000)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    Teller += -1
    basic.show_string("" + str((Teller)))
input.on_button_pressed(Button.B, on_button_pressed_b)

Teller = 0
Teller = 0
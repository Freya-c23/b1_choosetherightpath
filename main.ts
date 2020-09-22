input.onButtonPressed(Button.A, function () {
    if (true) {
        music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
        basic.showLeds(`
            . # . # .
            . . . . .
            # . . . #
            # . . . #
            . # # # .
            `)
        basic.pause(1000)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    Teller += 1
    basic.showString("" + (Teller))
})
input.onButtonPressed(Button.B, function () {
    if (true) {
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        basic.showLeds(`
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            # . . . #
            `)
        basic.pause(1000)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    Teller += -1
    basic.showString("" + (Teller))
})
let Teller = 0
Teller = 0

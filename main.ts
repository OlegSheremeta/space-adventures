control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_BUTTON_EVT_UP, function () {
    if (start == true) {
        if (x != 0) {
            x += -1
            music.playTone(988, music.beat(BeatFraction.Sixteenth))
        }
    }
    control.waitMicros(3000)
    control.waitMicros(3000)
})
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_AB, EventBusValue.MICROBIT_BUTTON_EVT_DOWN, function () {
    if (start == true) {
        music.playTone(294, music.beat(BeatFraction.Sixteenth))
        eneX = x
        eneY = 4
        eneAct = 1
        for (let index = 0; index < 5; index++) {
            led.plot(eneX, eneY)
            led.unplot(eneX, eneY + 1)
            music.playTone(698, music.beat(BeatFraction.Sixteenth))
            control.waitMicros(5120)
            eneY += -1
            basic.pause(100)
        }
        eneAct = 0
        led.unplot(eneX, 0)
    } else {
        start = true
    }
    basic.pause(15)
})
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_B, EventBusValue.MICROBIT_BUTTON_EVT_UP, function () {
    if (start == true) {
        if (x != 4) {
            x += 1
            music.playTone(988, music.beat(BeatFraction.Sixteenth))
        }
    }
    control.waitMicros(3000)
    control.waitMicros(3000)
})
let score = 0
let cancel = 0
let astY = 0
let eneAct = 0
let eneY = 0
let eneX = 0
let x = 0
let start = false
power.lowPowerRequest()
power.fullPowerOn(FullPowerSource.A)
power.fullPowerOn(FullPowerSource.B)
start = false
x = 2
let astX = 1
eneX = 3
eneY = 4
eneAct = 0
music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
led.plot(x, 4)
control.waitMicros(3000)
basic.forever(function () {
    if (start == true) {
        led.plot(x, 4)
        led.unplot(x + 1, 4)
        led.unplot(x - 1, 4)
    }
    if (astY == eneY && astX == eneX && eneAct == 1) {
        cancel = 1
    }
    control.waitMicros(5000)
})
loops.everyInterval(3000, function () {
    if (start == true) {
        music.playTone(349, music.beat(BeatFraction.Sixteenth))
        astX = randint(0, 4)
        astY = 0
        for (let index = 0; index < 5; index++) {
            if (cancel == 1) {
                music.playTone(880, music.beat(BeatFraction.Sixteenth))
                control.waitMicros(5120)
                cancel = 0
                eneAct = 0
                score += 1
                break;
            }
            led.plot(astX, astY)
            led.unplot(astX, astY - 1)
            music.playTone(523, music.beat(BeatFraction.Sixteenth))
            astY += 1
            basic.pause(500)
        }
        led.unplot(astX, 4)
        if (astY == 4) {
            basic.showNumber(score)
            basic.pause(5000)
            control.reset()
        }
    }
    control.waitMicros(5000)
})

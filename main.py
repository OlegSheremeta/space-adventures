def on_microbit_id_button_ab_evt_up():
    global eneX, eneY, eneAct, start
    if start == True:
        music.play_tone(294, music.beat(BeatFraction.SIXTEENTH))
        eneX = x
        eneY = 4
        eneAct = 1
        for index in range(5):
            led.plot(eneX, eneY)
            led.unplot(eneX, eneY + 1)
            music.play_tone(698, music.beat(BeatFraction.SIXTEENTH))
            control.wait_micros(5120)
            eneY += -1
            basic.pause(100)
        eneAct = 0
        led.unplot(eneX, 0)
    else:
        start = True
    basic.pause(15)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_AB,
    EventBusValue.MICROBIT_BUTTON_EVT_UP,
    on_microbit_id_button_ab_evt_up)

def on_microbit_id_button_a_evt_down():
    global x
    if start == True:
        if x != 0:
            x += -1
            music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
    control.wait_micros(3000)
    control.wait_micros(3000)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_DOWN,
    on_microbit_id_button_a_evt_down)

def on_microbit_id_button_b_evt_down():
    global x
    if start == True:
        if x != 4:
            x += 1
            music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
    control.wait_micros(3000)
    control.wait_micros(3000)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_BUTTON_EVT_DOWN,
    on_microbit_id_button_b_evt_down)

score = 0
cancel = 0
astY = 0
eneAct = 0
eneY = 0
eneX = 0
x = 0
start = False
power.low_power_request()
power.full_power_on(FullPowerSource.A)
power.full_power_on(FullPowerSource.B)
start = False
x = 2
astX = 1
eneX = 3
eneY = 4
eneAct = 0
music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
led.plot(x, 4)
control.wait_micros(3000)

def on_forever():
    global cancel
    if start == True:
        led.plot(x, 4)
        led.unplot(x + 1, 4)
        led.unplot(x - 1, 4)
    if astY == eneY and astX == eneX and eneAct == 1:
        cancel = 1
    control.wait_micros(5000)
basic.forever(on_forever)

def on_every_interval():
    global astX, astY, cancel, eneAct, score
    if start == True:
        music.play_tone(349, music.beat(BeatFraction.SIXTEENTH))
        astX = randint(0, 4)
        astY = 0
        for index2 in range(5):
            if cancel == 1:
                music.play_tone(880, music.beat(BeatFraction.SIXTEENTH))
                control.wait_micros(5120)
                cancel = 0
                eneAct = 0
                score += 1
                break
            led.plot(astX, astY)
            led.unplot(astX, astY - 1)
            music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
            astY += 1
            basic.pause(500)
        led.unplot(astX, 4)
        if astY == 4:
            basic.show_number(score)
            basic.pause(5000)
            control.reset()
    control.wait_micros(5000)
loops.every_interval(3000, on_every_interval)

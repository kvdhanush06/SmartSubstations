from flask import Blueprint, render_template

views = Blueprint("views", __name__)

led1 = LED(4)
led2 = LED(15)
led3 = LED(24)
led4 = LED(25)
led5 = LED(7)
led6 = LED(12)
led7 = LED(16)
led8 = LED(21)

switch1 = Button(2)
switch2 = Button(17)
switch3 = Button(22)
switch4 = Button(10)
switch5 = Button(11)
switch6 = Button(5)
switch7 = Button(13)
switch8 = Button(26)

led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
led6.off()
led7.off()
led8.off()

flag1 = True
flag2 = True
flag3 = True
flag4 = True
flag5 = True
flag6 = True
flag7 = True
flag8 = True


@views.route("/")
def home():
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8
    # while True:
    # if button.is_pressed and not(flag):
    # red.on()
    # flag = True
    # print("RED Light On")
    # return render_template('home.html', click_button=flag)
    # elif button.is_pressed and flag:
    # red.off()
    # flag = False
    # print("RED Light Off")
    # print(flag)
    return render_template('home.html', click_button1=flag1, click_button2=flag2, click_button3=flag3, click_button4=flag4, click_button5=flag5, click_button6=flag6, click_button7=flag7, click_button8=flag8)


@views.route("/get_button_state", methods=['GET'])
def get_button_state():
    global flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8

    if switch1.is_pressed and flag1:
        flag1 = False
        led1.on()
    elif switch1.is_pressed and not flag1:
        flag1 = True
        led1.off()
    if switch2.is_pressed and flag2:
        flag2 = False
        led2.on()
    elif switch2.is_pressed and not flag2:
        flag2 = True
        led2.off()
    if switch3.is_pressed and flag3:
        flag3 = False
        led3.on()
    elif switch3.is_pressed and not flag3:
        flag3 = True
        led3.off()
    if switch4.is_pressed and flag4:
        flag4 = False
        led4.on()
    elif switch4.is_pressed and not flag4:
        flag4 = True
        led4.off()
    if switch5.is_pressed and flag5:
        flag5 = False
        led5.on()
    elif switch5.is_pressed and not flag5:
        flag5 = True
        led5.off()
    if switch6.is_pressed and flag6:
        flag6 = False
        led6.on()
    elif switch6.is_pressed and not flag6:
        flag6 = True
        led6.off()
    if switch7.is_pressed and flag7:
        flag7 = False
        led7.on()
    elif switch7.is_pressed and not flag7:
        flag7 = True
        led7.off()
    if switch8.is_pressed and flag8:
        flag8 = False
        led8.on()
    elif switch8.is_pressed and not flag8:
        flag8 = True
        led8.off()
    return jsonify({"click_button1": flag1, "click_button2": flag2, "click_button3": flag3, "click_button4": flag4, "click_button5": flag5, "click_button6": flag6, "click_button7": flag7, "click_button8": flag8})

import os
import sys


def commands(bridge):
    while True:
        Subcommand = input('>').split(' ')
        if Subcommand[0] == "exit":
            break
        elif Subcommand[0] == "?":
            helpToString()
        elif Subcommand[0] == "show":
            os.system("mstpctl showbridge")
        elif checkSame(Subcommand):
            runOSComands(Subcommand, bridge)


def helpToString():
    print("spanning tree mode <MODE> {stp|rstp|mstp}\n"
          "spanning tree timer hello-time <TIME> (1<TIME<10) \n"
          "spanning tree max-hope <HOPE> (6<HOPE<40) \n"
          "spanning tree max-age <AGE> (6<AGE<40) \n"
          "spanning tree port-cost <PORT> <COST> ( PORT(interface name)) \n"
          "show (show your bridge details")


def successToString():
    print("[OK] execution command success")


def runOSComands(commands, bridge):
    if commands[2] == "mode":
        if validProtocol(commands[3]):
            os.system("mstpctl setforcevers " + bridge + " " + commands[3])
            successToString()
    elif commands[2] == "timer" and commands[3] == "hello-time":
        if checkParameterRange(commands[3], commands[4]):
            os.system("mstpctl sethello " + bridge + " " + commands[4])
            successToString()

    elif commands[2] == "max-hope":
        if checkParameterRange(commands[2], commands[3]):
            os.system("mstpctl setmaxhops " + bridge + " " + commands[3])
            successToString()

    elif commands[2] == "max-age":
        if checkParameterRange(commands[2], commands[3]):
            os.system("mstpctl setmaxage " + bridge + " " + commands[3])
            successToString()

    elif commands[2] == "port-cost":
        os.system("mstpctl setportpathcost " + bridge + " " + commands[3] + commands[4])
        successToString()

    else:
        print("[ERROR] Syntax ERROR please check your option command enter ? for more help")


def validProtocol(proto):
    if proto == "stp" or proto == "mstp" or proto == "rstp":
        return True
    else:
        print("[ERROR] invalid protocol! enter valid protocol : stp | rstp | mstp")


def checkSame(comand):
    if comand[0] == "spanning" and comand[1] == "tree":
        return True
    else:
        print("[ERROR] Syntax ERROR Do you mean spanning tree?")
        return False


def checkParameterRange(parameter, range):
    try:
        if parameter == "max-hope" or parameter == "max-age":
            if 40 > int(range) > 6:
                return True
            else:
                print("[ERROR]" + parameter + " invalid range enter ? for more help")
        elif parameter == "hello-time":
            if 10 > int(range) > 1:
                return True
            else:
                print("[ERROR]" + parameter + " invalid range enter ? for more help")
    except ValueError:
        print('\n[ERROR]You did not enter a valid integer')


def init(bridgname):
    os.system("mstpd")
    os.system("mstpctl addbridge " + bridge)


def wellcome():
    needbridg = input("welcome to mstpd \n do you need new bridge ?(y/n) default y\n>")
    if needbridg == "n":
        return input("enter your bridge name : \n> ")
    else:
        print('go creat bridge and comeback again')
        sys.exit(0)


if __name__ == '__main__':
    bridge = wellcome()
    init(bridge)
    print('Hi enter command! or ?\n'
          'enter exit to terminate')
    commands(bridge)


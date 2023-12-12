import os, time, sys

visuals = {
    "reset": '\033[0m',
    "bold": '\033[01m',
    "disable": '\033[02m',
    "underline": '\033[04m',
    "reverse": '\033[07m',
    "strikethrough": '\033[09m',
    "invisible": '\033[08m',
    "black": '\033[30m',
    "red": '\033[31m',
    "green": '\033[32m',
    "orange": '\033[33m',
    "blue": '\033[34m',
    "purple": '\033[35m',
    "cyan": '\033[36m',
    "lightgrey": '\033[37m',
    "darkgrey": '\033[90m',
    "lightred": '\033[91m',
    "lightgreen": '\033[92m',
    "yellow": '\033[93m',
    "lightblue": '\033[94m',
    "pink": '\033[95m',
    "lightcyan": '\033[96m'
}

'''
~~         : ~
~v(n)      : sets visual to the name in the colors dictionary above
~c         : clear
~d(t)      : delay(time)
~s(s,v)    : setting(name, value)
~i         : press enter to continue
~p(s)      : executes string (python)
~e(s)      : prints eval(s)

===== settings =====
type_speed : delay between letters
'''

def parentheses(input):
    found = False
    i=0
    start = 0
    level = 0
    while found == False:
        if input[i] == "(":
            level+=1
            if level == 1: start = i
        elif input[i] == ")":
            level-=1
            if level == 0: found=True
        i+=1
    return(input[start+1:][:i-3],i-1)


def draw(text):
    settings = {
        "type_speed": 0.025
    }
    print('\033[0m')
    raised = False
    skip = -1
    for i in range(len(text)):
        if i > skip:
            if raised:
                raised = False
                if text[i] == "v":
                    output = parentheses(text[i:])
                    print(visuals[text[i:][text[i:].find("(")+1:text[i:].find(")")]], end="")
                    skip = i+text[i:].find(")")
                elif text[i] == "d":
                    output = parentheses(text[i:])
                    time.sleep(float(text[i:][text[i:].find("(")+1:text[i:].find(")")]))
                    skip = i+text[i:].find(")")
                elif text[i] == "e":
                    output = parentheses(text[i:])
                    print(eval(output[0]), end="", flush=True)
                    skip = i+output[1]
                elif text[i] == "p":
                    output = parentheses(text[i:])
                    exec(output[0])
                    skip = i+output[1]
                elif text[i] == "s":
                    output = parentheses(text[i:])
                    val = text[i:][text[i:].find("(")+1:text[i:].find(")")].split(",")
                    settings[val[0]] = float(val[1])
                    skip = i+text[i:].find(")")
                elif text[i] == "c":
                    if sys.platform == "win32": os.system("cls")
                    else: os.system("clear")
                elif text[i] == "~": print("~", end="", flush=True)
                elif text[i] == "i": input("")
                else: raise Exception("cant recognize ~"+text[i])
            else:
                if text[i] == "~":
                    raised = True
                else:
                    print(text[i], end="", flush=True)
                    time.sleep(settings["type_speed"])

if __name__ == "__main__":
    logo = "~c~v(pink)~s(type_speed,0)    __                       __            __     __              __\n   / /   ___  ____  _____   / /____  _  __/ /_   / /_____  ____  / /\n  / /   / _ \/ __ \/ ___/  / __/ _ \| |/_/ __/  / __/ __ \/ __ \/ / \n / /___/  __/ /_/ (__  )  / /_/  __/>  </ /_   / /_/ /_/ / /_/ / /  \n/_____/\___/\____/____/   \__/\___/_/|_|\__/   \__/\____/\____/_/  \n~v(reset)____________________________________________________________________\n"
    draw(logo+"1: from file\n2: from input\n>")
    inp = input()
    if inp == "1":
        draw(logo)
        draw(open(input("file name: "),"r").read())
    elif inp == "2":
        draw(logo)
        draw(input("?: "))
    else: raise Exception(inp+" isnt a option!")

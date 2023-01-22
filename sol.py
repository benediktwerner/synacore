#!/usr/bin/env python3

import random, json

MOD = 32768

memory = [0] * 0b111_1111_1111_1111
regs = [0] * 8
stack = []

with open("challenge.bin", "rb") as f:
    data = f.read()
    for i, (a, b) in enumerate(zip(data[::2], data[1::2])):
        memory[i] = b << 8 | a

ip = 0
inp = ""
manual = True

inputs = [
    "go doorway",
    "go north",
    "go north",
    "go bridge",
    "go continue",
    "go down",
    "go east",
    "take empty lantern",
    "go west",
    "go west",
    "go passage",  # ladder + darkness
    "go ladder",
    "go west",
    "go south",
    "go north",  # can
    "take can",
    "use can",
    "use lantern",
    "go west",  # ladder
    "go ladder",
    "go darkness",
    "go continue",  # dark west, east -> continue -> back here
    "go west",
    "go west",
    "go west",
    "go west",  # east back, north stone arch
    "go north",  # south back, north forward
    "take red coin",
    "go north",  # formular: _ + _ * _^2 + _^3 - _ = 399, red coin = 2, blue coin = 9, shiny coin = 5, concave coin = 7, corroded coin = 3
    "go west",
    "take blue coin",
    "go up",
    "take shiny coin",
    "go down",
    "go east",
    "go east",
    "take concave coin",
    "go down",
    "take corroded coin",
    "go up",
    "go west",
    "use blue coin",
    "use red coin",
    "use shiny coin",
    "use concave coin",
    "use corroded coin",
    "go north",
    "take teleporter",
    "use teleporter",
    # "take business card",
    # "take strange book",
]
seen = {}
moves = []
output = ""
snapshot = None


def str_print(start, length):
    s = start
    curr = ""
    for i in range(length):
        c = memory[start + i]
        if c < 128:
            curr += chr(c)
        else:
            if curr:
                print(f"[{s}] {repr(curr)}")
            print(f"[{start + i}] {c}")
            curr = ""
            s = start + i + 1
    if curr:
        print(f"[{s}] {repr(curr)}")


while True:
    instr = memory[ip]
    # if ip == 1046:
    #     print(memory[25867 : 25867 + 53])
    #     str_print(6068, 30050 - 6068)

    ip += 1

    if 5483 <= ip <= 5496:
        continue

    def arg():
        global ip
        ip += 1
        return memory[ip - 1]

    def set_reg(f):
        r = arg() - MOD
        regs[r] = f()

    def val():
        n = arg()
        if n < MOD:
            return n
        return regs[n - MOD]

    match instr:
        case 0:  # halt
            print("reset")
            memory = snapshot[0][:]
            stack = snapshot[1][:]
            regs = snapshot[2][:]
            ip = snapshot[3]
            moves = []
            output = "- north\n- south\n- east\n- west"

            # break
        case 1:  # set
            set_reg(lambda: val())
        case 2:  # push
            stack.append(val())
        case 3:  # pop
            assert stack, "pop from empty stack"
            set_reg(lambda: stack.pop())
        case 4:  # eq
            set_reg(lambda: 1 if val() == val() else 0)
        case 5:  # gt
            set_reg(lambda: 1 if val() > val() else 0)
        case 6:  # jmp
            ip = val()
        case 7:  # jt
            if val() != 0:
                ip = val()
        case 8:  # jf
            if val() == 0:
                ip = val()
        case 9:  # add
            set_reg(lambda: (val() + val()) % MOD)
        case 10:  # mult
            set_reg(lambda: (val() * val()) % MOD)
        case 11:  # mod
            set_reg(lambda: val() % val())
        case 12:  # and
            set_reg(lambda: val() & val())
        case 13:  # or
            set_reg(lambda: val() | val())
        case 14:  # not
            set_reg(lambda: ~val() & 0b111_1111_1111_1111)
        case 15:  # rmem
            set_reg(lambda: memory[val()])
        case 16:  # wmem
            a = val()
            memory[a] = val()
        case 17:  # call
            target = val()
            stack.append(ip)
            ip = target
        case 18:  # ret
            if not stack:
                break
            ip = stack.pop()
        case 19:  # out
            c = chr(val())
            if not inputs:
                output += c
            if manual:
                print(c, end="")
        case 20:  # in
            if not inp:
                if inputs:
                    inp = inputs.pop(0)
                    print(inp)
                else:
                    if snapshot is None:
                        snapshot = (memory[:], stack[:], regs[:], ip - 1)
                    if manual:
                        inp = input("Input: ")
                    else:
                        options = [
                            line[2:]
                            for line in output.splitlines()
                            if line.startswith("- ")
                        ]
                        if options:
                            if "ladder" in options:
                                options.remove("ladder")
                                moves = []
                            elif output not in seen or len(seen[output]) > len(moves):
                                print("new")
                                seen[output] = moves[:]
                                with open("moves.json", "w") as f:
                                    json.dump(seen, f)
                            inp = random.choice(options)
                            moves.append(inp)
                            output = ""
                        else:
                            manual = True
                            inp = input("Input: ")
                if inp == "use teleporter":
                    regs[-1] = 25734
                inp += "\n"
            set_reg(lambda: ord(inp[0]))
            inp = inp[1:]
        case 21:  # noop
            pass

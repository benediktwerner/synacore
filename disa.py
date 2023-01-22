#!/usr/bin/env python3


MOD = 32768
REGS = "abcdefgh"
memory = []

with open("challenge.bin", "rb") as f:
    data = f.read()
    for a, b in zip(data[::2], data[1::2]):
        memory.append(b << 8 | a)

ip = 0
out = ""

while ip < len(memory):
    instr = memory[ip]
    start_ip = ip
    ip += 1

    def arg():
        global ip
        ip += 1
        return memory[ip - 1]

    def set_reg(f):
        print(REGS[arg() - MOD], "=", str(f()))

    def val():
        n = arg()
        if n < MOD:
            return n
        return REGS[n - MOD]

    if instr != 19 and out:
        print("out", repr(out))
        out = ""

    if instr != 19 or not out:
        print(f"[{start_ip}] ", end="")

    try:
        match instr:
            case 0:  # halt
                print("halt")
            case 1:  # set
                set_reg(lambda: val())
            case 2:  # push
                print("push", val())
            case 3:  # pop
                set_reg(lambda: "pop")
            case 4:  # eq
                set_reg(lambda: f"{val()} == {val()}")
            case 5:  # gt
                set_reg(lambda: f"{val()} > {val()}")
            case 6:  # jmp
                print("jmp", val())
            case 7:  # jt
                print(f"if {val()} != 0: jmp {val()}")
            case 8:  # jf
                print(f"if {val()} == 0: jmp {val()}")
            case 9:  # add
                set_reg(lambda: f"{val()} + {val()}")
            case 10:  # mult
                set_reg(lambda: f"{val()} * {val()}")
            case 11:  # mod
                set_reg(lambda: f"{val()} % {val()}")
            case 12:  # and
                set_reg(lambda: f"{val()} & {val()}")
            case 13:  # or
                set_reg(lambda: f"{val()} | {val()}")
            case 14:  # not
                set_reg(lambda: f"~{val()}")
            case 15:  # rmem
                set_reg(lambda: f"[{val()}]")
            case 16:  # wmem
                print(f"[{val()}] = {val()}")
            case 17:  # call
                print("call", val())
            case 18:  # ret
                print("ret")
            case 19:  # out
                v = val()
                if isinstance(v, int) and v < 128:
                    out += chr(v)
                else:
                    if out:
                        print("out", repr(out))
                        out = ""
                    print("out", v)
            case 20:  # in
                set_reg(lambda: "in")
            case 21:  # noop
                print("noop")
            case _:  # invalid
                print("#", instr, repr(chr(instr)) if instr < 128 else "")
    except IndexError:
        for i in range(start_ip, ip):
            instr = memory[i]
            print("#", instr, repr(chr(instr)) if 0 <= instr < 128 else "")

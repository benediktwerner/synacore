https://challenge.synacor.com/

## Print encrypted string

```python
f = lambda k:"".join(chr(int(c)^k) for c in x.splitlines())
x = """<nums from strs.txt one per line here>"""
f(encryption code in c)
```

## Important Functions

- 1458: for_each_char(a: str, b: fn(a: char)) -> b: length of str
- 1518: print(a: str)
- 1531: out_decrypt(a: char) # decryption key in c
- 1543: for_each_char_checked(a: str, b: fn(a: char), c: succ) -> a: c if succ else 32767
- 1571: find_char(a: str, b: char) -> a: index of b in a or 32767
- 1588: find_string_in_list(a: List[str], b: str) -> a: index of b in a or 32767
- 1667: str_eq(a: str, b: str) -> a: a == b
- 1767: read(a: max_len, b: buffer) -> b # writes length to b[0]
- 2734: Game start

Handler names list at 27398:

- 25943: 0 go
- 25946: 1 look
- 25951: 2 help
- 25956: 3 inv
- 25960: 4 take
- 25965: 5 drop
- 25970: 6 use

Handler functions list at 27406:

- 3245: 0 go
- 2964: 1 look
- 3333: 2 help
- 3362: 3 inv
- 3400: 4 take
- 3488: 5 drop
- 3568: 6 use

Teleport handler: 5445

h Check:

```
[5483] a = 4
[5486] b = 1
[5489] call 6027
[5491] b = a == 6
[5495] if b == 0: jmp 5579 # failure

[6027] if a != 0: jmp 6035
[6030] a = b + 1
[6034] ret
[6035] if b != 0: jmp 6048
[6038] a = a + 32767
[6042] b = h
[6045] call 6027
[6047] ret
[6048] push a
[6050] b = b + 32767
[6054] call 6027
[6056] b = a
[6059] a = pop
[6061] a = a + 32767
[6065] call 6027
[6067] ret
```

```python
assert f(4, 1) == 6
assert f(3, f(3, h)) == 6

def f(a, b):
    if a == 0:
        return b + 1
    if b == 0:
        return f(a - 1, h)
    return f(a - 1, f(a, b - 1))
```

## Maze notes

```
S start
D doorway
B bridge
C continue
N next
P passage

N down to next S
C As you continue along the bridge, it snaps! You try to grab the bridge, but it evades your grasp in the darkness. You are plummeting quickly downward into the chasm...
B This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.
. The cave acoustics dramatically change as you find yourself at a legde above a large chasm. There is barely enough light here to notice a rope bridge leading out into the dark emptiness.
. The cave is somewhat narrow here, and the light from the doorway to the south is quite dim.
D This seems to be the mouth of a deep cave. As you peer north into the darkness, you think you hear the echoes of bats deeper within.
S (tablet) You find yourself standing at the base of an enormous mountain. At its base to the north, there is a massive doorway. A sign nearby reads "Keep out! Definitely no treasure within!"
.
-

-
E (empty lantern) You are standing in a large cavern full of bioluminescent moss. The cavern extends to the west.
S You are standing in a large cavern full of bioluminescent moss. It must have broken your fall! The cavern extends to the east and west; at the west end, you think you see a passage leading out of the cavern.
. You are standing in a large cavern full of bioluminescent moss.  The cavern extends to the east.  There is a crevise in the rocks which opens into a passage.
P You are in a crevise on the west wall of the moss cavern.  A dark passage leads further west.  There is a ladder here which leads down into a smaller, moss-filled cavern below.
N ladder to next S | darkness remaining

S You are in a maze of twisty little passages, all dimly lit by more bioluminescent moss.  There is a ladder here leading up.
3x north/south goes back to start

east The passage to the east looks very dark; you think you hear a Grue.
    west back to S
    north
        north
            north back to S
            X
        south back to this
        east
            north
                north back to S
                south
                    south back to S
                    X
                X
            X
    east
        north
            north back to S
            south
            east
                north back to S
                south
                    north
                    south
                    west
                east
        south
    X

west
    north loops back to this
    south The east passage appears very dark; you feel likely to be eaten by a Grue.
        north (can) ZETOFQDyNMHm
            west back to S
        west
            east back to this
            north back to S
            south
                north back to ^
                west back to this
                south back to S
        east
            north
            south
```

## Island maze: Vault room

```
*   8   -   1 < 30
4   *   11  *
+   4   -   18
22  -   9   *
^^
```

## Vault code seen in the mirror: xbYuVVVAdxqO

OpxbAVVVuYdx

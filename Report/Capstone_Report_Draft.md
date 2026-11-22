# Nand2Tetris Capstone Report
## Make the Computer Draw a Box

**Course:** Nand to Tetris – I (ETCCNT301)  
**University:** K.R. Mangalam University, School of Engineering & Technology  
**Student name:** [Enter your name]  
**University roll number:** [Enter your full roll number]  
**Personal number (K):** 76  

## 1. Objective
The objective of this capstone is to build the Hack computer's top-level hardware
chips, write a Python assembler that translates Hack assembly into 16-bit machine
instructions, and write a Hack assembly program that displays a black rectangle
while a key is pressed and clears it when the key is released.

## 2. Personalized box calculation
For K = 76:
- K mod 3 = 1, so the assembler's extra feature is a clear error message with
  the source line number when it encounters an invalid instruction.
- K mod 4 = 0, so the width is 16 × (0 + 1) = 16 pixels.
- Height = 20 rows.
- Starting row = 76; ending row = 76 + 20 − 1 = 95.
- One screen row contains 32 words. The first word address is
  SCREEN + 32 × 76 = 16384 + 2432 = 18816.
- The program writes one 16-bit screen word per row, with a stride of 32 words.

## 3. Part A — Hardware
The project supplies CPU.hdl, Memory.hdl and Computer.hdl. To make the project
runnable without the student's previous lab files, these top-level chips use
the simulator's built-in Register, ALU, PC, RAM16K, Screen, Keyboard and ROM32K
chips. This is the built-in-chip fallback permitted by the capstone brief.
The report must not describe these built-in chips as individually implemented.

**Insert genuine screenshots after running the official tests:**
- Figure 1: CPU.tst result.
- Figure 2: Memory.tst result.
- Figure 3: ComputerAdd.tst result.
- Figure 4: ComputerMax.tst result.
- Figure 5: ComputerRect.tst result.

## 4. Part B — Python assembler
The assembler uses two passes. In the first pass it removes comments and blank
lines, records label addresses, and counts ROM instructions. In the second pass
it translates A-instructions and C-instructions into 16-bit binary strings.
Predefined Hack symbols are supported, and new variables are allocated from
RAM address 16 upward.

For K = 76, invalid input is reported with a line number rather than producing
an unhandled traceback. The assembler uses only Python's standard library.

**Required validation:** run the official Add.asm, Max.asm, Rect.asm and Pong.asm
through this assembler and the official assembler, then compare the generated
`.hack` files. Insert evidence of the comparisons here.

## 5. Part C — Box program
Box.asm checks the memory-mapped keyboard address KBD (24576). If a key is
pressed, it writes -1 to the 20 screen words. If no key is pressed, it writes
0 to those words. The pointer begins at address 18816 and advances by 32 after
each write. The loop runs for 20 rows and then checks the keyboard again.

**Insert Figure 6:** CPU Emulator screenshot with a key held and the black box
visible. Also test and record that the box disappears after key release.

## 6. Mistake fixed
[Write a truthful account of one mistake you personally encountered while
running or testing the project. Explain the symptom, the cause, the correction,
and how you verified the fix. Do not invent a debugging story.]

## 7. Conclusion
The capstone combines digital hardware, Hack assembly language, binary
instruction encoding, memory-mapped I/O and a two-pass assembler. The final
verification is complete only after the official hardware tests, four official
assembler comparisons and keyboard-controlled box demonstration have been run
successfully and their screenshots have been added.

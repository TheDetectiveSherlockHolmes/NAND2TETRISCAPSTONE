# Nand2Tetris Capstone — K = 76

## Personalized requirements
- K = 76
- K mod 3 = 1: assembler reports invalid instructions with source line numbers.
- K mod 4 = 0: box width = 16 × (0 + 1) = 16 pixels.
- Box height = 20 rows; top row = 76; left edge.
- Screen word address for row 76 = 16384 + 32×76 = 18816.
- Box covers screen rows 76 through 95 inclusive.

## Project structure
- `Part-A-Hardware/`: CPU.hdl, Memory.hdl, Computer.hdl.
- `Part-B-Assembler/`: two-pass Python assembler and smoke tests.
- `Part-C-Box/`: Box.asm and its assembled Box.hack.
- `Report/`: report draft and screenshot checklist.

## Dependencies
1. Python 3.9+ (standard library only; no pip packages).
2. Nand2Tetris Software Suite / Hardware Simulator and CPU Emulator.
3. VS Code or another text editor (optional).
4. Git (optional, for GitHub submission).

Official resources:
- https://www.nand2tetris.org/software
- https://www.nand2tetris.org/course

## Run the assembler
From this folder:
```bash
python3 Part-B-Assembler/assembler.py Part-C-Box/Box.asm
```
This creates `Part-C-Box/Box.hack`.
To specify an output path:
```bash
python3 Part-B-Assembler/assembler.py Part-C-Box/Box.asm Part-C-Box/Box.hack
```
No third-party Python packages are required.

## Part A: Hardware Simulator
Open the Hardware Simulator supplied with Nand2Tetris. Set the project directory to
`Part-A-Hardware`. Load and test CPU.hdl, Memory.hdl and Computer.hdl with the
official `.tst` files from the Nand2Tetris Project 05 materials:
- CPU.tst
- Memory.tst
- ComputerAdd.tst
- ComputerMax.tst
- ComputerRect.tst

The capstone brief permits using built-in chips when older student chips are
unavailable, provided the report states this. This implementation uses built-in
`Register`, `ALU`, `PC`, `RAM16K`, `Screen`, `Keyboard`, and `ROM32K`; the three
top-level chips are supplied here. Do not claim that these built-ins were
individually implemented by you.

If the simulator reports a missing built-in chip or syntax error, capture the
exact message and resolve it before claiming a passing test. Keep screenshots
of each successful test in `Report/screenshots/`.

## Part B: Required official assembler comparison
Download the official Nand2Tetris software/course materials and locate the
official assembler. Test your assembler on the official Add.asm, Max.asm,
Rect.asm and Pong.asm. Compare your `.hack` output byte-for-byte with the
official assembler output. The included Add and Max programs are smoke tests,
not substitutes for all four required official programs.

For K=76, the extra feature is line-numbered error reporting. Quick check:
```bash
python3 Part-B-Assembler/assembler.py invalid_example.asm
```
with an invalid instruction in the file. Expected: a message such as
`Error: Line 3: unknown computation 'D++A'` and a non-zero exit code.

## Part C: Run the box
1. Open `Part-C-Box/Box.hack` in the CPU Emulator.
2. Load the Hack computer's screen and keyboard (the CPU Emulator does this).
3. Run the program.
4. Press and hold any key: a black 16×20-pixel rectangle should appear at the
   left edge, beginning at screen row 76.
5. Release the key: the rectangle should disappear.
6. Save a screenshot while the box is visible.

The program continuously redraws the 20 screen words. Each row is 32 words apart.
The first word is SCREEN + 32×76 = 18816; the final word is row 95.


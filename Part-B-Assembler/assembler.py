#!/usr/bin/env python3
"""
Hack assembler for the K.R. Mangalam University Nand2Tetris capstone.
Personalized K=76 feature: invalid instructions produce a clear line-numbered
error instead of an unhandled exception.
Usage: python3 assembler.py input.asm [output.hack]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

PREDEFINED = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    **{f"R{i}": i for i in range(16)},
    "SCREEN": 16384, "KBD": 24576,
}
DEST = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111",
}
JUMP = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}
COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101",
}

SYMBOL_RE = re.compile(r"^[A-Za-z_.$:][A-Za-z0-9_.$:]*$")

class AssemblyError(Exception):
    pass

def clean_lines(source: str):
    """Yield (original_line_number, stripped_instruction)."""
    for number, raw in enumerate(source.splitlines(), start=1):
        line = raw.split("//", 1)[0].strip()
        if line:
            yield number, re.sub(r"\s+", "", line)

def assemble(source: str):
    lines = list(clean_lines(source))
    symbols = dict(PREDEFINED)
    instructions = []

    # Pass 1: labels point to the ROM address of the next instruction.
    rom_address = 0
    for line_no, line in lines:
        if line.startswith("("):
            if not line.endswith(")") or line.count("(") != 1 or line.count(")") != 1:
                raise AssemblyError(f"Line {line_no}: invalid label declaration '{line}'")
            label = line[1:-1]
            if not SYMBOL_RE.match(label):
                raise AssemblyError(f"Line {line_no}: invalid label name '{label}'")
            if label in symbols:
                print(f"Warning: Line {line_no}: label '{label}' is already defined; keeping its first address.", file=sys.stderr)
            else:
                symbols[label] = rom_address
        else:
            instructions.append((line_no, line))
            rom_address += 1

    # Pass 2: translate instructions and allocate variables from RAM[16].
    next_variable = 16
    machine_code = []
    for line_no, line in instructions:
        try:
            if line.startswith("@"):
                symbol = line[1:]
                if not symbol:
                    raise AssemblyError("empty A-instruction")
                if symbol.isdigit():
                    value = int(symbol)
                elif SYMBOL_RE.match(symbol):
                    if symbol not in symbols:
                        symbols[symbol] = next_variable
                        next_variable += 1
                    value = symbols[symbol]
                else:
                    raise AssemblyError(f"invalid A-instruction operand '{symbol}'")
                if not 0 <= value <= 32767:
                    raise AssemblyError(f"A-instruction value {value} is outside 0..32767")
                machine_code.append(f"0{value:015b}")
            else:
                if line.count(";") > 1 or line.count("=") > 1:
                    raise AssemblyError(f"invalid C-instruction '{line}'")
                if ";" in line:
                    left, jump = line.split(";")
                else:
                    left, jump = line, ""
                if "=" in left:
                    dest, comp = left.split("=")
                else:
                    dest, comp = "", left
                if comp not in COMP:
                    raise AssemblyError(f"unknown computation '{comp}'")
                if dest not in DEST:
                    raise AssemblyError(f"invalid destination '{dest}'")
                if jump not in JUMP:
                    raise AssemblyError(f"invalid jump '{jump}'")
                machine_code.append("111" + COMP[comp] + DEST[dest] + JUMP[jump])
        except AssemblyError as exc:
            raise AssemblyError(f"Line {line_no}: {exc}") from None
    return machine_code, symbols

def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python3 assembler.py input.asm [output.hack]", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else input_path.with_suffix(".hack")
    try:
        code, _symbols = assemble(input_path.read_text(encoding="utf-8"))
    except (OSError, AssemblyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    output_path.write_text("\n".join(code) + "\n", encoding="utf-8")
    print(f"Assembly successful: {len(code)} instructions written to {output_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

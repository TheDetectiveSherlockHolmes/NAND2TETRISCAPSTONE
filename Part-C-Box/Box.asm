// K=76: 16 pixels wide (one word), 20 rows tall, beginning at row 76.
// SCREEN + 32*76 = 18816. Each next screen row is 32 words away.
// Any key pressed: write -1 (black). No key: write 0 (white).

(LOOP)
    @KBD
    D=M
    @DRAW_BLACK
    D;JNE

    // No key is pressed: clear the 20-word column.
    @18816
    D=A
    @PTR
    M=D
    @20
    D=A
    @COUNT
    M=D
(CLEAR_LOOP)
    @PTR
    A=M
    M=0
    @32
    D=A
    @PTR
    M=D+M
    @COUNT
    M=M-1
    D=M
    @CLEAR_LOOP
    D;JGT
    @LOOP
    0;JMP

(DRAW_BLACK)
    // A key is pressed: paint the same 20-word column black.
    @18816
    D=A
    @PTR
    M=D
    @20
    D=A
    @COUNT
    M=D
(BLACK_LOOP)
    @PTR
    A=M
    M=-1
    @32
    D=A
    @PTR
    M=D+M
    @COUNT
    M=M-1
    D=M
    @BLACK_LOOP
    D;JGT
    @LOOP
    0;JMP

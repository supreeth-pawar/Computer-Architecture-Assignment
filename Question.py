
memory = {100: 12, 104: 8}
R1 = R2 = R3 = 0

print("LOAD R1, 100")
R1 = memory[100]
print("R1 =", R1)

print("\nLOAD R2, 104")
R2 = memory[104]
print("R2 =", R2)

print("\nADD R3, R1, R2")
R3 = R1 + R2
print("R1 =", R1, "R2 =", R2, "R3 =", R3)

print("\nSTORE R3, 108")
memory[108] = R3
print("Memory[108] =", memory[108])

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

M = float(input("M: "))
K = float(input("K: "))

S = sorted([A, B, C])

print("YES" if S[0] * S[1] <= M * K else "NO")
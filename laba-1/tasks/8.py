string = input().lower().replace(' ', '')
print("YES" if string[:len(string)//2] == string[len(string)//2 + 1:][::-1] else "NO")
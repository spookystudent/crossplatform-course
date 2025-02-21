a = float(input())
b = float(input())
c = float(input())

z1 = (
    (1/a) - (1/(b+c))
) / (
    (1/a) + (1/(b+c))
) * (
    1 + (
        (b**2 + c**2 - a**2)
    ) / (
        2*b*c
    )
) / (
    (
        a - b - c
    ) / (a * b * c)
)

z2 = ((
    a - b - c
) / 2 ) * a

print(z1)
print(z2)
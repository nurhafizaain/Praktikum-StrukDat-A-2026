nilai = [75, 80, 65, 90, 85]

nilai.append(95)
nilai.remove(65)
nilai.sort()
jum = 0
for i in nilai:
    jum += i
rata = (jum)/5
print(rata)
print(nilai)
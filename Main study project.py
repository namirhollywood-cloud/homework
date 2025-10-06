msc_price = 13_000
spb_price = 20_000
ekb_price = 30_000

dist = input("Введите пункт назначения (msc, spb, ekb): ")
adults = input("Введите взрослых: ")
kids = int(input("Введите кол-во детей"))

if dist == "msc":
    dist_price = msc_price
elif dist == "spb":
    dist_price = spb_price
else:
    dist_price = ekb_price

total = dist_price * (2 * adults + kids) // 2

print("Цена поездки", total)
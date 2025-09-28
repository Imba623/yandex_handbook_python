n = int(input())
do_starta = 3
for i in range(n):
    for y in range(do_starta, 0, -1):
        print(f"До старта {y} секунд(ы)")
    print(f"Старт {i + 1}!!!")
    do_starta += 1

import time


n = int(input())

x = float(input())


def calc(n,x):
        for i in range(n):
            print(x**2 - x**2 +x**4 - x**5 + x + x)





start = time.time()
calc(n,x)
end = time.time()

print(f"Время выполнения: {end - start:.4f} секунд")

if __name__ == '__main__':
    n = int(input())
    for x in range(1, (n+1)):
        print(x, end="", flush=True)


for item in range(0, 10):
    padding = len(str(bin(n)[2:]))
    print(f"{item:{padding}} {oct(item):{padding}} {hex(item):{padding}} {bin(item):{padding}}")

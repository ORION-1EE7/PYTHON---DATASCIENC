# 5- EXEMPLE 

```abap
def main():
    N = 3
    M = 2

    # I: 1D Array Input
    arr = [0] * N
    for a in range(N):
        arr[a] = int(input(f"Enter a value for arr[{a}]: "))
  
    print()
    for b in range(N):  # Adjusted to match C code behavior
        print(f"arr[{b}] = {arr[b]}")

    # II: 2D Array Input
    ARR = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            ARR[i][j] = int(input(f"Enter the value of ARR[{i}][{j}]: "))
  
    print()
    for i in range(N):
        for j in range(M):
            print(f"ARR[{i}][{j}] = {ARR[i][j]}")

if __name__ == "__main__":
    main()

```

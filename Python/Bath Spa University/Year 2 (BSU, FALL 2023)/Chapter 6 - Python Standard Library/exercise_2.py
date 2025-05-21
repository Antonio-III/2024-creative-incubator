import numpy as np

ARRAY=np.array([20,23,82,40,32,15,67,52])

def main()->None:
    a = ARRAY
    indices_even=np.where(a%2==0)

    print(f'Even numbers in indices: {indices_even}')

    # asc sort
    print(f'Array sorted ascending order: {np.sort(a)}')

    # slice from i 3 to end
    print(f'Sliced from index 3 {a[3:]}')

    # slice from i 0 to 4 (inclusive?)
    print(f'Sliced until index 4 inclusive: {a[:4+1]}')

    # output 32 15 67 using negative nums
    print(f'Negative slicing: {a[-3:-1]}')

if __name__ == "__main__":
	main()
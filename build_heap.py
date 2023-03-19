import sys


def heapify_down(arr: list[int], i: int, swaps: tuple[int, int]) -> int:
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i

    if left_child < len(arr) and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < len(arr) and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))
        swaps = heapify_down(arr, smallest, swaps)

    return swaps


def build_heap(data: list[int]) -> int:
    middle = len(data) // 2
    swaps = []

    # Iterate from the middle of the array to the beginning
    for i in range(middle, -1, -1):
        swaps = heapify_down(data, i, swaps)

    # Iterate from the middle of the array to the end
    for i in range(middle + 1, len(data)):
        swaps = heapify_down(data, i, swaps)

    return swaps


def main():
    source = input().strip()
    if source[0:1] == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif source[0:1] == "F":
        with open(f"tests/{input()}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

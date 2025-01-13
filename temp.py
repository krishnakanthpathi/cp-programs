import sys

def ask(left, right):
    print(f"? {left} {right}")
    sys.stdout.flush()
    return int(input())  # Returns the index of the second maximum element

def tell(val):
    print(f"! {val}")
    sys.stdout.flush()

def main():
    n = int(input())
    l, r = 1, n

    while l < r:
        mid = (l + r) // 2
        sec_max = ask(l, r)  # Query the entire range [l, r]

        if sec_max <= mid:
            # If the second max is in the first half
            sec_max_left = ask(l, mid)  # Query only the first half
            if sec_max == sec_max_left:
                r = mid  # Narrow down to the first half
            else:
                l = mid + 1  # Otherwise, move to the second half
        else:
            # If the second max is in the second half
            sec_max_right = ask(mid + 1, r)  # Query only the second half
            if sec_max == sec_max_right:
                l = mid + 1  # Narrow down to the second half
            else:
                r = mid  # Otherwise, move to the first half

    # At the end of the binary search, l == r and is the index of the max element
    tell(l)

main()

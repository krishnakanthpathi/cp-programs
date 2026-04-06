import math

def nthpermuation(zeros, ones, n):

    total_len = zeros + ones
    
 
    result = []
    
    for i in range(total_len):
        if zeros > 0:
            remaining_len = (total_len - 1) - i
            count_with_zero = math.comb(remaining_len, ones)
            
            if n <= count_with_zero:
                result.append('0')
                zeros -= 1
            else:
                result.append('1')
                ones -= 1
                n -= count_with_zero
        else:
            result.append('1')
            ones -= 1
            
    return "".join(result)

# --- Wrapper Helper ---
def solve_from_string(s, n):
    """Helper to take a string like '0011' instead of counts"""
    z = s.count('0')
    o = s.count('1')
    return get_nth_binary_permutation(z, o, n)

# --- Usage Examples ---

# Example 1: Direct counts (3 zeros, 2 ones), find 5th permutation
# Sequence: 00011, 00101, 00110, 01001, 01010 ...
print(f"5th permutation of 3 zeros, 2 ones: {get_nth_binary_permutation(3, 2, 5)}")

# Example 2: Using an input string "011", find 2nd permutation
print(f"2nd permutation of '011': {solve_from_string('011', 2)}")
def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    return sum(list(range(A,B)))
print(main(3,6))
print(main(-6,8))
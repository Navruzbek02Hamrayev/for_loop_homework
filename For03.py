def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    l=[]
    l.append(k)
    return l*n
print(main(5,3))
print(main(-1,4))
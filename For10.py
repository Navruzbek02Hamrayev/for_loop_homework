def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    i=0
    l=[]
    while i<len(list1):
        l.append(list1[i].capitalize())
        i+=1
    return l
print(main(['rustam', 'diyor', 'alisher', 'bektosh']))
def mistura_strings(s1, s2):
    i = 0
    lst1 = []
    lst2 = []
    for letter in s1:
        lst1.append(letter)
    
    for letter in reversed(s2):
        lst2.append(letter)
    
    while i < len(s2):
        char1 = lst1[i]
        char2 = lst2[i]
        s3 = s3 + char1 + char2
        i = i + 1
    
    while i < len(s1):
        char1 = lst1[i]
        s3 = s3 + char1
        i = i + 1
    
    print(s3)

# Utilizamos da função "slice" para fatiar uma dada string em python ! # 

s1 = "lizadama"
s2 = "bela"
fatiadora = len(s1)
slice1 = slice(0,len(s1)//2)
slice2 = slice(len(s1)//2, len(s1))
s3 = s1[slice1] + s2 + s1[slice2]
print(s3)

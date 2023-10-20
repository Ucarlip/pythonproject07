#character in string has index number
    # 01234567890123
infoA = 'Hello SAU 2023'
    # 43240987654321 คิด -

print(infoA[6]) # s
print(infoA[-8]) # s

#เข้าถึงตัวอักษรหหลายๆ ตัว ใน String เราจะใช้ Slicing index number
# SAU
print(infoA[6:9])
print(infoA[-8:-5])

# o SAU 20
print(infoA[4:12])

#string Method
print( infoA.upper())
print( infoA.lower())
print( infoA.capitalize())
print( infoA.title())
print( infoA.count('1'))
print( infoA.isdigit())
print( infoA.islower())
infoB = infoA.replace('SAU','IOT')
print(infoB)
print(infoB.replace('Hello','Hi......'))

#string function
print( len(infoA) )

print('SAU',35,end='')
print('SAU'+str(35))
print('SAU',35,sap='')
print('20','02','2023',sep='/')
print(20,'มกราคม',2023,sep='-')
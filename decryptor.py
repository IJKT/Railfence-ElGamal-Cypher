import ast

# Your string
str_lst = '[[11, 14], [7, 0, 7]]'

# Convert string to list
lst = ast.literal_eval(str_lst)

print(lst)  # Outputs: [[11, 14], [7, 0, 7]]



def decimal_to_text(decimal):
    ascii_values = [int(value) for value in decimal.split()]
    text = ''.join(chr(value) for value in ascii_values)
    return text

def decryptRailFence(cipher, key):

	# membuat matrix dari ciphertext
	rail = [['\n' for i in range(len(cipher))]
				for j in range(key)]
	
	# menemukan direction
	dir_down = False
	row, col = 0, 0
	
	# mengkonstruksi matrix dimana huruf yang koresponden dengan '*'
	for i in range(len(cipher)):
		# jika direction sedang keatas dan row berada di 0, direction turun (if kiri)
		# jika direction sedang kebawah dan row berada di key-1, direction naik (if kanan)
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		# menempatkan '*' ke tempat yang tepat
		rail[row][col] = '*'
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
			
	# mengkonstruksi matrix dari atas ke bawah
	index = 0
	for _col in range(key):
		for _row in range(len(cipher)):
			if ((rail[_col][_row] == '*') and (index < len(cipher))):
				rail[_col][_row] = cipher[index]
				index += 1
	count = 0
	for row in rail:
		print(rail[count])
		count += 1
	# mengconstruct plaintext
	plaintext = []
	dir_down = False
	row, col = 0, 0
	for i in range(len(cipher)):
		
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
			
        #melakukan pengecekan apabila [row][col] bukan kosongan alias ada isinya
		if (rail[row][col] != '\n'):
			plaintext.append(rail[row][col])
			col += 1
			
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(plaintext))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# inputs
while True:
    publicKey_p = int(input("Masukkan bilangan prima (p) : "))
    if is_prime(publicKey_p):
        break
    else:
        print("Bilangan tidak prima, silakan masukkan lagi...")
#diantara 1 sampai p-2
while True:
    privateKey_x = int(input("Masukkan bilangan acak (x) : "))
    if privateKey_x < publicKey_p-2 and privateKey_x >= 1:
        break
    else:
         print("Bilangan tidak valid, silakan masukkan lagi...")
#sesuaikan dengan enkripsi
cipherText_a = int(input("Masukkan a : "))

# publicKey_p = 19
# PrivateKey_x = 5
# cipherText_a = 11 

# [,  7, [] ,1,1 ,7 ,[17[0824, [0]21 7 ][]77 ,0,,,,,, ,[],    0 7 ,  ,]1,21 0[[][, 980]4,, 771][ ] ]]7 ,, 817,,,,[1] ,,1,7 7 87  [

cipherText = input("Masukkan message yang mau didekripsi : ")
cipherText = decryptRailFence(cipherText, cipherText_a)
cipherText = ast.literal_eval(cipherText)

# ciphertext_real = [[11, 14], [7, 0, 7], [7, 0, 18], [7, 0, 18], [7, 7, 7], [2, 14], [18, 11], [7, 7, 7], [7, 7, 9], [7, 0, 18], [7, 0, 0], [2, 2]]


axInversed = (cipherText_a**(publicKey_p-1-privateKey_x))%publicKey_p
print(f"a^-1 = {cipherText_a} ^ {publicKey_p-1-privateKey_x} Mod {publicKey_p} = {axInversed}")
toDecrypt = []

count = 0
toTranslate = 0
for subtext in cipherText:
    toDecryptSubList = []
    for n in subtext:
        toDecryptSubList.append((n*axInversed)%publicKey_p)
        print(f"m[{count}] = {n}*{axInversed} Mod {publicKey_p} = {(n*axInversed)%publicKey_p}")
        count += 1
    toDecrypt.append(toDecryptSubList)
    print(f"message to translate[{toTranslate}] = {toDecryptSubList}")
    toTranslate += 1

#translate decimal to text
combined_cipher = [int(''.join(map(str, num))) for num in toDecrypt]
for n in combined_cipher:
  print(decimal_to_text(str(n)), end='')
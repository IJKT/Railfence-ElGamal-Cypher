def text_to_decimal(text):
  ascii_values = [ord(char) for char in text]
  decimal = ascii_values
  return decimal

def encryptRailFence(text, key):

    # membuat matrix dari plaintext
	rail = [['\n' for i in range(len(text))]
				for j in range(key)]
	
	# menginisiasi direction
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		# jika direction sedang keatas dan row berada di 0, direction turun (if kiri)
		# jika direction sedang kebawah dan row berada di key-1, direction naik (if kanan)
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		# memasukkan huruf yang koresponden
		rail[row][col] = text[i]
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1
		
	count = 0
	for row in rail:
		print(rail[count])
		count += 1
	# mengconstruct ciphertext
    
	ciphertext = []
	for _col in range(key):
		for _row in range(len(text)):
			if rail[_col][_row] != '\n':
				ciphertext.append(rail[_col][_row])
	return("" . join(ciphertext))

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
#lebih kecil dari p
while True:
    publicKey_g = int(input("Masukkan bilangan acak (g) : "))
    if publicKey_g < publicKey_p and publicKey_g >= 1:
        break
    else:
        print("Bilangan tidak valid, silakan masukkan lagi...")

#diantara 1 sampai p-2
while True:
    privateKey_x = int(input("Masukkan bilangan acak (x) : "))
    if privateKey_x < publicKey_p-2 and privateKey_x >= 1:
        break
    else:
         print("Bilangan tidak valid, silakan masukkan lagi...")
     
#diantara 1 sampai p-1
while True:
    random_k = int(input("Masukkan bilangan acak (k) : "))
    if random_k < publicKey_p-1 and random_k >= 1:
        break
    else:
         print("Bilangan tidak valid, silakan masukkan lagi...")


# publicKey_p = 19
# publicKey_g = 7
# PrivateKey_x = 5
# random_k = 8

message = input("Masukkan message yang mau dienkripsi : ")
# message = "Hello World!"
# enkripsi
publicKey_y = (publicKey_g**privateKey_x)%publicKey_p
print(f"y = {publicKey_g}^{privateKey_x} Mod {publicKey_p} = {publicKey_y}")
cipherText_a = (publicKey_g**random_k)%publicKey_p
print(f"a = {publicKey_g} ^ {random_k}Mod{publicKey_p} = {cipherText_a}")
cipherText = []

mToDecimal_divided = []
for i in text_to_decimal(message):
  mToDecimal_divided.append([int(j) for j in str(i)])

count = 0
for sub_list in mToDecimal_divided:
  cipherTextSubList = []
  for n in sub_list:
    b = ((publicKey_y**random_k)*n)%publicKey_p
    print(f"b[{count}] = {(publicKey_y**random_k)*n} Mod {publicKey_p} = {b}")
    cipherTextSubList.append((b))
    count += 1
  cipherText.append(cipherTextSubList) 
print (f"ciphertext = {encryptRailFence(str(cipherText), cipherText_a)}")
print (f"a = {cipherText_a}")
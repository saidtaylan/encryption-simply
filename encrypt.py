import random
encryption_dict_first = {}
encryption_dict_second = {}
encryption_dict = {}
encryption_dict_first_key_list = []
encryption_dict_first_value_list = []
userFile = input('Dosyanızın, encrypt.py dosyası ie aynı konumda olduğundan emin olduktan sonra, dosyaınızın ismini uzantısı ile birlikte giriniz:  ')
for i in range(65,127):
    encryption_dict_first[chr(i)] = str(i) + " "
for a,b in encryption_dict_first.items():
    encryption_dict_first_key_list.append(a)
    encryption_dict_first_value_list.append(b)
random.shuffle(encryption_dict_first_key_list)
random.shuffle(encryption_dict_first_value_list)
encryption_dict_first = dict(zip(encryption_dict_first_key_list, encryption_dict_first_value_list))
for i in encryption_dict_first:
    encryption_dict_second[encryption_dict_first[i]] = i
with open(userFile,'r',encoding='utf-8') as input_file:
    inputFile = input_file.readlines()
for i in range(len(inputFile)):
    for k in encryption_dict_first:
        inputFile[i] = inputFile[i].replace(k,encryption_dict_first[k])  
userOutput = input('Dosyanız şifrelendi. Dosyanızın isminin ne olmasını istersiniz? (Dosya ismini, uzantısı ile birlikte yazın):  ')  
with open(userOutput,'w',encoding='utf-8') as output_file:
    output_file.writelines(inputFile)

print()
print("\nŞifrelenmiş dosyayı çözmek için gereken veri sözlüğü aşağıdadır. Bunu kopyalayıp saklayınız. \n Ancak kopyalarken sağdan ve soldan boşlukları almayınız. Sadece süslü parantezler de dahil olmak üzere veri setini seçiniz.")
print('-----------------------------------------------------')
print('\n',encryption_dict_second)
print()
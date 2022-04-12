import ast
userFile = input('Hangi dosyayının şifresini çözmek istiyorsunuz? (Uzantısı ile birlikte yazın. unencrypt.py dosyası ile dosyanızın aynı konumda olduğundan emin olun.):  ')
print()
userDict = input('Dosya şifreleme işlemi esnasında size verilen, şifre çözme için gerekli olan veri setini(sözlük yapısı) buraya giriniz:  ')
print()
unencrypt_value_dict =  ast.literal_eval(userDict)
with open(userFile,'r',encoding='utf-8') as read_encrypted_file:
    encrypted_file = read_encrypted_file.readlines()

for i in range(len(encrypted_file)):
    for k in unencrypt_value_dict:
        encrypted_file[i] = encrypted_file[i].replace(k,unencrypt_value_dict[k])      

userOutput = input('Şifrelenmiş dosya başarıyla çözüldü. Çıktı dosyasını isminin ne olmasını istersiniz? (Uzantısı ile birlikte yazın. unencrypt.py dosyası ile aynı konumda olduğundan emin olun.):  ')

with open(userOutput,'w',encoding='utf-8') as unencrypted_file:
    unencrypted_file.writelines(encrypted_file)

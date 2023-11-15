import hashlib
"""
message: flag{y0u_Are_rE4ll_Jwt_****}
password: 444ceddca7c2baed444e8b53aab89c06
"""
dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def collision(key, len):
    if len == 0:
        return
    for c in dict:
        key += c
        flag = "flag{y0u_Are_rE4ll_Jwt_" + key + "}"
        md5 = hashlib.md5()
        md5.update(flag.encode('utf-8'))
        md5Value = md5.hexdigest()
        if md5Value == "444ceddca7c2baed444e8b53aab89c06":
            print(flag)
        collision(key, len - 1)
        key = key[0:-1]

collision("", 4)
print("end")

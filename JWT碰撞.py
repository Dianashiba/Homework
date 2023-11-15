import jwt
"""
JWT = eyJpc19hZG1pbiI6ZmFsc2UsIm5hbWUiOiIxMjMiLCJ1c2VyX2lkIjoyfQ.ZUdJwg.3QSZRjI6bOzDsaW6e4wB_b2-fMQ
{"alg":"HS256","typ":"JWT"}.{"username":"Dianashiba"}
"""
dict = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Payload = {
  "is_admin": "false",
  "name": "123",
  "user_id": "2"
}
def collision(key, len):
    if len == 0:
        return
    for c in dict:
        key += c
        JWT = jwt.encode(Payload, key, "HS256")
        if JWT == "eyJpc19hZG1pbiI6ZmFsc2UsIm5hbWUiOiIxMjMiLCJ1c2VyX2lkIjoyfQ.ZUdJwg.3QSZRjI6bOzDsaW6e4wB_b2-fMQ":
            print(key)
            return
        collision(key, len - 1)
        key = key[0:-1]
collision("", 4)
print("end")

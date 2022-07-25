PTA = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
CTA = " qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"


def mono_alpabetic_cipher_encrypt(pt):
    ans = ""
    for i in pt:
        try:
            ans += CTA[PTA.index(i)]
        except:
            ans += i
    return ans

def mono_alpabetic_cipher_decrypt(pt):
    ans = ""
    for i in pt:
        try:
            ans += PTA[CTA.index(i)]
        except:
            ans += i
    return ans


print(mono_alpabetic_cipher_encrypt("ATTACKm#4Once"))
print(mono_alpabetic_cipher_decrypt(mono_alpabetic_cipher_encrypt("ATTACKm#4Once")))

PTA = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
CTA = ' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'

def mono_alpabetic_cipher(pt):
    ans = ''
    for i in pt:
        try:
            ans += CTA[PTA.index(i)]
        except:
            ans += i
    return ans

print(mono_alpabetic_cipher("ATTACKm4Once"))
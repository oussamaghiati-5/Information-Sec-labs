ciphertext = "VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZLGFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVCOPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWLGOFGGGVAQFGIEZLTUS"

group1 = ciphertext[0::4]
group2 = ciphertext[1::4]
group3 = ciphertext[2::4]
group4 = ciphertext[3::4]


import string
from collections import Counter

def most_frequent_letter(text):
    counts = Counter(c for c in text.upper() if c in string.ascii_uppercase) # ignore spaces/punctuation
    letter, n = counts.most_common(1)[0]
    return letter, n, 100 * n / sum(counts.values())

print(most_frequent_letter(group1))
print(most_frequent_letter(group2))
print(most_frequent_letter(group3))
print(most_frequent_letter(group4))

print("\n\nBased on the table, we can map each result to E letter and recover the letter we shifted with.\n\n")

print("Results: E -> G gives C as key.\n E -> S gives O as key.\n E -> H gives D.\n E -> I gives E as key.")

key = "CODE"

import string

A = string.ascii_uppercase
def shift(text, k):
    """Shift letters by k (positive = encrypt, negative = decrypt); spaces unchanged."""
    return "".join(A[(A.index(c) + k) % 26] if c in A else c for c in text.upper())

def encrypt(text, k): return shift(text, k)
def decrypt(text, k): return shift(text, -k)

plain1 = decrypt(group1,2)
plain2 = decrypt(group2,14)
plain3 = decrypt(group3,3)
plain4 = decrypt(group4,4)



groups = [plain1, plain2, plain3, plain4]

rebuilt = ""
for i in range(len(group1)):        
    for g in groups:
        if i < len(g):              
            rebuilt += g[i]

print(rebuilt)      
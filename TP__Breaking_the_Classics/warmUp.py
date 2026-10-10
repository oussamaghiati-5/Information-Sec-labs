import string

A = string.ascii_uppercase

def shift(text, k):
    """Shift letters by k (positive = encrypt, negative = decrypt); spaces unchanged."""
    return "".join(A[(A.index(c) + k) % 26] if c in A else c for c in text.upper())

def encrypt(text, k): return shift(text, k)
def decrypt(text, k): return shift(text, -k)

# Brute force + automatic ranking by English likelihood
COMMON = {"THE","BE","TO","OF","AND","A","IN","THAT","HAVE","I","IT","FOR","NOT","ON","WITH",
          "AS","YOU","DO","AT","THIS","BUT","HIS","BY","FROM","IS","KEY","TRY","FORCE","BRUTE",
          "UNKNOWN","ARE","WAS","CAN","USE","USING"}
FREQ = "ETAOINSHRDLU"  # most frequent English letters

def score(text):
    words = text.split()
    word_hits = sum(w in COMMON for w in words) * 10
    letter_score = sum(FREQ.count(c) for c in text)  # weak tiebreaker
    return word_hits + letter_score * 0.1

def brute_force(cipher):
    results = [(k, decrypt(cipher, k)) for k in range(26)]
    return sorted(results, key=lambda r: score(r[1]), reverse=True)

if __name__ == "__main__":
    # 1. Encrypt (K = 4)
    msg1 = "CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ"
    print("1. Encrypted :", encrypt(msg1, 4))

    # 2. Decrypt (K = 8)
    msg2 = "GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA"
    print("2. Decrypted :", decrypt(msg2, 8))

    # 3. Brute force (unknown key)
    msg3 = "ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"
    print("3. All 26 candidates:")
    for k in range(26):
        print(f"   K={k:2d} -> {decrypt(msg3, k)}")
    best_k, best_plain = brute_force(msg3)[0]
    print(f"\n   Best guess: K={best_k} -> {best_plain}")
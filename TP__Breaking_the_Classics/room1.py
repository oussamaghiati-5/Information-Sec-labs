print("Plaint text: KEEP THE SECRET SAFE")
print("Cipher text: LTTN EKT YTJRTE YQGT")

print("\n\n-------------------------------------------\n\n")
print("Cipher text: ERVYE DXVR SXFPJ")
print("Cipher text: TRUST YOUR LOGIC")

print("\n\n-------------------------------------------\n\n")



print("Question: How could an attacker use this information to recover part of an unknown substitution key?\n")
print("Answer: The attacker will count the frequencies of letters in the cipher text and use the real english letters frequencies and map them to each other.")



print("\n\n-------------------------------------------\n\n")



import string
from collections import Counter

ENGLISH_ORDER = "ETRSOAHNDIGL"   # E > T > R > S/O > A > H > N > D > I > G > L

def frequency_attack(cipher, fix=None):
    letters = [c for c in cipher.upper() if c in string.ascii_uppercase]  # ignore spaces/punctuation
    counts = Counter(letters)
    total = len(letters)

    # Frequency table, most to least frequent
    ranked = sorted(string.ascii_uppercase, key=lambda c: (-counts[c], c))
    print("Letter  Count  Percent")
    for c in ranked:
        if counts[c]:
            print(f"  {c}     {counts[c]:4d}   {100 * counts[c] / total:6.2f}%")

    # Map i-th most frequent cipher letter -> i-th most frequent English letter (partial)
    mapping = {c: ENGLISH_ORDER[i] for i, c in enumerate(ranked[:len(ENGLISH_ORDER)])}
    if fix:                       # manual override for ties the frequencies cannot decide
        mapping.update(fix)

    plain = "".join(mapping.get(c, c.lower()) if c.isalpha() else c for c in cipher.upper())

    print("\nMapping (cipher -> plain):", mapping)
    print("Plaintext:", plain)
    return mapping, plain

cipher = ("EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD, "
          "MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY, QOZ YKXRE IXRZY."
          "IKTO DXV RTJXHTR EKT BTYYQFT, EKT HPFTOTRT LTD KQY GXVR STEETRY")

fix = {
    "X": "O", "Y": "S",                       # tie: S/O
    "J": "C", "B": "M", "N": "P", "G": "F", "C": "Q", "V": "U",
    "D": "Y", "H": "V", "I": "W", "L": "K", "M": "B",
}
frequency_attack(cipher, fix=fix)

class Arg:
    def __init__(ok, proof):
        ok.proof = proof
    def getProof(ok):
        return ok.proof
class Edit:
    def Edit(k):
        k.proof = "UTKA"
k = Arg(input())
k1 = Arg(input())
print(k.getProof(), k1.getProof())
Edit.Edit(k1)
print(k.getProof(), k1.getProof())

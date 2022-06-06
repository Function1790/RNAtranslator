Translating_RNA=[[] for i in range(10)]
Type_Protein=[]

def appendList(array:list, item):
    array.append(item)

def translate(codon) -> str:
    for i in range(len(Translating_RNA)):
        for j in Translating_RNA[i]:
            if j==codon:
                return Type_Protein[i]
    return None

def main():
    global Translating_RNA, Type_Protein
    while True:
        print(end="\n\nRNA의 염기서열을 입력하세요.\n>>")
        nucleic_sequence=input()
        length=len(nucleic_sequence)
        for i in range(length//3):
            n=i*3
            print(nucleic_sequence[n:n+3])
            protein=translate(nucleic_sequence[n:n+3])
            print(f"{i + 1}번째 코돈 : {protein}")
        if length%3!=0:
            print(f"나머지 : {nucleic_sequence[length//3*3]}")

appendList(Translating_RNA[0], "UUU");#페닐 알라닌
appendList(Translating_RNA[0], "UUC");#페닐 알라닌
appendList(Type_Protein, "페닐 알라닌");

appendList(Translating_RNA[1], "CUU");#류신
appendList(Translating_RNA[1], "CUC");#류신
appendList(Translating_RNA[1], "CUA");#류신
appendList(Translating_RNA[1], "CUG");#류신
appendList(Type_Protein, "류신");

appendList(Translating_RNA[2], "UCU");#세린
appendList(Translating_RNA[2], "UCC");#세린
appendList(Translating_RNA[2], "UCA");#세린
appendList(Translating_RNA[2], "UCG");#세린
appendList(Type_Protein, "세린");

appendList(Translating_RNA[3], "CCU");#프롤린
appendList(Translating_RNA[3], "CCC");#프롤린
appendList(Translating_RNA[3], "CCA");#프롤린
appendList(Translating_RNA[3], "CCG");#프롤린
appendList(Type_Protein, "프롤린");

appendList(Translating_RNA[4], "UAU");#시스테인
appendList(Translating_RNA[4], "UAC");#시스테인
appendList(Type_Protein, "시스테인");

appendList(Translating_RNA[5], "UGG");#트립토판
appendList(Type_Protein, "트립토판");

appendList(Translating_RNA[6], "CGU");#아르지닌
appendList(Translating_RNA[6], "CGC");#아르지닌
appendList(Translating_RNA[6], "CGA");#아르지닌
appendList(Translating_RNA[6], "CGG");#아르지닌
appendList(Type_Protein, "아르지닌");

appendList(Translating_RNA[7], "AUU");#아이소 류신
appendList(Translating_RNA[7], "AUC");#이이소 류신
appendList(Translating_RNA[7], "AUA");#아이소 류신
appendList(Type_Protein, "아이소 류신");

appendList(Translating_RNA[8], "AUG");#메싸이 오닌
appendList(Type_Protein, "메싸이 오닌");

appendList(Translating_RNA[9], "GUU");#발린
appendList(Translating_RNA[9], "GUA");#발린
appendList(Translating_RNA[9], "GUC");#발린
appendList(Translating_RNA[9], "GUG");#발린
appendList(Type_Protein, "발린");

main()
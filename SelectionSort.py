def selectionSort(vetor):
    n = len(vetor)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vetor[j]<vetor[min_idx]:
                min_idx=j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

vetor = [1, 3, 5, 4, 2, 6, 8, 7, 10, 9]
selectionSort(vetor)
print(vetor)
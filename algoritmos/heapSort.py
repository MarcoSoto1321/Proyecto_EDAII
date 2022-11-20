class heapsort:
    def __init__(self) -> None:
        pass

    def heapify(self, arr, N, i):
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2    
        if l < N and arr[largest].dato < arr[l].dato:
            largest = l
        if r < N and arr[largest].dato < arr[r].dato:
            largest = r
        if largest != i:
            arr[i].dato, arr[largest].dato = arr[largest].dato, arr[i].dato  # swap
            self.heapify(arr, N, largest)

    def heapSort(self, arr):
        N = len(arr)
        for i in range(N//2 - 1, -1, -1):
            self.heapify(arr, N, i)
        for i in range(N-1, 0, -1):
            arr[i].dato, arr[0].dato = arr[0].dato, arr[i].dato  # swap
            self.heapify(arr, i, 0)
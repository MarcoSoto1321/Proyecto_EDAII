class heapsort:
    def __init__(self) -> None:
        pass

    def heapify_diasParaEntregar(self, arr, N, i):
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2    
        if l < N and arr[largest].diasParaEntregar < arr[l].diasParaEntregar:
            largest = l
        if r < N and arr[largest].diasParaEntregar < arr[r].diasParaEntregar:
            largest = r
        if largest != i:
            arr[i].diasParaEntregar, arr[largest].diasParaEntregar = arr[largest].diasParaEntregar, arr[i].diasParaEntregar  # swap
            self.heapify_diasParaEntregar(arr, N, largest)

    def heapSort_diasParaEntregar(self, arr):
        N = len(arr)
        for i in range(N//2 - 1, -1, -1):
            self.heapify_diasParaEntregar(arr, N, i)
        for i in range(N-1, 0, -1):
            arr[i].diasParaEntregar, arr[0].diasParaEntregar = arr[0].diasParaEntregar, arr[i].diasParaEntregar  # swap
            self.heapify_diasParaEntregar(arr, i, 0)

    def heapify_urgencia(self, arr, N, i):
        largest = i  
        l = 2 * i + 1     
        r = 2 * i + 2    
        if l < N and arr[largest].urgencia < arr[l].urgencia:
            largest = l
        if r < N and arr[largest].urgencia < arr[r].urgencia:
            largest = r
        if largest != i:
            arr[i].urgencia, arr[largest].urgencia = arr[largest].urgencia, arr[i].urgencia  # swap
            self.heapify_urgencia(arr, N, largest)

    def heapSort(self, arr):
        N = len(arr)
        for i in range(N//2 - 1, -1, -1):
            self.heapify_urgencia(arr, N, i)
        for i in range(N-1, 0, -1):
            arr[i].urgencia, arr[0].urgencia = arr[0].urgencia, arr[i].urgencia  # swap
            self.heapify_urgencia(arr, i, 0)

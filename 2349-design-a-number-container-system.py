class NumberContainers:
    # hashmap with key = number, value = a sorted list (minheap for logn inserts) of indices
    # map with indec to number
    def __init__(self):
        self.index_to_number = {}
        self.num_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number

        heapq.heappush(self.num_to_indices[number], index)
                    


    def find(self, number: int) -> int:
        if not self.num_to_indices[number]:
            return -1

        while self.num_to_indices[number]:
            index = self.num_to_indices[number][0]

            if self.index_to_number[index] == number:
                return index

            heapq.heappop(self.num_to_indices[number])
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
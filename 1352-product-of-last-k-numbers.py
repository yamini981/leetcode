class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.products = []

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.products = []
        else:
            self.products.append(num)
        if len(self.products) > 1:
            self.products[-1] *= self.products[-2]
        


    # 3  0  2  5  4
    # 2 10 40

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        if k == len(self.products):
            return self.products[-1]
        return self.products[-1] // self.products[len(self.products) - k - 1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
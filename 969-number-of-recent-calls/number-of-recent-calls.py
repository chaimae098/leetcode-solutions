class RecentCounter:

    def __init__(self):
        self.request =[]


    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request and self.request[0]<t-3000:
            self.request.pop(0)
        return len(self.request)    



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
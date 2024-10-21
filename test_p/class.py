class Book():
    def __init__(self, page) -> int:
        self.open = int(page)
    
pnumber = Book(10)

print(pnumber.open)
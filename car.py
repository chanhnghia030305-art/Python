class Car:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

        
    def drive(self):
        print(f"Bạn đang lái chiếc xe {self.name} của hãng {self.brand} màu {self.color}.")
        
        
kiaMorning = Car("KIA Morning", "KIA", "Đỏ")
kiaMorning.drive()  # Output: Bạn đang lái chiếc xe KIA Morning của hãng KIA màu Đỏ.

ferrariF8 = Car("Ferrari F8", "Ferrari", "Đỏ")
ferrariF8.drive()  # Output: Bạn đang lái chiếc xe Ferrari F8 của hãng Ferrari màu Đỏ.
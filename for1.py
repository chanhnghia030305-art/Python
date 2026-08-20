colors = ("đỏ", "xanh", "vàng")
for c in colors:
    print(c)
    
info = {"tên": "An", "tuổi": 20} # lặp qua dictionary

for key in info:              # lặp qua key
    print(key)

for key, value in info.items():  # lặp qua cả key và value
    print(key, value)
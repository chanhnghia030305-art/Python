class Task:
    def __init__(self, name, done):
        self.name = name
        self.done = done
        
tasks = [
    Task("Lên kế hoạch", True),
    Task("Tìm dữ liệu", False),
    Task("Sắp xếp dữ liệu", False)
    
]

count = 0
for task in tasks:
    if task.done:
        status = "✅ Hoàn thành"
        count += 1
    else:
        status = "❌ Chưa hoàn thành"
    print(f"{task.name}: {status}")
    
print(f"Có {count}/{len(tasks)} đã hoàn thành")
          
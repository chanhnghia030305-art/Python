# task_plus.py
class Task:
    def __init__(self, ten_task, hoan_thanh=False):
        self.ten_task = ten_task
        self.hoan_thanh = hoan_thanh

    def danh_dau_hoan_thanh(self):
        self.hoan_thanh = True

    def __str__(self):
        trang_thai = "✔" if self.hoan_thanh else "✘"
        return f"[{trang_thai}] {self.ten_task}"
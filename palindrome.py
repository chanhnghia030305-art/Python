def isPalindrome(x: int) -> bool:
    # Số âm không thể là palindrome (vì dấu "-" ở đầu)
    # Số kết thúc bằng 0 (trừ số 0) cũng không thể là palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10

    # Nếu số chữ số chẵn: x == reverted
    # Nếu số chữ số lẻ: x == reverted // 10 (bỏ chữ số giữa)
    return x == reverted or x == reverted // 10


print(isPalindrome(122))  
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Bước 1: Tìm vị trí xuất hiện đầu tiên của ký tự ch trong chuỗi word
        index = word.find(ch)
        
        # Bước 2: Nếu không tìm thấy ký tự ch, trả về nguyên chuỗi ban đầu
        if index == -1:
            return word
        
        # Bước 3: Nếu tìm thấy, ta sẽ đảo ngược đoạn từ đầu (0) đến vị trí index (bao gồm ch)
        # word[:index+1] là đoạn từ đầu đến index
        # [::-1] là cú pháp đảo ngược chuỗi
        reversed_part = word[:index+1][::-1]
        
        # Bước 4: Ghép đoạn đã đảo ngược với phần còn lại của chuỗi (từ index+1 trở đi)
        result = reversed_part + word[index+1:]
        
        # Bước 5: Trả về kết quả cuối cùng
        return result
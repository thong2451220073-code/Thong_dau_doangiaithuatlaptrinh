class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Tách chuỗi thành danh sách các từ
        words = title.split()
        
        # Duyệt từng từ trong danh sách
        for i in range(len(words)):
            
            # Nếu độ dài từ <= 2 → viết thường toàn bộ
            if len(words[i]) <= 2:
                words[i] = words[i].lower()
            
            # Nếu độ dài >= 3 → viết hoa chữ đầu, còn lại viết thường
            else:
                words[i] = words[i].capitalize()
        
        # Ghép các từ lại thành chuỗi, cách nhau bằng dấu cách
        return " ".join(words)
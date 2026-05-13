class Solution:
    def convertTemperature(self, celsius):

        # Đổi sang Kelvin
        kelvin = celsius + 273.15

        # Đổi sang Fahrenheit
        fahrenheit = celsius * 1.8 + 32

        # Trả về kết quả
        return [kelvin, fahrenheit]
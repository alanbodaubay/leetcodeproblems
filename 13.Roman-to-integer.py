class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_values[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

def main():
    roman_numeral = input("Roman numeral: ").strip().upper()
    solution = Solution()
    result = solution.romanToInt(roman_numeral)
    print(f"Integer of {roman_numeral} is {result}")

if __name__ == "__main__":
    main()
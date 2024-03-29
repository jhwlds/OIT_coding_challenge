class RomanNumerals:

    roman_to_int_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    
    int_to_roman_mapping = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def to_roman(self, num, result=''):

        if num > 3999:
            raise ValueError("The number is higher than 3,999!")
        
        if num == 0:
            return result
        
        for value in sorted(self.int_to_roman_mapping.keys(), reverse=True):

            if num >= value:
                result += self.int_to_roman_mapping[value] 
                num -= value  
                return self.to_roman(num, result)
            
    
    def to_decimal(self, s, index=0):

        if index == len(s):
            return 0
        
        #Check if two letters are counted as roman numerals
        if index + 1 < len(s) and s[index:index+2] in self.roman_to_int_mapping:
            value = self.roman_to_int_mapping[s[index:index+2]]
            return value + self.to_decimal(s, index + 2)
        
        else:
            value = self.roman_to_int_mapping[s[index]]
            return value + self.to_decimal(s, index + 1)
    
    def is_valid_roman(self, s):

        try:
            value = self.to_decimal(s)
            if s == self.to_roman(value):
                return True
            else:
                raise ValueError
            
        except (KeyError, ValueError):
            return False
        


        

        
def get_user_input():
    converter = RomanNumerals()
    while True:
        print("\nChoose the conversion type:")
        print("1: Number to Roman Numeral")
        print("2: Roman Numeral to Number\n")
        conversion_type = input("Enter your choice (type 'end' to exit): ")
        
        if conversion_type.lower() == 'end':

            print("Exiting the program.")
            break

        if conversion_type not in ['1', '2']:

            print()
            print("-"*35)
            print("Invalid choice. Please try again.")
            print("-"*35)
            continue 
        
        while conversion_type == '1':

            user_input = input("\nPlease enter a number or menu to go back to menu: ")

            if user_input.lower() == 'menu':
                break

            try:
                num = int(user_input)
                print(f"\nRoman numeral: {converter.to_roman(num)}")

            except ValueError as e:
                print()
                print("-"*75)
                print(f"Error: {e}. Please try again.")
                print("-"*75)
            


        while conversion_type == '2':



            user_input = input("\nPlease enter a Roman numeral or menu to go back to menu: ").upper()

            if user_input.lower() == 'menu':
                break

            if not converter.is_valid_roman(user_input):
                print("\n" + "-"*70)
                print("Error: Invalid Roman numeral. Please try again.")
                print("-"*70)
                continue

            try:
                result = converter.to_decimal(user_input)
                print(f"\nDecimal number: {result}")

            except KeyError as e:
                
                print("\n" + "-"*70)
                print("Error: Invalid Roman numeral. Please try again.")
                print("-"*70)


if __name__ == "__main__":
    get_user_input()





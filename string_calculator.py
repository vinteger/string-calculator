class StringCalculator:
    def add(self, numbers):
        sum = 0
        if not numbers:
            return 0

        str_arr = numbers.split(",")
        for number in str_arr:
            another_str = number.split("\n")
            for number in another_str:

                sum += int(number)

        return sum

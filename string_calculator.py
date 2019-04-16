import re


class StringCalculator:

    def add(self, numbers):

        total = 0
        negative_numbers = []

        if not numbers:
            return 0

        has_delimiter = re.split("^//(.*)\n", numbers)
        has_long_delimiter = re.split("^//\[(.*)\]\n", numbers)

        delimiter = ','

        if len(has_delimiter) > 1:
            _, delimiter, numbers = has_delimiter

        if len(has_long_delimiter) > 1:
            _, delimiter, numbers = has_long_delimiter

        for line in numbers.split("\n"):

            for delimited in line.split(delimiter):
                value = int(delimited)

                if value < 0:
                    negative_numbers.append(delimited)

                if value > 1000:
                    value = 0

                total += value

        if len(negative_numbers) > 0:
            raise ValueError("negatives not allowed: " + ", ".join(negative_numbers))

        return total

import re


class StringCalculator:

    def add(self, numbers):

        total = 0

        if not numbers:
            return 0

        has_delimiter = re.split("^//(.*)\n", numbers)

        delimiter = ','
        if len(has_delimiter) > 1:
            _, delimiter, numbers = has_delimiter

        for line in numbers.split("\n"):

            for delimited in line.split(delimiter):
                value = int(delimited)
                if value < 0:
                    raise ValueError("negatives not allowed: "+delimited)
                total += value

        return total

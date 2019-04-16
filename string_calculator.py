import re


class StringCalculator:

    def add(self, numbers):

        total = 0
        negative_numbers = []

        if not numbers:
            return 0

        has_delimiter = re.split("^//(.*)\n", numbers)
        has_long_delimiter = re.split("^//\[(.*)\]\n", numbers)

        delimiters = [',', '\n']

        if len(has_delimiter) > 1:
            _, delimiter, numbers = has_delimiter
            delimiters = [delimiter]

        if len(has_long_delimiter) > 1:
            _, delimiter, numbers = has_long_delimiter
            delimiters = delimiter.split("][")

        numbers = self.flatten(self.split_strings(numbers, delimiters))

        for n in numbers:
            value = int(n)

            if value < 0:
                negative_numbers.append(n)

            if value > 1000:
                value = 0

            total += value

        if len(negative_numbers) > 0:
            raise ValueError("negatives not allowed: " + ", ".join(negative_numbers))

        return total

    def split_strings(self, numbers, delimiters):
        if delimiters:
            split = numbers.split(delimiters[0])
            return [self.split_strings(s, delimiters[1:]) for s in split]
        else:
            return numbers

    def flatten(self, lst):
        return sum(([x] if not isinstance(x, list) else self.flatten(x)
                    for x in lst), [])

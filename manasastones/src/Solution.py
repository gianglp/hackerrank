# a case has a number of stones, value a and value b
class Case:
    def __init__(self, number_of_stones, a, b):
        self.number_of_stones = number_of_stones
        self.a = a
        self.b = b

    def find_last_stones(self):
        result = []
        # we already have the first stone which is always 0
        number_of_stones_to_guess = self.number_of_stones - 1

        '''
        we only have 2 possible values, so this is similar to a sequence of coins problem
        2 value would be tail or head.
        a number of stones to guess equals to the number of coins
        we have a total of 2**(number_of_stones_to_guess) probabilities
        the final stone value would be
        last_stone_value = a * (number of heads in the sequence) + b * (number of tails in the sequence)
        last_stone_value = a * (number of heads) + b * [(number of stones to guess) - number of heads]
        we just have to go through all possible pairs by iterate from 0 -> nuber of coins and calculate the
        last stone value using the formular above
        '''
        for index in range(0, number_of_stones_to_guess, 1):
            last_start_with_a = self.a * index + self.b * (number_of_stones_to_guess - index)
            result.append(last_start_with_a)

            last_start_with_b = self.b * index + self.a * (number_of_stones_to_guess - index)
            result.append(last_start_with_b)
        result = sorted(set(result))

        print(*result)

# first number is number of case
number_of_cases = int(input().strip())
cases = []
for i in range(number_of_cases):
    stones = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    cases.append(Case(stones, a, b))
for case in cases:
    case.find_last_stones()

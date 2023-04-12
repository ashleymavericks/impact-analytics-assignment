from functools import lru_cache

class GraduationCeremony:
    def __init__(self, num_days):
        if num_days < 4:
            raise Exception("Invalid Input, num_days should be 4 or greater")
        self.num_days = num_days


    def total_ways_to_attend_classes(self):

        @lru_cache(None)
        def recursive_calculation(num_days, num_consecutive_missed):
            # not allowed to miss classes for four or more consecutive days.
            if num_consecutive_missed == 4:
                return 0
            if num_days == 0:
                return 1

            return recursive_calculation(num_days - 1, 0) + recursive_calculation(num_days - 1, num_consecutive_missed + 1)

        total_ways_to_attend = recursive_calculation(self.num_days, 0)
        total_ways_to_miss_last_day = recursive_calculation(self.num_days - 1, 1)

        return f"{total_ways_to_miss_last_day}/{total_ways_to_attend}"


if __name__ == "__main__":
    inputs = [5, 10, 12, 17]  # number of academic days
    for i in inputs:
        graduation = GraduationCeremony(i)
        print(f"For {i} days: {graduation.total_ways_to_attend_classes()}")

 
## Output:
# For 5 days: 14/29
# For 10 days: 372/773
# For 12 days: 1382/2872
# For 17 days: 36776/76424

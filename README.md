# Approach
- Dynamic Programming (Memoization)
- Base cases
  - `num_consecutive_missed = 4`, which represents the maximum number of consecutive days that cannot be missed, then the current sequence of missed days is not valid and the function returns 0.
  - `num_days = 0`, which represents the last day then the function returns 1, as there is only one way to attend classes on the last day.

- Recursive calls
```python
# represents attending class on the current day, so num_consecutive_missed is reset to 0
recursive_calculation(num_days - 1, 0) 
  
# represents missing class on the current day, so m is incremented by 1
recursive_calculation(num_days - 1, num_consecutive_missed + 1) 
```

- The sum of these two recursive calls represents the total number of valid ways to attend classes from the current day onwards.

# Time and Space complexity
- Time Complexity: O(num_days)
- Space Complexity: O(num_days)

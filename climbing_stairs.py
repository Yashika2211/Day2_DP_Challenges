"""
LeetCode 70: Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    # Base cases
    if n <= 2:
        return n
    

    one_step_before = 2  # Ways to climb 2 stairs
    two_steps_before = 1  # Ways to climb 1 stair
    current = 0
    

    for i in range(3, n + 1):

        current = one_step_before + two_steps_before
        

        two_steps_before = one_step_before
        one_step_before = current
    
    return one_step_before

# Test cases
if __name__ == "__main__":
    test_cases = [2, 3, 4, 5, 10]
    for test in test_cases:
        print(f"n = {test}, distinct ways = {climbStairs(test)}")


# Day 2 - Dynamic Programming Challenges  

Welcome to my repository! This is part of my **60 Days to Code, Create & Conquer Challenge**.  
Here, I've included solutions to two dynamic programming problems I tackled today.

## 📝 Problems Solved:

### 1. Climbing Stairs (LeetCode 70)
   - **Problem**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
   - **Approach**: Optimized using Bottom-Up DP with constant space.  
   - **Complexity**: Time O(n), Space O(1).  
   - **Key Insight**: This is essentially a Fibonacci sequence where F(n) = F(n-1) + F(n-2).

### 2. Longest Common Subsequence (LeetCode 1143)
   - **Problem**: Given two strings text1 and text2, return the length of their longest common subsequence.
   - **Approach**: Solved using a DP table and also implemented a space-optimized version.  
   - **Complexity**: Time O(n * m), Space O(n * m) or O(min(n,m)) for optimized version.  
   - **Key Insight**: The DP state transition is based on whether characters match or not.

## 🧠 Dynamic Programming Takeaways:

1. **Identify the Subproblems**: Break down the problem into smaller, overlapping subproblems.
2. **Define State**: Clearly define what each state in your DP table represents.
3. **Establish Recurrence Relation**: Determine how to calculate the current state from previous states.
4. **Base Cases**: Set up the initial values for your DP table.
5. **Space Optimization**: Consider if you can reduce space complexity by using rolling arrays or variables.

## 🚀 How to Run:

1. Clone the repository:  
   ```bash
   git clone https://github.com/YashikaBhatia/Day2_DP_Challenges.git

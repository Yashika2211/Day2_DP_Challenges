"""
LeetCode 1143: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.
"""

def longestCommonSubsequence(text1, text2):
 
    # Get the lengths of both strings
    m, n = len(text1), len(text2)
    
    # dp[i][j] represents the length of LCS for text1[0...i-1] and text2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
           
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
           
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    
    return dp[m][n]


def longestCommonSubsequence_optimized(text1, text2):
   
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    
    # We only need two rows: current and previous
    prev_row = [0] * (n + 1)
    curr_row = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr_row[j] = prev_row[j - 1] + 1
            else:
                curr_row[j] = max(prev_row[j], curr_row[j - 1])
        
        # Swap rows for next iteration
        prev_row, curr_row = curr_row, [0] * (n + 1)
    
    return prev_row[n]

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("bsbininm", "jmjkbkjkv")
    ]
    
    for text1, text2 in test_cases:
        lcs_length = longestCommonSubsequence(text1, text2)
        lcs_length_opt = longestCommonSubsequence_optimized(text1, text2)
        print(f"Text1: '{text1}', Text2: '{text2}'")
        print(f"LCS Length: {lcs_length}, Optimized: {lcs_length_opt}\n")


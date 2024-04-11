x = "01101110"
y = "10101000"
z = "0110110011101000"
'''
Both Time Complexity and Space Complexity are O(N*M) where N and M are lengths of x and y.
'''
def shuffling(x, y, z):
    a = len(x)
    b = len(y)
    if len(z) != a + b:
        return "Impossible!"
    dp = [[0]*(b) for i in range(b)]
    dp[0][0] = 1
    for i in range(1, a):
        dp[i][0] = int(dp[i - 1][0] and x[i - 1] == z[i - 1])
    for j in range(1, b):
        dp[0][j] = int(dp[0][j - 1] and y[j - 1] == z[j - 1])
    for i in range(1, a):
        for j in range(1, b):
            dp[i][j] = int(dp[i - 1][j] and (x[i - 1] == z[i + j - 1]) or (dp[i][j - 1] and (y[j - 1] == z[i + j - 1])))
    return dp[-1][-1] == 1 
if __name__ == "__main__":
    print(shuffling(x, y, z))

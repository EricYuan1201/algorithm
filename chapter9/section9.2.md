#9 62.不同路径，63. 不同路径 II

##9 62.不同路径

之前写过，复习下

```java
public int uniquePaths(int m, int n) {
    int[][] dp = new int[m][n];
    dp[0][0] = 0;
    for (int i = 0; i < m; i++) {
        dp[i][0] = 1;
    }
    for (int j = 0; j < n; j++) {
        dp[0][j] = 1;
    }
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[m - 1][n - 1];
}

```
##63. 不同路径 II

之前写过

```java
public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    //走到第i，j的时候的步数
    //假设是3行4列。
    int[][] dp = new int[obstacleGrid.length][obstacleGrid[0].length];
    int obstacleI = -1;
    for (int i = 0; i < obstacleGrid[0].length; i++) {
        if (obstacleGrid[0][i] == 1) {
            obstacleI = i;
            dp[0][i] = 0;
        } else if (obstacleI >= 0 && i > obstacleI) {
            dp[0][i] = 0;
        } else {
            dp[0][i] = 1;
        }
    }
    int obstacleJ = -1;
    for (int j = 0; j < obstacleGrid.length; j++) {
        if (obstacleGrid[j][0] == 1) {
            obstacleJ = j;
            dp[j][0] = 0;
        } else if (obstacleJ >= 0 && j > obstacleJ) {
            dp[j][0] = 0;
        } else {
            dp[j][0] = 1;
        }
    }
    for (int i = 1; i < obstacleGrid.length; i++) {
        for (int j = 1; j < obstacleGrid[0].length; j++) {
            if (obstacleGrid[i][j] == 1) {
                continue;
            }
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
}

```

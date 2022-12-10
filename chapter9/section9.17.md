#6 583. 两个字符串的删除操作，72. 编辑距离

##6 583. 两个字符串的删除操作

之前做过这个题目，有点印象

```java
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            char c1 = word1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                char c2 = word2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        int lcs = dp[m][n];
        return m - lcs + n - lcs;
    }

```
##72. 编辑距离

看过，依然做不来。

```java
public int minDistance(String word1, String word2) {
    int n = word1.length();
    int m = word2.length();

    // 有一个字符串为空串
    if (n * m == 0) {
        return n + m;
    }

    // DP 数组
    int[][] D = new int[n + 1][m + 1];

    // 边界状态初始化
    for (int i = 0; i < n + 1; i++) {
        D[i][0] = i;
    }
    for (int j = 0; j < m + 1; j++) {
        D[0][j] = j;
    }

    // 计算所有 DP 值
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < m + 1; j++) {
            int left = D[i - 1][j] + 1;
            int down = D[i][j - 1] + 1;
            int left_down = D[i - 1][j - 1];
            if (word1.charAt(i - 1) != word2.charAt(j - 1)) {
                left_down += 1;
            }
            D[i][j] = Math.min(left, Math.min(down, left_down));
        }
    }
    return D[n][m];
}


```

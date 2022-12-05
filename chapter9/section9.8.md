#6 139.单词拆分，背包问题总结篇！

##6 139.单词拆分

https://leetcode.cn/problems/word-break/solution/dan-ci-chai-fen-by-leetcode-solution/

看了一下题解

```java

public boolean wordBreak(String s, List<String> wordDict) {
    Set<String> wordDictSet = new HashSet(wordDict);
    boolean[] dp = new boolean[s.length() + 1];
    dp[0] = true;
    for (int i = 1; i <= s.length(); i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length()];
}

```
##背包问题总结篇！



```java


```

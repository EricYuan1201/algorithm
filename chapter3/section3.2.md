#day07 454.四数相加II，383. 赎金信， 15. 三数之和，18. 四数之

##day07 454.四数相加II

四数一分为二？

```java

public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i : nums1) {
        for (int j : nums2) {
            map.put(i + j, map.getOrDefault(i + j, 0) + 1);
        }
    }
    int res = 0;
    for (int j : nums3) {
        for (int k : nums4) {
            if (map.containsKey(-(j + k))) {
                res += map.get(-(j + k));
            }
        }
    }
    return res;
}

```
##383. 赎金信

学习一下char用法


```java

public boolean canConstruct(String ransomNote, String magazine) {
  if (magazine.length() < ransomNote.length()) {
     return false;
  }
  int[] arr = new int[26];
  for (char c1: magazine.toCharArray()) {
     arr[c1 - 'a'] ++;
  }
  for (char c2: ransomNote.toCharArray()) {
     arr[c2 - 'a'] --;
     if (arr[c2 - 'a'] < 0) {
        return false;
     }
  }
  return true;
}

```
##15. 三数之和

用map确实能实现，但是效率非常之低


```java

public static List<List<Integer>> threeSum(int[] nums) {
    if (nums == null || nums.length == 0) {
        return null;
    }
    Arrays.sort(nums);
    Set<List<Integer>> lists = new HashSet<>();
    for (int i = 0; i < nums.length; i++) {
        if (i >= 1 && nums[i] == nums[i - 1]) continue;
        Map<Integer, Integer> map = new HashMap<>();
        for (int j = i + 1; j < nums.length; j++) {
            if (map.containsKey(-nums[i] - nums[j])) {
                List<Integer> list = Arrays.asList(nums[i], nums[j], -nums[i] - nums[j]);
                lists.add(list);
            } else {
                map.put(nums[j], j);
            }
        }
    }
    return new ArrayList<>(lists);
}	

```
##18. 四数之和



```java


```

#242.有效的字母异位词，349. 两个数组的交集， 202. 快乐数，1. 两数之和

##242.有效的字母异位词

之前写过这个题？

```java

public boolean isAnagram(String s, String t) {
  Map<Character, Integer> map = new HashMap<>();
  char[] charsS = s.toCharArray();
  char[] charsT = t.toCharArray();
  for (char s1 : charsS) {
     if (map.containsKey(s1)) {
        map.put(s1, map.get((Character) s1) + 1);
     } else {
        map.put(s1, 1);
     }
  }
  for (char t1 : charsT) {
     if (map.containsKey(t1)) {
        map.put(t1, map.get(t1) -1);
     } else {
        return false;
     }
  }
  for (Character character : map.keySet()) {
     Integer integer = map.get(character);
     if (integer != 0) {
        return false;
     }
  }
  return true;
}
   
```
##349. 两个数组的交集

这个题不写了，直接用set就行。

```java

Set<Integer> set = new HashSet<>();

HashMap<Character, Integer> map = new HashMap<>();

```
##202. 快乐数


有循环的情况倒是没有想出来

```java

public static boolean isHappy(int n) {
  Set<Integer> set = new HashSet<>();

  while (n != 1 && !set.contains(n)) {
     set.add(n);
     n = getNext(n);
  }
  return n == 1;
}

public static int getNext(int n) {
  int sum = 0;
  int d = 0;
  while (n > 0) {
     d = (n % 10);
     n = n / 10;
     sum += d * d;
  }
  return sum;
}

```
##1. 两数之和

入门题，没什么好说的。

```java

public int[] twoSum(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
        return null;
    }
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        if (map.containsKey(target - nums[i])) {
            return new int[]{i, map.get(target -nums[i])};
        } else {
            map.put(nums[i], i);
        }
    }
    return null;
}

```

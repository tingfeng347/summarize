

DFS一般在树，图，网格结构中使用

```java
	//岛屿的周长463
class Solution {
    public int islandPerimeter(int[][] grid) {
        int n=grid.length;
        int m=grid[0].length;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    return dfs(grid,i,j);
                }
            }
        }
        return 0;
 }
 public int dfs(int [][]grid,int i,int j){
       int n=grid.length;
        int m=grid[0].length;
     if(i<0||i>=n||j<0||j>=m){
         return 1;
     }
     if(grid[i][j]==0){
         return 1;
     }
     if(grid[i][j]==2){
         return 0;
     }
     grid[i][j]=2;
     return
     dfs(grid,i+1,j)+
     dfs(grid,i-1,j)+
     dfs(grid,i,j+1)+
     dfs(grid,i,j-1);
 }
}
//////////////////

      int dx[]={0,1,0,-1};
     int dy[]={1,0,-1,0};
     int n=grid.length;
     int m=grid[0].length;
     int ans=0;
     for(int i=0;i<n;i++){
         for(int j=0;j<m;j++){
             if(grid[i][j]==1){
                 int cnt=0;
                 for(int k=0;k<4;k++){
                     int xx=dx[k]+i;
                     int yy=dy[k]+j;
                     if(xx<0||xx>=n||yy<0||yy>=m||grid[xx][yy]==0){
                         cnt+=1;
                     }
                 }ans+=cnt;
             }
         }
     }
return ans;
```



```java
DFS，  对于这一题LCP07 ，最先会想到动态规划
    
class Solution {
    int ways,n,k;
    List<List<Integer>>edges;
    public int numWays(int n, int[][] relation, int k) {
        ways=0;
        this.n=n;
        this.k=k;
    edges=new  ArrayList<List<Integer>>();
    for(int i=0;i<n;i++){
        edges.add(new ArrayList<Integer>());
    }
    for(int[] edge :relation){
        int src=edge[0],dst=edge[1];
        edges.get(src).add(dst);
    }
    dfs(0,0);
    return ways;
    }
    public void dfs(int index,int steps){
        if(steps==k){
            if(index==n-1){
                ways++;
            }
            return;
        }
        List<Integer>list =edges.get(index);
        for(int n:list){		//0-1  1-3 3-5
            dfs(n,steps+1);
        }
    }
}
```

![image-20230911181352708](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20230911181352708.png)

![image-20230911181436193](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20230911181436193.png)

```java
337打家劫舍
    
    public int rob(TreeNode root) {
    if (root == null) return 0;

    int money = root.val;
    if (root.left != null) {
        money += (rob(root.left.left) + rob(root.left.right));
    }

    if (root.right != null) {
        money += (rob(root.right.left) + rob(root.right.right));
    }

    return Math.max(money, rob(root.left) + rob(root.right));
}
////////////////////////////////////   记忆化 - 解决重复子问题，引用数组，或map

public int rob(TreeNode root) {
    HashMap<TreeNode, Integer> memo = new HashMap<>();
    return robInternal(root, memo);
}

public int robInternal(TreeNode root, HashMap<TreeNode, Integer> memo) {
    if (root == null) return 0;
    if (memo.containsKey(root)) return memo.get(root);
    int money = root.val;

    if (root.left != null) {
        money += (robInternal(root.left.left, memo) + robInternal(root.left.right, memo));
    }
    if (root.right != null) {
        money += (robInternal(root.right.left, memo) + robInternal(root.right.right, memo));
    }
    int result = Math.max(money, robInternal(root.left, memo) + robInternal(root.right, memo));
    memo.put(root, result);
    return result;
}
//////////////////////////////////////// 用一个数组，来表示偷与不偷 ，arr[0]不偷,arr[1]

public int rob(TreeNode root) {
    int[] result = robInternal(root);
    return Math.max(result[0], result[1]);
}

public int[] robInternal(TreeNode root) {
    if (root == null) return new int[2];
    int[] result = new int[2];

    int[] left = robInternal(root.left);
    int[] right = robInternal(root.right);

    result[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    result[1] = left[0] + right[0] + root.val;

    return result;
}


```


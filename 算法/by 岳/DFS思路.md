





```java
一个整体，拆分成一个小部分，进行构思解决，
    例：一个n叉树求高度，那我们可以先求一个子树的高度，此高度需要返回，所以高度可以在叶子节点的时候返回+1；子树的高度获取后是不是得保存一下，所以递归后加一行比较。依次向上返回，直到求出高度。
    问：何时递归
    
    
```

# 递归+记忆化搜

```java

class Solution {931力扣   递归+记忆化搜索绝了  动态规划也可以解决  想想用二维数组就解决他  向这种俩东西，返回的还是一个数值，不要犹豫直接上
    int n,m;
   int arr[][];
    public int minFallingPathSum(int[][] matrix) {
        n=matrix.length;
        m=matrix[0].length;
      
        int jk=Integer.MAX_VALUE;
arr=new int [n][m];
for(int i=0;i<n;i++){						//定
    Arrays.fill(arr[i],Integer.MIN_VALUE);	//定
    
}

    for(int j=0;j<m;j++){
        
     jk= Math.min(dfs(matrix,n-1,j),jk) ;
    }

return jk;
    }
    int dfs(int[][] matrix,int i,int j){
        if(j<0||j>=m){
            return Integer.MAX_VALUE;
        }
       
        if(i==0){         
            return  matrix[0][j];
        }
   if(arr[i][j]!=Integer.MIN_VALUE)return arr[i][j]; //定
   return arr[i][j]=Math.min(Math.min(dfs(matrix,i-1,j),dfs(matrix,i-1,j-1)),dfs(matrix,i-1,j+1)) +matrix[i][j];    
       
    }
}
```

```java
class Solution {
    int [][] mm;
    char[] s,t;
    public int minDistance(String word1, String word2) {
        s=word1.toCharArray();
        t=word2.toCharArray();
        int n=s.length;
        int m=t.length;
mm=new int[n][m];
    for(int i=0;i<n;i++){
        Arrays.fill(mm[i],-1);
    }
    return dfs(n-1,m-1);
    }
    int dfs(int i,int j){
        if(i<0)return j+1;
        if(j<0)return i+1;
        if(mm[i][j]!=-1)return mm[i][j];
        if(s[i]==t[j]){return mm[i][j]=dfs(i-1,j-1);}   //01背包的选与不选
        return mm[i][j]=Math.min(Math.min(dfs(i-1,j),dfs(i,j-1)),dfs(i-1,j-1))+1; //这是几种不同的情况
    }

}再贴一个
```

```java
class Solution { 322  完全背包选与不选
    int []coin;
    int  memo[][];
    public int coinChange(int[] coins, int amount) {
        coin=coins;
       int n=coins.length;
       memo=new int[n][amount+1];
       for(int i=0;i<n;i++){
           Arrays.fill(memo[i],-1);
       }
    int ans=   dfs(n-1,amount);
return ans<Integer.MAX_VALUE/2?ans:-1;
    }int dfs(int i,int c){
        if(i<0)return c==0?0:Integer.MAX_VALUE/2;
        if(memo[i][c]!=-1)return memo[i][c];
        if(c<coin[i])return memo[i][c]=dfs(i-1,c);
        return memo[i][c]=Math.min(dfs(i-1,c),dfs(i,c-coin[i])+1);
    }
}

```

学弟亲传，快读快写，外加回溯用boolean，然后用动态数组能加快速度，比数组要好一点

```java
package 竞赛;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class yym5 {
	static StreamTokenizer st = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
	static PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

	static ArrayList<Integer>[] li;

	public static void main(String[] args) throws Exception {

		int n = Int();
		int q = Int();
		li = new ArrayList[n + 1];
		for (int i = 0; i < n; i++) {
			int f = Int();
			int g = Int();
			if (li[f] == null)
				li[f] = new ArrayList();
			li[f].add(g);
		}

		for (int i = 0; i < q; i++) {
			int as = Int();
			ArrayList<Integer> list = new ArrayList<>();

			pw.print(0 + " ");

			dfs(as, 0, list);

			for (int k = 0; k < list.size(); k++) {
				pw.print(list.get(k) + " ");
			}
			pw.println();

		}
		pw.flush();
	}

	static boolean dfs(int as, int k, ArrayList<Integer> list) {
		if (k == as) {

			return true;
		}
		if (li[k] == null)
			return false;
		for (int kl : li[k]) {
			{

				list.add(kl);
				boolean ss = dfs(as, kl, list);
				if (ss)
					return true;
				else
					list.remove(list.size() - 1);
			}

		}
		return false;
	}

	public static int Int() throws Exception {
		st.nextToken();
		return (int) st.nval;
	}
}
```


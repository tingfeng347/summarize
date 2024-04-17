```java
//1466   队列 入列第一个 判断令加  while  for  队列添加
class Solution {

    public int minReorder(int n, int[][] c) {
   List<List<int[]>> graph=new ArrayList<>();
    for(int i=0;i<n;i++){
        graph.add(new ArrayList<>());
    }
for(int[] uv:c){
    graph.get(uv[0]).add(new int[]{uv[1],1});
    graph.get(uv[1]).add(new int[]{uv[0],0});
}
int res=0;
Queue<Integer> queue=new LinkedList<>();
queue.offer(0);
boolean[]  vied=new boolean[n];
vied[0]=true;
while(!queue.isEmpty()){
    int u=queue.poll();
    for(int []v:graph.get(u)){
        if(vied[v[0]]){
            continue;
        }
        vied[v[0]]=true;
        res+=v[1];
        queue.offer(v[0]);
    }
}
return res;
}
}
```


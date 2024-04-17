# Docker 总结



## 1.黑马程序员





## 2.自己总结



**常见命令**

```bash
# 查看 docker 版本
$ docker --version

# 查看 docker 帮助文档 
$ docker --help

# 查看 docker 本地镜像列表
$ docker images

# 查看 docker 本地运行中的容器
$ docker ps
# 查看 docker 本地运行中的容器的ID
$ docker ps -q

# 查看 docker 本地的所有容器（运行中的、停止的）
$ docker ps -a
# 查看 docker 本地的所有容器ID（运行中的、停止的）
$ docker ps -a -q

# 登录 Docker Hub
$ docker login

# 退出 Docker Hub
$ docker logout

# 搜索 Docker Hub 中的镜像
$ docker search 镜像名:版本号

# 从 Docker Hub 拉取镜像到本地
$ docker pull 镜像名:版本号

# 利用 Dockerfile 构建镜像（在 Dockerfile 所在路径下）
$ docker build -t 镜像名:镜像Tag .

# 由镜像来启动一个容器
$ docker run 镜像ID/镜像名:Tag
# 启动镜像可以添加的参数
-d（在后台运行容器，守护进程）
-it（容器的 Shell 映射到当前的 Shell，然后你在本机窗口输入的命令，就会传入容器）
/bin/bash（容器启动以后，内部第一个执行的命令。这里是启动 Bash，保证用户可以使用 Shell（这个命令放在最后，与 -it 搭配））
--name（为容器取自定义名称）
-p 99:80（容器的 80 端口映射到本机的 99 端口）
--rm（在容器终止运行后自动删除容器文件）
-v 本机地址:容器地址（将主机的文件或目录挂载到容器里（只有一份源文件））

# 终止容器
$ docker stop 容器ID
# 终止所有容器（先查询出所有的容器ID再进行遍历终止）
$ docker stop $(docker ps -a -p)

# 强行终止容器（杀死容器）
$ docker kill 容器ID

# 启动已经生成、已经停止运行的容器
$ docker start 容器ID

# 将一个运行态的容器终止，然后再重新启动它
$ docker restart 容器ID

# 删除一个已经终止的容器
$ docker rm 容器ID

# 进入一个正在运行的 docker 容器
$ docker exec -it 容器ID /bin/bash
# 如果 docker run 命令运行容器的时候，没有使用 -it 参数，就要用这个命令进入容器。一旦进入了容器，就可以在容器的 Shell 执行命令了

# 在主机与容器之间拷贝文件/目录
$ docker cp 主机路径 容器ID:容器路径
$ docker cp 容器ID:容器路径 主机路径

# 将容器打包为镜像
$ docker commit -m "说明" -a "作者" 容器ID 镜像名:Tag

# 删除本地镜像
$ docker rmi 镜像ID/镜像名:Tag

# 查看日志
$ docker logs 容器ID
# 查看实时日志（可以看到实时动态过程日志）
$ docker logs -f 容器ID
# 查看日志（最后10行）
$ docker logs -f --tail=10 容器ID
# 指定日期查看日志
$ docker logs -f -t --since="2021-11-24" 容器ID
```


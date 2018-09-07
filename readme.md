# 一个网页视频播放

视频上传到哔哩哔哩、优酷等都需要审核，所以做了一个简单的视频的网页播放器，对于浏览器而言，播放的视频是需要用`h264`编码成`.mp4`格式的，所以首先要保证上传要进行播放的视频是用`h264`编码的`.mp4`格式的。

### 步骤

1. 克隆我的项目到本地：

   `git clone git@github.com:Jim0618/simple-video-webpage-flask.git`

2. 将视频命名为`paper-talk.mp4`,放进`video`文件夹里
3. 在主目录运行：`nohup python main.py &`

### 注意

1. 默认访问地址是：`http://<your local IP>:8200`,譬如：`http://123.4.56.7:8200`,`<your local IP>`是你本机的`ip`地址。
2. 网页该视频播放的尺寸是：` width="1404" height="928" `,这可以进行修改。

3. 直接杀死进程就可以停止网页访问
4. 本地`python`需要安装`flask`


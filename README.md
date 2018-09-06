# getzhihu

## 提取知乎问答页面信息的小程序

### 要求：

基于pyhon3.0

安装beautifulsoup4
```shell
pip3 install beautifulsoup4
```

### 使用方法：
1. 将知乎问答页面的网页源代码保存到当前目录html.txt文件下；
2. 运行saveHtml2Txt.py脚本提取网页信息；
3. 注意保存网页源代码的方式，具体请参考下例。

提取到的内容会被保存到本目录下的一个txt文件中，文件名为问题名。


### 例：
- 打开任意一个问答页面；

- 如果问题描述没有完全展开，请点击 **显示全部**；

- 如果打开的是显示特定答案的页面，请点击 **查看全部 xxx 个回答**；

  ![点击显示全部](https://github.com/xuejianbest/images/blob/master/getzhihu/%E6%98%BE%E7%A4%BA.png)


- 为了页面能够加载出更多的答案，手动将浏览器竖直滚动条多往下拉几次；

- 按键盘F12，打开开发者工具，按照如下方式右键鼠标，复制html内容，并保存到当前目录下的html.txt文件；

  ![点击显示全部](https://github.com/xuejianbest/images/blob/master/getzhihu/%E7%BD%91%E9%A1%B5html.png)


- 运行当前目录下的脚本文件：
  ```shell
  pyhton3 saveHtml2Txt.py
  ```

- 运行成功显示`done....`，结果将保存为当前目录下txt文件。

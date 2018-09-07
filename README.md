# getzhihu

## 提取知乎问答页面信息的小程序

### 要求：

基于pyhon3.0

安装beautifulsoup4、lxml、selenium
```shell
pip3 install beautifulsoup4 lxml selenium
```

### 使用方法：
1. 将save2Html.py脚本内`url = 'https://***'`替换为需要获取的url地址；
2. 分别执行以下命令：
    ```shell
    python3 save2Html.py
    python3 save2Txt.py
    ```

提取到的内容会被保存到本目录下的一个txt文件中，文件名为问题名。


# 参与 FaceOff 开发

[English](contributing.md)

从仓库根目录运行 `python3 -m http.server 8000 --bind 127.0.0.1`，用桌面浏览器打开本地页面。资源包和加载器需要放在一起。

修改界面后，请启动受影响模式的一场对局，实际操作改动的设置或控件，再回到菜单。涉及联机时，用相同版本分别测试创建房间和加入房间。在拉取请求中记录浏览器、模式、实测结果及尚未验证的项目。

保留发行文件中的署名与第三方许可，同步更新对应的中英文文档。提交类型后写三个小写英文单词，例如 `docs: explain duel modes`。面向玩家的修改记入 Unreleased。发布时遵循语义化版本规范；公共游戏逻辑或网络代码的修改需请同伴审阅。

[组织贡献指南](https://github.com/BigBrainDevBros/.github/blob/main/contributing.zh-cn.md)

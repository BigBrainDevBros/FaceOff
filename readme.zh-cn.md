<div align="center">

# 对枪 FACEOFF

**在浏览器里直接玩的 1v1 回合制射击游戏**
*买枪、对枪、拿下回合。CS2 的伤害、护甲和固定弹道，8 把武器，4 张小地图，排位匹配，人机对战和点对点联机。不用安装，没有服务器。*

[![Play: Live](https://img.shields.io/badge/Play-Live%20on%20GitHub%20Pages-success.svg?style=flat-square&logo=githubpages)](https://bigbraindevbros.github.io/FaceOff/)
[![Bilibili Toy](https://img.shields.io/badge/Also%20on-Bilibili%20Toy-00A1D6.svg?style=flat-square&logo=bilibili&logoColor=white)](https://www.bilibili.com/toy/faceoff)
[![Version](https://img.shields.io/badge/Version-V10.1-blue.svg?style=flat-square)](#v10-更新内容)
[![Engine: Three.js](https://img.shields.io/badge/Engine-Three.js-black.svg?style=flat-square)](https://threejs.org)
[![Mode: 1v1](https://img.shields.io/badge/Mode-1v1%20Duel-orange.svg?style=flat-square)](#对局规则)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](license)

[在线游玩](https://bigbraindevbros.github.io/FaceOff/) · [B站 Toy 版](https://www.bilibili.com/toy/faceoff) · [English](readme.md) · [MIT 许可证](license)

[玩家指南](docs/wiki/home.zh-cn.md) · [贡献指南](contributing.zh-cn.md)

</div>

> [!NOTE]
> **官方发布地址，同一作者。** 《对枪 FACEOFF》只在两个地方发布：
> 本仓库（在线地址 [bigbraindevbros.github.io/FaceOff](https://bigbraindevbros.github.io/FaceOff/)）和
> [bilibili.com/toy/faceoff](https://www.bilibili.com/toy/faceoff)。两边出自同一位作者，不存在谁搬运谁。
> 两个版本的主菜单右下角都有指向对方的链接。

---

## Star History

<a href="https://www.star-history.com/?type=date&repos=BigBrainDevBros%2FFaceOff">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&legend=top-left" />
    <img alt="BigBrainDevBros/FaceOff Star History Chart" src="https://api.star-history.com/chart?repos=BigBrainDevBros%2FFaceOff&type=date&legend=top-left" />
  </picture>
</a>

---

**[English](readme.md)** • **[简体中文](readme.zh-cn.md)**

## 目录

- [开始游玩](#开始游玩)
- [对局规则](#对局规则)
- [武器与装备](#武器与装备)
- [地图](#地图)
- [段位](#段位)
- [联机](#联机)
- [按键](#按键)
- [V10 更新内容](#v10-更新内容)
- [隐私](#隐私)
- [自己部署](#自己部署)
- [许可证](#许可证)

---

## 开始游玩

用电脑浏览器（Chrome、Edge、Firefox 或 Safari）打开 **[bigbraindevbros.github.io/FaceOff](https://bigbraindevbros.github.io/FaceOff/)**，在主菜单选模式：

| 模式 | 内容 | 算段位分 |
| :--- | :--- | :--- |
| **排位赛** | 匹配真人对手，或打难度跟着段位走的排位人机 | 算 |
| **练习** | 自选地图和人机难度 | 不算 |
| **房间对战** | 开房间，把房间码发给朋友 | 不算 |

点一下游戏画面锁定鼠标就能开打。需要键盘和鼠标，暂不支持手机和平板。

## 对局规则

- **先赢 9 回合。** 打到 8:8 进入加赛，谁先领先 2 回合谁赢。
- **每回合：** 先在出生区短暂购买，然后开打。击倒对手就赢这一回合；时间到了，血量高的人赢。
- **别想蹲到结束：** 每回合最后一段时间，双方位置会定时互相暴露。
- **经济：** 开局 $800。赢回合、连败补偿、击杀都有钱拿。死了会丢掉除默认手枪外的全部装备，所以有时候存钱打手枪局是对的。

## 武器与装备

| 类别 | 武器 |
| :--- | :--- |
| 步枪 | AK-47、M4A4 |
| 狙击枪 | AWP |
| 冲锋枪 | MAC-10 |
| 手枪 | USP-S、Tec-9、沙漠之鹰 |
| 近战 | 刀 |

- **数值照 CS2。** 伤害、穿甲、射速、弹匣、价格、移速都按 CS2。爆头 ×4，腿 ×0.75，远了有衰减。
- **一枪爆头。** AK-47 和沙漠之鹰戴头盔也一枪死；M4A4 和 USP-S 要两枪。AWP 打头或身体都是一枪。
- **固定弹道。** 每把枪的后坐每次都一样（AK 前 10 发往上，之后左右摆），练熟了能往下压住。第一发永远打在准星上。
- **先停再打。** 跑着、跳着开枪基本打不中；松开方向键（或按反方向）大约 0.1 秒就恢复准度。
- **配件：** 所有枪都能开镜（鼠标右键），可以加装全息 / 红点（$200）或 2 倍镜（$500）。
- **护甲：** 防弹衣 $650 护身体；防弹衣 + 头盔 $1000（已有满甲只补头盔 $350）再护头。护甲 100 点，被打会掉。

## 地图

| 地图 | 特点 |
| :--- | :--- |
| 靶场 RANGE | 中线木箱、东侧长廊、两端高台 |
| 货场 DEPOT | 集装箱巷战、二层钢走道 |
| 天台 SKYLINE | 高楼屋顶、中央钢平台 |
| 庭院 PATIO | 小巷拐角、庭院与阳台 |

## 段位

- **段位：** 新手 → 枪手 → 射手 → 精锐 → 王牌 → 宗师（每段 III → I）→ 枪神。
- **匹配对手：** 优先匹配实力接近的在线玩家；30 秒没人可以改打排位人机。
- **排位人机：** 难度跟着段位走（新手 简单、枪手 普通、射手 困难、精锐及以上 职业），拿真人对局的一部分分数；王牌及以上打人机不再加减分。
- **定级赛：** 前 5 场匹配对局决定起始段位。
- **账号：** 在 B站 Toy 上玩，经你授权后使用 B站昵称和头像；在 GitHub Pages 上玩，会自动建一个本地账号。进度保存在浏览器里，段位页的**存档码**可以把进度转到另一台设备。
- 排位赛页面显示在线、正在匹配、正在对战的人数。匹配不需要服务器：第一个在线的玩家充当大厅，他离开后由别人自动接班。

## 联机

- **房间码：** 一人创建房间，把 5 位房间码发给对方，对方输入加入。
- **点对点直连：** 房主的浏览器负责运行对局，对方直接连过来，没有游戏服务器。
- **房间码连不上时，** 可以改用手动邀请码 / 回复码，或者打开 **联机对战 → 网络诊断** 查看是哪一步被拦住了。
- 双方版本必须一致。同一版本下，GitHub Pages 版和 B站 Toy 版可以互相联机。

## 按键

| 操作 | 按键 |
| :--- | :--- |
| 移动 | `W` `A` `S` `D` |
| 开火 | 鼠标左键 |
| 开镜 / 刀重击 | 鼠标右键 |
| 跳 / 蹲 | `Space` / `Ctrl` |
| 静步（没有脚步声） | `Shift` |
| 换弹 | `R` |
| 主武器 / 手枪 / 刀 / 道具 | `1` `2` `3` `4` |
| 捡枪 | `E` |
| 购买菜单 | `B` |
| 快捷购买：全装 / 经济 / 复购上回合 | `F1` / `F2` / `F3` |
| 跳过购买（人机局） | `F4` |
| 计分板 | `Tab` |
| 菜单 | `Esc` |

大部分按键可以在 **设置 → 键位** 里改，`B`、`Tab`、`Esc` 固定不变。

## V10 更新内容

- **CS2 枪法：** CS2 伤害、爆头 ×4、护甲点数、固定弹道、跑打惩罚、CS2 价格和经济。
- **排位赛页面（V9）：** 匹配对手、跟着段位走的排位人机、实时在线人数。练习和房间对战不再改变段位。
- **合并社区修复：** 命中框更准、穿箱子只算一次穿透、手雷不再卡进墙缝、补充人机寻路，人机更聪明（不再透视你的枪和血量、只瞄露出来的部位、会穿烟射击、会根据你前几回合的打法调整战术）。
- **新增：** 快捷购买键、回合伤害小结、暴露阶段脉冲、赛点紧张节拍、脚下影子。

## 隐私

- **没有统计、追踪和广告。**
- **只存在本地：** 设置、战绩和段位进度都保存在你的浏览器里。
- **联机时**只会连接公共的 PeerJS 信令服务和公共 STUN 服务器，用来帮双方建立直连；连上之后，对局数据直接在两名玩家之间传输。
- **在 B站 Toy 上玩时**，昵称和头像通过 B站自己的授权窗口读取，只用于显示。

## 自己部署

网站是纯静态文件：`index.html`，加上 `assets/pack-*.js` 和 `assets/boot.js`。把仓库根目录交给任何静态托管服务（GitHub Pages、Cloudflare Pages、Netlify、nginx）都能跑。

在本地试玩：

```bash
git clone https://github.com/BigBrainDevBros/FaceOff.git
cd FaceOff
python3 -m http.server 8000
```

然后打开 `http://localhost:8000`。

## 许可证

[MIT](license) © AMFI-Disable

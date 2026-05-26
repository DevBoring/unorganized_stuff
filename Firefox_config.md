1. 清除追踪参数 / 屏蔽遥测
这两个设置能防止你的浏览行为被追踪和回传。

· privacy.query_stripping.enabled：设为 true。Firefox 会自动去掉链接里用来追踪你的尾巴参数。
· toolkit.telemetry.enabled：设为 false。关闭火狐自己的遥测数据收集。

2. 隔绝网络窥探 / 关闭自动播放
可以防止你的操作习惯、设备状态甚至本地IP被网页嗅探到。

· dom.event.clipboardevents.enabled：设为 false。禁止网页知道你何时复制、剪切或粘贴了内容。
· dom.battery.enabled：设为 false。禁止网页读取你的设备电量信息。
· media.peerconnection.enabled：设为 false。这是最关键的一项，能彻底关闭 WebRTC，防止真实的本地和内网 IP 地址泄露。
· media.autoplay.default：设为 5。阻止所有网页的媒体自动播放，既防骚扰又防恶意利用。

3. 阻断后台预加载
能避免浏览器在后台偷偷进行网络连接，减少不必要的风险。

· network.prefetch-next：设为 false。禁止 Firefox 预先加载网页猜测你会点击的链接。
· browser.urlbar.speculativeConnect.enabled：设为 false。禁止在地址栏输入时，预先连接到推测的网址。
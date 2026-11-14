# setting up my pc or laptop

##通用

1. 載windows 刷入usb

2. `ei.cfg`
```
[Channel]
Retail

[VL]
0
```
放`sources`夾

3. 灌新電腦，選English(world)，windows pro (非N)

4. 用 `fn`+`shift`+`F10` 開 `cmd` 打`OOBE\BYPASSNRO`

5. 成功進桌面開始搞驅動，設定 > windows update 先自動載一遍，再去品牌網站或獨顯官網載一次補齊或更新。

##啟用windows pro & office

1. https://massgrave.dev/office_c2r_links#english-en-us 載 office

2. https://massgrave.dev/ 照步驟啟用 windows & office

3. 設定 > system > activation 檢查

## 初始化與提升效能

1. powershell 跑
```
irm https://christitus.com/win | iex
```
2. `install` 選要的app

3. `tweaks` 按 `advanced`

   取消勾選 `start menu previous layout - enable`
   
   勾選 `background apps - disable`

   勾選 `brave browser - debloat`

   勾選 `ipv6 - set ipv4 as preferred`

   勾選 `microsoft edge - debloat`

   勾選 `microsoft edge - remove`

   勾選 `teredo - disable`

   Run tweak

4. 按 O&O shutup10++

   `actions` > `apply only recommended settings`
   

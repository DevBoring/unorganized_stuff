# Firefox 隱私與安全設定

## 1. 清除追蹤參數 / 屏蔽遙測

這兩個設定能防止你的瀏覽行為被追蹤與回傳。

- `privacy.query_stripping.enabled`：設為 `true`  
  Firefox 會自動移除連結中用於追蹤的尾端參數。

- `toolkit.telemetry.enabled`：設為 `false`  
  關閉 Firefox 自身的遙測資料收集。

---

## 2. 隔絕網路窺探 / 關閉自動播放

可以防止網站嗅探你的操作習慣、裝置狀態，甚至本機 IP。

- `dom.event.clipboardevents.enabled`：設為 `false`  
  禁止網站得知你何時複製、剪下或貼上內容。

- `dom.battery.enabled`：設為 `false`  
  禁止網站讀取裝置電量資訊。

- `media.peerconnection.enabled`：設為 `false`  
  這是最重要的一項，可徹底關閉 WebRTC，防止真實本機與內網 IP 位址洩漏。

- `media.autoplay.default`：設為 `5`  
  阻止所有網站的媒體自動播放，避免騷擾與潛在惡意利用。

---

## 3. 阻擋背景預載

避免瀏覽器在背景偷偷建立網路連線，降低不必要的風險。

- `network.prefetch-next`：設為 `false`  
  禁止 Firefox 預先載入它猜測你可能會點擊的連結。

- `browser.urlbar.speculativeConnect.enabled`：設為 `false`  
  禁止在網址列輸入時，預先連線到推測的網站。
# Firefox 隱私與安全設定

## 1. 清除追蹤參數 / 屏蔽遙測

這些設定能防止你的瀏覽行為被追蹤與回傳。

- `privacy.query_stripping.enabled`：設為 `true`  
  Firefox 會自動移除連結中用於追蹤的尾端參數。

- `toolkit.telemetry.enabled`：設為 `false`  
  關閉 Firefox 自身的遙測資料收集。

- `datareporting.healthreport.uploadEnabled`：設為 `false`  
  停止上傳 Firefox 健康報告與使用統計。

---

## 2. 抗指紋保護（Fingerprinting）

降低網站透過瀏覽器特徵辨識你的能力。

- `privacy.resistFingerprinting`：設為 `true`  
  模擬類似 Tor Browser 的防指紋行為，例如隱藏真實螢幕尺寸、統一時區與部分系統資訊。

---

## 3. 隔絕網路窺探 / 防止 IP 洩漏

避免網站取得敏感資訊或洩漏真實 IP。

- `dom.event.clipboardevents.enabled`：設為 `false`  
  禁止網站得知你何時複製、剪下或貼上內容。

- `dom.battery.enabled`：設為 `false`  
  禁止網站讀取裝置電量資訊。

- `media.peerconnection.enabled`：設為 `false`  
  徹底停用 WebRTC，避免在使用 VPN 時洩漏真實本機或內網 IP 位址。

---

## 4. 關閉自動播放

減少干擾與潛在惡意內容。

- `media.autoplay.default`：設為 `5`  
  阻止所有網站的媒體自動播放。

---

## 5. 阻擋背景預載

避免瀏覽器在背景偷偷建立網路連線。

- `network.prefetch-next`：設為 `false`  
  禁止 Firefox 預先載入猜測你可能會點擊的連結。

- `browser.urlbar.speculativeConnect.enabled`：設為 `false`  
  禁止在網址列輸入時，預先連線到推測的網站。
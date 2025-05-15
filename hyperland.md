以下示範以 Arch Linux（使用 pacman 管理套件）搭配 SDDM 作為顯示管理器為例，其他發行版請對應改成你的套件管理指令與路徑。

---

## 一、安裝並切換到 Hyperland

1. **安裝必要套件**

   ```bash
   sudo pacman -Syu \
     hyperland \
     wlroots \
     waybar \
     wayland-protocols \
     xdg-desktop-portal-wlr \
     swaybg swaylock \
     alacritty    # 或其他你喜歡的 Wayland 端末
   ```

   > 這幾個套件包含 Hyperland 核心、背景/鎖定程式、狀態列、GUI 端末，以及必要的 Wayland 協議。

2. **建立 Wayland Session 描述檔**
   在 `/usr/share/wayland-sessions/hyperland.desktop`（如不存在就新建）寫入：

   ```ini
   [Desktop Entry]
   Name=Hyperland
   Comment=Hyperland Wayland Session
   Exec=hyperland
   Type=Application
   DesktopNames=Hyperland
   Keywords=wm;tiling;
   ```

3. **設定 SDDM（或其他顯示管理器）預設**

   * 登出後，在登入畫面（SDDM）選擇「Hyperland」即可進入。
   * 如果想要預設就進入 Hyperland，可在 `/etc/sddm.conf` 或 `/etc/sddm.conf.d/hyperland.conf` 加入：

     ```ini
     [Autologin]
     User=你的使用者名稱
     Session=hyperland
     ```

4. **自訂啟動腳本（選用）**
   如果要在 Hyperland 啟動時預載你的環境變數、Keymap、輸入法，可在家目錄放：

   * `~/.config/hypr/startup` （這支 shell 檔在 hyperland 啟動時自動執行）
     範例內容：

   ```bash
   #!/usr/bin/env bash
   setxkbmap -model pc105 -layout us,tw -option grp:win_space_toggle
   export GTK_THEME=Sweet-Candy
   export QT_QPA_PLATFORMTHEME=qt5ct
   # 啟動背景、狀態列
   swaybg -i ~/Pictures/wallpaper.jpg &
   waybar &
   ```

---

## 二、如果後悔，還原回 Plasma

1. **登出 Hyperland**
2. **在 SDDM 登入畫面選回「Plasma (Wayland 或 X11)」**
3. **移除 Hyperland**

   ```bash
   sudo pacman -Rns hyperland \
     waybar \
     swaybg swaylock \
     xdg-desktop-portal-wlr
   sudo rm /usr/share/wayland-sessions/hyperland.desktop
   ```

   這樣就完全把 Hyperland 與相關套件、Session 描述檔刪除，不會影響 Plasma。

---

## 三、如果喜歡 Hyperland，要刪除 Plasma

1. **確定切換到 Hyperland 並正常運作**

2. **透過 SDDM（或其他顯示管理器）預設進入 Hyperland**

3. **移除 Plasma**

   ```bash
   sudo pacman -Rns plasma \
     plasma-desktop \
     kde-frameworks \
     sddm
   ```

   > 刪除 SDDM 後，你需要改用其他登入管理器（如 ly, nodm）或直接透過 TTY+startx／startwayland 自動進入 Hyperland。

4. **（選用）安裝輕量登入工具**

   ```bash
   sudo pacman -S ly
   sudo systemctl enable ly
   ```

   或在 `~/.bash_profile`／`~/.profile` 裡加入：

   ```bash
   [[ -z $DISPLAY && $XDG_SESSION_TYPE != wayland ]] && exec hyperland
   ```

---

### 小提醒

* **備份 dotfiles**：切換前建議先把 `~/.config/hypr`、`~/.config/plasma-*`、`~/.config/sddm.conf*` 放進 Git，避免誤刪。
* **字體、鍵盤、輸入法**：Hyperland 下的設定要獨立管理，不一定沿用 Plasma 的方式。
* **顯示管理器**：刪除 SDDM 之後，請務必確保有其他可用的登入／啟動方式，不然會進不去圖形介面。

以上步驟即可讓你在 Hyperland 與 Plasma 之間自由切換，並能視喜好完整移除、不留殘跡。祝玩得愉快！

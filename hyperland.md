以下是在 Arch Linux 上從 KDE Plasma 切換到 Hyprland、保留 Plasma 以便隨時回切，並最終選擇性移除 Plasma 的步驟：

---

## 1. 安裝 Hyprland 及相依套件

```bash
sudo pacman -Syu

# 安裝 Hyprland 及常用 Wayland 工具
sudo pacman -S hyprland wayland-protocols \
                   xorg-server-xwayland \
                   swaybg swayidle swaylock \
                   xdg-desktop-portal-hyprland \
                   xsettingsd

# 安裝你慣用的 terminal emulator（以下為示例）
sudo pacman -S alacritty kitty
```

> * `xdg-desktop-portal-hyprland`：讓 Flatpak/Snap GUI 在 Hyprland 下正常運作
> * `xsettingsd`：讓 X11/GTK2 應用讀取 icon/theme 設定

---

## 2. 建立 Wayland Session 檔

在 `/usr/share/wayland-sessions/` 下新增 `hyprland.desktop`，讓登入管理器（SDDM、LightDM、GDM…）可選：

```bash
sudo tee /usr/share/wayland-sessions/hyprland.desktop << 'EOF'
[Desktop Entry]
Name=Hyprland
Comment=Hyprland Wayland Compositor
Exec=Hyprland
Type=Application
DesktopNames=Hyprland
EOF
```

---

## 3. （選填）複製並調整設定檔

```bash
mkdir -p ~/.config/hypr
cp /etc/xdg/hypr/hyprland.conf ~/.config/hypr/hyprland.conf
# 然後用你喜歡的編輯器調整快捷鍵、工作區、啟動程式...
```

---

## 4. 切換到 Hyprland

1. **登出** KDE Plasma
2. 在登入畫面選擇「Hyprland」Session
3. 登入即可進入 Hyprland
4. 若想回 Plasma，登出後選回「Plasma」Session 即可

---

## 5. 決定移除 Plasma（可跳過）

確認 Hyprland 一切正常、且你可透過 TTY（`Ctrl`+`Alt`+`F2`）或登入管理器重新登入後，再執行：

```bash
# 移除 Plasma 及 KDE 應用套件
sudo pacman -Rns plasma-desktop plasma-workspace kde-applications \
                 sddm kde-cli-tools

# 清理孤立套件
sudo pacman -Qtdq | sudo pacman -Rns -

# （選擇性）移除 SDDM
# sudo pacman -Rns sddm
```

> **注意**：
>
> * 刪除 `sddm` 前，請確認你已安裝其他登入管理器（如 `lightdm`）或知道如何從 TTY 啟動 Hyprland（`export XDG_SESSION_TYPE=wayland && exec Hyprland`）。
> * `-Rns` 會移除套件及其未被其他套件依賴的設定檔。

---

### 小結

1. **安裝**：`pacman -S hyprland …`
2. **Session**：新增 `/usr/share/wayland-sessions/hyprland.desktop`
3. **切換**：登入畫面選擇 Hyprland／Plasma
4. **移除**：`pacman -Rns plasma-desktop plasma-workspace kde-applications …`

如此即可在 Arch 上無痛試用 Hyprland，隨時回到 Plasma，最後再決定是否徹底移除 Plasma。祝順利玩轉！

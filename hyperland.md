以下是從 Plasma 切換到 Hyperland、再切回 Plasma，並在確認喜歡後移除 Plasma 的完整流程，以 Arch Linux 為例；若你用的是其他發行版，請將套件管理器指令對應替換即可。

⸻

1. 安裝 Hyperland（以 Arch 為例）
	1.	安裝必要套件

sudo pacman -Syu hyprland wayland-protocols wlroots \
    swaybg swayidle swaylock grim slurp \
    waybar mako foot alacritty \
    qt5-wayland qt6-wayland xorg-xwayland \
    xdg-desktop-portal-hyprland \
    qt5ct qt6ct lxappearance

	•	hyprland：核心 Compositor
	•	wayland-protocols、wlroots：Wayland 基礎
	•	swaybg 等：背景、鎖屏、截圖、狀態列與通知
	•	foot、alacritty：範例 terminal（可自行替換）
	•	qt*-wayland、qt5ct、qt6ct、lxappearance：讓 Qt/GTK 應用在 Wayland 下套用圖示與主題

	2.	建立 Hyperland Session 檔
在 /usr/share/wayland-sessions/ 下新增 hyperland.desktop：

[Desktop Entry]
Name=Hyperland
Comment=Lightweight Wayland compositor
Exec=Hyprland
Type=Application
DesktopNames=Hyperland

或者如果是用 SDDM，也可以放在 ~/.local/share/wayland-sessions/。

	3.	新增使用者設定檔
建立目錄與預設設定：

mkdir -p ~/.config/hypr
cp /etc/hypr/hyprland.conf ~/.config/hypr/hyprland.conf

然後依喜好編輯 ~/.config/hypr/hyprland.conf，例如設定自動啟動 status bar、鍵盤布局、wallpaper 等。

⸻

2. 切換到 Hyperland
	1.	登出 Plasma
	2.	在登入畫面（SDDM/GDM/LightDM）選擇「Hyperland」Session
	3.	登入即可進入 Hyperland

提示：若發現某些 KDE 應用還是用 X11 後端，可在 hyprland.conf 的 exec 區塊裡加入：

exec=export QT_QPA_PLATFORM=wayland
exec=export _JAVA_AWT_WM_NONREPARENTING=1



⸻

3. 後悔時直接回到 Plasma
	1.	登出 Hyperland
	2.	在登入畫面選擇「Plasma（Wayland）」或「Plasma（X11）」
	3.	登入，即恢復 Plasma

無需移除任何檔案，所有 KDE 設定都完好保留在 ~/.config/、~/.local/。

⸻

4. 如果決定只用 Hyperland，移除 Plasma

⚠️ 請先務必確認 Hyperland 下所有常用功能與應用都正常運作，再開始移除。

	1.	移除 Plasma 及其元套件（以 Arch 為例）：

sudo pacman -Rns plasma-meta kde-applications-meta \
    kde-frameworks-meta xorg-server xorg-apps \
    sddm

	•	plasma-meta、kde-applications-meta、kde-frameworks-meta：一鍵移除所有 Plasma 核心與 KDE 應用
	•	xorg-server、xorg-apps：如果只想保留 Wayland，可一併移除 Xorg
	•	sddm：如果你改用其他登入管理器（例如 ly、greetd）

	2.	(可選) 安裝輕量登入管理器

sudo pacman -S ly
sudo systemctl enable ly.service


	3.	清理殘留設定
如果確定不再需要 KDE 設定檔，可刪除：

rm -rf ~/.config/plasma* ~/.config/kde* ~/.local/share/plasma*



⸻

完整回顧：
	•	安裝 Hyperland → 建立 Session → 登入
	•	不滿意？登出 → 選 Plasma → 登入
	•	喜歡？移除 Plasma 元套件 → 清理設定
	•	確保先在 Hyperland 下測試完所有工作流再移除 Plasma！

如此一來，你既能無縫試用 Hyperland，又能隨時回頭，最終再依喜好決定是否徹底移除 Plasma。
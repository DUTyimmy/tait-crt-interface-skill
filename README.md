[简体中文](#简体中文) · [English](#english)

# Tait CRT Interface Skill

把人物、生物、物品或其他视觉主题重新绘制成一张带有早期计算机界面、共享像素网格与老式 CRT 信号质感的复古插画。

Turn a portrait, creature, object, or visual theme into a retro illustration built from early computer-interface graphics, a shared pixel grid, and an aged CRT signal surface.

## 参考图 / Examples

| Example 01 | Example 02 |
|---|---|
| <!-- 在此添加参考图 01 / Add reference image 01 here --><br><br><br><br> | <!-- 在此添加参考图 02 / Add reference image 02 here --><br><br><br><br> |
| Example 03 | Example 04 |
| <!-- 在此添加参考图 03 / Add reference image 03 here --><br><br><br><br> | <!-- 在此添加参考图 04 / Add reference image 04 here --><br><br><br><br> |

---

## 简体中文

### 简介

`tait-crt-interface-skill` 是一个用于 Codex 的图像生成 Skill。它不会简单地给参考图添加像素化滤镜，而是提取主体最有辨识度的特征，将其抽象、卡通化和扁平化，再重新构造成上世纪 80 年代 CRT 终端里的像素插画。

可调用名称为：`tait-crt-interface-skill`。

### 视觉特征

- 一个占据画面主要面积的像素风主体，作为无边框系统壁纸
- 早期 Macintosh、Minitel 与 8-bit 计算机界面语言
- 3–6 个大小、比例和位置各异的悬浮视窗
- 1–3 个用于展示五官、饰品或局部特征的元素提取视窗
- 主体、文字、图标和窗口共用同一个方形像素网格
- 棋盘格光学灰度、硬边锯齿、扫描线、辉光、噪点和信号干扰
- 四周固定的 CRT 球面桶形畸变
- 多套预设色卡，也可以根据上传图片自动创作 2–5 色
- 固定署名 `tait-crt-interface-skill`

### 安装

将整个 Skill 文件夹放入 Codex 的技能目录：

```text
~/.codex/skills/tait-crt-interface-skill
```

如果 Skill 没有立即出现，请重启 Codex。

### 使用方法

上传一张参考图片，然后按名称调用：

```text
使用 $tait-crt-interface-skill 把这张图片生成 CRT 复古电脑界面插画
```

如果没有提前指定，Skill 会分两轮询问：

1. 先展示色卡，请你选择 `经典`、`粉黛`、`极客01`、`极客02`、`游戏01`、`游戏02`，或回复 `如图`。
2. 再选择 `3:4`、`4:3`、`9:16`、`16:9`，也可以输入其他比例。

也可以在第一次调用时直接写清色卡和比例，从而立即生成：

```text
使用 $tait-crt-interface-skill 生成图片，极客02色卡，4:3比例
```

### 输出

每次调用只生成并返回一张最终位图。Skill 不展示内部提示词，不自动生成多个方案，也不会为了制造低保真效果而先生成低分辨率小图再放大。

### 文件结构

- `SKILL.md`：完整工作流、构图规则和质量门槛
- `README.md`：简体中文与英文使用说明
- `assets/`：色卡等交互资产
- `references/`：色彩与需求规范
- `scripts/`：共享像素网格、色卡约束、CRT 畸变与固定署名处理

---

## English

### Overview

`tait-crt-interface-skill` is an image-generation Skill for Codex. Instead of applying a pixelation filter to a reference, it extracts the subject's most recognizable traits, abstracts and flattens them, and redraws the result as a stylized pixel illustration from an imagined 1980s CRT terminal.

Callable name: `tait-crt-interface-skill`.

### Visual Direction

- One dominant pixel-art subject used as borderless system wallpaper
- Early Macintosh, Minitel, and 8-bit computer-interface language
- Three to six floating windows with varied sizes, proportions, and positions
- One to three feature-extraction windows for eyes, accessories, or other distinctive details
- One shared square-pixel lattice across the subject, text, icons, and windows
- Checkerboard optical midtones, hard stair-step edges, scanlines, bloom, noise, and signal interference
- Mandatory spherical CRT barrel distortion around all four edges
- Multiple preset palettes or a custom two-to-five-color palette derived from the uploaded image
- A fixed `tait-crt-interface-skill` signature

### Installation

Place the complete Skill folder in the Codex skills directory:

```text
~/.codex/skills/tait-crt-interface-skill
```

Restart Codex if the Skill does not appear immediately.

### Usage

Upload a reference image and invoke the Skill by name:

```text
Use $tait-crt-interface-skill to turn this image into a retro CRT computer-interface illustration.
```

When the request does not already include them, the Skill asks for two choices in separate turns:

1. Choose `经典`, `粉黛`, `极客01`, `极客02`, `游戏01`, `游戏02`, or reply `如图` to derive colors from the uploaded image.
2. Choose `3:4`, `4:3`, `9:16`, `16:9`, or enter another aspect ratio.

You can provide both choices in the initial request to generate immediately:

```text
Use $tait-crt-interface-skill to generate an image with the 极客02 palette at 4:3.
```

### Output

Each invocation generates and returns exactly one finished raster image. The Skill does not reveal its internal prompt, create multiple automatic variants, or produce and upscale a low-resolution precursor.

### Folder Structure

- `SKILL.md`: complete workflow, composition rules, and quality gates
- `README.md`: Simplified Chinese and English usage guide
- `assets/`: palette card and other interaction assets
- `references/`: color and requirements specifications
- `scripts/`: shared-grid, palette, CRT-distortion, and locked-signature finalization

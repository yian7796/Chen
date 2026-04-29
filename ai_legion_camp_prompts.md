# AI 軍團軍營視覺包（可直接生圖）

## 1) 主場景：白天版（營運例會）
**Prompt**
```text
三國風軍營全景，白天柔和日光，中央大型指揮帳篷作為AI作戰中心，帳內有發光戰略地圖與任務看板；
左側情報帳展示市場趨勢卷軸與旗標，右側財務帳有算盤、帳冊與數據圖板；
後方高台軍師推演沙盤，前景有會議紀要桌與簡報卷軸台，側翼是視覺設計工坊掛滿圖表；
整體為Q版精緻插畫風，乾淨線條，柔和配色，統一三國人物風格，cinematic composition, high detail, no text, no watermark
```

## 2) 主場景：夜戰版（緊急決策）
**Prompt**
```text
三國風軍營夜景，藍黑色天幕與火把光源，中央指揮帳篷內戰略地圖發出暖色光，六位角色圍繞任務看板協同決策；
左側情報帳有即時軍情卷軸，右側財務帳以木牌和帳冊呈現成本變化，後方軍師高台有沙盤與旗陣；
雨後地面微反光，氛圍緊張但秩序井然，Q版插畫，線條清晰，統一角色比例，cinematic lighting, high detail, no text
```

## 3) 主場景：雨天版（風險演練）
**Prompt**
```text
三國風軍營雨天場景，細雨、灰藍天空，中央帳篷防雨帷幕半開，內部看板顯示風險等級與應變流程；
趙雲在情報帳整理外部趨勢，司馬懿在財務帳校對帳冊，諸葛亮於高台推演策略，龐統紀錄行動項，周瑜整理簡報卷軸，大喬校正圖表視覺；
整體Q版插畫，柔和低飽和配色，乾淨背景，焦點明確，high detail, no text, no watermark
```

---

## 分鏡（同場景系列圖）

### A. 遠景 establishing shot
```text
wide establishing shot, Three Kingdoms style AI command camp, all six role stations visible, balanced composition, chibi illustration, clean line art, soft color palette
```

### B. 中景（主公指揮台）
```text
medium shot of central command tent, strategy board and milestone map in focus, characters discussing tasks, chibi Three Kingdoms style, cinematic but clean
```

### C. 六分身特寫模板
> 將 `{role}`、`{character}`、`{props}` 替換即可。

```text
close-up portrait in a circular badge style, {character} as {role}, chest-up 3/4 left pose, calm confident expression, holding {props}, chibi Three Kingdoms illustration, soft neutral background, consistent line thickness
```

---

## 負面詞（共用）
```text
photorealistic, 3d render, messy background, neon cyberpunk, modern city, text, logo, watermark, extra limbs, deformed hands, distorted face, low-res, blurry
```

## 推薦參數
- Aspect ratio：
  - 主場景：16:9（1536x864 或 1920x1080）
  - 頭像：1:1（1024x1024）
- Steps：28~40
- CFG / Guidance：6~8
- Seed：固定同一組（維持系列一致）

## 角色對應（供替換）
- 趙雲：外部趨勢斥候（props: 長槍、情報卷軸）
- 司馬懿：內部財務主簿（props: 帳冊、算盤）
- 諸葛亮：戰略解讀（props: 羽扇、沙盤）
- 龐統：會議總結（props: 筆札、紀要卷）
- 周瑜：PPT 文官（props: 簡報卷軸、指揮棒）
- 大喬：視覺工官（props: 團扇、圖表畫卷）

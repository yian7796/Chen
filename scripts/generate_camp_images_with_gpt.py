#!/usr/bin/env python3
"""Generate AI legion camp images with OpenAI GPT image API."""
import base64
import os
from pathlib import Path

from openai import OpenAI

PROMPTS = {
    "camp_day": "三國風軍營全景，白天柔和日光，中央大型指揮帳篷作為AI作戰中心，帳內有發光戰略地圖與任務看板；左側情報帳展示市場趨勢卷軸與旗標，右側財務帳有算盤、帳冊與數據圖板；後方高台軍師推演沙盤，前景有會議紀要桌與簡報卷軸台，側翼是視覺設計工坊掛滿圖表；整體為Q版精緻插畫風，乾淨線條，柔和配色，統一三國人物風格，cinematic composition, high detail, no text, no watermark",
    "camp_night": "三國風軍營夜景，藍黑色天幕與火把光源，中央指揮帳篷內戰略地圖發出暖色光，六位角色圍繞任務看板協同決策；左側情報帳有即時軍情卷軸，右側財務帳以木牌和帳冊呈現成本變化，後方軍師高台有沙盤與旗陣；雨後地面微反光，氛圍緊張但秩序井然，Q版插畫，線條清晰，統一角色比例，cinematic lighting, high detail, no text",
    "camp_rain": "三國風軍營雨天場景，細雨、灰藍天空，中央帳篷防雨帷幕半開，內部看板顯示風險等級與應變流程；趙雲在情報帳整理外部趨勢，司馬懿在財務帳校對帳冊，諸葛亮於高台推演策略，龐統紀錄行動項，周瑜整理簡報卷軸，大喬校正圖表視覺；整體Q版插畫，柔和低飽和配色，乾淨背景，焦點明確，high detail, no text, no watermark",
}

NEGATIVE = "photorealistic, 3d render, messy background, neon cyberpunk, modern city, text, logo, watermark, extra limbs, deformed hands, distorted face, low-res, blurry"


def main() -> None:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    model = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")

    out_dir = Path("assets/camp")
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, prompt in PROMPTS.items():
        resp = client.images.generate(
            model=model,
            prompt=f"{prompt}\nNegative prompt: {NEGATIVE}",
            size="1536x1024",
        )
        image_b64 = resp.data[0].b64_json
        png = base64.b64decode(image_b64)
        path = out_dir / f"{name}.png"
        path.write_bytes(png)
        print(f"generated {path}")


if __name__ == "__main__":
    main()

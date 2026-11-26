# 改善ログ: AI画像・動画生成ツールの導入に伴うルール更新

## 役割
Open Generative AI(旧名 Open Higgsfield AI)の導入に合わせて RULES.md を更新した理由を記録します。

## 目的
AGENTS.md の「ルール変更が必要な場合は、変更理由を improvement_logs に記録してから更新する」に従うためです。

## 使い方
AI生成ツールの運用ルールを見直すときに参照します。

## 保存先
`company/workspace/logs/improvement_logs/20261126_open_higgsfield_rules_update.md`

## 完了条件
変更前の課題、変更内容、次回確認項目が明記されていること。

# 変更前の課題
- `20260607_video_generation_improvement.md` で、動画が手書きのAVIと静止画中心になり「より動画らしい画作り」が課題として残っていた。
- サムネイルスキルは画像生成プロンプトまでで止まっており、実際に生成する手順と費用の記録方法がなかった。
- AI生成物の肖像・商用利用・YouTubeの合成コンテンツ開示を確認するルールがなかった。

# 変更内容
- thumbnail_designer: 画像を生成するときは `open_higgsfield_image_skill.md` を確認し、生成記録を残す。
- content_maker: 映像素材を生成するときは `open_higgsfield_video_skill.md` を確認し、シーン表と生成記録を残す。
- legal_checker: AI生成物について、実在人物の顔・声、既存作品との類似、モデルの商用利用条件、合成コンテンツ開示の要否を確認する。

# 次回確認項目
- 実際の生成1回あたりの消費クレジットを記録し、1本あたりの予算が妥当か見直す。
- よく使うモデルと、うまくいったプロンプトを各エージェントの MEMORY.md に追記する。
- アプリの更新でモデル名や画面が変わった場合、導入ガイドとスキルを更新する。

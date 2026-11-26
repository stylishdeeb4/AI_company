# 作業ログ: Open Higgsfield(Open Generative AI)導入準備

## 役割
AI画像・動画生成アプリ Open Higgsfield AI をAI会社に導入するために行った作業の履歴を記録します。

## 目的
誰が、何を調べ、どのファイルを作成・更新したかを後から追えるようにするためです。

## 使い方
このアプリの使い方や運用ルールを見直すときに参照します。

## 保存先
`company/workspace/logs/work_logs/20261126_open_higgsfield_setup.md`

## 完了条件
調査結果、作成・更新したファイル、残りの作業が明記されていること。

## 調査結果
- 「Open Higgsfield AI」は `Anil-matcha/Open-Higgsfield-AI` から `Anil-matcha/Open-Generative-AI` に改名されていた(両URLのタグとコミットが一致することで確認)。
- ライセンスはMIT。最新版は v2.0.0。Mac / Windows / Linux のインストーラーがリリースページに実在することを確認。
- Higgsfield公式の製品ではない。同名のコピーリポジトリが複数ある。
- 生成は MuAPI(muapi.ai)経由の有料APIで、前払いクレジット制の従量課金。ローカル生成(sd.cpp)はデスクトップ版のみ無料で使える。
- 「コンテンツフィルターなし」をうたっているため、権利・規約チェックは自社で行う必要がある。

## 作業内容
- 新規作成: `company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md`
- 新規作成: `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md`
- 新規作成: `company/agents/content_maker/skills/open_higgsfield_video_skill.md`
- 新規作成: `company/workspace/tickets/waiting/20261126_open_higgsfield_setup.md`
- 更新: `company/agents/thumbnail_designer/RULES.md`(画像生成スキルの参照を追加)
- 更新: `company/agents/content_maker/RULES.md`(動画素材生成スキルの参照を追加)
- 更新: `company/agents/legal_checker/RULES.md`(AI生成物のチェック項目を追加)
- 更新: `.vercelignore`(導入ガイドをWebサイトに公開しない)

## 残りの作業
- ユーザー本人のPCへのインストールとMuAPIキーの登録(AI社員は代行できない)。
- テスト生成の消費クレジットを確認し、1本あたりの生成予算を決める。

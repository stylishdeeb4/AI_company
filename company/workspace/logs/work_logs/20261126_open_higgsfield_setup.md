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

## 追記: 無料運用への変更(同日)
ユーザーから「無料で行いたい」と依頼があり、運用方針を0円(ローカル生成のみ)に変更した。

### 追加の調査結果
- 無料で使えるのはデスクトップアプリのローカル生成だけ。⚡ Local があるのは Image Studio と Video Studio のみで、Lip Sync、Cinema Studio、ブラウザ版などはクラウド(有料)専用。
- MuAPI の無料エンドポイントは透かし処理や音声系だけで、画像・動画生成には使えない。
- 画像のローカル生成(sd.cpp)は全PCで可能。16:9の出力は Z-Image / SDXL が 1792×1024、SD 1.5系が 896×512(アプリのソース `electron/lib/localInference.js` で確認)。
- 動画のローカル生成(Wan2GP)は NVIDIA/AMD のGPUが必要で、Macは不可。
- ライセンス: Z-Image と Wan 2.1/2.2 は Apache 2.0、SDXL は CreativeML Open RAIL++-M、Dreamshaper 8 は CreativeML OpenRAIL-M。Realistic Vision v5.1、Anything v5 などは未確認。

### 変更したファイル
- `company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md`(無料運用版に書き直し。有料化は付録に移動)
- `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md`(ローカルモデルのみ)
- `company/agents/content_maker/skills/open_higgsfield_video_skill.md`(静止画+編集ソフトを標準に。Wan2GPは使えるPCのみ)
- thumbnail_designer、content_maker、legal_checker の RULES.md(消費クレジットの記録を、0円運用の確認とライセンス一覧の参照に変更)
- チケットの完了条件とユーザー作業

## 残りの作業
- ユーザー本人のPCへのインストールとローカルモデルの導入(AI社員は代行できない)。
- テスト生成の時間を確認し、ユーザーのPCで使える標準モデルを確定する。

## 追記: 無料クラウドサービスの調査(同日)
- ユーザーのPC(Windows / Core i5-7200U / メモリ16GB / Intel HD Graphics 620)ではローカル生成が遅いため、無料のクラウド画像・動画生成サービスを調査した。
- 調査資料: `company/workspace/references/20261126_free_cloud_ai_generation_research.md`
- 推奨: 画像・動画とも Adobe Firefly(無料プラン、Adobe自社のFireflyモデル)を標準候補とし、ChatGPT・Gemini・Ideogram を補助、ローカル生成を予備とする。
- 各社の公式ページは作業環境のネットワーク制限で直接開けず、公式ドメインに絞った検索結果で確認した。
- 標準ツールの決定とスキルへの反映は、ユーザーの判断待ち。

## 追記: Firefly を標準に変更(同日)
ユーザーの指示で、標準の画像・動画生成ツールを Adobe Firefly(無料プラン)に変更した。
- 新規作成: `company/agents/thumbnail_designer/skills/firefly_image_skill.md`(予備ツールの順番: ChatGPT → Gemini → ローカル生成)
- 新規作成: `company/agents/content_maker/skills/firefly_video_skill.md`(AI動画はフックなど重要なカットに絞り、残りは静止画+編集ソフト)
- 新規作成: `company/workspace/tickets/waiting/20261126_firefly_setup.md`(ユーザーの始め方とテスト手順)
- 更新: `open_higgsfield_image_skill.md`、`open_higgsfield_video_skill.md` を予備扱いに
- 更新: `thumbnail_creation_skill.md` の手順7に Firefly スキルへの案内を追加
- 更新: thumbnail_designer、content_maker、legal_checker の RULES.md、thumbnail_designer と content_maker の MEMORY.md
- 更新: Open Higgsfield の導入ガイドとチケットに「予備」の注記

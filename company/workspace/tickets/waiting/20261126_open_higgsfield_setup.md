# 役割
AI画像・動画生成アプリ Open Higgsfield AI(現名称 Open Generative AI)をAI会社に導入するための作業チケットです。

# 目的
サムネイル画像とショート動画の映像素材を自前で生成できるようにし、制作本数と見た目の質を上げて、登録者5万人の目標に近づけます。

# 使い方
AI社員側の準備(導入ガイド、スキル、ルール更新)は完了済みです。ユーザー本人のPCでのインストールとMuAPIキーの登録を待っているため `waiting/` に置いています。下の「ユーザー作業」がすべて終わったら `done/` に移します。

# 保存先
`company/workspace/tickets/waiting/20261126_open_higgsfield_setup.md`

# 完了条件
- ユーザーのPCでアプリが起動し、テスト画像を1枚生成できていること
- テスト1枚の消費クレジットが記録されていること
- 1本の動画あたりの生成予算が決まっていること

# 担当エージェント
- main_manager(全体整理、予算確認)
- researcher(アプリとMuAPIの調査)
- thumbnail_designer(画像生成スキル)
- content_maker(動画素材生成スキル)
- legal_checker(AI生成物のチェック項目追加)
- accountant(生成費用の記録)

# 使用スキル
- 新規: `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md`
- 新規: `company/agents/content_maker/skills/open_higgsfield_video_skill.md`

# 成果物
- 導入ガイド: `company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md`

# AI社員側の作業(完了)
- [x] アプリの正体、改名、ライセンス、最新版、費用の仕組みを調査
- [x] 導入ガイドを作成
- [x] thumbnail_designer 用の画像生成スキルを作成
- [x] content_maker 用の動画素材生成スキルを作成
- [x] thumbnail_designer、content_maker、legal_checker の RULES.md を更新
- [x] 導入ガイドがWebサイトに公開されないよう `.vercelignore` に追加

# ユーザー作業(確認待ち)
- [ ] muapi.ai のアカウント作成と少額チャージ
- [ ] アクセスキーの作成
- [ ] 自分のPCにインストール(Mac / Windows)
- [ ] アプリにキーを登録し、テスト画像を1枚生成
- [ ] テスト1枚の消費クレジットを確認
- [ ] 1本の動画あたりの生成予算を決める

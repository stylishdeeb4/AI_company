# 役割
AI画像・動画生成アプリ Open Higgsfield AI(現名称 Open Generative AI)をAI会社に導入するための作業チケットです。

# 目的
サムネイル画像とショート動画の映像素材を自前で生成できるようにし、制作本数と見た目の質を上げて、登録者5万人の目標に近づけます。

# 使い方
AI社員側の準備(導入ガイド、スキル、ルール更新)は完了済みです。ユーザーの希望により0円(ローカル生成のみ)で運用します。ユーザー本人のPCでのインストールを待っているため `waiting/` に置いています。下の「ユーザー作業」がすべて終わったら `done/` に移します。

# 保存先
`company/workspace/tickets/waiting/20261126_open_higgsfield_setup.md`

# 完了条件
- ユーザーのPCでアプリが起動し、ローカル生成(⚡ Local)でテスト画像を1枚生成できていること
- テスト1枚の生成時間が記録されていること
- 費用が0円のままであること(MuAPIのキーを登録していないこと)

# 担当エージェント
- main_manager(全体整理、0円運用の確認)
- researcher(アプリ、ローカルモデル、ライセンスの調査)
- thumbnail_designer(画像生成スキル)
- content_maker(動画素材生成スキル)
- legal_checker(AI生成物のチェック項目追加)

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
- [x] ユーザーの希望により、ガイドとスキルを無料運用(ローカル生成のみ)に変更

# ユーザー作業(確認待ち)
- [ ] 自分のPCのチップ・メモリ・GPUを確認する
- [ ] 自分のPCにインストール(Mac / Windows)
- [ ] 起動時のAPIキー入力はスキップ
- [ ] Settings → Local Models で sd.cpp と画像モデルを入れる
- [ ] ⚡ Local でテスト画像を1枚生成し、生成時間をメモ
- [ ] (NVIDIA GPUがある場合のみ・任意)Wan2GP を入れて動画を試す

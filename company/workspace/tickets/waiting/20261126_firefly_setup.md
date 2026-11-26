# 役割
Adobe Firefly(無料プラン)をAI会社の標準の画像・動画生成ツールとして使い始めるための作業チケットです。

# 目的
ユーザーのPC(Windows / Core i5-7200U / メモリ16GB / Intel HD Graphics 620)ではローカルのAI生成が遅いため、PCの性能に関係なく使えるクラウドの無料ツールで、収益化したYouTube動画に使える画像・動画素材を0円で作れるようにします。

# 使い方
AI社員側の準備(スキル、ルール更新)は完了済みです。ユーザーがFireflyにログインしてテスト生成するのを待っているため `waiting/` に置いています。下の「ユーザー作業」が終わったら `done/` に移します。

# 保存先
`company/workspace/tickets/waiting/20261126_firefly_setup.md`

# 完了条件
- ユーザーがAdobeの無料アカウントでFireflyにログインできていること
- Adobe自社の「Firefly」モデルで、テスト画像1枚とテスト動画1本を生成できていること
- 1日に何回くらい生成できるかの目安が記録されていること

# 担当エージェント
- main_manager(全体整理)
- researcher(無料クラウドサービスの調査)
- thumbnail_designer(画像生成スキル)
- content_maker(動画素材生成スキル)
- legal_checker(AI生成物のチェック)

# 使用スキル
- 標準: `company/agents/thumbnail_designer/skills/firefly_image_skill.md`
- 標準: `company/agents/content_maker/skills/firefly_video_skill.md`
- 予備: `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md`
- 予備: `company/agents/content_maker/skills/open_higgsfield_video_skill.md`

# 根拠資料
`company/workspace/references/20261126_free_cloud_ai_generation_research.md`

# 始め方(ユーザー向け)
1. ブラウザで https://firefly.adobe.com を開きます。
2. 「ログイン」から Adobe の無料アカウントを作ります(Google アカウントなどでも登録できます)。
3. 有料プランやクレジット購入の案内が出ても選びません。
4. 画像生成(文章から画像)を開き、モデルの選択で名前が「Firefly」で始まるものを選びます。
5. 比率を 16:9 にして、次のプロンプトで1回生成します。
   ```text
   A Japanese freelancer working on a laptop at a bright cafe, natural light, shallow depth of field, cinematic, no text
   ```
6. 動画生成(文章から動画)を開き、同じく「Firefly」の動画モデルを選んで、次のプロンプトで1回生成します。
   ```text
   Steam rising from a coffee cup next to a laptop on a cafe table, slow push-in camera, soft morning light, cinematic
   ```
7. 生成できたらダウンロードして、どれくらい回数が使えたか(残り回数の表示があればその数)をメモします。

# AI社員側の作業(完了)
- [x] 無料クラウドサービスを調査し、Firefly を標準に決定
- [x] thumbnail_designer 用の Firefly 画像生成スキルを作成
- [x] content_maker 用の Firefly 動画素材生成スキルを作成
- [x] Open Higgsfield のスキルを予備に変更
- [x] thumbnail_designer、content_maker、legal_checker の RULES.md を更新

# ユーザー作業(確認待ち)
- [ ] Adobe の無料アカウントを作って Firefly にログイン
- [ ] Firefly モデルでテスト画像を1枚生成
- [ ] Firefly モデルでテスト動画を1本生成
- [ ] 1日に生成できた回数の目安をメモ

> **2026-11-26 更新:** 標準ツールは Adobe Firefly に変更(`company/workspace/tickets/waiting/20261126_firefly_setup.md`)。このチケットは予備ツールの導入として、急がない扱いにします。

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

# ユーザーPC情報(2026-11-26 ユーザー申告)
| 項目 | 内容 |
| --- | --- |
| OS | Windows |
| CPU | Intel Core i5-7200U(2017年ごろのノート向け、2コア4スレッド) |
| メモリ | 15.9GB(16GB) |
| GPU | Intel HD Graphics 620(CPU内蔵。専用メモリなし、共有メモリ7.9GB。NVIDIAのGPUはなし) |

判定:
- 動画の無料生成(Wan2GP): 不可(GPU性能不足)
- 画像の無料生成: Dreamshaper 8 を標準とし、まず1枚の生成時間を実測する。アプリは内蔵GPU向けの Vulkan 版エンジンを選ぶが、内蔵GPUは非力なため、1枚数分〜10分以上かかる見込み(推定)
- Z-Image Turbo: メモリは足りるが非常に遅い見込み。他のアプリを閉じた状態で1回だけ試す
- SDXL: 使わない(重すぎる)

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
- [x] 自分のPCのCPU・メモリ・GPUを確認する
- [ ] 自分のPCにインストール(Mac / Windows)
- [ ] 起動時のAPIキー入力はスキップ
- [ ] Settings → Local Models で sd.cpp と Dreamshaper 8 を入れる
- [ ] ⚡ Local でテスト画像を1枚生成し、生成時間をメモ
- [ ] Dreamshaper 8 の1枚の生成時間を見て、使い続けるか、無料枠のあるクラウドサービスに切り替えるかを決める

# スキル名
Open Higgsfield(Open Generative AI)画像生成スキル

# 目的
`thumbnail_creation_skill.md` で決めたサムネイル案を、Open Generative AI(旧名 Open Higgsfield AI)の Image Studio で実際の画像にする。生成の条件と費用を記録し、同じ品質の画像を再現できるようにする。

# 前提
- アプリはユーザー本人のPCにインストール済みであること。導入手順は `company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md` を参照。
- thumbnail_designer はプロンプト、モデル、設定を作る。生成ボタンの操作はユーザーが行う。
- MuAPIのキーは扱わない。依頼文や成果物にキーを書かない。

# 入力情報
- `thumbnail_creation_skill.md` の成果物(構図案3つ、画像生成プロンプト)
- 使う比率(通常のサムネイルは 16:9、ショートのカバーは 9:16)
- 参照画像(ユーザー本人の写真、過去のサムネイルなど。使用許可のあるものだけ)
- 今回の生成予算(未設定なら main_manager がユーザーに確認する)

# 作業手順
0. 使用スキルの確認
   - このファイル `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md` と、`thumbnail_creation_skill.md` を使うことを確認します。
   - 成果物の冒頭に「使用スキル名」と「スキル保存先」を明記します。

1. 生成モードを決める
   - 参照画像なし: Image Studio の text-to-image。
   - 参照画像あり(本人の写真で人物を揃える、過去サムネの雰囲気に寄せる): image-to-image。参照画像は最大14枚。

2. モデルを決める
   - 試し生成: 安いモデル、またはローカル生成(sd.cpp の SDXL など。無料)。
   - 本番生成: 写実系や質感が必要なときは Nano Banana 2、Seedream 5.0、Flux など上位モデル。
   - モデル名と料金はアプリ内の表示を正とし、記憶で決めない。

3. プロンプトを整える
   - 英語で書く(多くのモデルで英語の方が意図どおりになりやすい)。
   - 主役、表情、視線、背景、光、色、カメラ(寄り・引き)、余白の位置(文字を置く側)を入れる。
   - 文字は生成しない。末尾に `no text, no letters, no watermark` を入れ、文字はCanvaで後から入れる。
   - 実在の有名人、既存キャラクター、ブランド名、他人の作品名をプロンプトに入れない。

4. 試し生成をする
   - 構図案ごとに2〜4枚。比率はこの段階で本番と同じにする。
   - 良かった案だけを本番モデルで作り直す。

5. 仕上げる
   - 必要に応じて image-to-image の Upscaler(高解像度化)、Background Remover(背景除去)を使う。
   - YouTubeサムネイルは 1280×720 以上で書き出す。

6. 生成記録を残す
   - 下の「出力形式」の生成記録表に、全試行を記録する(採用しなかったものも)。

7. Canvaで文字入れ
   - `thumbnail_creation_skill.md` の文字案・Canva編集指示に従う。

8. 権利・開示チェックを依頼する
   - legal_checker に、肖像・既存作品との類似・モデルの商用利用条件を確認してもらう。
   - 実写と見間違うリアルな人物画像を使う場合は、YouTube の「改変または合成されたコンテンツ」開示が要るかを legal_checker と判断する。

# 出力形式
1. 使用スキル名とスキル保存先
2. 生成の狙い(どのサムネイル案を画像にするか)
3. 生成設定(モード、モデル、比率、解像度、参照画像の有無)
4. プロンプト(英語)と日本語の意図メモ
5. 生成記録表

   | No | 構図案 | モデル | プロンプト要約 | 比率 | 消費クレジット | 結果 | 採用 |
   | --- | --- | --- | --- | --- | --- | --- | --- |

6. 採用画像のファイル名と保管場所(ユーザーPC内のフォルダ名)
7. Canva編集指示
8. リスクチェック(肖像、既存作品、商用利用、合成コンテンツ開示)

# 品質基準
- 使用スキル名とスキル保存先が成果物に明記されていること。
- スマホの小さい表示でも主役が一目で分かること。
- 文字を置く余白が確保されていること。
- 画像内に崩れた文字、余計なロゴ、透かしがないこと。
- 手・顔・指など破綻しやすい部分が崩れていないこと。
- 実在人物・既存キャラクター・ブランドに似せていないこと。
- 全試行のモデルと消費クレジットが記録されていること。

# 意図と違う成果物が出た場合
1. プロンプト、モデル、参照画像のどれが原因かを切り分けます。
2. 一度に変える条件は1つだけにして再生成します。
3. 原因を `company/workspace/logs/error_logs/` に、うまくいった条件を `company/agents/thumbnail_designer/MEMORY.md` に記録します。

# 保存先
生成記録と途中案:

`company/workspace/outputs/agent_outputs/YYYYMMDD_動画テーマ_image_generation_v01.md`

完成仕様(採用画像のファイル名、プロンプト、Canva指示):

`company/workspace/outputs/final_outputs/`

画像ファイル本体は原則ユーザーPCに保管します。リポジトリに入れる場合はユーザーの確認を取ります(`final_outputs` 配下はWebサイトとして公開される可能性があるため、`.vercelignore` の対象か確認する)。

# 実行用プロンプトテンプレート
```text
あなたはthumbnail_designerです。
company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md に従って、
以下のサムネイル案を Open Generative AI の Image Studio で生成するための設定とプロンプトを作成してください。

【元にするサムネイル案】
〇〇(thumbnail_creation_skill の成果物のパス、または構図案)

【比率】
16:9 / 9:16

【参照画像】
なし / あり(内容: 〇〇、使用許可: 本人)

【生成予算】
〇〇クレジットまで

出力形式:
1. 使用スキル名とスキル保存先
2. 生成の狙い
3. 生成設定
4. プロンプト(英語)と意図メモ
5. 生成記録表(空欄の枠)
6. 採用画像の保管ルール
7. Canva編集指示
8. リスクチェック
```

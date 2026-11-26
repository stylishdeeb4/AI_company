# Open Higgsfield(現名称: Open Generative AI)導入ガイド

## 役割
AI会社でオープンソースのAI画像・動画生成アプリ「Open Higgsfield AI」(現名称「Open Generative AI」)を導入し、サムネイル制作とショート動画制作に使えるようにするための手順書です。

## 目的
サムネイル背景画像、ショート動画の映像素材、顔出しなし解説動画(リップシンク)を自前で作れるようにし、動画の制作本数と見た目の質を上げて、登録者5万人の目標に近づけます。

## 使い方
1. 「1. これは何か」と「3. 費用」を読んで、導入方法を決めます。
2. 「4. 導入手順」に沿って、ユーザー本人のPCにインストールします(AI社員は代わりにインストールできません)。
3. 導入後は「5. AI会社での運用ルール」に従い、各AI社員のスキルファイルから使います。

## 保存先
`company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md`

## 完了条件
- ユーザーのPCでアプリが起動し、MuAPIのキーを登録して、テスト画像を1枚生成できていること。
- 費用、セキュリティ、権利面の運用ルールが共有されていること。

---

## 1. これは何か

| 項目 | 内容 |
| --- | --- |
| 正式名称 | **Open Generative AI**(旧名: Open Higgsfield AI。2026年11月時点で改名済み) |
| 公開元 | GitHub: https://github.com/Anil-matcha/Open-Generative-AI(旧URL `Anil-matcha/Open-Higgsfield-AI` からも同じリポジトリに届きます) |
| ライセンス | MIT(アプリ自体は無料・商用利用可) |
| 最新版 | v2.0.0(2026-11-26確認) |
| 中身 | 画像・動画・音声・リップシンク・シネマ風カメラ操作などをまとめた「AI生成スタジオ」アプリ |
| 生成の仕組み | アプリは窓口で、実際の生成は **MuAPI(muapi.ai)** という有料APIを経由して各社のAIモデルを呼び出す |

**注意: Higgsfield公式の製品ではありません。** Higgsfield(higgsfield.ai)の機能を参考に、有志が作ったオープンソースの代替アプリです。同じ名前を名乗る別のコピーリポジトリが複数あるため、ダウンロードは必ず上記の公式リポジトリから行います。

### 主な機能とAI会社での使い道

| 機能 | できること | AI会社での使い道 | 担当 |
| --- | --- | --- | --- |
| Image Studio | 文章→画像、画像→画像(参照画像は最大14枚) | サムネイルの背景・人物・小物の画像 | thumbnail_designer |
| Image-to-Image系 | 高解像度化、背景除去、部分編集 | 採用画像の仕上げ | thumbnail_designer |
| Video Studio | 文章→動画、画像→動画 | ショート動画のBロール(イメージ映像)、静止画を動かす | content_maker |
| Lip Sync Studio | 顔写真+音声→話す動画 | 顔出しなし解説動画(本人の写真・本人の声のみ) | content_maker |
| Cinema Studio | レンズ・焦点距離・絞りを指定した映画風の画 | オープニングや印象的なカット | content_maker |
| Workflow Studio | 画像→動画→音声などをつなぐ自動化 | 定型ショートの量産(慣れてから) | content_maker |
| ローカル生成(デスクトップ版のみ) | PC上で画像を無料生成(SD 1.5 / SDXL / Z-Image) | 試し生成のコスト削減 | thumbnail_designer |

対応モデルの例(アプリ内の表示が正。随時増減します):
- 画像: Nano Banana 2、Seedream 5.0、Flux、Ideogram v3、Midjourney v7、GPT-4o
- 動画: Kling v3、Sora 2、Veo 3、Seedance 2.0、Hailuo 2.3、Wan 2.6
- リップシンク: Infinite Talk、LTX Lipsync、LatentSync など

---

## 2. 導入方法の選び方

| 方法 | 向いている人 | インストール | おすすめ度 |
| --- | --- | --- | --- |
| **A. デスクトップアプリ** | 普段使いする人 | 必要(1クリックのインストーラー) | **おすすめ** |
| B. ブラウザ版(muapi.ai上のホスト版) | まず触って試したい人 | 不要 | お試し向け |
| C. ソースコードから起動 / Docker | アプリを改造したい開発者 | Node.js 18以上・git が必要 | 通常は不要 |

AI会社としては **A. デスクトップアプリ** を標準にします。理由:
- インストーラーをダブルクリックするだけで、ターミナル操作がほぼ不要。
- ローカル生成(無料)が使えるのはデスクトップ版だけ。
- 生成履歴やAPIキーが自分のPC内に保存される。

B のブラウザ版: https://muapi.ai/open-generative-ai (無料登録で利用可、生成は有料クレジット)

---

## 3. 費用

| 項目 | 費用 |
| --- | --- |
| アプリ本体 | 無料(MIT) |
| クラウド生成(MuAPI経由) | **有料。前払いクレジット制の従量課金**。月額料金なし、生成した分だけ残高から引かれる。クレジットに有効期限なし(MuAPI公式ドキュメントより) |
| ローカル生成 | 無料(電気代のみ)。ただしPCの性能が必要 |

- モデルごとに1回あたりの料金が大きく違います(動画は画像よりかなり高い)。料金表: https://muapi.ai/docs/pricing
- **最初は少額だけチャージ**し、どのモデルが何クレジット使うかを確認してから増額します。
- 使った金額は accountant が経費として管理します(「5. 運用ルール」参照)。

---

## 4. 導入手順(A. デスクトップアプリ)

### ステップ1: MuAPIのアカウントとキーを作る
1. https://muapi.ai にアクセスしてアカウントを作成します。
2. 請求(Billing)ページで少額をチャージします(Stripe決済)。
3. https://muapi.ai/access-keys でアクセスキーを作成します。
4. 表示された **キーの値(長い英数字の文字列)** をコピーします。キーの「名前・ラベル」ではありません。

> キーはパスワードと同じ扱いです。チャット、GitHub、スプレッドシート、AI社員への依頼文に貼らないでください。アプリの入力欄にだけ貼ります。

### ステップ2: インストーラーをダウンロードする
公式リリースページ: https://github.com/Anil-matcha/Open-Generative-AI/releases

| お使いのPC | ダウンロードするファイル |
| --- | --- |
| Mac(Apple M1/M2/M3/M4チップ) | [Open.Generative.AI-2.0.0-arm64.dmg](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI-2.0.0-arm64.dmg) |
| Mac(Intelチップ) | [Open.Generative.AI-2.0.0.dmg](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI-2.0.0.dmg) |
| Windows(64bit) | [Open.Generative.AI.Setup.2.0.0.exe](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI.Setup.2.0.0.exe) |
| Linux(Ubuntu) | [.deb](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/open-generative-ai_2.0.0_amd64.deb) または [.AppImage](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI-2.0.0.AppImage) |

Macのチップの確認方法: 画面左上のAppleメニュー →「このMacについて」→「チップ」欄が「Apple M〜」ならApple Silicon版、「Intel」ならIntel版。

### ステップ3-A: Macでのインストール
このアプリはAppleの公証(notarize)を受けていないため、初回だけブロックされます。

1. ダウンロードした `.dmg` を開き、アプリを「アプリケーション」フォルダへドラッグします。
2. 次のどちらかで許可します。
   - **ターミナルを使う方法**: ターミナルを開いて次を実行し、その後アプリを右クリック →「開く」→ もう一度「開く」。
     ```bash
     xattr -cr "/Applications/Open Generative AI.app"
     ```
   - **ターミナルを使わない方法**: 一度アプリを開こうとしてブロックされた後、「システム設定」→「プライバシーとセキュリティ」→ 下の方の「"Open Generative AI"はブロックされました」→「このまま開く」→「開く」。
3. 2回目以降は普通に開けます。

### ステップ3-B: Windowsでのインストール
インストーラーにコード署名がないため、SmartScreenの警告が出ます。

1. `.exe` をダブルクリックします。
2. 「WindowsによってPCが保護されました」と出たら「詳細情報」→「実行」をクリックします。
3. 自動でインストールされ、スタートメニューにショートカットができます(インストール先: `%LocalAppData%`)。

### ステップ4: 初回設定とテスト生成
1. アプリを起動すると、APIキーの入力画面が出ます。ステップ1でコピーしたキーを貼り付けます。
2. **Image Studio** を開き、安めの画像モデルを選びます。
3. 比率を `16:9`(サムネイル用)にして、次のテストプロンプトで1枚生成します。
   ```text
   A Japanese freelancer working on a laptop at a bright cafe, natural light, shallow depth of field, cinematic, no text
   ```
4. 生成できたらダウンロードボタンで保存できることを確認します。
5. MuAPIの残高がどれだけ減ったかを確認し、メモしておきます(accountantへの共有用)。

### ステップ5(任意): 無料のローカル生成を設定する
- 「Settings」→「Local Models」→ **sd.cpp** をインストールし、モデル(SD 1.5 / SDXL / Z-Image)をダウンロードします。APIキー不要・無料です。
- Apple Silicon の Mac でも動きます。モデルは数GBあるので、ストレージの空きを確認してください。
- 動画のローカル生成(Wan2GP)は NVIDIA または AMD のGPUを積んだPCが必要です。持っていなければ設定不要です。

---

## 5. AI会社での運用ルール

### 担当と使うスキル
| 用途 | 担当 | スキルファイル |
| --- | --- | --- |
| サムネイル用画像の生成 | thumbnail_designer | `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md` |
| ショート・長尺動画の映像素材、リップシンク | content_maker | `company/agents/content_maker/skills/open_higgsfield_video_skill.md` |
| AI生成物の権利・規約チェック | legal_checker | `company/agents/legal_checker/RULES.md` |
| 生成費用の記録 | accountant | 生成記録の「消費クレジット」欄を月ごとに集計 |

AI社員は「プロンプト、モデル、設定」を作ります。アプリでの生成ボタン操作は、ユーザー本人のPCで行います。

### セキュリティ
- MuAPIのキーはアプリ内にだけ保存します(アプリのブラウザストレージに保存され、MuAPI以外には送られない仕様)。リポジトリ、チャット、ログに書きません。
- キーが漏れたかもしれないときは、muapi.ai でそのキーを削除して作り直します。
- アプリは公式リポジトリのリリースページからのみ入手します。似た名前のコピーリポジトリや配布サイトからは入れません。

### 権利・規約(このアプリは「コンテンツフィルターなし」をうたっているため、チェックは自分たちで行う)
- 実在の人物(芸能人・他人)の顔や声を使った生成、Body Swap、リップシンクはしません。使うのはユーザー本人、または書面で許可を得た人だけです。
- 既存のキャラクター、ブランドロゴ、有名作品に似せた画像・動画を作りません。
- 生成物を商用(収益化動画、LP、広告)に使えるかは、モデルごとの利用規約によります。迷ったら legal_checker が確認します。
- YouTubeでは、本物と見間違うようなリアルな合成・改変コンテンツを投稿するとき、YouTube Studio のアップロード画面で「改変または合成されたコンテンツ」の開示が必要です。リップシンク動画や実写風のAI映像は原則「開示する」で扱います。
- 動画の中でこのアプリを紹介する場合は「Open Generative AI」と呼び、Higgsfield公式の製品だと誤解される言い方をしません。

### 費用管理
- 試し生成は「安いモデル・短い尺・低解像度」で行い、本番だけ高品質モデルを使います。
- 生成ごとに、使ったモデルと消費クレジットを生成記録に残します。
- 1本の動画あたりの生成予算はユーザーが決めます。未設定の間は、main_manager が生成前にユーザーへ確認します。

---

## 6. よくあるトラブル

| 症状 | 原因と対処 |
| --- | --- |
| Macで「開けません」「壊れています」と出る | 公証なしのため。ステップ3-Aの `xattr` コマンド、または「このまま開く」で許可する |
| Windowsで青い警告画面が出る | 署名なしのため。「詳細情報」→「実行」 |
| キーを入れても生成できない | キーの「名前」を貼っている可能性。キーの値(長い文字列)を貼り直す |
| 生成が途中で失敗する | MuAPIの残高不足を確認。チャージ後に再実行 |
| 生成履歴が消えた | 履歴はアプリ内に保存されるため、アプリのデータ削除や再インストールで消える。採用した画像・動画はすぐダウンロードして保管する |
| Linux で AppImage が起動しない | `sudo apt install libfuse2`、または `.deb` 版を使う |

---

## 7. ユーザーがやることチェックリスト
- [ ] muapi.ai のアカウント作成と少額チャージ
- [ ] アクセスキーの作成(値をコピー)
- [ ] 自分のPCに合ったインストーラーをダウンロードしてインストール
- [ ] アプリにキーを登録し、テスト画像を1枚生成
- [ ] テスト1枚の消費クレジットを確認
- [ ] 1本の動画あたりの生成予算を決める
- [ ] (任意)ローカル生成 sd.cpp の設定

完了したら、チケット `company/workspace/tickets/waiting/20261126_open_higgsfield_setup.md` を `done/` に移します。

---

## 出典(2026-11-26確認)
- 公式リポジトリ README: https://github.com/Anil-matcha/Open-Generative-AI
- リリース(v2.0.0): https://github.com/Anil-matcha/Open-Generative-AI/releases
- MuAPI 料金: https://muapi.ai/docs/pricing
- MuAPI クレジットと支払い: https://muapi.ai/docs/payments
- MuAPI アクセスキー: https://muapi.ai/access-keys

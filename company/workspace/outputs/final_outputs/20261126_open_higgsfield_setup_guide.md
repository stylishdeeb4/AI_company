# Open Higgsfield(現名称: Open Generative AI)導入ガイド【無料運用版】

## 役割
AI会社でオープンソースのAI画像・動画生成アプリ「Open Higgsfield AI」(現名称「Open Generative AI」)を **0円で** 導入し、サムネイル制作とショート動画制作に使えるようにするための手順書です。

## 目的
自分のPCの中だけで画像(PCによっては動画も)を生成し、費用をかけずにサムネイルと動画素材を自前で作れるようにして、登録者5万人の目標に近づけます。

## 使い方
1. 「1. 無料でできること・できないこと」を読みます。
2. 「2. 自分のPCで何ができるか」で、自分のPCに合うモデルを確認します。
3. 「3. 導入手順」に沿って、ユーザー本人のPCにインストールします(AI社員は代わりにインストールできません)。
4. 導入後は「4. AI会社での運用ルール」に従い、各AI社員のスキルファイルから使います。

## 保存先
`company/workspace/outputs/final_outputs/20261126_open_higgsfield_setup_guide.md`

## 完了条件
- ユーザーのPCでアプリが起動し、ローカル生成(⚡ Local)でテスト画像を1枚作れていること。
- 費用が0円のままであること(有料APIのキーを登録していないこと)。

---

## 0. これは何か

| 項目 | 内容 |
| --- | --- |
| 正式名称 | **Open Generative AI**(旧名: Open Higgsfield AI。2026年11月時点で改名済み) |
| 公開元 | GitHub: https://github.com/Anil-matcha/Open-Generative-AI(旧URL `Anil-matcha/Open-Higgsfield-AI` からも同じリポジトリに届きます) |
| ライセンス | MIT(アプリ自体は無料) |
| 最新版 | v2.0.0(2026-11-26確認) |
| 中身 | 画像・動画・リップシンクなどをまとめた「AI生成スタジオ」アプリ |

**Higgsfield公式の製品ではありません。** 有志が作ったオープンソースの代替アプリです。同じ名前のコピーリポジトリが複数あるため、ダウンロードは必ず上記の公式リポジトリから行います。

---

## 1. 無料でできること・できないこと

このアプリには「クラウド生成(有料)」と「ローカル生成(無料)」の2つがあります。**無料で使えるのはローカル生成だけ**で、デスクトップアプリ版でしか使えません。

| 機能 | 無料(ローカル) | 備考 |
| --- | --- | --- |
| Image Studio(文章→画像) | **できる** | すべてのPCで可能。速さはPC次第 |
| Video Studio(文章→動画、画像→動画) | **NVIDIA/AMDのGPUがあるPCだけできる** | 別ソフト Wan2GP の導入が必要。Macは不可 |
| Lip Sync Studio(話す動画) | できない | クラウドのみ(有料) |
| Cinema Studio、Marketing、Agent ほか | できない | クラウドのみ(有料) |
| 高解像度化、背景除去 | できない | クラウドのみ(有料)。Canvaなど無料の編集ツールで代用 |
| ブラウザ版(muapi.ai上) | できない | 常にクラウド生成(有料) |
| Nano Banana、Kling、Veo、Sora など有名モデル | できない | クラウドのみ(有料) |

**間違って課金されることはありません。** クラウド生成には MuAPI のキー登録と前払いチャージの両方が必要です。キーを登録しなければ、有料の生成は動きません。

**画質の目安:** 無料のローカルモデルは、有料の最新モデルより画質が落ちます(特に手・指・顔の細部)。また、画像の中に日本語の文字はきれいに入りません。文字はCanvaで後から入れる前提で使います。

---

## 2. 自分のPCで何ができるか

### PCの確認方法
- **Mac:** 画面左上のAppleメニュー →「このMacについて」で「チップ」と「メモリ」を確認。
- **Windows:** タスクマネージャー(Ctrl+Shift+Esc)→「パフォーマンス」→「GPU」でGPUの名前と「専用GPUメモリ」、「メモリ」で搭載メモリを確認。

### PC別にできること

| PC | 無料の画像生成 | 無料の動画生成 |
| --- | --- | --- |
| Mac(Apple M1〜M4)メモリ16GB以上 | ◎ Z-Image Turbo(おすすめ)/ SDXL | × |
| Mac(Apple M1〜M4)メモリ8GB | ○ Dreamshaper 8 のみ(Z-Imageはフリーズするため使わない) | × |
| Mac(Intel) | △ 動くがかなり遅い | × |
| Windows + NVIDIA GPU(専用メモリ8GB以上。AMDも可だが導入が難しい) | ◎ Z-Image Turbo / SDXL | ○ Wan 2.1 1.3B(480p) |
| Windows(NVIDIAのGPUなし) | △ 動くが遅い可能性あり。まず Dreamshaper 8 で試す | × |

目安:
- Apple M2 で Dreamshaper 8 は1ステップ1〜2秒。1枚20ステップで30秒前後です。
- 16:9で作ったときの画像サイズ:
  - Z-Image / SDXL は 1792×1024 で出力されます。YouTubeサムネイル推奨の1280×720を超えるので、そのまま使えます。
  - Dreamshaper 8 などのSD 1.5系は 896×512 で出力されます。Canvaで1280×720に引き伸ばすため少しぼやけます。背景向きです。
- 必要なストレージの空き:
  - Z-Image Turbo: 約6GB(本体3.4GB+補助ファイル2.7GB)
  - SDXL: 約7GB
  - Dreamshaper 8: 約2GB

### 収益化動画で使ってよいモデル(ライセンス)

| モデル | ライセンス | 収益化動画・LPでの利用 |
| --- | --- | --- |
| Z-Image Turbo / Z-Image Base | Apache 2.0 | ○ 使える |
| SDXL Base 1.0 | CreativeML Open RAIL++-M | ○ 使える(違法・有害な用途の禁止などの利用制限あり) |
| Dreamshaper 8 | CreativeML OpenRAIL-M | ○ 使える(同上の利用制限あり) |
| Realistic Vision v5.1、Anything v5 | 未確認 | 使う前に legal_checker が確認。確認まではテスト用のみ |
| Wan 2.1 / Wan 2.2(動画) | Apache 2.0 | ○ 使える |
| Flux.1 Dev、Qwen Image、Hunyuan Video 1.5、LTX-2 | モデルごとに独自条件(非商用、売上条件、地域条件など) | 使う前に legal_checker が確認 |

**標準モデル:** 画像は **Z-Image Turbo**(メモリ8GBのMacは **Dreamshaper 8**)。動画は **Wan 2.1 1.3B**(NVIDIA GPUがある場合のみ)。

---

## 3. 導入手順(0円)

### ステップ1: インストーラーをダウンロードする
公式リリースページ: https://github.com/Anil-matcha/Open-Generative-AI/releases

| お使いのPC | ダウンロードするファイル |
| --- | --- |
| Mac(Apple M1〜M4) | [Open.Generative.AI-2.0.0-arm64.dmg](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI-2.0.0-arm64.dmg) |
| Mac(Intel) | [Open.Generative.AI-2.0.0.dmg](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI-2.0.0.dmg) |
| Windows(64bit) | [Open.Generative.AI.Setup.2.0.0.exe](https://github.com/Anil-matcha/Open-Generative-AI/releases/download/v2.0.0/Open.Generative.AI.Setup.2.0.0.exe) |

### ステップ2-A: Macでのインストール
このアプリはAppleの公証を受けていないため、初回だけブロックされます。

1. ダウンロードした `.dmg` を開き、アプリを「アプリケーション」フォルダへドラッグします。
2. 次のどちらかで許可します。
   - **ターミナルを使う方法**: ターミナルで次を実行し、アプリを右クリック →「開く」→ もう一度「開く」。
     ```bash
     xattr -cr "/Applications/Open Generative AI.app"
     ```
   - **ターミナルを使わない方法**: 一度アプリを開こうとしてブロックされた後、「システム設定」→「プライバシーとセキュリティ」→「"Open Generative AI"はブロックされました」の横の「このまま開く」→「開く」。
3. 2回目以降は普通に開けます。

### ステップ2-B: Windowsでのインストール
1. `.exe` をダブルクリックします。
2. 「WindowsによってPCが保護されました」と出たら「詳細情報」→「実行」をクリックします(コード署名がないために出る警告です)。
3. 自動でインストールされ、スタートメニューにショートカットができます。

### ステップ3: 起動する(APIキーは入れない)
1. アプリを起動すると、APIキーの入力画面が出ることがあります。**何も入れずに閉じます(スキップ)。**
2. キーを入れないことで、有料のクラウド生成が動かない状態になります。

### ステップ4: 無料の画像生成エンジンを入れる
1. アプリの **Settings → Local Models** を開きます。
2. **sd.cpp inference engine** をインストールします(ワンクリックで自動ダウンロード)。
3. 自分のPCに合うモデルをダウンロードします(「2. 自分のPCで何ができるか」を参照)。
   - メモリ16GB以上: **Z-Image Turbo**(補助ファイル2つも一緒にダウンロード)
   - メモリ8GBのMac / 遅いPC: **Dreamshaper 8**
4. ダウンロードはアプリの中で完結し、PC全体には何もインストールされません。

### ステップ5: テスト画像を1枚作る
1. **Image Studio** を開き、モデル選択の横にある **⚡ Local** の切り替えをオンにします。
2. ステップ4で入れたモデルを選び、比率を `16:9` にします。
3. 次のプロンプトで生成します。
   ```text
   A Japanese freelancer working on a laptop at a bright cafe, natural light, shallow depth of field, cinematic, no text
   ```
4. 生成できたらダウンロードして保存します。生成にかかった時間をメモします(AI社員が今後の作業量を見積もるのに使います)。

### ステップ6(NVIDIA GPUがあるWindowsのみ・任意): 無料の動画生成を入れる
動画のローカル生成には、別のソフト **Wan2GP** が必要です。導入に少しパソコン操作の知識が要ります。

1. Python と git を入れたうえで、PowerShell で次を実行します。
   ```bash
   git clone https://github.com/deepbeepmeep/Wan2GP
   cd Wan2GP
   install.bat
   ```
2. アプリの **Settings → Local Models → Wan2GP** で、Wan2GP のフォルダを指定し、**Save** → **Check** を押します。
3. **Video Studio** で **⚡ Local** をオンにし、**Wan 2.1 1.3B** を選びます(480p、最も軽いモデル。目安はGPUの専用メモリ6〜8GB以上)。
4. 初回はモデルの自動ダウンロードがあるため時間がかかります。

GPUがないPCでは、無料の動画は「静止画をAIで作り、無料の動画編集ソフト(CapCutの無料機能、iMovie、DaVinci Resolve無料版など)でズーム・パン(ゆっくり寄る・横に流す)をかける」方法で作ります。

---

## 4. AI会社での運用ルール

### 担当と使うスキル
| 用途 | 担当 | スキルファイル |
| --- | --- | --- |
| サムネイル用画像の生成 | thumbnail_designer | `company/agents/thumbnail_designer/skills/open_higgsfield_image_skill.md` |
| ショート・長尺動画の映像素材 | content_maker | `company/agents/content_maker/skills/open_higgsfield_video_skill.md` |
| AI生成物の権利・規約チェック | legal_checker | `company/agents/legal_checker/RULES.md` |

AI社員はプロンプト、モデル、設定を作ります。アプリでの生成ボタン操作は、ユーザー本人のPCで行います。

### 0円を守るルール
- MuAPI のキーは登録しません。
- AI社員は、有料モデル・有料スタジオ(Lip Sync、Cinema Studio、クラウドの高解像度化など)を前提にした案を出しません。
- 有料に切り替えたくなった場合は、ユーザーが判断して「付録: 有料にする場合」を使います。

### 権利・規約
このアプリは「コンテンツフィルターなし」をうたっているため、チェックは自分たちで行います。
- 実在の人物(芸能人・他人)に似せた画像・動画を作りません。
- 既存のキャラクター、ブランドロゴ、有名作品に似せた画像・動画を作りません。
- 収益化動画・LP・広告には「2. 収益化動画で使ってよいモデル」で○のモデルだけを使います。
- YouTubeでは、本物と見間違うようなリアルな合成・改変コンテンツを投稿するとき、YouTube Studio のアップロード画面で「改変または合成されたコンテンツ」の開示が必要です。実写風のAI人物・AI映像を使う場合は legal_checker と判断します。
- 動画の中でこのアプリを紹介する場合は「Open Generative AI」と呼び、Higgsfield公式の製品だと誤解される言い方をしません。

### 安全面
- アプリは公式リポジトリのリリースページからのみ入手します。
- 生成履歴はアプリ内に保存され、アプリのデータ削除や再インストールで消えます。採用した画像・動画はすぐダウンロードして保管します。

---

## 5. よくあるトラブル

| 症状 | 原因と対処 |
| --- | --- |
| Macで「開けません」「壊れています」と出る | 公証なしのため。ステップ2-Aの方法で許可する |
| Windowsで青い警告画面が出る | 署名なしのため。「詳細情報」→「実行」 |
| 生成ボタンを押すとキーを求められる | ⚡ Local がオフになっている。オンにしてローカルモデルを選ぶ |
| Macが固まる | メモリ8GBで Z-Image を使っている。Dreamshaper 8 に切り替える |
| 1枚に何分もかかる | GPUが使われていない可能性。アプリをターミナル/PowerShellから起動するとログが見える。まず Dreamshaper 8 で試す |
| モデルのダウンロードが失敗する | ストレージの空き不足を確認。Settings → Local Models から再ダウンロード |

---

## 6. ユーザーがやることチェックリスト
- [ ] 自分のPCのチップ・メモリ・GPUを確認する
- [ ] 自分のPCに合うインストーラーをダウンロードしてインストール
- [ ] 起動時のAPIキー入力はスキップ
- [ ] Settings → Local Models で sd.cpp と画像モデルを入れる
- [ ] ⚡ Local でテスト画像を1枚生成し、かかった時間をメモ
- [ ] (NVIDIA GPUがある場合のみ・任意)Wan2GP を入れて動画を試す

完了したら、チケット `company/workspace/tickets/waiting/20261126_open_higgsfield_setup.md` を `done/` に移します。

---

## 付録: 有料にする場合(任意)
- 有名モデル(Nano Banana、Kling、Veo など)、リップシンク、Cinema Studio を使いたくなった場合は、muapi.ai でアカウント作成 → 前払いチャージ → https://muapi.ai/access-keys でキー作成 → アプリにキー登録、の順で有料化できます。
- 料金は前払いクレジット制の従量課金です(月額なし)。料金表: https://muapi.ai/docs/pricing
- 有料化はユーザーが判断します。AI社員からは提案しかしません。

---

## 出典(2026-11-26確認)
- 公式リポジトリ README(ローカル生成の章): https://github.com/Anil-matcha/Open-Generative-AI
- リリース(v2.0.0): https://github.com/Anil-matcha/Open-Generative-AI/releases
- Wan2GP: https://github.com/deepbeepmeep/Wan2GP
- Z-Image Turbo(Apache 2.0): https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
- Dreamshaper 8(CreativeML OpenRAIL-M): https://huggingface.co/Lykon/dreamshaper-8
- MuAPI 料金(有料化する場合のみ): https://muapi.ai/docs/pricing

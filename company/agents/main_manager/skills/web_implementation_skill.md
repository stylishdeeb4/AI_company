# スキル名
LP・HP Web実装スキル

# 役割
LPまたはHPの構成、コピー、デザイン指示をもとに、HTML / CSS / JavaScriptなどで実装し、公開前チェックまで行うためのスキルです。

# 目的
スマホ対応、SEO、アクセシビリティ、表示速度、運用しやすさを考慮した実用的なLP・HPを実装することです。

# 使用前確認
作業前に以下を確認します。

- `company/AGENTS.md`
- `company/agents/main_manager/RULES.md`
- このファイル `company/agents/main_manager/skills/web_implementation_skill.md`
- 必要に応じて `lp_hp_creation_skill.md`
- 必要に応じて `web_design_skill.md`

成果物の冒頭またはREADMEに、使用スキル名と保存先を明記します。

# 入力情報
- LP / HPの種別
- 実装方法
- ページ構成
- セールスコピー
- デザイン指示
- 画像生成プロンプト
- SEO設定
- フォーム設計
- 法務チェック結果
- 納品してほしい成果物

# 作業手順
1. 実装方法を確認する
   - HTML / CSS / JavaScript
   - React / Next.js
   - WordPress
   - STUDIO / Wix / UTAGE / Shopify
   - Canvaモックアップ
   - おまかせ

2. 実装スコープを決める
   - 1ページLPか、複数ページHPかを確認します。
   - 必要ファイルと保存先を決めます。

3. ファイル構成を作る
   HTML / CSS / JavaScriptの場合:
   - `index.html`
   - `style.css`
   - `script.js`
   - `assets/`
   - `README.md`

4. HTML構造を作る
   - 意味のあるHTML構造にします。
   - 見出し構造を整理します。
   - CTA、フォーム、FAQ、フッターを配置します。
   - alt属性を設定します。

5. CSSを作る
   - スマホファーストで書きます。
   - タブレット、PCに対応します。
   - 余白、文字サイズ、ボタン、カード、フォームを整理します。
   - 色のコントラストを確保します。

6. JavaScriptを作る
   - 必要最小限にします。
   - FAQアコーディオン、フォーム補助、スムーススクロールなどに限定します。
   - 不要に重くしません。

7. SEO設定を入れる
   - title
   - description
   - OGP
   - H1 / H2
   - URLスラッグ案
   - 画像alt
   - FAQ構造

8. フォームを設計する
   - 入力項目
   - 必須項目
   - 任意項目
   - 送信ボタン文言
   - 送信後メッセージ
   - 個人情報同意文

9. 法務・リスクチェックを反映する
   - 誇大表現
   - 景品表示法
   - 薬機法
   - 金融・投資表現
   - 著作権
   - 商標
   - 個人情報
   - 特商法
   - プライバシーポリシー

10. 公開前チェックを行う
   - スマホ表示
   - PC表示
   - CTAリンク
   - フォーム
   - 誤字脱字
   - title / description
   - OGP
   - alt
   - 表示速度
   - アクセシビリティ
   - 法務表現
   - 全体導線

# 実装時の必須ルール
- スマホ対応
- タブレット対応
- PC対応
- alt属性の設定
- 見出し構造の整理
- title / description設定
- OGP設定
- CTAボタンのリンク仮設定
- フォーム項目の仮設定
- 不要に重い画像を使わない
- 意味のあるHTML構造にする
- CSSは読みやすく整理する
- JavaScriptは必要最小限にする

# HTML / CSS / JavaScript実装の出力形式
## index.html
```html
ここにHTMLを出力
```

## style.css
```css
ここにCSSを出力
```

## script.js
```javascript
ここにJavaScriptを出力
```

# React / Next.js実装の出力形式
- コンポーネント設計
- ページ構成
- CSS設計
- レスポンシブ対応
- SEOメタ情報
- OGP設定
- フォームUI
- CTAボタン
- FAQアコーディオン
- 画像最適化方針

# ノーコード実装の出力形式
- セクション構成
- 入力する本文
- 配置指示
- デザイン指示
- ボタン設定
- フォーム項目
- SEO設定
- 公開前チェックリスト

# SEO設定項目
- メインキーワード
- 関連キーワード
- メタタイトル
- メタディスクリプション
- H1
- H2
- URLスラッグ
- OGPタイトル
- OGP説明文
- 画像alt案
- FAQ案
- 内部リンク案
- ブログ記事案

# 保存先
途中成果物:

`company/workspace/outputs/agent_outputs/`

完成版:

`company/workspace/outputs/final_outputs/`

実装ファイル:

`company/workspace/outputs/final_outputs/lp_hp_project/`

作業ログ:

`company/workspace/logs/work_logs/`

改善ログ:

`company/workspace/logs/improvement_logs/`

# 完了条件
- ターゲットと目的が明確。
- ファーストビューで何のページか分かる。
- CTAが明確。
- スマホで読みやすい。
- ページ構成が自然。
- セールスコピーが入っている。
- ワイヤーフレームが反映されている。
- デザイン指示が反映されている。
- SEO設定がある。
- 法務・リスクチェックが反映されている。
- 公開前チェックリストがある。
- ユーザーがそのまま制作・実装に使える状態になっている。

# 実行用プロンプトテンプレート
```text
あなたはmain_managerです。
engineerとして、以下のLP/HPを実装してください。

【実装方法】
〇〇

【ページ種別】
〇〇

【ページ構成】
〇〇

【コピー】
〇〇

【デザイン指示】
〇〇

【SEO設定】
〇〇

【フォーム設計】
〇〇

【法務チェック結果】
〇〇

出力形式：
1. 実装方針
2. ファイル構成
3. index.html
4. style.css
5. script.js
6. SEO設定
7. フォーム設計
8. 公開前チェックリスト
9. 保存先
10. 改善案
```


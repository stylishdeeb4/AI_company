# 使用した正しいスキル
- LP・HP企画構成コピー作成スキル: `company/agents/content_maker/skills/lp_hp_creation_skill.md`
- LP・HP Webデザイン設計スキル: `company/agents/thumbnail_designer/skills/web_design_skill.md`
- LP・HP Web実装スキル: `company/agents/main_manager/skills/web_implementation_skill.md`

## 1. 依頼内容の整理
- 制作物: LP
- ページ目的: 無料AI業務診断の申込獲得
- ターゲット: AIを業務に使いたいが、導入順序が分からないフリーランス・個人事業主・小規模事業者
- 主なCTA: 無料診断を受ける
- 実装方法: HTML / CSS / JavaScript
- 必要ページ: 1ページ完結
- 不足情報: 正式サービス情報、診断ロジック、実績、フォーム送信先
- 仮設定: サービス名は「AI Workstyle Audit」。診断は15分、レポートはPDF想定。

## 2. ページ戦略
- ターゲットの悩み: AIツールの情報はあるが、自分の業務のどこに使えばよいか分からない。
- ターゲットが得たい未来: AI化すべき作業、後回しにする作業、30日で試す改善策が明確になる。
- 訴求軸: ツール導入前に、業務を棚卸しして優先順位を決める。
- 差別化ポイント: ツール紹介ではなく、業務分解・効果見込み・実行順序まで出す。
- CTAまでの導線: AI導入の迷い、診断の価値、診断項目、レポート例、流れ、FAQ、申込。

## 3. LP構成
| セクション | 目的 | 掲載内容 | CTA |
| --- | --- | --- | --- |
| First View | 価値提示 | メインコピー、CTA、診断内容 | 無料診断 |
| Problem | 共感 | AI導入が止まる理由 | なし |
| Diagnosis | 内容説明 | 5項目診断 | 無料診断 |
| Report | 成果物提示 | レポート内容 | なし |
| Reason | 差別化 | 業務設計の重要性 | なし |
| Flow | 行動イメージ | 申込からレポートまで | 無料診断 |
| FAQ | 不安解消 | よくある質問 | なし |
| CTA | 申込導線 | 最終案内 | 無料診断 |

## 4. ファーストビュー案
- メインキャッチ: AI導入の前に、まず「任せる仕事」を決める。
- サブコピー: 15分の無料診断で、あなたの業務をAI化しやすい順に整理し、30日で試す改善ロードマップを作ります。
- CTAボタン: 無料診断を受ける
- 補足文: 初心者歓迎・オンライン対応・営業目的の診断ではありません
- 背景画像案: 業務カードがAI診断ボード上で分類されるビジュアル
- 信頼要素: 15分診断、5項目チェック、30日アクション
- スマホ表示の注意点: Hero内でCTAと3つの信頼要素を見せる。

## 5. セクション別コピー
### First View
- 見出し: AI導入の前に、まず「任せる仕事」を決める。
- 本文: AI Workstyle Auditは、あなたの業務を棚卸しし、AIで効率化しやすい作業を優先順位つきで整理する無料診断です。
- CTA: 無料診断を受ける
- 画像案: 業務カードを診断するワークボード

### Problem
- 見出し: AIツールを増やしても、業務は自動では変わりません。
- 本文: 多くの人が、AIツールを探すところで止まります。本当に必要なのは、どの作業を任せるか、どの順番で試すかを決めることです。
- 箇条書き: ツール比較で迷う / プロンプトが定着しない / 効果が見えず続かない

### Diagnosis
- 見出し: 5つの観点で、AI化しやすい業務を診断します。
- 箇条書き: 頻度 / 時間 / 判断の難しさ / テンプレート化しやすさ / 収益・発信への影響
- CTA: 無料診断を受ける

### Report
- 見出し: 診断後に、30日で試すロードマップを渡します。
- 本文: すぐ試す作業、準備が必要な作業、今はやらない作業を分けます。成果保証ではなく、実行順序を明確にするためのレポートです。

### FAQ
- 見出し: よくある質問
- 本文: 初心者でも使えるか、診断だけでよいか、ツール指定があるか、成果保証の有無などを回答します。

## 6. ワイヤーフレーム
```text
[Header]
ロゴ / ナビ / CTA

[First View]
メインコピー
サブコピー
CTA
診断ボード画像

[Problem]
AI導入で止まる理由

[Diagnosis]
5項目診断

[Report]
診断レポート内容

[Reason]
選ばれる理由

[Flow]
利用の流れ

[FAQ]
よくある質問

[CTA]
無料診断

[Footer]
運営者情報 / 規約
```

## 7. デザイン指示
- デザイン方針: 実務的、診断ツール感、信頼感。
- メインカラー: Navy `#101828`
- サブカラー: Blue `#2563eb`
- アクセントカラー: Lime `#a3e635`
- フォント方針: system-ui、見出し太め、本文は読みやすく。
- ボタンデザイン: 8px角丸、塗りCTA、補助ボタンはアウトライン。
- 余白: セクション間を広く、カード内は24px以上。
- 画像の雰囲気: 業務カード、診断ボード、チェックリスト。
- スマホ表示: 1カラム、CTAは大きく、診断項目は縦積み。
- PC表示: HeroとReportは2カラム。
- 注意点: 成果保証に見える文言を避ける。

## 8. 画像生成プロンプト
### 画像1
- 用途: ファーストビュー
- 配置場所: Hero右側
- プロンプト: `Professional AI workflow audit dashboard, task cards sorted into priority columns, clean desk, laptop, checklist, navy blue and lime accents, practical business style, no logos, no readable brand text, website hero image`
- 避けたい表現: 実在サービスロゴ、過度なSF、読めるUI文字

### 画像2
- 用途: 診断レポート
- 配置場所: Report section
- プロンプト: `Simple AI workstyle audit report, priority matrix, 30 day action roadmap, clean business document, blue and lime color accents, no logos, no readable text`
- 避けたい表現: 成果保証、売上保証、複雑すぎる文字

### 画像3
- 用途: CTA前
- 配置場所: Final CTA
- プロンプト: `Small business owner reviewing organized AI task roadmap, calm confident atmosphere, laptop and checklist, practical consulting mood, no logos, no text`
- 避けたい表現: 札束、過度な成功演出、実在ロゴ

## 9. 実装ファイル
`company/workspace/outputs/final_outputs/lp_hp_project/ai_workstyle_audit_lp/`

## 10. SEO設定
- メインキーワード: AI 業務効率化 診断
- 関連キーワード: AI導入 初心者, ChatGPT 業務改善, AI活用 何から, 業務自動化 相談
- メタタイトル: AI Workstyle Audit | AI導入前の無料業務診断
- メタディスクリプション: AI導入前に、あなたの業務を棚卸し。AI化しやすい作業と30日で試す改善ロードマップを無料診断で整理します。
- H1: AI導入の前に、まず「任せる仕事」を決める。
- URLスラッグ: `ai-workstyle-audit`
- OGPタイトル: AI Workstyle Audit
- OGP説明文: AI導入前の無料業務診断。AI化しやすい作業と30日ロードマップを整理します。
- 画像alt案: AI業務診断ボードでタスクを優先順位ごとに整理する画面

## 11. フォーム設計
- フォームの目的: 無料診断申込
- 入力項目: 名前、メール、業種、相談したい業務、希望日時
- 必須項目: 名前、メール、相談したい業務
- 任意項目: 業種、希望日時
- 送信ボタン文言: 無料診断を申し込む
- 送信後メッセージ: 送信ありがとうございます。内容を確認し、診断日程についてご連絡します。
- 個人情報同意文: 入力内容は診断対応のために使用します。プライバシーポリシーをご確認ください。

## 12. 法務・リスクチェック
- 誇大表現: 成果保証、売上保証、必ず自動化できる表現は不使用。
- 景品表示法: 実績は掲載していない。
- 薬機法: 該当なし。
- 金融・投資表現: 該当なし。
- 著作権: 画像は自作生成素材。
- 商標: 特定AIサービス名に依存しない。
- 個人情報: フォーム同意文を設置。
- 特商法: 有料販売時は別途必要。
- プライバシーポリシー: 仮リンク。
- 修正が必要な表現: 診断項目と運営者情報は正式情報に差し替え。

## 13. 公開前チェックリスト
- スマホ表示確認: CSS対応済み。実機確認推奨。
- PC表示確認: CSS対応済み。
- CTAリンク: ページ内リンク。
- フォーム: UIのみ。送信処理は仮。
- 誤字脱字: 簡易確認済み。
- title: 設定済み。
- description: 設定済み。
- OGP: 設定済み。
- alt: 設定済み。
- 表示速度: 画像1枚中心で軽量。
- アクセシビリティ: label、focus、semantic HTML対応。
- 法務表現: 成果保証表現なし。
- 全体導線: 問題、診断、レポート、流れ、FAQ、CTA。

## 14. 改善案
- CVR改善案: CTAを「15分でAI化できる業務を診断する」に変更テスト。
- ファーストビュー改善案: ターゲットを「個人事業主」か「会社員」に絞る。
- CTA改善案: 無料診断とLINE相談の反応差を検証。
- SEO改善案: 「AI導入 何から」「ChatGPT 業務改善」記事を追加。
- デザイン改善案: 実際の診断レポート画面を追加。
- 追加入力すべき情報: 診断項目、運営者プロフィール、予約URL、プライバシーポリシー。

## 15. 保存先
- 途中成果物: `company/workspace/outputs/agent_outputs/20260608_ai_workstyle_audit_lp_plan.md`
- 完成版: `company/workspace/outputs/final_outputs/20260608_ai_workstyle_audit_lp_package.md`
- 実装ファイル: `company/workspace/outputs/final_outputs/lp_hp_project/ai_workstyle_audit_lp/`
- 作業ログ: `company/workspace/logs/work_logs/20260608_ai_workstyle_audit_lp.md`
- 改善ログ: `company/workspace/logs/improvement_logs/20260608_ai_workstyle_audit_lp_improvement.md`


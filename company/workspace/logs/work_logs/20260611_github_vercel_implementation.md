# 作業ログ: GitHub / Vercel 公開実装

- 作業日時: 2026-06-11
- 担当: main_manager
- 対象業務: AI業務改善診断LP / HPを GitHub と Vercel に載せやすい形へ整備

## 確認した内容
- GitHub リモートは `origin=https://github.com/stylishdeeb4/AI_company.git`
- ルート `index.html` は `ai_business_diagnosis_lp/` へリダイレクトする構成
- Vercel CLI はローカル未導入
- GitHub 認証は `gh auth status` で有効

## 実施した変更
- `.gitignore` に `node_modules/` と `.vercel/` を追加
- `vercel.json` を追加
- Vercel で `/` `/service` `/faq` `/columns` が `ai_business_diagnosis_lp` 配下の静的HTMLへ向くように設定
- アセット、`style.css`、`script.js` も Vercel ルーティング対象に追加

## 判断メモ
- GitHub Pages 側はルート `index.html` リダイレクト構成を維持した
- Vercel 側はリポジトリルートから直接 `ai_business_diagnosis_lp` を公開できるように、ネストした成果物を明示的にルーティングする方針にした
- Vercel CLI 未導入のため、ローカルからの即時 deploy は未実施

## 次の作業
- GitHub に必要ファイルを commit / push する
- Vercel プロジェクトをこのリポジトリに接続し、ルート公開を確認する
- 公開後に `/` `/service` `/faq` `/columns` の表示確認を行う

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
- GitHub へ commit / push を実施
- 公開フォルダ `ai_business_diagnosis_lp/` 単体にも `vercel.json` を追加
- 公開フォルダ単体を Vercel 本番デプロイし、専用URLを発行

## 判断メモ
- GitHub Pages 側はルート `index.html` リダイレクト構成を維持した
- Vercel 側はリポジトリルートから直接 `ai_business_diagnosis_lp` を公開できるように、ネストした成果物を明示的にルーティングする方針にした
- リポジトリルート全体ではサイズ超過になったため、公開対象フォルダ単体を Vercel デプロイ対象に切り替えた

## 公開結果
- GitHub Pages:
  - URL: `https://stylishdeeb4.github.io/AI_company/`
  - 確認内容: トップ応答 `200`、`service.html` 応答 `200`、`faq.html` 応答 `200`
- Vercel:
  - Inspect URL: `https://vercel.com/stylishdeeb4s-projects/ai_business_diagnosis_lp/7WajizrzKkppULfR4d6R87aDyrJL`
  - Production URL: `https://aibusinessdiagnosislp.vercel.app`
  - 確認内容: `/` 応答 `200`、`/faq` 応答 `200`、`/service` ヘッダ応答 `200`、`/columns` ヘッダ応答 `200`

## 次の作業
- Vercel の本番URLを必要に応じて案内用URLとして採用する
- GitHub 側にも今回の Vercel 用補助ファイルを commit / push する
- 予約リンク、フォーム送信先、法務ページURLを実運用値に差し替える

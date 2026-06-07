# LP/HP制作依頼テンプレート README

## 役割
`lp_hp_request_prompt.md` の用途と使い方を説明する補助ファイルです。

## 目的
LP・HP制作依頼を受けたとき、main_managerが必要なAI社員を選び、企画・構成・コピー・デザイン・実装・SEO・法務チェック・品質チェックまで一括で進められるようにします。

## 使い方
LPまたはHP制作を依頼するときは、`lp_hp_request_prompt.md` の各項目を埋めて使用します。不足情報がある場合は、main_managerが仮設定を置いて作業を進めます。

## 保存先
`company/workspace/templates/lp_hp_request_prompt_README.md`

## 完了条件
LP/HP制作依頼テンプレートの場所、用途、使い方が分かること。

## 関連ファイル
- テンプレート本体: `company/workspace/templates/lp_hp_request_prompt.md`
- 汎用依頼テンプレート: `company/workspace/templates/request_template.md`
- AI会社一括起動プロンプト: `company/workspace/templates/company_startup_prompt.md`

## 使用時の担当エージェント
- main_manager: 全体整理、タスク分解、品質確認
- researcher: 市場・競合・SEO調査
- content_maker: コピー、本文、FAQ作成
- thumbnail_designer: designer兼任としてワイヤーフレーム、デザイン指示、画像案作成
- legal_checker: 表現・法務リスク確認
- secretary: チケット、ログ、ファイル整理

## 不足しているエージェントの扱い
現時点で `marketer`、`designer`、`engineer`、`seo_specialist`、`quality_checker` は専用エージェントとして存在しません。テンプレートの指定どおり、以下の兼任で進めます。

- marketer: main_manager + content_maker
- designer: thumbnail_designer
- engineer: main_managerがCodex実装担当として実行
- seo_specialist: researcher
- quality_checker: main_manager


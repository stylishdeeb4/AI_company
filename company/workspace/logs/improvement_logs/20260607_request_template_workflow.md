# 改善ログ: 依頼テンプレートとAI会社一括起動ルールの追加

## 役割
ユーザーからの依頼形式と、AI会社が依頼を受けた後の標準手順を記録します。

## 目的
依頼ごとの認識ズレを減らし、エージェント選定、チケット作成、スキル確認、保存、ログ記録を毎回実行するためです。

## 使い方
今後の作業依頼を受ける前に、標準依頼フローの改善履歴として参照します。

## 保存先
`company/workspace/logs/improvement_logs/20260607_request_template_workflow.md`

## 完了条件
依頼テンプレート、必須作業順序、一括起動ルール、反映ファイルが明記されていること。

# 追加内容
- ユーザー依頼テンプレートを作成。
- AI会社一括起動プロンプトを作成。
- `AGENTS.md`、`docs/workflow.md`、`main_manager/RULES.md`、`main_manager/MEMORY.md` に運用ルールを反映。

# 反映ファイル
- `company/AGENTS.md`
- `company/docs/workflow.md`
- `company/agents/main_manager/RULES.md`
- `company/agents/main_manager/MEMORY.md`
- `company/workspace/templates/request_template.md`
- `company/workspace/templates/company_startup_prompt.md`


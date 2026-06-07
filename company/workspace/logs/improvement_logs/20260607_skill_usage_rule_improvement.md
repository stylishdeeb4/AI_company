# 改善ログ: 正しいスキル使用ルールの追加

## 役割
正しいスキルファイルを確認してから成果物を作るための改善内容を記録します。

## 目的
新しく作成したスキルがあるにもかかわらず、古い手順や曖昧な記憶で作業してしまうことを防ぐためです。

## 使い方
スキルを使う依頼を受けたとき、作業前確認のルールとして参照します。

## 保存先
`company/workspace/logs/improvement_logs/20260607_skill_usage_rule_improvement.md`

## 完了条件
改善対象、追加ルール、反映ファイル、次回確認項目が明記されていること。

# 改善対象
- main_managerの作業分解と最終確認
- content_makerのYouTube台本作成
- thumbnail_designerのサムネイル案作成

# 追加ルール
- 作業前に使用するスキルファイルの場所を確認する。
- 成果物を作る前に、参照したスキル名と保存先を明記する。
- `company/agents/*/skills/` に新しいスキルがある場合は、そのスキルを優先する。
- 意図と違う成果物が出た場合は、原因を `error_logs` に残す。
- 修正後は、同じ依頼を正しいスキルで改めて実行する。

# 反映ファイル
- `company/agents/main_manager/RULES.md`
- `company/agents/main_manager/MEMORY.md`
- `company/agents/content_maker/RULES.md`
- `company/agents/content_maker/MEMORY.md`
- `company/agents/content_maker/skills/youtube_script_skill.md`
- `company/agents/thumbnail_designer/RULES.md`
- `company/agents/thumbnail_designer/MEMORY.md`
- `company/agents/thumbnail_designer/skills/thumbnail_creation_skill.md`

# 次回確認項目
- 使用スキル名が成果物に書かれているか。
- スキル保存先が成果物に書かれているか。
- スキルの出力形式に沿っているか。
- スキルの品質基準でチェックしているか。


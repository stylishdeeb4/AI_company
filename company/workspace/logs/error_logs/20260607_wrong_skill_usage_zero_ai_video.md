# エラーログ: 正しいスキル参照不足による成果物ミスマッチ

## 役割
今回の成果物がユーザー意図とズレた原因、修正内容、再発防止策を記録します。

## 目的
次回以降、古いスキルや曖昧な手順ではなく、正しいフォルダにある最新スキルを確認してから作業するためです。

## 使い方
YouTube台本、サムネイル、複数エージェント連携の依頼を受ける前に参照します。

## 保存先
`company/workspace/logs/error_logs/20260607_wrong_skill_usage_zero_ai_video.md`

## 完了条件
何が起きたか、本来どうすべきだったか、原因、誤認識、修正対象、再発防止策が明記されていること。

# 何が起きたか
「0から始めるAI活用」の5万人達成感謝動画制作で、成果物作成前に使用するスキルファイル名と保存先を明記しなかった。

また、content_makerとthumbnail_designer用に新しく作成済みの正しいスキルを、作業工程として明示的に参照した記録が不足していた。その結果、ユーザーから見ると「正しいスキルを使った成果物」ではなく、通常のアドホックな成果物に見える状態になった。

# 本来どうすべきだったか
- 作業前に `company/agents/content_maker/skills/youtube_script_skill.md` を確認する。
- 作業前に `company/agents/thumbnail_designer/skills/thumbnail_creation_skill.md` を確認する。
- 成果物を作る前に、参照したスキル名と保存先を明記する。
- 台本は `youtube_script_skill.md` の入力情報、作業手順、台本テンプレート、品質基準に沿って作る。
- サムネイル案は `thumbnail_creation_skill.md` の入力情報、作業手順、出力形式、品質基準に沿って作る。
- 意図と違う成果物が出た場合は、原因を `error_logs` に残してから修正する。

# なぜミスが起きたか
- main_managerの作業手順に「使用するスキルファイルの場所を確認し、成果物内に明記する」という工程がなかった。
- content_makerとthumbnail_designerのRULESに、スキルファイルの確認を必須化する記述が弱かった。
- 直前に作成したスキルを使うべき場面で、スキル名・パス・適用箇所を成果物に明記しなかった。
- 最終成果物の保存は行ったが、正しいスキルを使った証跡が不足していた。

# どのルール・スキル・保存先の認識が間違っていたか
- ルール: main_managerの作業手順に、スキル確認と使用スキル明記が不足していた。
- ルール: content_makerとthumbnail_designerの作業手順に、作業前のスキルファイル確認が不足していた。
- スキル: `youtube_script_skill.md` と `thumbnail_creation_skill.md` を、成果物作成の明示的な基準として使う必要があった。
- 保存先: エラー時は `company/workspace/logs/error_logs/`、改善策は `company/workspace/logs/improvement_logs/` に保存すべきだった。

# どのファイルを修正すべきか
- `company/agents/main_manager/RULES.md`
- `company/agents/main_manager/MEMORY.md`
- `company/agents/content_maker/RULES.md`
- `company/agents/content_maker/MEMORY.md`
- `company/agents/content_maker/skills/youtube_script_skill.md`
- `company/agents/thumbnail_designer/RULES.md`
- `company/agents/thumbnail_designer/MEMORY.md`
- `company/agents/thumbnail_designer/skills/thumbnail_creation_skill.md`
- `company/workspace/logs/improvement_logs/20260607_skill_usage_rule_improvement.md`

# 次回以降の再発防止策
1. 作業前に必ず使用するスキルファイルの場所を確認する。
2. 成果物の冒頭に、参照したスキル名と保存先を明記する。
3. 新しいスキルが `company/agents/*/skills/` にある場合は、古い手順や記憶ではなくそのファイルを優先する。
4. 意図と違う成果物が出た場合は、原因、修正内容、再発防止策を `error_logs` に記録する。
5. 修正後は同じ依頼を、正しいスキルを使って改めて実行する。


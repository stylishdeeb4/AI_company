# 無料クラウドAI画像・動画生成サービス調査

## 役割
ユーザーのPC(Windows / Core i5-7200U / メモリ16GB / Intel HD Graphics 620)ではローカルのAI生成が遅いため、無料で使えるクラウドの画像・動画生成サービスを比較した調査資料です。担当: researcher。

## 目的
サムネイル画像とショート動画の素材を、0円で、収益化したYouTube動画に使える条件で作れるサービスを選ぶためです。

## 使い方
- 「1. 結論」で標準ツールを確認します。
- 新しいサービスを使う前に「3. 使わないサービス」に入っていないか確認します。
- 無料枠や規約はよく変わるため、使う前に各サービスの画面と規約で最新の条件を確認します。

## 保存先
`company/workspace/references/20261126_free_cloud_ai_generation_research.md`

## 完了条件
無料枠、商用利用、透かし、注意点がサービスごとに整理され、標準ツールの推奨があること。

## 調査方法と限界(2026-11-26)
- この作業環境では各社の公式ページを直接開けなかった(ネットワーク制限)。代わりに、検索対象を各社の公式ドメイン(adobe.com、openai.com、policies.google.com、support.google.com、ideogram.ai など)に絞った検索結果で確認した。
- 「公式」と書いた項目は公式ドメインの検索結果で確認したもの。「第三者情報」と書いた項目はレビューサイトの情報で、確度が低い。
- 法的な判断ではない。収益化動画で初めて使う前に legal_checker が規約本文を確認する。

---

## 1. 結論

| 用途 | 標準ツール | 理由 |
| --- | --- | --- |
| サムネイル画像 | **Adobe Firefly(無料プラン、Adobe自社のFireflyモデル)** | 毎日の無料枠があり、Adobeが「商用利用向けに設計」と明言している |
| サムネイル画像(補助) | ChatGPT(無料)、Gemini(無料) | 画質が高い。生成物の権利はユーザー側(規約上)。ただし無料枠が少なく、数が公表されていない |
| 文字入りデザインの試作 | Ideogram(無料) | 商用利用可と公式に明記。ただし無料プランの画像は全て一般公開される |
| ショート動画の素材 | **Adobe Firefly(無料プラン、Firefly Video Model)** | 毎日の無料枠があり、透かしなし(公式FAQ)、Adobe自社モデルは商用利用向け |
| 文字入れ・仕上げ | Canva(無料) | AI生成機能は使わず、文字入れとレイアウトだけに使う |
| 予備 | Open Generative AI のローカル生成(Dreamshaper 8) | 回数制限なしで0円だが、このPCでは1枚数分以上かかる見込み |

---

## 2. 使ってよいサービスの詳細

### Adobe Firefly(無料プラン)
| 項目 | 内容 | 確度 |
| --- | --- | --- |
| 無料枠 | 画像・動画などの生成AI機能で、毎日一定回数まで無料。毎日リセット。回数は非公表で変わることがある | 公式 |
| 動画 | 無料ユーザーも Firefly Video Model と一部のパートナーモデルで、文章→動画、画像→動画が使える | 公式 |
| 商用利用 | Adobe自社のFireflyモデルの出力は商用利用向けに設計。ベータ表示のない機能は商用プロジェクトに使える。ベータ機能も、製品内で特に断りがなければ商用利用可 | 公式 |
| パートナーモデル | Google・OpenAIなど他社モデルは条件が異なり、商用に使えるかの判断は作成者の責任 | 公式 |
| 透かし | 動画には透かしを付けない(Fireflyモデル、パートナーモデルとも) | 公式 |
| その他 | 出力に「コンテンツクレデンシャル」(AIで作ったことを示す情報)が付く。消さない | 公式 |
| 注意 | Fireflyで作った画像を動画の開始画像に使おうとすると、コンテンツクレデンシャルのためにはじかれることがある | 第三者情報(ユーザー報告) |

**ルール:** モデル選択では Adobe の「Firefly」モデルを選び、パートナーモデル(Google、OpenAI など)は使わない。

### ChatGPT(無料プラン)
| 項目 | 内容 | 確度 |
| --- | --- | --- |
| 無料枠 | 1日2〜3枚程度との報告が多いが、OpenAIは数を公表していない | 第三者情報 |
| 権利 | 利用規約上、法律が許す範囲で出力の権利はユーザーに移る | 公式 |
| 注意 | 他のユーザーにも似た出力が出ることがある(独占できない) | 公式 |

### Gemini(無料)
| 項目 | 内容 | 確度 |
| --- | --- | --- |
| 無料枠 | 使った計算量で決まる上限制。5時間ごとに回復し、週ごとの上限あり。Nano Banana Pro は少しだけ使え、超えると通常版に切り替わる。自分の残り回数は「設定 → 使用量の上限」で確認できる | 公式 |
| 枚数の目安 | 1日20枚程度との報告 | 第三者情報 |
| 権利 | Googleは生成されたコンテンツの所有権を主張しない(Google利用規約) | 公式 |
| 動画(Veo) | 無料ユーザーは使えない(有料プランの機能) | 公式 |
| 透かし | 全画像に見えない透かし(SynthID)が入る。無料版で目に見える透かしが入るかは情報が食い違う | 第三者情報 |

### Ideogram(無料プラン)
| 項目 | 内容 | 確度 |
| --- | --- | --- |
| 無料枠 | 週30クレジット(毎週土曜 00:00 UTC にリセット)。Google または Apple でログインしたアカウントが対象(Microsoftログインの扱いはページによって食い違う) | 公式 |
| 権利 | Ideogramは所有権を主張せず、商用利用を含めどんな目的にも使ってよい | 公式 |
| 注意 | 無料プランで作った画像は全て一般公開される。公開前の動画のサムネイル案が他人に見える | 公式 |

---

## 3. 使わないサービス(収益化動画には不向き)

| サービス | 理由 | 確度 |
| --- | --- | --- |
| Microsoft Designer / Copilot の画像生成 | Designerの規約が「個人利用のみ、商用不可」と引用されている。無料版は商用不可との回答もある | 第三者情報(Microsoft Q&A) |
| Canva の AI画像生成(Magic Media) | 無料プランのAI生成物は商用不可とするレビューが多い。文字入れ・レイアウトには使ってよい | 第三者情報 |
| Google Flow / ImageFX / Whisk(Google Labs) | Labs の試験提供で、個人の非商用利用向けとの報告 | 第三者情報(Googleコミュニティ) |
| Kling(無料) | 無料プランは個人の非商用利用のみ。透かしあり | 第三者情報 |
| Hailuo、Pika など | 無料版は透かしあり、または商用ライセンスなしとの報告 | 第三者情報 |
| Grok Imagine | 無料プランで動画は使えないとの報告が多い。画像は権利がユーザー側とされるが、Grokの表記を求めている | 第三者情報 |

---

## 4. 共通ルール
- 実在の人物、既存キャラクター、ブランドロゴ、有名作品に似せた画像・動画を作らない。
- 本物と見間違うリアルなAI人物・AI映像を使う動画は、YouTube Studio で「改変または合成されたコンテンツ」の開示を legal_checker と判断する。
- AI生成物は著作権で守られない可能性があり、他人が似た画像を使っても止められないことがある。チャンネルの顔になる要素(ロゴ、キャラクター)はAI生成だけに頼らない。
- 無料枠は予告なく変わる。使えなくなったら、他の標準ツールか予備(ローカル生成)に切り替える。

---

## 出典
- Adobe Firefly: https://www.adobe.com/products/firefly.html
- Adobe 生成クレジット FAQ: https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html
- Adobe AI動画生成: https://www.adobe.com/products/firefly/features/ai-video-generator.html
- Adobe 画像→動画 FAQ: https://www.adobe.com/products/firefly/features/image-to-video.html
- Adobe パートナーモデル: https://www.adobe.com/in/products/firefly/discover/partner-models-ai-creative-workflows.html
- OpenAI 利用規約: https://openai.com/policies/row-terms-of-use/
- Gemini アプリの上限: https://support.google.com/gemini/answer/16275805?hl=en
- Google AI プラン: https://gemini.google/subscriptions/
- Google 利用規約: https://policies.google.com/terms?hl=en-US
- Nano Banana Pro 発表: https://blog.google/innovation-and-ai/products/nano-banana-pro/
- Ideogram 料金: https://ideogram.ai/pricing/
- Ideogram プランとクレジット: https://docs.ideogram.ai/plans-and-billing/available-plans
- Microsoft Designer の商用利用(Q&A): https://learn.microsoft.com/en-us/answers/questions/5677241/can-i-use-a-microsoft-designer-created-image-for-c
- Google Flow の商用利用(コミュニティ): https://support.google.com/gemini/thread/410116358/i-want-to-know-that-if-i-use-flow-to-generate-image-and-video-can-i-use-them-for-commercial-use?hl=en
- Canva 無料プランの商用利用(レビュー): https://www.marqeable.com/blog/canva-ai-image-generator-review-marketing/
- Kling 無料プラン(レビュー): https://www.eesel.ai/blog/kling-ai-pricing
- Grok Imagine 無料プラン(レビュー): https://aliteq.com/is-grok-imagine-free

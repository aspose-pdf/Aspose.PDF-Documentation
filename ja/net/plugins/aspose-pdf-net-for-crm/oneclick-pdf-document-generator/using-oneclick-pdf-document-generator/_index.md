---
title: OneClick PDFドキュメントジェネレータの使用
type: docs
weight: 10
url: ja/net/using-oneclick-pdf-document-generator/
description: Microsoft DynamicsでAspose.PDF OneClick PDFドキュメントジェネレータを使用する方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## テンプレートを作成しCRMに追加する

- Wordを開き、テンプレートを作成します。
- CRMからデータを取得するMailMergeフィールドを挿入します。

![MailMergeフィールドを挿入](using-oneclick-pdf-document-generator_1.png)

- フィールド名がCRMのフィールドと正確に一致していることを確認します。
- テンプレートは個々のエンティティで使用するためのものです。

![デモテンプレート](using-oneclick-pdf-document-generator_2.png)

- テンプレートが作成されたら、CRM内でOneClick PDF Configurationエンティティを開き、新しいレコードを作成します。
- テンプレートの名前を付け、テンプレートが定義されているエンティティを選択し、作成したドキュメントを添付ファイルに添付します。

![テンプレートを選択](using-oneclick-pdf-document-generator_3.png)

## リボンボタンからドキュメントを生成する

- ドキュメントを生成したいレコードを開きます。
- ドキュメントを生成したいレコードを開きます。
- リボンからOneClick PDFボタンをクリックします。

![Click OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- ポップアップから: テンプレート、ファイル名、アクションを選択し、生成をクリックします。
- 選択に基づいて、ダウンロードされたファイルまたはメモを確認します。

## OneClickボタンの設定と使用

- フォームから直接OneClickボタンを使用するために、フォームカスタマイズを開きます。
- OneClickボタンを追加したい場所にWebResourceを挿入します。
- WebresourceでOpenButtonPageを選択し、名前を付けます。
- 以下のサンプルでデータフィールドにボタンを設定します。

![WebResource Properties](using-oneclick-pdf-document-generator_5.png)

- 各ボタンについて別の行を使用し、次の構文を使用します：
  - 構文:テンプレート名 |<アクション: ダウンロード/ノート>|出力ファイル名
  - 例:デモ|ダウンロード|私のダウンロードファイル
- カスタマイズを保存して公開します。
- フォームにボタンが利用可能です。

![The button is available on the form](using-oneclick-pdf-document-generator_6.png)
![The button is available on the form](using-oneclick-pdf-document-generator_6.png)

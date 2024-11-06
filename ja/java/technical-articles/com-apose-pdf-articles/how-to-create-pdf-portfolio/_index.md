---
title: PDFポートフォリオの作成方法
type: docs
weight: 10
url: ja/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

PDFポートフォリオは、さまざまなソースからのコンテンツ（例：PDF、Word、Excel、JPEGファイル）を1つの統一されたコンテナにまとめることができます。元のファイルは個々のアイデンティティを維持しますが、PDFポートフォリオファイルにまとめられます。ユーザーは、各コンポーネントファイルを他のコンポーネントファイルとは独立して開く、読む、編集する、フォーマットすることができます。

Aspose.PDF for Javaを使用すると、Documentクラスを使用してPDFポートフォリオドキュメントを作成できます。個々のファイルをFileSpecificationオブジェクトにロードし、add(...)メソッドを使用してDocument.Collectionオブジェクトに追加します。ファイルが追加されたら、Documentクラスのsave(..)メソッドを使用してポートフォリオドキュメントを生成します。

{{% /alert %}}

## コードサンプル

以下の例では、Microsoft XPSファイル、Wordドキュメント、PDF、および画像ファイルを使用してPDFポートフォリオを作成します。

**Aspose.PDFで作成されたPDFポートフォリオ**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}
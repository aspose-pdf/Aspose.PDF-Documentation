---
title: PDFファイルから生のテキストを抽出する
linktitle: PDFからテキストを抽出
type: docs
weight: 10
url: ja/php-java/extract-text-from-all-pdf/
description: この記事では、Aspose.PDF for PHPを使用してPDF文書からテキストを抽出するさまざまな方法について説明します。ページ全体から、特定の部分から、列に基づいて、など。
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF文書のすべてのページからテキストを抽出する

PDF文書からテキストを抽出することは一般的な要求です。この例では、Aspose.PDF for PHPがPDF文書のすべてのページからテキストを抽出する方法を示します。
すべてのPDFページからテキストを抽出するには：

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)クラスのオブジェクトを作成します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用してPDFを開き、[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) コレクションの [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) メソッドを呼び出します。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) クラスはドキュメントからテキストを吸収し、[getText() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--)で返します。

次のコードスニペットは、PDFドキュメントのすべてのページからテキストを抽出する方法を示しています。

```php

    // 入力PDFファイルから新しいDocumentオブジェクトを作成します。
    $document = new Document($inputFile);

    // ドキュメントからテキストを抽出するための新しいTextAbsorberオブジェクトを作成します。
    $textAbsorber = new TextAbsorber();

    // ドキュメントからテキストを抽出します。
    $textAbsorber->visit($document);

    // 抽出されたテキストの内容を取得します。
    $content = $textAbsorber->getText();

    // 抽出されたテキストを出力ファイルに保存します。
    file_put_contents($outputFile, $content);
```
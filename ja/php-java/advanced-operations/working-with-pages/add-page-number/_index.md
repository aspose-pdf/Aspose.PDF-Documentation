---
title: PDFにページ番号を追加
linktitle: ページ番号を追加
type: docs
weight: 100
url: /ja/php-java/add-page-number/
description: Aspose.PDF for PHP via Javaは、PageNumber Stampクラスを使用してPDFファイルにページ番号のスタンプを追加できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

すべてのドキュメントにはページ番号が必要です。ページ番号は、読者がドキュメントの異なる部分を見つけやすくします。
**Aspose.PDF for PHP via Java**を使用すると、PageNumberStampを使用してページ番号を追加できます。

{{% alert color="primary" %}}

オンラインで試すことができます。このリンクでAspose.PDFの変換品質をチェックし、結果をオンラインで見ることができます [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number)

{{% /alert %}}

[PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) クラスを使用して、PDFドキュメントにページ番号のスタンプを追加できます。
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) クラスは、ページ番号に基づくスタンプを作成するためのメソッドを提供します。例えばフォーマット、マージン、アライメント、開始番号などです。ページ番号スタンプを追加するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトと、必要なテキストプロパティを持つ [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) オブジェクトを作成する必要があります。その後、PDFファイルにスタンプを追加するために [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスの [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.Page#addStamp-com.aspose.pdf.Stamp-) メソッドを呼び出すことができます。また、ページ番号スタンプのフォント属性を設定することもできます。

以下のコードスニペットは、PDFファイルにページ番号を追加する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ページ番号スタンプを作成
    $pageNumberStamp = new PageNumberStamp();

    // スタンプが背景かどうか
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // テキストプロパティを設定
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // 特定のページにスタンプを追加
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```
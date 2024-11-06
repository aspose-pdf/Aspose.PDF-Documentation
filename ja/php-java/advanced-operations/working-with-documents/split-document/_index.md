---
title: PDFをプログラムで分割する
linktitle: PDFファイルを分割する
type: docs
weight: 60
url: ja/php-java/split-document/
description: このトピックでは、PHPアプリケーションでPDFページを個々のPDFファイルに分割する方法を示します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDFを使用してPDFファイルを分割し、このリンクで結果をオンラインで取得できます：[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

このトピックでは、Aspose.PDF for PHP via Javaを使用して、PHPアプリケーション内でPDFページを個別のPDFファイルに分割する方法を示します。PHPを使用してPDFページを1ページのPDFファイルに分割するには、以下の手順に従います：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) コレクションを介してPDFドキュメントのページをループします。

1. 各反復処理で、新しい Document オブジェクトを作成し、個々の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) オブジェクトを空のドキュメントに追加します。
1. Save メソッドを使用して新しい PDF を保存します。

次の PHP コードスニペットは、PDF ページを個別の PDF ファイルに分割する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // すべてのページをループする
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```
---
title: PHPでPDFのページ数を取得する
type: docs
weight: 40
url: ja/java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - ページ数を取得

**Aspose.PDF Java for PHP**を使用してPDFドキュメントのページ数を取得するには、単に**GetNumberOfPages**クラスを呼び出します。

PHPコード

```php

# PDFドキュメントを作成

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "ページ数:" . $page_count . PHP_EOL;

```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**ページ数を取得 (Aspose.PDF)**をダウンロードします：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
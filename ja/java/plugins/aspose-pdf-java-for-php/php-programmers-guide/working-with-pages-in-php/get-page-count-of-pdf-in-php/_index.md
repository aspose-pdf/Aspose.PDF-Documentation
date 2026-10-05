---
title: "PHP での PDF のページ数の取得"
linktitle: "PHP での PDF のページ数の取得"
type: docs
weight: 40
url: /ja/java/get-page-count-of-pdf-in-php/
description: Aspose.PDF を使用した文書解析で、PHP で PDF ドキュメントの総ページ数を取得する方法をご紹介します。
lastmod: "2026-10-05"
---
## Aspose.PDF - ページ数の取得

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントのページ数を取得するには、シンプルに **GetNumberOfPages** クラスを呼び出すだけです。

PHP コード

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロードВ **ページ数の取得 (Aspose.PDF)**В からВ 下記のいずれかのソーシャルコーディングサイトから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)

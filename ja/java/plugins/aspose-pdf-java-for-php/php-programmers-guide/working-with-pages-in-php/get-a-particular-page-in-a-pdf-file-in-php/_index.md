---
title: "PHP での PDF ファイルからの特定ページの取得"
linktitle: "PHP での PDF ファイルからの特定ページの取得"
type: docs
weight: 30
url: /ja/java/get-a-particular-page-in-a-pdf-file-in-php/
description: "Aspose.PDF を使用して PHP で PDF ファイルから特定のページを取得し、対象ページを処理する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - ページ取得

**Aspose.PDF Java for Ruby** を使用して PDF ドキュメントの特定のページを取得するには、**GetPage** クラスを呼び出してください。

Ruby コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## 実行コードのダウンロード

**Get Page (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)

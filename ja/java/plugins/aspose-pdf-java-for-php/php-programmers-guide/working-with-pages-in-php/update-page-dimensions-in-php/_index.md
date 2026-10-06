---
title: "PHP での ページ寸法の更新"
linktitle: "PHP での ページ寸法の更新"
type: docs
weight: 90
url: /ja/java/update-page-dimensions-in-php/
description: Aspose.PDF を使用して、PHP で PDF ドキュメント内のページ寸法を変更する方法を学び、レイアウト制御を向上させましょう。
lastmod: "2026-10-06"
---
## Aspose.PDF - ページ寸法の更新

**Aspose.PDF Java for PHP** を使用してページ寸法を更新するには、単に **UpdatePageDimensions** クラスを呼び出してください。

PHP コード

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get page collection
$page_collection = $pdf->getPages();

# get particular page
$pdf_page = $page_collection->get_Item(1);

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Dimensions updated successfully!" . PHP_EOL;

```

**実行コードをダウンロード**

ダウンロード **Update Page Dimensions (Aspose.PDF)** から、以下に記載されたソーシャルコーディングサイトのいずれかから取得してください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)

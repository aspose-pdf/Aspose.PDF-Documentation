---
title: 在 PHP 中更新页面尺寸
linktitle: 在 PHP 中更新页面尺寸
type: docs
weight: 90
url: /zh/java/update-page-dimensions-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 修改 PDF 文档的页面尺寸，以实现更好的布局控制。
lastmod: "2026-10-06"
---
## Aspose.PDF - 更新页面尺寸

要使用 **Aspose.PDF Java for PHP** 更新页面尺寸，只需调用 **UpdatePageDimensions** 类。

PHP 代码

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

**下载运行代码**

下载В **更新页面尺寸 (Aspose.PDF)**В 来自В 以下提及的任何社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)

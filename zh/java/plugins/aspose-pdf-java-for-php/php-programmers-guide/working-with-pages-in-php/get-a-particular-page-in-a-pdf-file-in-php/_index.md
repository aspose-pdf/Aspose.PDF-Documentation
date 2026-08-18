---
title: 在 PHP 中获取 PDF 文件中的特定页面
linktitle: 在 PHP 中获取 PDF 文件中的特定页面
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 从 PHP 中的 PDF 文件中检索特定页面以进行目标页面处理。
lastmod: "2026-06-09"
---
## Aspose.PDF - 获取页面

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档中的特定页面，只需调用 **GetPage** 类即可。

红宝石代码

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

## 下载运行代码

从以下任何一个社交编码网站下载 **获取页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)

---
title: 在 PHP 中删除 PDF 文件的特定页面
linktitle: 在 PHP 中删除 PDF 文件的特定页面
type: docs
weight: 20
url: /zh/java/delete-a-particular-page-from-the-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中删除 PDF 文档的特定页面，从而简化文档编辑。
lastmod: "2026-10-06"
---
## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for PHP** 删除 PDF 文档的特定页面，只需调用 **DeletePage** 类。

PHP 代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**下载运行中**

下载 **删除页面 (Aspose.PDF)**В 来自В 以下任意提及的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)

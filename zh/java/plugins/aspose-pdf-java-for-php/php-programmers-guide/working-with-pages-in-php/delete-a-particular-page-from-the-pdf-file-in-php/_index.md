---
title: 在 PHP 中从 PDF 文件中删除特定页面
linktitle: 在 PHP 中从 PDF 文件中删除特定页面
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-php/
description: 探索如何使用 Aspose.PDF 从 PHP 中的 PDF 文档中删除特定页面，从而简化文档编辑。
lastmod: "2026-06-09"
---
## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for PHP** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 类即可。

PHP代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```

**下载运行**

从以下任何社交编码网站下载 **删除页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)

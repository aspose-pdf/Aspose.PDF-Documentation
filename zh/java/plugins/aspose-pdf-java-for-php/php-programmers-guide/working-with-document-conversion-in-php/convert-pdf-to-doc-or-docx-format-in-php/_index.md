---
title: 在 PHP 中将 PDF 转换为 DOC 或 DOCX 格式
linktitle: 在 PHP 中将 PDF 转换为 DOC 或 DOCX 格式
type: docs
weight: 10
url: /java/convert-pdf-to-doc-or-docx-format-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 将 PDF 文档转换为 DOC 或 DOCX 格式，以便更轻松地进行文档编辑。
lastmod: "2026-06-09"
---
## Aspose.PDF - 将 PDF 转换为 DOC 或 DOCX

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档转换为 DOC 或 DOCX 格式，只需调用 **PdfToDoc** 模块即可。

PHP代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```

**下载运行代码**

从以下任何社交编码网站下载**将 PDF 转换为 DOC 或 DOCX (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)

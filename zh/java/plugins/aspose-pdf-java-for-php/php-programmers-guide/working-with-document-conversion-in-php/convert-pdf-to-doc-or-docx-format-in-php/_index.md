---
title: 在 PHP 中将 PDF 转换为 DOC 或 DOCX 格式
linktitle: 在 PHP 中将 PDF 转换为 DOC 或 DOCX 格式
type: docs
weight: 10
url: /zh/java/convert-pdf-to-doc-or-docx-format-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 将 PDF 文档转换为 DOC 或 DOCX 格式，以便更轻松地编辑文档。
lastmod: "2026-10-06"
---
## Aspose.PDF - 将 PDF 转换为 DOC 或 DOCX

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档转换为 DOC 或 DOCX 格式，只需调用 **PdfToDoc** 模块。

PHP 代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```

**下载运行代码**

下载\u0412\u00A0**Convert PDF to DOC or DOCX (Aspose.PDF)**\u0412\u00A0 来自\u0412\u00A0 以下提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)

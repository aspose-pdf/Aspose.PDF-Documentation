---
title: 将PDF转换为DOC或DOCX格式的PHP代码
type: docs
weight: 10
url: /java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将PDF转换为DOC或DOCX

要使用 **Aspose.PDF Java for PHP** 将PDF文档转换为DOC或DOCX格式，只需调用 **PdfToDoc** 模块。

PHP代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 保存合并后的输出文件（目标文档）
$pdf->save($dataDir . "output.doc");

print "文档已成功转换";

```

**下载运行代码**

从以下任一社交编码网站下载 **Convert PDF to DOC or DOCX (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)
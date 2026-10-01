---
title: تحويل PDF إلى تنسيق DOC أو DOCX في PHP
linktitle: تحويل PDF إلى تنسيق DOC أو DOCX في PHP
type: docs
weight: 10
url: /ar/java/convert-pdf-to-doc-or-docx-format-in-php/
description: تعلم كيفية تحويل مستندات PDF إلى صيغ DOC أو DOCX في PHP باستخدام Aspose.PDF لتسهيل تحرير المستندات.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل PDF إلى DOC أو DOCX

لتحويل مستند PDF إلى تنسيق DOC أو DOCX باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **PdfToDoc**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.doc");

print "Document has been converted successfully";

```

**تحميل الكود الجاري**

تنزيلВ **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)

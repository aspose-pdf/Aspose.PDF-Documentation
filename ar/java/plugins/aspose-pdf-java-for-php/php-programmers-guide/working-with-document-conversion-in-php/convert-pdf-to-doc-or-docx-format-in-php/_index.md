---
title: تحويل PDF إلى تنسيق DOC أو DOCX في PHP
type: docs
weight: 10
url: ar/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى DOC أو DOCX

لتحويل مستند PDF إلى تنسيق DOC أو DOCX باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **PdfToDoc**.

كود PHP

```php

# افتح المستند الهدف
$pdf = new Document($dataDir . 'input1.pdf');

# احفظ الملف الناتج المتسلسل (المستند الهدف)
$pdf->save($dataDir . "output.doc");

print "تم تحويل المستند بنجاح";

```

**تنزيل الكود القابل للتشغيل**

قم بتنزيل **تحويل PDF إلى DOC أو DOCX (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)
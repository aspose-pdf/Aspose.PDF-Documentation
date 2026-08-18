---
title: تسلسل ملفات PDF في PHP
linktitle: تسلسل ملفات PDF في PHP
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-php/
description: تعرف على كيفية ربط ملفات PDF متعددة في مستند واحد في PHP باستخدام Aspose.PDF لتسهيل إدارة المستندات.
lastmod: "2026-06-09"
---
## Aspose.PDF - تسلسل ملفات PDF

لتسلسل ملفات PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء فئة **ConcatenatePdfFiles**.

كود PHP

```php

# Open the target document
$pdf1 = new Document($dataDir . 'input1.pdf');

# Open the source document
$pdf2 = new Document($dataDir . 'input2.pdf');

# Add the pages of the source document to the target document
$pdf1->getPages()->add($pdf2->getPages());

# Save the concatenated output file (the target document)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "New document has been saved, please check the output file" . PHP_EOL;

```

** تنزيل كود التشغيل **

تنزيل В ** تسلسل ملفات PDF (Aspose.PDF)** В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)

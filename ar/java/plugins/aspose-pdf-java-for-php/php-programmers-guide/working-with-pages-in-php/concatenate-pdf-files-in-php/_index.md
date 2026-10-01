---
title: دمج ملفات PDF في PHP
linktitle: دمج ملفات PDF في PHP
type: docs
weight: 10
url: /ar/java/concatenate-pdf-files-in-php/
description: تعلم كيفية دمج ملفات PDF متعددة في مستند واحد باستخدام PHP و Aspose.PDF لتسهيل إدارة المستندات.
lastmod: "2026-10-01"
---
## Aspose.PDF - دمج ملفات PDF

لدمج ملفات PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **ConcatenatePdfFiles**.

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

**تحميل الكود الجاري**

تحميلВ **Concatenate PDF Files (Aspose.PDF)**В منВ أي من المواقع الاجتماعية للبرمجة المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)

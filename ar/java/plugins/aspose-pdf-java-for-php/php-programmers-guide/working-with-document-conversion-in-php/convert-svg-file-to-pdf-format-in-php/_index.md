---
title: تحويل ملف SVG إلى تنسيق PDF في PHP
linktitle: تحويل ملف SVG إلى تنسيق PDF في PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
description: اكتشف كيفية تحويل ملفات SVG إلى تنسيق PDF في PHP باستخدام Aspose.PDF لإدارة المستندات بشكل فعال.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل SVG إلى PDF

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **SvgToPdf**.

كود PHP

```php
# Instantiate LoadOption object using SVG load option
$options = new SvgLoadOptions();

# Create document object
$pdf = new Document($dataDir . 'Example.svg', $options);

# Save the output to XLS format
$pdf->save($dataDir . "SVG.pdf");

print "Document has been converted successfully";

```

** تنزيل كود التشغيل **

تنزيل В **تحويل SVG إلى PDF (Aspose.PDF)** В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)

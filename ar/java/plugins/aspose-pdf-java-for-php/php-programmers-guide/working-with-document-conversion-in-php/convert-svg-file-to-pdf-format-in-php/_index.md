---
title: تحويل ملف SVG إلى تنسيق PDF في PHP
linktitle: تحويل ملف SVG إلى تنسيق PDF في PHP
type: docs
weight: 40
url: /ar/java/convert-svg-file-to-pdf-format-in-php/
description: استكشف كيفية تحويل ملفات SVG إلى تنسيق PDF في PHP باستخدام Aspose.PDF لإدارة المستندات الفعّالة.
lastmod: "2026-10-05"
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

**تنزيل الشفرة القابلة للتشغيل**

تحميل **تحويل SVG إلى PDF (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)

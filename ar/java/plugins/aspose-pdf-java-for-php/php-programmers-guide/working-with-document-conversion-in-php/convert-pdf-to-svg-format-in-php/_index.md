---
title: تحويل PDF إلى تنسيق SVG في PHP
linktitle: تحويل PDF إلى تنسيق SVG في PHP
type: docs
weight: 30
url: /ar/java/convert-pdf-to-svg-format-in-php/
description: اكتشف كيفية تحويل مستندات PDF إلى تنسيق SVG في PHP باستخدام Aspose.PDF لتحويل رسومات المتجهات عالية الجودة.
lastmod: "2026-10-01"
---
## Aspose.PDF - تحويل PDF إلى SVG

لتحويل PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

كود PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# instantiate an object of SvgSaveOptions
$save_options = new SvgSaveOptions();

# do not compress SVG image to Zip archive
$save_options->CompressOutputToZipArchive = false;

# Save the output to XLS format
$pdf->save($dataDir . "Output.svg", $save_options);

print "Document has been converted successfully" . PHP_EOL;

```

**تحميل الكود القائم**

تحميلВ **تحويل PDF إلى تنسيق SVG (Aspose.PDF)**В منВ أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)

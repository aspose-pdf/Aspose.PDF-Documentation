---
title: تحويل PDF إلى تنسيق SVG في PHP
linktitle: تحويل PDF إلى تنسيق SVG في PHP
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-php/
description: اكتشف كيفية تحويل مستندات PDF إلى تنسيق SVG في PHP باستخدام Aspose.PDF لتحويل الرسومات المتجهة عالية الجودة.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحويل PDF إلى SVG

لتحويل تنسيق PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **PdfToSvg**.

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

** تنزيل كود التشغيل **

تنزيل В ** تحويل PDF إلى تنسيق SVG (Aspose.PDF)** В fromВ أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)

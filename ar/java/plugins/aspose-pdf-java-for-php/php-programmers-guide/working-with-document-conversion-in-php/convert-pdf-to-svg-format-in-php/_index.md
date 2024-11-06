---
title: تحويل PDF إلى SVG في PHP
type: docs
weight: 30
url: ar/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل PDF إلى SVG

لتحويل PDF إلى تنسيق SVG باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء وحدة **PdfToSvg**.

كود PHP

```php

# افتح المستند الهدف
$pdf = new Document($dataDir . 'input1.pdf');

# إنشاء كائن من SvgSaveOptions
$save_options = new SvgSaveOptions();

# لا تقم بضغط صورة SVG إلى أرشيف Zip
$save_options->CompressOutputToZipArchive = false;

# احفظ المخرج بتنسيق XLS
$pdf->save($dataDir . "Output.svg", $save_options);

print "تم تحويل المستند بنجاح" . PHP_EOL;

```

**تحميل الكود التشغيلي**

قم بتحميل **تحويل PDF إلى SVG (Aspose.PDF)** من أي من مواقع ترميز الشبكات الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)
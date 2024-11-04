---
title: تحويل ملف SVG إلى تنسيق PDF في PHP
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحويل SVG إلى PDF

لتحويل ملف SVG إلى تنسيق PDF باستخدام **Aspose.PDF Java for PHP**، قم باستدعاء وحدة **SvgToPdf**.

كود PHP

```php
# إنشاء كائن LoadOption باستخدام خيار تحميل SVG
$options = new SvgLoadOptions();

# إنشاء كائن الوثيقة
$pdf = new Document($dataDir . 'Example.svg', $options);

# حفظ الناتج بتنسيق XLS
$pdf->save($dataDir . "SVG.pdf");

print "تم تحويل الوثيقة بنجاح";

```

**تحميل كود التشغيل**

قم بتحميل **تحويل SVG إلى PDF (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)
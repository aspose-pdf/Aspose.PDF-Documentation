---
title: تحسين مستند PDF للويب في PHP
linktitle: تحسين مستند PDF للويب في PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: تعرف على كيفية تحسين مستند PDF للحصول على أداء أسرع للويب وتقليل حجم الملف في PHP باستخدام Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء طريقة **optimize_web** للفئة **Optimize**.

كود PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

** تنزيل كود التشغيل **

قم بتنزيل ** ** تحسين ملف PDF للويب (Aspose.PDF) ** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)

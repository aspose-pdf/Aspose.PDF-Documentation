---
title: تحسين مستند PDF للويب في PHP
linktitle: تحسين مستند PDF للويب في PHP
type: docs
weight: 60
url: /ar/java/optimize-pdf-document-for-the-web-in-php/
description: تعرف على كيفية تحسين مستند PDF للحصول على أداء ويب أسرع وتقليل حجم الملف باستخدام PHP وAspose.PDF.
lastmod: "2026-10-05"
---
## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الطريقة **optimize_web** من فئة **Optimize**.

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

**تنزيل الشفرة القابلة للتشغيل**

تنزيل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)

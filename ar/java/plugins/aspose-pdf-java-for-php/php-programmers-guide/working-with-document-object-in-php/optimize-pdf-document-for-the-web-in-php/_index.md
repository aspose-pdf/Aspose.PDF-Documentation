---
title: تحسين مستند PDF للويب في PHP
type: docs
weight: 60
url: ar/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تحسين PDF للويب

لتحسين مستند PDF للويب باستخدام **Aspose.PDF Java for PHP**، ببساطة قم باستدعاء طريقة **optimize_web** من فئة **Optimize**.

كود PHP

```php

 public static function optimize_web($dataDir=null)

{

    # افتح مستند PDF.

    $doc = new Document($dataDir . "input1.pdf");

    # تحسين للويب

    $doc->optimize();

    # احفظ المستند الناتج

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "تم تحسين PDF للويب، يرجى التحقق من ملف الإخراج." . PHP_EOL;

}    
```

**تحميل الكود الجاري**

قم بتحميل **تحسين PDF للويب (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
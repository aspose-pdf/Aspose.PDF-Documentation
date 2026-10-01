---
title: تعيين انتهاء صلاحية PDF في PHP
linktitle: تعيين انتهاء صلاحية PDF في PHP
type: docs
weight: 80
url: /ar/java/set-pdf-expiration-in-php/
description: اكتشف كيفية تعيين تاريخ انتهاء صلاحية لملف PDF في PHP، مع التحكم في الوصول باستخدام Aspose.PDF.
lastmod: "2026-10-01"
---
## Aspose.PDF - تعيين انتهاء صلاحية PDF

لتعيين انتهاء صلاحية مستند В PDF باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء الفئة **SetExpiration**.

كود PHP

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

$javascript = new JavascriptAction(
        "var year=2014;
    var month=4;
    today = new Date();
    today = new Date(today.getFullYear(), today.getMonth());
    expiry = new Date(year, month);
    if (today.getTime() > expiry.getTime())
    app.alert('The file is expired. You need a new one.');");
$doc->setOpenAction($javascript);

# save update document with new information
$doc->save($dataDir . "set_expiration.pdf");

print "Update document information, please check output file." . PHP_EOL;

```

**تحميل الشيفرة التشغيلية**

تحميل **Set PDF Expiration (Aspose.PDF)** من أي من مواقع الترميز الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)

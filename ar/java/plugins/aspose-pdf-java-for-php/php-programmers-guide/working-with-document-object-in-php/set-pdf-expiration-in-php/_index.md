---
title: ضبط انتهاء صلاحية PDF في PHP
linktitle: ضبط انتهاء صلاحية PDF في PHP
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
description: اكتشف كيفية تعيين تاريخ انتهاء الصلاحية لملف PDF في PHP، والتحكم في الوصول باستخدام Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - ضبط انتهاء صلاحية PDF

لتعيين انتهاء صلاحية مستند Pdf باستخدام **Aspose.PDF Java لـ PHP**، ما عليك سوى استدعاء فئة **SetExpiration**.

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

** تنزيل كود التشغيل **

تنزيلВ **تعيين انتهاء صلاحية ملف PDF (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)

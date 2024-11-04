---
title: تعيين انتهاء صلاحية PDF في PHP
type: docs
weight: 80
url: /java/set-pdf-expiration-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - تعيين انتهاء صلاحية PDF

لتعيين انتهاء صلاحية مستند PDF باستخدام **Aspose.PDF Java for PHP**، ببساطة استدعِ فئة **SetExpiration**.

كود PHP

```php

# افتح مستند PDF.
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

# حفظ المستند المحدث بالمعلومات الجديدة
$doc->save($dataDir . "set_expiration.pdf");

print "تحديث معلومات المستند، يرجى التحقق من ملف الإخراج." . PHP_EOL;

```

**تحميل كود التشغيل**

قم بتحميل **Set PDF Expiration (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/SetExpiration.php)
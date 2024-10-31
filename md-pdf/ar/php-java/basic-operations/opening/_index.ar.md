---
title: فتح مستند PDF
linktitle: فتح
type: docs
weight: 20
url: /php-java/open-pdf-document/
description: تعلم كيفية فتح ملف PDF باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## فتح مستند PDF موجود

ملفات PDF أو ملفات تنسيق المستندات المحمولة أصبحت المعيار العالمي لتبادل المستندات. تُستخدم على نطاق واسع لحفظ تنسيق المستند. ومع ذلك، قد يكون العمل مع ملفات PDF باستخدام لغات البرمجة مثل PHP عبر Java أمرًا صعبًا بعض الشيء. يقدم هذا المقال مكتبة Aspose.PDF لـ PHP عبر Java التي تتيح لك فتح ملفات PDF بسرعة وسهولة.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "تم فتح المستند بنجاح. حجم الملف: " . filesize($inputFile);
```
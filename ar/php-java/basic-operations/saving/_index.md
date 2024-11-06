---
title: حفظ مستند PDF
linktitle: حفظ
type: docs
weight: 30
url: ar/php-java/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF باستخدام Aspose.PDF لمكتبة PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حفظ مستند PDF إلى نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو التلاعب به إلى نظام الملفات باستخدام طريقة الحفظ لفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```
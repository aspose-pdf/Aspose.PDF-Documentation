---
title: تحويل PDF/A إلى تنسيق PDF
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: /php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل ملف PDF/A إلى مستند PDF باستخدام مكتبة PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل مستند PDF/A إلى PDF

تحويل مستند PDF/A إلى PDF يعني إزالة قيود <abbr title="Portable Document Format Archive">PDF/A</abbr> من المستند الأصلي. تحتوي فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) على طريقة removePdfaCompliance(..) لإزالة معلومات الامتثال لـ PDF من الملف المدخل/المصدر.

```php
// قم بإنشاء مثيل جديد لفئة Document مع الملف المدخل
$document = new Document($inputFile);

// إزالة الامتثال PDF/A من المستند
$document->removePdfaCompliance();

// حفظ المستند المعدل إلى الملف المخرَج
$document->save($outputFile);
```

تُزال هذه المعلومات أيضًا إذا قمت بإجراء أي تغييرات في المستند (مثل
 أضف الصفحات). في المثال التالي، يفقد المستند الناتج الامتثال لـ PDF/A بعد إضافة الصفحة.

```php
// إنشاء مثيل جديد من فئة Document مع الملف المدخل
$document = new Document($inputFile);

// إزالة الامتثال لـ PDF/A من المستند
$document->getPages()->add();

// حفظ المستند المعدل في الملف الناتج
$document->save($outputFile);
```
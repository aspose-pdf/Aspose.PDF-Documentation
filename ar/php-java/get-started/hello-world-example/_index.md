---
title: مثال مرحبا بالعالم باستخدام PHP عبر Java
linktitle: مثال مرحبا بالعالم
type: docs
weight: 40
url: ar/php-java/hello-world-example/
description: توضح هذه الصفحة كيفية استخدام برمجة بسيطة لإنشاء مستند PDF يحتوي على نص - مرحبا بالعالم باستخدام Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مثال مرحبا بالعالم

يُستخدم مثال "مرحبا بالعالم" عادةً لإظهار الميزات الأساسية للغة البرمجة أو البرنامج مع حالة استخدام بسيطة.

تمكن واجهة برمجة التطبيقات Aspose.PDF لـ PHP عبر Java المطورين من إنشاء وقراءة وتحرير ومعالجة ملفات PDF داخل تطبيقات Java الخاصة بهم. يدعم قراءة وتحويل أنواع ملفات مختلفة إلى ومن صيغة PDF. توضح هذه المقالة عن مرحبا بالعالم كيفية إنشاء ملف PDF باستخدام واجهة برمجة التطبيقات Aspose.PDF لـ PHP عبر Java. بعد [تثبيت Aspose.PDF لـ PHP عبر Java](/pdf/php-java/installation/) في بيئتك، يمكنك تنفيذ نموذج الكود أدناه لمعرفة كيفية عمل واجهة برمجة التطبيقات Aspose.PDF.

يتبع جزء الكود أدناه هذه الخطوات:


1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) إلى كائن الوثيقة
1. إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. إضافة TextFragment إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) للصفحة
1. حفظ مستند PDF الناتج

مقطع الشيفرة التالي هو برنامج Hello World لعرض عمل Aspose.PDF لـ PHP عبر Java API.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```
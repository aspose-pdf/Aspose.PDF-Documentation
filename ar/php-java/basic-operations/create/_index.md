---
title: إنشاء مستند PDF
linktitle: إنشاء
type: docs
weight: 10
url: /ar/php-java/create-document/
description: تعرف على كيفية إنشاء ملف PDF في Aspose.PDF لـ PHP عبر Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF لـ PHP عبر Java** API يتيح لمطوري التطبيقات تضمين وظيفة معالجة مستندات PDF في تطبيقاتهم. يمكن استخدامه لإنشاء وقراءة ملفات PDF دون الحاجة إلى أي برنامج آخر مثبت على الجهاز الأساسي. يمكن استخدام Aspose.PDF لـ PHP عبر Java في مجموعة متنوعة من أنواع التطبيقات مثل تطبيقات سطح المكتب، JSP، وتطبيقات JSF.

## كيفية إنشاء ملف PDF باستخدام PHP عبر Java

لإنشاء ملف PDF باستخدام PHP عبر Java، يمكن استخدام الخطوات التالية.

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) إلى كائن المستند

1. إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. إضافة [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) في الصفحة
1. حفظ مستند PDF الناتج

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```
---
title: تحويل HTML إلى PDF
linktitle: تحويل HTML إلى PDF
type: docs
weight: 40
url: /ar/php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: يوضح هذا الموضوع كيف يتيح لك Aspose.PDF تحويل صيغ HTML وMHTML إلى ملف PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة

تشرح هذه المقالة كيفية تحويل HTML إلى PDF باستخدام PHP. الكود بسيط جدًا، فقط قم بتحميل HTML إلى فئة Document واحفظه كملف PDF ناتج. تحويل MHTML إلى PDF في Java مشابه أيضًا. يغطي المواضيع التالية

## مكتبة Java لتحويل HTML إلى PDF

**Aspose.PDF for PHP عبر Java** هو API لمعالجة PDF يتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسلاسة. يمكن تخصيص عملية تحويل HTML إلى PDF بشكل مرن.

## تحويل HTML إلى PDF

يوضح المثال البرمجي التالي بلغة Java كيفية تحويل مستند HTML إلى PDF.

1. قم بإنشاء مثيل لفئة [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).

1. قم بتهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ مستند PDF الناتج عن طريق استدعاء طريقة [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-).

```php
    // قم بإنشاء مثيل لـ HtmlLoadOptions لتحديد خيارات التحميل لملف HTML
    $loadOption = new HtmlLoadOptions();

    // قم بإنشاء كائن Document جديد وقم بتحميل ملف HTML
    $document = new Document($inputFile, $loadOption);

    // احفظ المستند كملف PDF
    $document->save($outputFile);
```

## التحويل المتقدم من HTML إلى PDF

محرك التحويل من HTML يحتوي على العديد من الخيارات التي تتيح لنا التحكم في عملية التحويل.

### دعم استعلامات الوسائط

1. قم بإنشاء [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) لـ HTML.
1. [اضبط وضع الطباعة أو الشاشة](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-).

1. تهيئة [كائن المستند](https://reference.aspose.com/page/java/com.aspose.page/document).
1. احفظ مستند PDF الناتج.

الاستعلامات الإعلامية هي تقنية شائعة لتقديم ورقة أنماط مخصصة لأجهزة مختلفة. يمكننا تعيين نوع الجهاز باستخدام فئة [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```php

    // إنشاء مثيل لـ HtmlLoadOptions لتحديد خيارات التحميل لملف HTML
    $htmlMediaType = new HtmlMediaType();

    // تعيين وضع الطباعة أو الشاشة
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // إنشاء كائن مستند جديد وتحميل ملف HTML
    $document = new Document($inputFile, $loadOption);

    // حفظ المستند كملف PDF
    $document->save($outputFile);
```

### تفعيل (تعطيل) تضمين الخطوط

1. أضف خيارات تحميل [Html](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) جديدة.
1. تعطيل تضمين الخطوط.
1. احفظ مستندًا جديدًا.

غالبًا ما تستخدم صفحات HTML الخطوط (مثلًا.
 الخطوط من المجلد المحلي، خطوط جوجل، إلخ). يمكننا أيضًا التحكم في تضمين الخطوط في مستند باستخدام خاصية [setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-).

```php

    // إنشاء مثيل من HtmlLoadOptions لتحديد خيارات التحميل لملف HTML
    $loadOption = new HtmlLoadOptions();

    // تعطيل تضمين الخطوط
    $loadOption->setEmbedFonts(true);

    // إنشاء كائن مستند جديد وتحميل ملف HTML
    $document = new Document($inputFile, $loadOption);

    // حفظ المستند كملف PDF
    $document->save($outputFile);
```

## تحويل MHTML إلى PDF

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>، اختصار لـ MIME HTML، هو تنسيق أرشيف صفحة ويب يستخدم لدمج الموارد التي تمثل عادةً بواسطة روابط خارجية (مثل الصور، الرسوم المتحركة الفلاش، تطبيقات جافا الصغيرة، وملفات الصوت) مع كود HTML في ملف واحد. The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

يُظهر مقتطف الشفرة التالي كيفية تحويل ملفات MHTML إلى تنسيق PDF باستخدام Java:

```php

    // إنشاء مثيل جديد لفئة MhtLoadOptions.
    $loadOption = new MhtLoadOptions();

    // إنشاء مثيل جديد لفئة Document وتحميل ملف MHTML.
    $document = new Document($inputFile, $loadOption);

    // حفظ المستند كملف PDF.
    $document->save($outputFile);
```
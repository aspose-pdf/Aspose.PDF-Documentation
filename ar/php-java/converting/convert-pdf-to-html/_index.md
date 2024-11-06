---
title: تحويل ملف PDF إلى تنسيق HTML
linktitle: تحويل ملف PDF إلى تنسيق HTML
type: docs
weight: 50
url: ar/php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى تنسيق HTML باستخدام مكتبة PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

يوفر Aspose.PDF لـ PHP العديد من الميزات لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات مخرجات متنوعة. تناقش هذه المقالة كيفية تحويل ملف PDF إلى تنسيق HTML وحفظ الصور من ملف PDF في مجلد معين.

{{% alert color="success" %}}
**حاول تحويل PDF إلى HTML عبر الإنترنت**

يقدم لك Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى HTML باستخدام التطبيق المجاني](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

عند تحويل ملف PDF كبير يحتوي على عدة صفحات إلى تنسيق HTML، يظهر الناتج كصفحة HTML واحدة. قد ينتهي الأمر بأن تكون طويلة جداً. للتحكم في حجم الصفحة، من الممكن تقسيم الناتج إلى عدة صفحات أثناء تحويل PDF إلى HTML.

## تحويل صفحات PDF إلى HTML

يوفر Aspose.PDF for PHP العديد من الميزات لتحويل تنسيقات الملفات المختلفة إلى مستندات PDF وتحويل ملفات PDF إلى تنسيقات إخراج متنوعة. تناقش هذه المقالة كيفية تحويل ملف PDF إلى تنسيق HTML وحفظ الصور من ملف PDF في مجلد معين.

يظهر مقتطف الكود التالي جميع الخيارات الممكنة التي يمكنك استخدامها عند تحويل PDF إلى HTML.

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOption = new HtmlSaveOptions();

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOption);
```

## تحويل PDF إلى HTML - تقسيم الناتج إلى HTML متعدد الصفحات

Aspose.PDF لـ PHP يدعم ميزة تحويل مستندات PDF إلى تنسيقات إخراج مختلفة بما في ذلك HTML. ولكن عند تحويل ملفات PDF الكبيرة (المكونة من عدة صفحات)، قد يكون لديك متطلب لحفظ صفحة PDF فردية في ملف HTML منفصل.

عند تحويل ملف PDF كبير يحتوي على عدة صفحات إلى تنسيق HTML، يظهر الناتج كصفحة HTML واحدة. قد ينتهي الأمر بأن تكون طويلة جدًا. للتحكم في حجم الصفحة، من الممكن تقسيم الناتج إلى عدة صفحات أثناء التحويل من PDF إلى HTML. يرجى محاولة استخدام مقتطف الشيفرة التالي.

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOption = new HtmlSaveOptions();

// تحديد تقسيم الناتج إلى عدة صفحات
$saveOption->setSplitIntoPages(true);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOption);
```

## تحويل PDF إلى HTML - تجنب حفظ الصور بتنسيق SVG


تنسيق الإخراج الافتراضي لحفظ الصور عند التحويل من PDF إلى HTML هو SVG. أثناء التحويل، يتم تحويل بعض الصور من PDF إلى صور متجهة SVG. قد يكون ذلك بطيئًا. بدلاً من ذلك، يمكن تحويل الصور إلى PNG. للسماح بذلك، لدى Aspose.PDF الخيار لاستخدام SVG للمتجهات أو لإنشاء PNGs.

لإزالة عرض الصور تمامًا كتنسيق SVG عند تحويل ملفات PDF إلى تنسيق HTML، يرجى محاولة استخدام مقتطف الكود التالي.

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOption = new HtmlSaveOptions();

// تحديد المجلد حيث يتم حفظ صور SVG أثناء تحويل PDF إلى HTML
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOption);
```

## ضغط صور SVG أثناء التحويل

لضغط صور SVG أثناء تحويل PDF إلى HTML، يرجى محاولة استخدام الكود التالي:

```php
// إنشاء كائن مستند جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOptions);
```

## تحويل PDF إلى HTML - تحديد مجلد الصور

بشكل افتراضي، عند تحويل ملف PDF إلى HTML، يتم حفظ الصور في ملف PDF في مجلد منفصل يتم إنشاؤه في نفس الدليل الذي يتم إنشاء ملف HTML الناتج فيه. ولكن في بعض الأحيان، يكون من الضروري تحديد مجلد مختلف لحفظ الصور عند إنشاء ملفات HTML. لتحقيق ذلك، قدمنا [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).

يستخدم [setSpecialFolderForAllImages method](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) لتحديد المجلد الهدف لتخزين الصور.


```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOptions);
```

## تصيير النص الشفاف

في حالة احتواء ملف PDF المصدر/المدخل على نصوص شفافة مظللة بصور في المقدمة، فقد تكون هناك مشكلات في تصيير النصوص. لذلك من أجل معالجة مثل هذه السيناريوهات، يمكن استخدام خاصيتي SaveShadowedTextsAsTransparentTexts وSaveTransparentTexts.

```php
// إنشاء كائن Document جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOptions);
```


## عرض طبقات مستند PDF

يمكننا عرض طبقات مستند PDF في عنصر نوع طبقة منفصل أثناء تحويل PDF إلى HTML:

```php
// إنشاء كائن مستند جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن HtmlSaveOptions جديد لحفظ المستند كـ HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// حفظ المستند كـ HTML باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOptions);
```

يُعد تحويل PDF إلى HTML إحدى أكثر ميزات Aspose.PDF شهرة لأنه يجعل من الممكن عرض محتوى ملفات PDF على منصات مختلفة دون استخدام عارض مستندات PDF. يتوافق HTML الناتج مع معايير WWW ويمكن عرضه بسهولة في جميع متصفحات الويب. باستخدام هذه الميزة، يمكن عرض ملفات PDF على الأجهزة المحمولة لأنك لا تحتاج إلى تثبيت أي تطبيق لعرض PDF ولكن يمكن استخدام متصفح ويب بسيط.
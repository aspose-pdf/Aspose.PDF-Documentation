---
title: تحويل PDF إلى Microsoft Word
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: تحويل ملف PDF إلى تنسيق DOC وDOCX بسهولة وتحكم كامل باستخدام Aspose.PDF لـ PHP. تعرف على كيفية تحسين تحويل مستندات PDF إلى Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

توضح هذه المقالة كيفية تحويل PDF إلى Word باستخدام PHP. الكود بسيط جدًا، فقط قم بتحميل PDF إلى فئة Document واحفظه كإخراج بتنسيق Microsoft Word DOC أو DOCX. يغطي الموضوعات التالية

- [تحويل PDF إلى DOC باستخدام PHP](#convert-pdf-to-doc)
- [تحويل PDF إلى DOCX باستخدام PHP](#convert-pdf-to-docx)
- [تحويل PDF إلى Word باستخدام PHP](#convert-pdf-to-docx)
- [تحويل PDF إلى DOC باستخدام PHP](#convert-pdf-to-doc)
- [تحويل PDF إلى DOCX باستخدام PHP](#convert-pdf-to-docx)
- [كيفية تحويل ملف PDF إلى Word DOC باستخدام PHP](#convert-pdf-to-doc) أو [Word DOCX](#convert-pdf-to-docx)

- [مكتبة أو API أو كود لتحويل، حفظ، إنشاء مستندات Word من PDF باستخدام PHP](#convert-pdf-to-docx)

## تحويل PDF إلى DOC

إحدى الميزات الأكثر شعبية هي تحويل PDF إلى Microsoft Word DOC، مما يجعل المحتوى سهل التلاعب. يتيح لك Aspose.PDF for PHP تحويل ملفات PDF إلى DOC.

**Aspose.PDF for PHP** يمكنه إنشاء مستندات PDF من الصفر ويعد أداة رائعة لتحديث وتحرير والتلاعب في مستندات PDF الموجودة. ميزة هامة هي القدرة على تحويل الصفحات والمستندات الكاملة بصيغة PDF إلى صور. ميزة أخرى شائعة هي تحويل PDF إلى Microsoft Word DOC، مما يجعل المحتوى سهل التلاعب. (معظم المستخدمين لا يمكنهم تحرير مستندات PDF ولكن يمكنهم بسهولة العمل مع الجداول والنصوص والصور في Microsoft Word.)

لتبسيط الأمور وجعلها مفهومة، يوفر Aspose.PDF for PHP كودًا بخطين لتحويل ملف PDF المصدر إلى ملف DOC.

يوضح مقطع الكود التالي في Java عملية تحويل ملف PDF إلى تنسيق DOC.

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/page/java/com.aspose.page/document) مع مستند PDF المصدر.

2. احفظه بتنسيق **SaveFormat.Doc** عن طريق استدعاء طريقة **Document.save()**.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن DocSaveOptions جديد
$saveOption = new DocSaveOptions();

// ضبط تنسيق الإخراج إلى DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// احفظ المستند كملف DOC
$document->save($outputFile, $saveOption);
```

## استخدام فئة DocSaveOptions

توفر [فئة DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى تنسيق DOC. من بين هذه الخصائص، يتيح لك Mode تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. كل من هذه القيم له فوائد وقيود محددة:

- وضع [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) سريع وجيد للحفاظ على المظهر الأصلي لملف PDF، لكن قابلية تحرير المستند الناتج قد تكون محدودة.
 كل كتلة نصية مجمعة بصريًا في ملف PDF الأصلي يتم تحويلها إلى مربع نص في مستند الإخراج. يحقق هذا أقصى تشابه مع الأصل بحيث يبدو مستند الإخراج جيدًا، لكنه يتكون بالكامل من مربعات نصية وقد يجعل التحرير في Microsoft Word صعبًا.

- الوضع الكامل هو وضع التعرف الكامل، حيث تقوم المحرك بتجميع وتحليل متعدد المستويات لاستعادة المستند الأصلي وفقًا لنية المؤلف مع إنتاج مستند سهل التحرير. القيد هو أن مستند الإخراج قد يبدو مختلفًا عن الأصل.

- يمكن استخدام خاصية RelativeHorizontalProximity للتحكم في القرب النسبي بين العناصر النصية مما يعني أن المسافة معيرة بحجم الخط. قد يكون للخطوط الأكبر مسافات أكبر بين المقاطع الصوتية ولا تزال تعتبر ككل واحد. يتم تحديدها كنسبة مئوية من حجم الخط، على سبيل المثال، 1 = 100٪. هذا يعني أن حرفين بحجم 12pt يتم وضعهما على بعد 12pt هما قريبان.

- يتم استخدام RecognitionBullets لتشغيل التعرف على النقاط أثناء التحويل.
```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن جديد لـ DocSaveOptions
$saveOption = new DocSaveOptions();

// تعيين وضع التعرف إلى EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// تعيين تنسيق الإخراج إلى DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// تعيين وضع التعرف كـ Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// تعيين القرب الأفقي كـ 2.5
saveOptions->setRelativeHorizontalProximity(2.5f);

// تمكين القيمة للتعرف على الرموز النقطية أثناء عملية التحويل
saveOptions->setRecognizeBullets(true);

// حفظ المستند كـ DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

تقدم Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظائف وجودة العمل.

[![تحويل PDF إلى DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOCX

يوفر التعداد DocFormat أيضًا خيار اختيار DOCX كتنسيق إخراج لوثائق Word. لتحويل ملف PDF المصدر إلى تنسيق DOCX، استخدم مقطع الشيفرة المحدد أدناه.

## كيفية تحويل PDF إلى DOCX

يوضح مقطع الشيفرة Java التالي عملية تحويل ملف PDF إلى تنسيق DOCX.

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/page/java/com.aspose.page/document) مع وثيقة PDF المصدر.
2. احفظه بتنسيق **SaveFormat.DocX** عن طريق استدعاء الطريقة **Document.save()**.

```php
    // تحميل وثيقة PDF
    $document = new Document($inputFile);
    
    // حفظ الوثيقة كـ DOCX
    $document->save($outputFile, SaveFormat::$DocX);
```

تمتلك فئة [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) خاصية باسم Format توفر القدرة على تحديد تنسيق الوثيقة الناتجة، أي DOC أو DOCX.
 من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير قيمة Docx من التعداد DocSaveOptions.DocFormat.

يرجى إلقاء نظرة على مقطع الشيفرة التالي الذي يوفر القدرة على تحويل ملف PDF إلى تنسيق DOCX باستخدام Java.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن DocSaveOptions جديد
$saveOption = new DocSaveOptions();

// تعيين وضع التعرف إلى EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// تعيين تنسيق الإخراج إلى DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// حفظ المستند كـ DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

تقدم Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.


[![Aspose.PDF Convertion PDF to DOCX Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}

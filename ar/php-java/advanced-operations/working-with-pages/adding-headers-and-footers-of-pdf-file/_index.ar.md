---
title: إضافة رأس وتذييل إلى ملف PDF
linktitle: إضافة رأس وتذييل إلى ملف PDF
type: docs
weight: 70
url: /php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF لـ PHP عبر Java يتيح لك إضافة رأس وتذييل إلى ملف PDF الخاص بك باستخدام فئة TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُستخدم الأختام في ملفات PDF غالبًا في العقود والتقارير والمواد المقيدة، لإثبات أن المستندات قد تمت مراجعتها وتم وضع علامة عليها كـ "مقروءة"، "مؤهلة"، أو "سرية"، إلخ. ستوضح لك هذه المقالة كيفية إضافة أختام الصور والنصوص إلى مستندات PDF باستخدام **Aspose.PDF لـ PHP عبر Java**.

إذا قمت بقراءة الشيفرات البرمجية أعلاه سطرًا بسطر، يجب أن تجد أن الصياغة ومنطق الشيفرة سهل الفهم للغاية.

## إضافة نص في رأس ملف PDF

يمكنك استخدام فئة [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) لإضافة نص في رأس ملف PDF.

 class TextStamp توفر الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط إلخ. لإضافة نص في الرأس، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة النص في رأس ملف PDF.

تحتاج إلى تعيين خاصية TopMargin بطريقة تعدل النص في منطقة الرأس في ملف PDF الخاص بك. كما تحتاج إلى تعيين HorizontalAlignment إلى Center وVerticalAlignment إلى Top.

يظهر لك مقطع الشيفرة التالي كيفية إضافة نص في رأس ملف PDF باستخدام PHP.

```php

    // افتح المستند
    $document = new Document($inputFile);

    // إنشاء رأس
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // تعيين خصائص الختم
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // إضافة التذييل في الصفحة الأولى
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // حفظ مستند الإخراج
    $document->save($outputFile);
    $document->close();
```

## إضافة نص في تذييل ملف PDF

يمكنك استخدام فئة TextStamp لإضافة نص في تذييل ملف PDF. توفر فئة TextStamp الخصائص اللازمة لإنشاء ختم نصي مثل حجم الخط، نمط الخط، ولون الخط وغيرها. من أجل إضافة نص في التذييل، تحتاج إلى إنشاء كائن Document وكائن TextStamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة addStamp من Page لإضافة النص في تذييل الـPDF.

يعرض لك مقتطف الشيفرة التالي كيفية إضافة نص في تذييل ملف PDF باستخدام PHP.

```php

    // افتح المستند
    $document = new Document($inputFile);

    // أنشئ الرأس
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // تعيين خصائص الختم
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // إضافة تذييل في الصفحة الأولى
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // احفظ ملف الإخراج
    $document->save($outputFile);
    $document->close();
```


## إضافة صورة في رأس ملف PDF

يمكنك استخدام فئة [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) لإضافة صورة في رأس ملف PDF. توفر فئة الطابع الصورة الخصائص اللازمة لإنشاء طابع قائم على الصورة مثل حجم الخط، نمط الخط، ولون الخط، إلخ. لإضافة صورة في الرأس، تحتاج إلى إنشاء كائن مستند وكائن طابع صورة باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) الخاصة بالصفحة لإضافة الصورة في رأس ملف PDF.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // إنشاء تذييل
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // ضبط خصائص الطابع
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // إضافة تذييل للصفحة الأولى
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```


يوضح لك مقطع الشيفرة التالي كيفية إضافة صورة في رأس ملف PDF باستخدام PHP.

## إضافة صورة في تذييل ملف PDF

يمكنك استخدام فئة Image Stamp لإضافة صورة في تذييل ملف PDF. توفر فئة Image Stamp الخصائص اللازمة لإنشاء ختم يعتمد على الصورة مثل حجم الخط، ونمط الخط، ولون الخط إلخ. من أجل إضافة صورة في التذييل، تحتاج إلى إنشاء كائن Document وكائن Image Stamp باستخدام الخصائص المطلوبة. بعد ذلك، يمكنك استدعاء طريقة AddStamp للصفحة لإضافة الصورة في تذييل ملف PDF.

{{% alert color="primary" %}}

تحتاج إلى ضبط خاصية BottomMargin بطريقة تضبط الصورة في منطقة التذييل لملف PDF الخاص بك. تحتاج أيضًا إلى ضبط [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) إلى `Center` و [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) إلى `Bottom`.

{{% /alert %}}

يوضح لك مقطع الشيفرة التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام PHP.

```php

    // فتح المستند
    $document = new Document($inputFile);
    
    // إنشاء تذييل
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // تعيين خصائص الختم
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // إضافة تذييل إلى الصفحة الأولى
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```

## إضافة رؤوس مختلفة في ملف PDF واحد

نعلم أنه يمكننا إضافة TextStamp في قسم الرأس/التذييل للمستند باستخدام خصائص TopMargin أو Bottom Margin، ولكن في بعض الأحيان قد نحتاج إلى إضافة رؤوس/تذييلات متعددة في مستند PDF واحد. **Aspose.PDF for PHP عبر Java** يشرح كيفية القيام بذلك.

من أجل تحقيق هذا المتطلب، سنقوم بإنشاء كائنات [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) فردية (يعتمد عدد الكائنات على عدد الرؤوس/التذييلات المطلوبة) وسنضيفها إلى مستند PDF.
 قد نقوم أيضًا بتحديد معلومات تنسيق مختلفة لكائن الطابع الفردي. في المثال التالي، قمنا بإنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وثلاثة كائنات [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) ثم استخدمنا طريقة [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) للصفحة لإضافة النص في قسم الرأس من ملف PDF. يوضح لك المقتطف البرمجي التالي كيفية إضافة صورة في تذييل ملف PDF باستخدام Aspose.PDF لـ PHP عبر Java.

```php

    // فتح المستند
    $document = new Document($inputFile);

    // إنشاء ثلاثة طوابع
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // تعيين محاذاة الطابع (وضع الطابع في أعلى الصفحة، متمركز أفقيًا)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // تحديد نمط الخط كغليظ
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // تعيين معلومات لون النص الأمامي كالأحمر
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // تحديد حجم الخط كـ 14
    $stamp1->getTextState()->setFontSize(14);

    // الآن نحتاج إلى تعيين المحاذاة الرأسية لكائن الطابع الثاني كأعلى
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // تعيين معلومات المحاذاة الأفقية للطابع كالمركز
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // تعيين عامل التكبير لكائن الطابع
    $stamp2->setZoom(10);

    // تعيين تنسيق كائن الطابع الثالث
    // تحديد معلومات المحاذاة الرأسية لكائن الطابع كأعلى
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // تعيين معلومات المحاذاة الأفقية لكائن الطابع كالمركز
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // تعيين زاوية الدوران لكائن الطابع
    $stamp3->setRotateAngle(35);
    // تعيين اللون الوردي كلون خلفية للطابع
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // تغيير معلومات نوع الخط للطابع إلى Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // يتم إضافة الطابع الأول على الصفحة الأولى;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // // يتم إضافة الطابع الثاني على الصفحة الثانية;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // يتم إضافة الطابع الثالث على الصفحة الثالثة.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // حفظ المستند الناتج
    $document->save($outputFile);
    $document->close();
```
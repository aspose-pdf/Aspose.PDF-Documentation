---
title: تحويل تنسيقات الصور المختلفة إلى PDF
linktitle: تحويل الصور إلى PDF
type: docs
weight: 60
url: /php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: يوضح لك هذا الموضوع كيفية استخدام مكتبة Aspose.PDF لـ PHP لتحويل تنسيقات الصور المختلفة إلى PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF لـ PHP** يسمح لك بتحويل تنسيقات مختلفة من الصور إلى ملفات PDF. مكتبتنا توضح مقتطفات كود لتحويل تنسيقات الصور الأكثر شعبية، مثل - BMP وCGM وDMF وJPG وPNG وSVG وتنسيقات TIFF.

## تحويل BMP إلى PDF

قم بتحويل ملفات BMP إلى مستند PDF باستخدام مكتبة **Aspose.PDF لـ PHP**.

صور <abbr title="ملف صورة نقطية">BMP</abbr> هي ملفات تحمل الامتداد .BMP تمثل ملفات الصور النقطية التي تستخدم لتخزين الصور الرقمية النقطية. هذه الصور مستقلة عن محول الرسوميات وتُسمى أيضًا تنسيق الملف النقطي المستقل عن الجهاز (DIB).
يمكنك تحويل BMP إلى PDF باستخدام Aspose.PDF لـ PHP API.
 لذلك، يمكنك اتباع الخطوات التالية لتحويل صور BMP:

1. قم بإنشاء كائن Document جديد
1. أضف صفحة جديدة إلى المستند
1. قم بتعيين الهوامش للصفحة إلى 0 (إذا لزم الأمر)
1. قم بإنشاء كائن Image جديد وحدد ملف BMP المدخل
1. أضف الصورة إلى الصفحة
1. احفظ المستند في ملف PDF الناتج

لذلك، يتبع مقتطف الشيفرة التالي هذه الخطوات ويظهر كيفية تحويل BMP إلى PDF باستخدام PHP:

```php
// قم بإنشاء كائن Document جديد
$document = new Document();

// أضف صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// قم بتعيين الهوامش للصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// قم بإنشاء كائن Image جديد وحدد ملف BMP المدخل
$image = new Image();
$image->setFile($inputFile);

// أضف الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// احفظ المستند في ملف PDF الناتج
$document->save($outputFile);
```

## تحويل CGM إلى PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> هو معيار ISO يوفر تنسيق ملف صورة ثنائي الأبعاد يعتمد على المتجه لتخزين واسترجاع معلومات الرسومات. CGM هو تنسيق مستقل عن الجهاز. يعد CGM تنسيق رسومات متجه يدعم ثلاث طرق ترميز مختلفة: ثنائي (الأفضل لسرعة قراءة البرنامج)، قائم على الحروف (ينتج أصغر حجم ملف ويسمح بنقل البيانات بشكل أسرع) أو ترميز نص واضح (يسمح للمستخدمين بقراءة وتعديل الملف باستخدام محرر نصوص).

يوضح لك جزء الشيفرة التالي كيفية تحويل ملفات CGM إلى تنسيق PDF باستخدام Aspose.PDF لـ PHP.

1. قم بإنشاء مثيل من [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) لتحديد أي خيارات خاصة لتحميل ملف CGM.
1. قم بإنشاء مثيل لفئة [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) مع ذكر اسم الملف المصدر والخيارات.
1. احفظ المستند بالاسم المطلوب للملف.

```php
$options = new CgmLoadOptions();

// أنشئ كائن Document وقم بتحميل ملف CGM باستخدام الخيارات المحددة
$document = new Document($inputFile, $options);

// احفظ المستند كملف PDF
$document->save($outputFile);
```


## تحويل DICOM إلى PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> هو معيار للتعامل مع الصور الطبية وتخزينها وطباعتها ونقل المعلومات. يشمل تعريف تنسيق الملف وبروتوكول الاتصالات الشبكية.

Aspsoe.PDF لـ PHP يسمح لك بتحويل ملفات DICOM إلى تنسيق PDF، تحقق من مقتطف الكود التالي:

1. إنشاء كائن Document جديد
1. إضافة صفحة جديدة إلى المستند
1. ضبط هوامش الصفحة إلى 0 (إذا لزم الأمر)
1. إنشاء كائن Image جديد وتعيين ملف BMP المدخل
1. تعيين ملف DICOM كملف مصدر للصورة
1. تعيين نوع ملف الصورة إلى DICOM
1. إضافة الصورة إلى الصفحة
1. حفظ المستند في ملف PDF الناتج

```php
// إنشاء كائن Document جديد
$document = new Document();

// إضافة صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// ضبط هوامش الصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// إنشاء كائن Image جديد
$image = new Image();

// تعيين ملف DICOM كملف مصدر للصورة
$image->setFile($inputFile);

// تعيين نوع ملف الصورة إلى DICOM
$image->setFileType(ImageFileType::$Dicom);

// إضافة الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// حفظ المستند كملف PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**حاول تحويل DICOM إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)، حيث يمكنك تجربة استكشاف الوظيفة والجودة التي تعمل بها.

[![Aspose.PDF تحويل DICOM إلى PDF باستخدام التطبيق المجاني](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## تحويل EMF إلى PDF

تنسيق ملف التعريف المحسن (<abbr title="Enhanced metafile format">EMF</abbr>) يخزن الصور الرسومية بشكل مستقل عن الجهاز. تتكون ملفات EMF الوصفية من سجلات بطول متغير بترتيب زمني يمكنه عرض الصورة المخزنة بعد تحليلها على أي جهاز إخراج.

لدينا عدة طرق لتحويل EMF إلى PDF.

## باستخدام فئة الصورة

يتكون مستند PDF من صفحات وكل صفحة تحتوي على كائنات فقرة واحدة أو أكثر. يمكن أن تكون الفقرة نصًا أو صورة أو جدولًا أو مربعًا عائمًا أو رسمًا بيانيًا أو عنوانًا أو حقل نموذج أو مرفقًا.

لتحويل ملف صورة إلى تنسيق PDF، قم بتضمينه في فقرة.

من الممكن تحويل الصور الموجودة في موقع مادي على القرص الصلب المحلي، أو الموجودة في عنوان URL ويب، أو في كائن Stream.

لإضافة صورة:

1. أنشئ كائنًا من فئة com.aspose.pdf.Image.
2. أضف الصورة إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) الخاصة بصفحة معينة.
3. حدد المسار أو مصدر الصورة.
    - إذا كانت الصورة موجودة في موقع على القرص الصلب، حدد موقع المسار باستخدام طريقة [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - إذا كانت الصورة موضوعة في FileInputStream، مرر الكائن الذي يحتوي على الصورة إلى طريقة [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

يظهر مقتطف الشيفرة التالي كيفية تحميل كائن الصورة، ضبط هامش الصفحة، وضع الصورة على الصفحة وحفظ النتيجة كملف PDF.

```php
$inputFile = "sample.emf";

// إنشاء كائن Document جديد
$document = new Document();

// إضافة صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// ضبط هوامش الصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// إنشاء كائن Image جديد وضبط ملف الإدخال
$image = new Image();
$image->setFile($inputFile);

// إضافة الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// حفظ المستند كملف PDF
$document->save($outputFile);
```


## تحويل JPG إلى PDF

لا داعي للتساؤل عن كيفية تحويل JPG إلى PDF، لأن مكتبة Apose.PDF لـ PHP لديها أفضل قرار.

يمكنك بسهولة تحويل صور JPG إلى PDF باستخدام Aspose.PDF لـ PHP باتباع الخطوات التالية:

1. تهيئة كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
2. إضافة صفحة جديدة إلى المستند
3. ضبط هوامش الصفحة إلى 0
4. إنشاء كائن صورة جديد وتعيين ملف الإدخال
5. حفظ ملف PDF الناتج

يوضح جزء الشيفرة أدناه كيفية تحويل صورة JPG إلى PDF باستخدام PHP:

```php
$inputFile = "sample.jpg";

// إنشاء كائن جديد من Document
$document = new Document();

// إضافة صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// ضبط هوامش الصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// إنشاء كائن صورة جديد وتعيين ملف الإدخال
$image = new Image();
$image->setFile($inputFile);

// إضافة الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// حفظ المستند كملف PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**حاول تحويل JPG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا على الإنترنت ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من JPG إلى PDF باستخدام التطبيق المجاني](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## تحويل PNG إلى PDF

**Aspose.PDF for PHP** يدعم ميزة تحويل صور PNG إلى صيغة PDF. تحقق من مقتطف الشيفرة التالي لتحقيق مهمتك.

<abbr title="رسومات الشبكة المحمولة">PNG</abbr> يشير إلى نوع من تنسيق ملفات الصور النقطية التي تستخدم الضغط بدون فقدان، مما يجعلها شائعة بين مستخدميها.

يمكنك تحويل PNG إلى صورة PDF باستخدام الخطوات التالية:

1. تهيئة كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. إضافة صفحة جديدة إلى المستند
1. ضبط هوامش الصفحة إلى 0
1. إنشاء كائن صورة جديد وضبط ملف الإدخال
1. حفظ ملف PDF الناتج

علاوة على ذلك، يوضح مقتطف الشيفرة أدناه كيفية تحويل PNG إلى PDF في تطبيقات PHP الخاصة بك:

```php
$inputFile = "sample.png";

// إنشاء كائن مستند جديد
$document = new Document();

// إضافة صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// تعيين هوامش الصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// إنشاء كائن صورة جديد وتعيين ملف الإدخال
$image = new Image();
$image->setFile($inputFile);

// إضافة الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**حاول تحويل PNG إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["PNG إلى PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PNG إلى PDF باستخدام التطبيق المجاني](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## تحويل SVG إلى PDF

الرسومات المتجهة القابلة للتوسع (SVG) هي مجموعة من المواصفات لتنسيق ملفات مبني على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). تعتبر مواصفات SVG معيارًا مفتوحًا تم تطويره من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

يتم تعريف صور SVG وسلوكياتها في ملفات نصية بصيغة XML. هذا يعني أنه يمكن البحث عنها وفهرستها وبرمجتها، وإذا لزم الأمر، ضغطها. وباعتبارها ملفات XML، يمكن إنشاء وتحرير صور SVG باستخدام أي محرر نصوص، ولكن غالبًا ما يكون من الأنسب إنشاءها باستخدام برامج الرسم مثل Inkscape.

## كيفية تحويل ملف SVG إلى تنسيق PDF

لتحويل ملفات SVG إلى PDF، استخدم الفئة المسماة [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 لاحقًا، يتم تمرير هذا الكائن كحجة أثناء تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF في تحديد تنسيق الإدخال لمستند المصدر.

يظهر مقتطف الشيفرة التالي عملية تحويل ملف SVG إلى تنسيق PDF.

```php
// إنشاء كائن SvgLoadOptions جديد
$loadOption = new SvgLoadOptions();

// إنشاء كائن Document جديد وتحميل ملف SVG
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**حاول تحويل تنسيق SVG إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## تحويل TIFF إلى PDF

**Aspose.PDF for PHP** تنسيق الملف المدعوم، سواء كان صورة <abbr title="تنسيق ملف الصورة الموسوم">TIFF</abbr> ذات إطار واحد أو متعددة الإطارات. هذا يعني أنه يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك.

TIFF أو TIF، تنسيق ملف الصورة الموسوم، يمثل الصور النقطية التي تُستخدم على مجموعة متنوعة من الأجهزة التي تتوافق مع معيار تنسيق الملف هذا. يمكن أن تحتوي صورة TIFF على عدة إطارات تحتوي على صور مختلفة. تنسيق ملف Aspose.PDF مدعوم أيضًا، سواء كان صورة TIFF ذات إطار واحد أو متعددة الإطارات. لذلك يمكنك تحويل صورة TIFF إلى PDF في تطبيقات Java الخاصة بك. لذلك، سننظر في مثال لتحويل صورة TIFF متعددة الصفحات إلى مستند PDF متعدد الصفحات باستخدام الخطوات التالية:

1. إنشاء كائن مستند جديد
1. إضافة صفحة جديدة إلى المستند
1. ضبط هوامش الصفحة على 0
1. إنشاء كائن صورة جديد
1. ضبط مسار ملف صورة TIFF المُدخلة
1. إضافة الصورة إلى الصفحة
1. حفظ المستند كملف PDF

علاوة على ذلك، يُظهر مقتطف الشيفرة البرمجية التالي كيفية تحويل صورة TIFF متعددة الصفحات أو متعددة الإطارات إلى PDF:

```php
// إنشاء كائن مستند جديد
$document = new Document();

// إضافة صفحة جديدة إلى المستند
$page = $document->getPages()->add();

// تعيين هوامش الصفحة إلى 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// إنشاء كائن صورة جديدة
$image = new Image();

// تعيين مسار ملف صورة TIFF المدخلة
$image->setFile($inputFile);

// إضافة الصورة إلى الصفحة
$page->getParagraphs()->add($image);

// حفظ المستند كملف PDF
$document->save($outputFile);
```
---
title: تحويل صيغ الملفات المختلفة إلى PDF
linktitle: تحويل صيغ الملفات الأخرى إلى PDF
type: docs
weight: 80
url: /php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: يوضح لك هذا الموضوع كيف يسمح لك Aspose.PDF بتحويل صيغ الملفات الأخرى إلى مستند PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## تحويل EPUB إلى PDF

تتيح لك **Aspose.PDF for PHP** ببساطة تحويل ملفات EPUB إلى صيغة PDF.

<abbr title="النشر الإلكتروني">EPUB</abbr> هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF). تحتوي الملفات على الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين.

من أجل تحويل ملفات EPUB إلى صيغة PDF، يحتوي Aspose.PDF for PHP على فئة تدعى [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) والتي تُستخدم لتحميل ملف EPUB المصدر.
 بعد ذلك، يتم تمرير الكائن كوسيطة إلى [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) لتهيئة الكائن، حيث يساعد محرك تصيير PDF في تحديد تنسيق إدخال المستند المصدر.

يظهر مقطع الشيفرة التالي عملية تحويل ملف EPUB إلى تنسيق PDF.

1. إنشاء [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) لـ EPUB.
2. تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. حفظ مستند PDF الناتج.

```php
// إنشاء مثيل جديد من EpubLoadOptions
$loadOption = new EpubLoadOptions();

// إنشاء كائن Document جديد وتحميل ملف EPUB
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**جرب تحويل EPUB إلى PDF عبر الإنترنت**

تقدم Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.
[![تحويل Aspose.PDF من EPUB إلى PDF باستخدام تطبيق مجاني](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## تحويل Markdown إلى PDF

{{% alert color="success" %}}
**حاول تحويل Markdown إلى PDF عبر الإنترنت**

يوفر Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من Markdown إلى PDF باستخدام تطبيق مجاني](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown هو أداة تحويل النص إلى HTML لمؤلفي الويب. يسمح لك Markdown بالكتابة بتنسيق نص عادي سهل القراءة والكتابة ثم تحويله إلى XHTML (أو HTML) صالح هيكليًا.

يظهر مقتطف الشفرة التالي كيفية استخدام هذه الوظيفة مع Aspose.PDF لـ PHP:

```php
// إنشاء مثيل جديد من MdLoadOptions
$loadOption = new MdLoadOptions();

// إنشاء مثيل جديد من Document وتحميل ملف Markdown المدخل
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```


## تحويل PCL إلى PDF

<abbr title="Printer Command Language">PCL</abbr> (لغة أوامر الطابعة) هي لغة طباعة طورتها شركة Hewlett-Packard للوصول إلى ميزات الطابعة القياسية. تعتبر مستويات PCL من 1 إلى 5e/5c لغات قائمة على الأوامر تستخدم تسلسلات التحكم التي تتم معالجتها وتفسيرها بترتيب استلامها. على مستوى المستهلك، يتم توليد تدفقات بيانات PCL بواسطة برنامج تشغيل الطابعة. يمكن أيضًا توليد مخرجات PCL بسهولة بواسطة التطبيقات المخصصة.

{{% alert color="success" %}}
**حاول تحويل PCL إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PCL إلى PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PCL إلى PDF باستخدام تطبيق مجاني](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**حاليًا، يتم دعم PCL5 والإصدارات الأقدم فقط.**

|**مجموعات الأوامر**|**الدعم**|**الاستثناءات**|**الوصف**|

| :- | :- | :- | :- |
|أوامر التحكم بالوظائف|+|وضع الطباعة المزدوجة|التحكم في عملية الطباعة: عدد النسخ، وحاوية المخرجات، والطباعة البسيطة/المزدوجة، والإزاحات اليسرى والعلوية إلخ.|
|أوامر التحكم بالصفحة|+|أمر تخطي التثقيب|تحديد حجم الصفحة، والهوامش، واتجاه الصفحة، والمسافات بين السطور، والمسافات بين الأحرف إلخ.|
|أوامر تحديد موضع المؤشر|+| |تحديد موضع المؤشر، ومن ثم، أصول النص أو الصور النقطية أو المتجهة والتفاصيل.|

| أوامر اختيار الخطوط | + | <p>1. أمر طباعة البيانات الشفافة.</p><p>2. الخطوط الناعمة المدمجة. في النسخة الحالية، بدلاً من إنشاء خط ناعم، تختار مكتبتنا الخط المناسب من الخطوط TrueType "الصلبة" الموجودة المثبتة على الجهاز المستهدف. <br> يتم تحديد الملاءمة من خلال نسبة العرض/الارتفاع. <br> هذه الميزة تعمل فقط للخطوط Bitmap و TrueType ولا تضمن أن النص المطبع بالخط الناعم سيكون مطابقًا للنص في الملف المصدر. <br> لأن رموز الحروف في الخط الناعم قد لا تتطابق مع الرموز الافتراضية.</p><p>3. مجموعات الرموز المعرفة من قبل المستخدم.</p> | السماح بتحميل الخطوط الناعمة (المضمنة) من ملف PCL وإدارتها في الذاكرة. |
| أوامر الرسومات النقطية | + | فقط بالأبيض والأسود | السماح بتحميل الصور النقطية من ملف PCL إلى الذاكرة، وتحديد معايير النقطية <br> مثل العرض، الارتفاع، نوع الضغط، الدقة، إلخ. |
| أوامر الألوان | + |  | السماح بالتلوين لجميع الكائنات القابلة للطباعة. |
| أوامر نموذج الطباعة | + |  | السماح بتعبئة النص، الصور النقطية والمناطق المستطيلة بأنماط نقطية محددة مسبقًا ومعرفة من قبل المستخدم، تحديد وضع الشفافية للأنماط وصورة النقط المصدرية. |
 <br>الأنماط المحددة مسبقًا هي التظليل والتظليل المتقاطع وتظليل المناطق.|
|أوامر تعبئة منطقة المستطيل|+| |تسمح بإنشاء وملء مناطق مستطيلة بالأنماط.|
|أوامر الرسومات المتجهة HP-GL/2|+|أمر المتجه الممسوح (SV)، أمر وضع الشفافية (TR)، أمر البيانات الشفافة (TD)، RO (تدوير نظام الإحداثيات)، أوامر الخطوط القابلة للتطوير أو نقطية (SB)، أمر ميل الحرف (SL) والمساحة الإضافية (ES) لم تُنفذ وأوامر DV (تحديد مسار النص المتغير) تم تنفيذها في الإصدار التجريبي.|<p>- السماح بتحميل الصور المتجهة HP-GL/2 من ملف PCL إلى الذاكرة. الصورة المتجهة لها أصل في الزاوية السفلية اليسرى من منطقة الطباعة، ويمكن تكبيرها، نقلها، تدويرها وقطعها.</p><p>- يمكن أن تحتوي الصورة المتجهة على نص، كملصقات، وأشكال هندسية مثل المستطيل، الدائرة، القطع الناقص، الخط، القوس، منحنى بيزيه والأشكال المعقدة المكونة من الأشكال البسيطة.</p><p>- يمكن ملء الأشكال المغلقة بما في ذلك حروف الملصقات بملء صلب أو نمط متجه.</p><p>- يمكن أن يكون النمط تظليلاً، تقاطع التظليل، تظليل، نمط مستخدم محدد، تظليل PCL أو تقاطع التظليل و PCL مستخدم محدد. أنماط PCL هي أنماط نقطية. يمكن تدوير الملصقات بشكل فردي، وتكبيرها، وتوجيهها في أربعة اتجاهات: للأعلى، للأسفل، لليسار ولليمين. تتضمن الاتجاهات اليسرى واليمنى ترتيب الحروف واحدًا بعد الآخر. تتضمن الاتجاهات العلوية والسفلية ترتيب الحروف واحدًا تحت الآخر.</p>|
|Macross|―| |تسمح بتحميل تسلسل من أوامر PCL في الذاكرة واستخدام هذا التسلسل عدة مرات، على سبيل المثال، لطباعة رأس الصفحة أو تعيين تنسيق واحد لمجموعة من الصفحات.|
|Unicode text|―| |تسمح بطباعة الأحرف غير ASCII. لم يتم التنفيذ بسبب عدم وجود ملفات نموذجية تحتوي على <br>نصوص يونيكود|
|PCL6 (PCL-XL)| |تم تحقيقه فقط في النسخة التجريبية Beta بسبب نقص في ملفات الاختبار. الخطوط المدمجة أيضًا غير مدعومة. امتداد JetReady غير مدعوم لأنه من المستحيل الحصول على مواصفات JetReady.|تنسيق ملف ثنائي.|

### تحويل ملف PCL إلى تنسيق PDF

للسماح بالتحويل من PCL إلى PDF، تحتوي [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java) على الفئة [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) والتي تُستخدم لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). يتم تمرير هذا الكائن لاحقًا كوسيط أثناء تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF على تحديد تنسيق إدخال المستند الأصلي.

يوضح مقتطف الكود التالي عملية تحويل ملف PCL إلى تنسيق PDF.

```php
// إنشاء مثيل جديد من PclLoadOptions
$loadOption = new PclLoadOptions();

// إنشاء مثيل جديد من Document وتحميل ملف PCL
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

### المشاكل المعروفة

1. قد يختلف مصدر السلاسل النصية والصور قليلاً عن تلك الموجودة في ملف PCL المصدر إذا لم يكن اتجاه الطباعة 0º. وينطبق الأمر نفسه على الصور المتجهة إذا كان نظام الإحداثيات للرسم المتجه تم تدويره (أمر RO مسبوق).
2. قد يختلف أصل التسميات في الصور المتجهة عن تلك الموجودة في ملف PCL المصدر إذا كانت التسميات متأثرة بتسلسل من الأوامر: أصل التسمية (LO)، تعريف مسار النص المتغير (DV)، الاتجاه المطلق (DI) أو الاتجاه النسبي (DR).
3. قد يتم قراءة النص بشكل غير صحيح إذا كان يجب عرضه بخط Bitmap أو TrueType الناعم (المضمن)، لأن هذه الخطوط حاليا مدعومة جزئياً فقط (راجع الاستثناءات في "جدول الميزات المدعومة"). في هذه الحالة يمكن قراءة النص بشكل صحيح فقط إذا كانت رموز الحروف في الخط الناعم تتوافق مع الرموز الافتراضية. كما يمكن أن يختلف نمط النص المقروء عن ذلك الموجود في ملف PCL المصدر لأنه ليس من الضروري تحديد النمط في رأس الخط الناعم.

1. إذا كان ملف PCL المفصّل يحتوي على خطوط Intellifont أو Universal، سيتم رمي استثناء، لأن خطوط Intellifont وUniversal غير مدعومة على الإطلاق.
1. إذا كان ملف PCL المفصّل يحتوي على أوامر الماكرو، فإن نتيجة التحليل ستختلف بشكل كبير عن الملف المصدر، لأن أوامر الماكرو غير مدعومة.

## تحويل النص إلى PDF

يوفر **Aspose.PDF for PHP** القدرة على تحويل ملفات النص إلى تنسيق PDF. في هذه المقالة، نوضح كيف يمكننا بسهولة وكفاءة تحويل ملف نصي إلى PDF باستخدام Aspose.PDF.
{{% alert color="primary" %}}

عندما تحتاج إلى تحويل ملف نصي إلى PDF، قم بقراءة ملف النص المصدر في بعض القارئ في البداية. لقد استخدمنا StringBuilder لقراءة محتويات ملف النص. قم بإنشاء كائن Document وأضف صفحة جديدة في مجموعة Pages. قم بإنشاء كائن جديد من TextFragment ومرر كائن StringBuilder إلى منشئه. أضف فقرة جديدة في مجموعة Paragraphs باستخدام كائن TextFragment واحفظ ملف PDF الناتج باستخدام طريقة Save لفئة Document.
**حاول تحويل النص إلى PDF عبر الإنترنت**

تقدم Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["النص إلى PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من النص إلى PDF باستخدام التطبيق المجاني](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)  
{{% /alert %}}

### تحويل ملف نصي عادي إلى PDF

```php
// إنشاء كائن وثيقة جديد.
$document = new Document();

// إضافة صفحة جديدة إلى الوثيقة.
$page = $document->getPages()->add();

// قراءة محتوى ملف النص المدخل.
$text = file_get_contents($inputFile);

// إنشاء كائن FontRepository جديد.
$fontRepository = new FontRepository();

// العثور على خط "Courier" في المستودع.
$font = $fontRepository->findFont("Courier");

// إنشاء كائن TextFragment جديد باستخدام النص المدخل.
$textFragment = new TextFragment($text);

// تعيين خط مقطع النص إلى "Courier".
$textFragment->getTextState()->setFont($font);

// إضافة مقطع النص إلى الصفحة.
$page->getParagraphs()->add($textFragment);

// حفظ الوثيقة إلى ملف الإخراج.
$document->save($outputFile);
```


## تحويل XPS إلى PDF

يدعم **Aspose.PDF for PHP** ميزة تحويل ملفات <abbr title="XML Paper Specification">XPS</abbr> إلى تنسيق PDF. تحقق من هذه المقالة لحل مهامك.

XPS، مواصفات الورق XML، هو تنسيق ملف من مايكروسوفت يستخدم لدمج إنشاء وعرض المستندات في ويندوز. مع Aspose.PDF for PHP، من الممكن تحويل ملفات XPS إلى PDF، وهو تنسيق الملف المحمول من أدوبي.

تنسيق الملف هو في الأساس ملف XML مضغوط، يستخدم بشكل أساسي للتوزيع والتخزين. من الصعب جداً تحريره وغالباً ما يتم تطبيقه بواسطة مايكروسوفت.

لتحويل ملف XPS إلى PDF باستخدام [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java)، استخدم فئة [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 يستخدم هذا لتهيئة كائن [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). لاحقًا، يتم تمرير هذا الكائن كحجة أثناء تهيئة كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) ويساعد محرك عرض PDF على تحديد تنسيق إدخال المستند المصدر.

يوضح جزء الشفرة التالي عملية تحويل ملف XPS إلى تنسيق PDF.

```php
// إنشاء مثيل جديد لفئة XpsLoadOptions
$loadOption = new XpsLoadOptions();

// إنشاء مثيل جديد لفئة Document وتحميل ملف XPS
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**حاول تحويل صيغة XPS إلى PDF عبر الإنترنت**

يقدم Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## تحويل PostScript إلى PDF

**Aspose.PDF for PHP** تدعم ميزات تحويل ملفات PostScript إلى تنسيق PDF. واحدة من الميزات في Aspose.PDF هي أنه يمكنك تعيين مجموعة من مجلدات الخطوط لاستخدامها أثناء التحويل.

من أجل تحويل ملف PostScript إلى تنسيق PDF، تقدم Aspose.PDF for PHP فئة [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) التي تُستخدم لتهيئة كائن LoadOptions. لاحقاً يمكن تمرير هذا الكائن كمعامل إلى مُنشئ كائن الوثيقة، مما سيساعد محرك عرض PDF في تحديد تنسيق وثيقة المصدر.

يمكن استخدام جزء الكود التالي لتحويل ملف PostScript إلى تنسيق PDF:

```php
// إنشاء كائن PsLoadOptions جديد.
$loadOption = new PsLoadOptions();

// إنشاء كائن Document جديد وتحميل ملف PS المدخل.
$document = new Document($inputFile, $loadOption);

// حفظ الوثيقة كملف PDF.
$document->save($outputFile);
```

## تحويل XML إلى PDF

يُستخدم تنسيق XML لتخزين البيانات المهيكلة.
 هناك عدة طرق لتحويل <abbr title="Extensible Markup Language">XML</abbr> إلى PDF في Aspose.PDF.

{{% alert color="success" %}}
**حاول تحويل XML إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا على الإنترنت ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)، حيث يمكنك تجربة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

فكر في الخيار باستخدام مستند XML مستند إلى معيار XSL-FO.

### تحويل XSL-FO إلى PDF

يمكن تنفيذ تحويل ملفات XSL-FO إلى PDF باستخدام كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) مع [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// تعيين المسار إلى ملفات العينة
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// إنشاء مثيل جديد لفئة XslFoLoadOptions وتمرير مسار ملف XSL-FO المدخل
$loadOption = new XslFoLoadOptions($inputFoFile);

// إنشاء مثيل جديد لفئة Document وتمرير ملف XML المدخل وخيارات تحميل XSL-FO
$document = new Document($inputFile, $loadOption);

// حفظ مستند PDF المحول إلى مسار ملف الإخراج
$document->save($outputFile);
```

## تحويل LaTeX/TeX إلى PDF

تنسيق ملف LaTeX هو تنسيق ملف نصي بعلامات في مشتق LaTeX من عائلة لغات TeX وLaTeX هو تنسيق مشتق من نظام TeX. LaTeX (ˈleɪtɛk/ lay-tek أو lah-tek) هو نظام لإعداد المستندات ولغة ترميز المستندات. ويستخدم على نطاق واسع في التواصل ونشر الوثائق العلمية في العديد من المجالات، بما في ذلك الرياضيات والفيزياء وعلوم الكمبيوتر. كما أن له دور بارز في إعداد ونشر الكتب والمقالات التي تحتوي على مواد متعددة اللغات المعقدة، مثل السانسكريتية والعربية، بما في ذلك الطبعات النقدية. يستخدم LaTeX برنامج التنضيد TeX لتنسيق مخرجاته وهو مكتوب بنفسه بلغة ماكرو TeX.

يدعم **Aspose.PDF for PHP** ميزة تحويل ملفات TeX إلى تنسيق PDF ولتحقيق هذا المتطلب، يحتوي حزمة com.aspose.pdf على فئة تُسمى [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) التي توفر الإمكانيات لتحميل ملفات LaTex وعرض الإخراج بتنسيق PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 يوضح مقطع الشيفرة التالي عملية تحويل ملف LaTex إلى تنسيق PDF.

```php
// إنشاء مثيل جديد لفئة LatexLoadOptions
$loadOption = new LatexLoadOptions();

// إنشاء مثيل جديد لفئة Document وتحميل ملف TeX باستخدام TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// حفظ المستند كملف PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**حاول تحويل LaTeX/TeX إلى PDF عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من LaTeX/TeX إلى PDF باستخدام التطبيق المجاني](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}
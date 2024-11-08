---
title: تحويل ملف PDF إلى صيغ أخرى
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى صيغ ملفات أخرى.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى EPUB باستخدام تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (اختصار للنشر الإلكتروني) هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF).
 ملفات لها الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز العرض المحدد. كما يدعم EPUB المحتوى ذو التنسيق الثابت. يهدف التنسيق إلى أن يكون تنسيقًا واحدًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. يحل محل المعيار Open eBook.

يدعم Aspose.PDF لـ PHP ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF لـ PHP على فئة باسم [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) والتي يمكن استخدامها كوسيطة ثانية للطريقة [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) لإنشاء ملف EPUB. يرجى محاولة استخدام مقطع الشيفرة التالي لتحقيق هذا المتطلب.

```php
// إنشاء مثيل جديد لفئة Document وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء مثيل جديد لفئة EpubSaveOptions
$saveOption = new EpubSaveOptions();

// حفظ المستند بتنسيق EPUB باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOption);
```

## تحويل PDF إلى LaTeX/TeX

**Aspose.PDF لـ PHP** يدعم تحويل PDF إلى LaTeX/TeX.  
تنسيق ملف LaTeX هو تنسيق ملف نصي مع علامات خاصة ويستخدم في نظام إعداد المستندات المستندة إلى TeX للطباعة عالية الجودة.

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) والتي توفر الطريقة `setOutDirectoryPath` لحفظ الصور المؤقتة أثناء عملية التحويل.

يظهر مقتطف الشيفرة التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام Java.

```php
// إنشاء كائن مستند جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن LaTeXSaveOptions جديد
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// حفظ المستند كـ LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

يقدم لك Aspose.PDF لـ PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF لتحويل PDF إلى LaTeX/TeX مع تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى نص

يدعم **Aspose.PDF for PHP** تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي.

### تحويل مستند PDF بالكامل إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام طريقة Visit لفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

يوضح مقتطف الشيفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن TextAbsorber لاستخراج النص من المستند
$textAbsorber = new TextAbsorber();

// استخراج النص من المستند
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// حفظ النص المستخرج إلى ملف الإخراج
file_put_contents($outputFile, $content);

// الحصول على حجم ملف الإخراج
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى نص عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### تحويل صفحة PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام Aspose.PDF for PHP. يجب عليك استخدام طريقة Visit لفئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) لحل هذه المهمة.

يوضح مقطع الشفرة التالي كيفية استخراج النصوص من الصفحات المحددة.

```php
// تحميل مستند PDF
$document = new Document($inputFile);

// إنشاء كائن TextAbsorber لاستخراج النص من المستند
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // حفظ النص المستخرج في الملف الناتج
    file_put_contents($outputFile, $content);
}
```


## تحويل PDF إلى XPS

يوفر **Aspose.PDF for PHP** إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="XML Paper Specification">XPS</abbr>. دعونا نحاول استخدام مقطع الشيفرة المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام Java.

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

يقدم لك Aspose.PDF for PHP تطبيقًا مجانيًا عبر الإنترنت ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى XPS باستخدام التطبيق المجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS يرتبط أساسًا بمواصفات الورق XML من قبل شركة Microsoft Corporation. مواصفات الورق XML (XPS)، التي كانت تُعرف سابقًا بالاسم الرمزي Metro ودمج مفهوم التسويق مسار الطباعة للجيل التالي (NGPP)، هي مبادرة من مايكروسوفت لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

لتحويل ملفات PDF إلى XPS، يحتوي Aspose.PDF على فئة [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) التي تستخدم كالحجة الثانية لمنشئ Document.save(..) لتوليد ملف XPS.
 The following code snippet shows the process of converting PDF files into XPS format.

```php
// إنشاء كائن مستند جديد وتحميل ملف PDF المدخل
$document = new Document($inputFile);

// إنشاء كائن XpsSaveOptions جديد
$saveOption = new XpsSaveOptions();

// حفظ المستند كملف XPS باستخدام خيارات الحفظ المحددة
$document->save($outputFile, $saveOption);
```
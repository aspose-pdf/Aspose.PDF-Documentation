---
title: محول HTML
type: docs
weight: 70
url: /ar/net/plugins/html/
description: كيفية تحويل ملفات PDF إلى ملفات HTML والعكس باستخدام إضافة Aspose.PDF PdfHtml
lastmod: "2024-01-24"
draft: false
---

في هذا المقال، سنوضح لك كيفية استخدام [إضافة PdfHtml](https://products.aspose.org/pdf/net/html-converter/)، والتي يمكنها تحويل ملفات PDF إلى ملفات HTML والعكس.

## المتطلبات الأساسية

ستحتاج إلى التالي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 21.1 أو أحدث
* ملف PDF نموذجي وملف HTML نموذجي

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لتحويل ملفات PDF إلى ملفات HTML والعكس باستخدام إضافة PdfHtml هي:

1. إنشاء كائن من الصف PdfHtml
2. إنشاء كائن من الصف PdfToHtmlOptions أو HtmlToPdfOptions، حسب اتجاه التحويل
3. إضافة مصادر البيانات الداخلية والخارجية إلى كائن الخيارات
4.
### الخطوة 1: إنشاء كائن من فئة PdfHtml

فئة PdfHtml هي الفئة الرئيسية التي توفر وظيفة تحويل ملفات PDF من وإلى ملفات HTML. لاستخدامها، تحتاج إلى إنشاء نسخة منها باستخدام المنشئ الافتراضي:

```cs
// إنشاء نسخة من إضافة PdfHtml
var plugin = new PdfHtml();
```

### الخطوة 2: إنشاء كائن من فئة PdfToHtmlOptions أو HtmlToPdfOptions، اعتمادًا على اتجاه التحويل

فئات PdfToHtmlOptions و HtmlToPdfOptions هي فئات مساعدة تسمح لك بتحديد خيارات ومعاملات مختلفة لعملية التحويل، مثل تنسيق الخروج، نطاق الصفحة، الترميز، الخطوط، وما إلى ذلك. لاستخدام هذه الفئات، تحتاج إلى إنشاء نسخة من الفئة المناسبة باستخدام المنشئ الافتراضي أو بتمرير بعض المعاملات. على سبيل المثال، لتحويل ملف PDF إلى ملف HTML مع الموارد المضمنة، يمكنك استخدام الكود التالي:

```cs

```cs
// إنشاء نموذج جديد من فئة PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

لتحويل ملف HTML إلى ملف PDF باستخدام الإعدادات الافتراضية، يمكنك استخدام الكود التالي:

```cs
// إنشاء نموذج جديد من فئة HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

يمكنك أيضًا تعيين خيارات أخرى، مثل تنسيق الخروج، نطاق الصفحات، الترميز، الخطوط، وغيرها باستخدام خصائص فئات الخيارات. على سبيل المثال، لتحويل ملف PDF إلى ملف HTML باستخدام ترميز UTF-8 وخط Arial، يمكنك استخدام الكود التالي:

```cs
// إنشاء نموذج جديد من فئة PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// تعيين الترميز إلى UTF-8
options.Encoding = Encoding.UTF8;

// تعيين الخط إلى Arial
options.Font = "Arial";
```

### الخطوة 3: إضافة مصادر البيانات الداخلية والخارجية إلى كائن الخيارات

مصادر البيانات الداخلية والخارجية هي ملفات PDF أو HTML التي تريد تحويلها وحفظها.
مصادر البيانات الإدخالية والإخراجية هي ملفات PDF أو HTML التي تريد تحويلها وحفظها.

```cs
// حدد مسارات ملفات الإدخال والإخراج
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// أضف مسارات الملفات إلى الخيارات
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### الخطوة 4: تشغيل طريقة Process لكائن PdfHtml

الخطوة النهائية هي تشغيل طريقة Process لكائن PdfHtml، مع تمرير كائن الخيارات كمعامل. ستقوم هذه الطريقة بإجراء التحويل وإرجاع كائن ResultContainer، الذي يحتوي على نتائج التحويل، مثل الحالة، الرسائل، مصادر البيانات الإخراجية، وما إلى ذلك. يمكنك الوصول إلى النتائج باستخدام الخصائص والطرق لفئة ResultContainer. على سبيل المثال، للحصول على النتيجة الأولى من مجموعة النتائج وطباعتها على وحدة التحكم، يمكنك استخدام الكود التالي:

```cs
// قم بمعالجة التحويل واحصل على حاوية النتائج
var resultContainer = plugin.Process(options);

// احصل على النتيجة الأولى من مجموعة النتائج
var result = resultContainer.ResultCollection[0];

// اطبع النتيجة على وحدة التحكم
Console.WriteLine(result);
```
```
changefreq: "monthly"
type: docs

النتيجة ستحتوي على معلومات مثل مسارات ملفات الإخراج.
```

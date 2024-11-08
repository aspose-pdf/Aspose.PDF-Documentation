---
title: محول JPEG
type: docs
weight: 90
url: /ar/net/plugins/jpeg/
description: كيفية تحويل صفحات PDF إلى صور JPEG باستخدام محول JPEG من Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

في هذا المقال، سنوضح لك كيفية استخدام [محول JPEG](https://products.aspose.org/pdf/net/jpeg-converter/)، الذي يمكنه تحويل صفحات PDF إلى صور JPEG وحفظها كملفات منفصلة.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض الصفحات

يمكنك تنزيل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لتحويل صفحات PDF إلى صور JPEG باستخدام محول JPEG هي:

1. إنشاء كائن من الفئة Jpeg
1. إنشاء كائن من الفئة JpegOptions وإضافة مسارات الملفات الخاصة بالإدخال والإخراج
1. تشغيل الطريقة Process للكائن Jpeg والحصول على حاوية النتيجة
1.
1.

لنرى كيفية تنفيذ هذه الخطوات في كود C#.

### الخطوة 1: إنشاء كائن من فئة Jpeg

فئة Jpeg هي الفئة الرئيسية التي توفر وظيفة تحويل صفحات PDF إلى صور JPEG. لاستخدامها، تحتاج إلى إنشاء نسخة منها باستخدام البناء الافتراضي:

```cs
// إنشاء نسخة جديدة من Jpeg
var converter = new Jpeg();
```

### الخطوة 2: إنشاء كائن من فئة JpegOptions وإضافة مسارات الملف الداخلي والخارجي

فئة JpegOptions هي فئة مساعدة تسمح لك بتحديد خيارات ومعاملات مختلفة لعملية التحويل، مثل دقة الإخراج، نطاق الصفحة، جودة الصورة، إلخ.
فئة JpegOptions هي فئة مساعدة تتيح لك تحديد خيارات ومعاملات مختلفة لعملية التحويل، مثل دقة الإخراج، ونطاق الصفحة، وجودة الصورة، وما إلى ذلك.

```cs
// حدد مسارات الملفات الإدخالية والمخرجة
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// إنشاء نموذج من فئة JpegOptions
var converterOptions = new JpegOptions();

// إضافة مسارات الملفات الإدخالية والمخرجة إلى الخيارات
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

يمكنك أيضًا تعيين خيارات أخرى، مثل دقة الإخراج، ونطاق الصفحة، وجودة الصورة، وما إلى ذلك باستخدام خصائص فئة JpegOptions. على سبيل المثال، لتحويل الصفحة الأولى فقط من ملف PDF إلى صورة JPEG بدقة 300 نقطة في البوصة، يمكنك استخدام الكود التالي:

```cs
// تعيين دقة الإخراج إلى 300 نقطة في البوصة
converterOptions.OutputResolution = 300;

// تعيين نطاق الصفحة إلى الصفحة الأولى
converterOptions.PageRange = new PageRange(1);
```
### الخطوة 3: تشغيل طريقة Process لكائن Jpeg والحصول على حاوية النتائج

الخطوة النهائية هي تشغيل طريقة Process لكائن Jpeg، مع تمرير كائن converterOptions كمعامل. ستقوم هذه الطريقة بإجراء التحويل وإرجاع كائن ResultContainer، الذي يحتوي على نتائج التحويل، مثل الحالة، الرسائل، مسارات الملفات الناتجة، وغيرها. يمكنك الوصول إلى النتائج باستخدام الخصائص والطرق لفئة ResultContainer. على سبيل المثال، للحصول على حاوية النتائج وطباعة حالة التحويل، يمكنك استخدام الكود التالي:

```cs
// معالجة التحويل والحصول على حاوية النتائج
ResultContainer resultContainer = converter.Process(converterOptions);

// طباعة حالة التحويل
Console.WriteLine(resultContainer.Status);
```

حالة التحويل يمكن أن تكون إما نجاح أو فشل، اعتمادًا على ما إذا كان التحويل قد تم بنجاح أم لا.

### الخطوة 4: طباعة مسارات الصور JPEG المحولة

تحتوي حاوية النتائج على مجموعة من النتائج، واحدة لكل مسار ملف ناتج.
يحتوي حاوية النتائج على مجموعة من النتائج، واحدة لكل مسار ملف خرج.

```cs
// طباعة مسارات الصور JPEG المحولة
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

سيكون لمسارات الملفات الخارجية الشكل {outputPath}{pageNumber}.jpg، حيث {outputPath} هو دليل الخروج و{pageNumber} هو رقم الصفحة من ملف PDF. على سبيل المثال، إذا كان دليل الخروج هو C:\Samples\images وكان لملف PDF ثلاث صفحات، فسوف تكون مسارات الملفات الخارجية:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```

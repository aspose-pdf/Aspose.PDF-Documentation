---
title: محول XLS
type: docs
weight: 20
url: /net/plugins/xls/
description: كيفية تحويل ملفات PDF إلى جداول بيانات Excel باستخدام إضافات Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

في هذا المقال، سنوضح لك كيفية استخدام [إضافة PdfXls](https://products.aspose.org/pdf/net/xls-converter/)، والتي يمكنها تحويل ملفات PDF إلى تنسيق Excel بدقة ووضوح عاليين.

{{% /alert %}}

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي تريد تحويله إلى تنسيق Excel

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لتحويل ملف PDF إلى تنسيق Excel باستخدام إضافة PdfXls هي:

1. إنشاء كائن من فئة PdfXls
1. إضافة مصادر البيانات الداخلية والخارجية إلى كائن PdfToXlsOptions
1. تشغيل طريقة Process لكائن PdfXls

دعونا نرى كيفية تطبيق هذه الخطوات في كود C#.
لنرى كيفية تطبيق هذه الخطوات في كود C#.

### الخطوة 1: إنشاء كائن من الفئة PdfXls

الفئة PdfXls هي الفئة الرئيسية التي توفر وظيفة تحويل PDF إلى Excel. لاستخدامها، تحتاج إلى إنشاء مثال عليها باستخدام المنشئ الافتراضي:

```csharp
// إنشاء مثال من إضافة PdfXls
var plugin = new PdfXls();
```

### الخطوة 2: إضافة مصادر البيانات الداخلية والخارجية إلى كائن PdfToXlsOptions

الفئة PdfToXlsOptions هي فئة مساعدة تتيح لك تحديد خيارات ومعاملات مختلفة لعملية التحويل. لاستخدامها، تحتاج إلى إنشاء مثال عليها وإضافة مصادر البيانات الداخلية والخارجية باستخدام الطرق `AddInput` و `AddOutput`. يمكن أن تكون مصادر البيانات إما مسارات ملفات أو تدفقات. على سبيل المثال، لتحويل ملف PDF باسم `sample.pdf` في مجلد `C:\Samples` إلى ملف Excel باسم `sample.xlsx` في نفس المجلد، يمكنك استخدام الكود التالي:

```csharp
// تحديد مسارات البيانات الداخلية والخارجية
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// إنشاء مثال من الفئة PdfToXlsOptions
var options = new PdfToXlsOptions();

// إضافة مسارات البيانات الداخلية والخارجية إلى الخيارات
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
يمكنك أيضاً تعيين خيارات أخرى، مثل تنسيق الإخراج، نطاق الصفحة، اسم ورقة العمل، وغيرها باستخدام خصائص فئة PdfToXlsOptions. على سبيل المثال، لتحويل ملف PDF إلى تنسيق XLSX، إدراج عمود فارغ في المركز الأول، وتسمية ورقة العمل باسم "MySheet"، يمكنك استخدام الكود التالي:

```csharp
// تعيين تنسيق الإخراج إلى XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// إدراج عمود فارغ في المركز الأول
options.InsertBlankColumnAtFirst = true;
```

### الخطوة 3: تشغيل طريقة Process لكائن PdfXls

الخطوة النهائية هي تشغيل طريقة Process لكائن PdfXls، مع تمرير كائن PdfToXlsOptions كمعامل.
الخطوة النهائية هي تشغيل طريقة Process لكائن PdfXls، مع تمرير كائن PdfToXlsOptions كمعامل.

```csharp
// معالجة تحويل PDF إلى Excel باستخدام الإضافة والخيارات
var resultContainer = plugin.Process(options);

// الحصول على النتيجة الأولى من مجموعة النتائج
var result = resultContainer.ResultCollection[0];

// طباعة النتيجة
Console.WriteLine(result);
```

ستحتوي النتيجة على معلومات مثل مسارات ملفات الإخراج.

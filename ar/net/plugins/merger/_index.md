---
title: الاندماج
type: docs
weight: 100
url: ar/net/plugins/merger/
description: كيفية دمج ملفات PDF متعددة في ملف واحد باستخدام إضافة دمج Aspose.PDF
lastmod: "2024-01-24"
---

في هذا المقال، سنوضح لك كيفية استخدام [إضافة الدمج](https://products.aspose.org/pdf/net/merger/)، والتي يمكن أن تدمج ملفات PDF متعددة في ملف واحد وحفظه كملف جديد.

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 21.1 أو أحدث
* ثلاث ملفات PDF عينة ترغب في دمجها

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لدمج ملفات PDF متعددة في ملف واحد باستخدام إضافة الدمج هي:

1. إنشاء كائن من فئة Merger
2. إنشاء كائن من فئة MergeOptions وإضافة مسارات الملفات الإدخالية والناتجة
3. تشغيل طريقة Process لكائن Merger

لنرى كيف يمكن تنفيذ هذه الخطوات في كود C#.

### الخطوة 1: إنشاء كائن من فئة Merger
### الخطوة 1: إنشاء كائن من فئة Merger

فئة Merger هي الفئة الرئيسية التي توفر وظيفة دمج ملفات PDF المتعددة في ملف واحد. لاستخدامها، تحتاج إلى إنشاء مثيل منها باستخدام المنشئ الافتراضي:

```cs
// إنشاء مثيل جديد من Merger
var pdfMerger = new Merger();
```

### الخطوة 2: إنشاء كائن من فئة MergeOptions وإضافة مسارات الملفات الإدخالية والناتجة

فئة MergeOptions هي فئة مساعدة تتيح لك تحديد خيارات ومعايير مختلفة لعملية الدمج، مثل نطاق الصفحات، الترتيب، الأمان، إلخ.
### الخطوة 3: تشغيل طريقة Process لكائن Merger

الخطوة النهائية هي تشغيل طريقة Process لكائن Merger، بمرور كائن mergeOptions كمعامل.

```cs
// تحديد مسارات الملفات الداخلة والخارجة
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// إنشاء نموذج من الفئة MergeOptions
var mergeOptions = new MergeOptions();

// إضافة مسارات الملفات الداخلة والخارجة إلى الخيارات
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

فئة MergeOptions هي فئة مساعدة تتيح لك تحديد خيارات ومعاملات مختلفة لعملية الدمج، مثل نطاق الصفحة والترتيب والأمان، وما إلى ذلك.
الخطوة النهائية هي تشغيل طريقة Process لكائن Merger، مع تمرير كائن mergeOptions كمعامل.

```cs
// معالجة الدمج وحفظ الملف المدمج
pdfMerger.Process(mergeOptions);

// طباعة رسالة تأكيد
Console.WriteLine("تم دمج ملفات PDF بنجاح.");
```

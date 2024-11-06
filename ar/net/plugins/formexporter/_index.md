---
title: مصدر النموذج
type: docs
weight: 50
url: ar/net/plugins/formexpoter/
description: كيفية تصدير قيم حقول النموذج إلى ملفات CSV باستخدام إضافة Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

في هذه المقالة، سنوضح لك كيفية استخدام [إضافة مصدر النموذج](https://products.aspose.org/pdf/net/form-exporter/)، والتي يمكن أن تصدر قيم حقول النموذج من ملفات PDF إلى ملفات CSV.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 21.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض حقول النماذج

يمكنك تنزيل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لتصدير قيم حقول النماذج إلى ملفات CSV باستخدام إضافة FormExporter هي:

1. إنشاء كائن من فئة `FormExporter`
1. إنشاء كائن من فئة `FormExporterValuesToCsvOptions` وتحديد الشرط والمحدد
1.
1.
1. قم بتشغيل طريقة `Process` لكائن `FormExporter`

دعونا نرى كيفية تنفيذ هذه الخطوات في كود C#.

### الخطوة 1: إنشاء كائن من فئة FormExporter

فئة FormExporter هي الفئة الرئيسية التي توفر وظيفة تصدير قيم حقول النموذج إلى ملفات CSV. لاستخدامها، تحتاج إلى إنشاء مثيل لها باستخدام الباني الافتراضي:

```cs
// إنشاء مثيل من الإضافة FormExporter
var plugin = new FormExporter();
```

### الخطوة 2: إنشاء كائن من فئة FormExporterValuesToCsvOptions وتحديد الشرط والمحدد

فئة FormExporterValuesToCsvOptions هي فئة مساعدة تتيح لك تحديد خيارات ومعاملات مختلفة لعملية التصدير، مثل الشرط والمحدد.
### الخطوة 3: إضافة مصادر البيانات الإدخالية والمخرجات إلى كائن الخيارات

مصادر البيانات الإدخالية والمخرجات هي ملفات PDF التي تريد تصديرها منها وملف CSV الذي تريد حفظه.

```cs
// إنشاء خيارات لتصدير قيم حقول النموذج إلى CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```
مصادر البيانات الداخلة والخارجة هي ملفات PDF التي تريد تصديرها وملف CSV الذي تريد حفظه.

```cs
// إضافة ملفات الإدخال والإخراج إلى الخيارات
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### الخطوة 4: تشغيل طريقة Process لكائن FormExporter

الخطوة النهائية هي تشغيل طريقة Process لكائن FormExporter، مع تمرير كائن الخيارات كمعامل.
الخطوة النهائية هي تشغيل طريقة Process لكائن FormExporter، مع تمرير كائن الخيارات كمعامل.

```cs
// معالجة قيم حقول النموذج باستخدام الإضافة
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

سيحتوي الناتج على معلومات مثل مسارات ملف الإدخال والمخرجات.

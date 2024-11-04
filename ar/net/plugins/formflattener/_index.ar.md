---
title: مُصدّر النماذج
type: docs
weight: 60
url: /net/plugins/formflattener/
description: كيفية تسطيح حقول النماذج في ملفات PDF باستخدام إضافة Aspose.PDF FormFlattener
lastmod: "2024-01-24"
---

في هذا المقال، سنعرض لك كيفية استخدام [إضافة FormFlattener](https://products.aspose.org/pdf/net/form-flattener/)، التي يمكن أن تقوم بتسطيح حقول النماذج في ملفات PDF.

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 21.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض حقول النماذج

يمكنك تنزيل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.

## الخطوات

الخطوات الأساسية لتسطيح حقول النماذج في ملفات PDF باستخدام إضافة FormFlattener هي:

1. إنشاء كائن من الفئة FormFlattener
1. إنشاء كائن من الفئة FormFlattenAllFieldsOptions أو FormFlattenSelectedFieldsOptions، بناءً على ما إذا كنت ترغب في تسطيح جميع الحقول أو بعضها
1. تشغيل طريقة Process لكائن FormFlattener

لنرى كيفية تنفيذ هذه الخطوات في كود C#.

### الخطوة 1: إنشاء كائن من فئة FormFlattener

فئة FormFlattener هي الفئة الرئيسية التي توفر وظيفة تسطيح حقول النماذج في ملفات PDF. لاستخدامها، تحتاج إلى إنشاء نسخة منها باستخدام المنشئ الافتراضي:

```cs
// إنشاء نسخة من مكون FormFlattener
var plugin = new FormFlattener();
```

### الخطوة 2: إنشاء كائن من فئة FormFlattenAllFieldsOptions أو FormFlattenSelectedFieldsOptions، حسب رغبتك في تسطيح جميع الحقول أو بعضها

فئات FormFlattenAllFieldsOptions و FormFlattenSelectedFieldsOptions هي فئات مساعدة تتيح لك تحديد الخيارات والمعايير المختلفة لعملية التسطيح.
خيارات FormFlattenAllFieldsOptions و FormFlattenSelectedFieldsOptions هي فئات مساعدة تتيح لك تحديد خيارات ومعايير مختلفة لعملية التسطيح.

```cs
// إنشاء خيارات لتسطيح جميع الحقول
var options = new FormFlattenAllFieldsOptions();
```

لتسطيح الحقول التي تكون الإحداثية السفلية اليسرى لها أكبر من 300، يمكنك استخدام الكود التالي:

```cs
// إنشاء خيارات لتسطيح الحقول المختارة
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### الخطوة 3: إضافة مصادر البيانات الداخلية والخارجية إلى كائن الخيارات

مصادر البيانات الداخلية والخارجية هي ملفات PDF التي ترغب في تسطيحها وحفظها.
مصادر البيانات الداخلة والخارجة هي ملفات PDF التي ترغب في تسطيحها وحفظها.

```cs
// أضف مصادر البيانات الداخلة والخارجة إلى الخيارات
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### الخطوة 4: تشغيل طريقة Process لكائن FormFlattener

الخطوة النهائية هي تشغيل طريقة Process لكائن FormFlattener، مع تمرير كائن الخيارات كمعامل. ستقوم هذه الطريقة بعملية التسطيح وتعيد كائن ResultContainer، الذي يحتوي على نتائج العملية، مثل الحالة، الرسائل، مصادر البيانات الخارجة، وغيرها. يمكنك الوصول إلى النتائج باستخدام الخصائص والطرق لكلاس ResultContainer. على سبيل المثال، للحصول على النتيجة الأولى من مجموعة النتائج وطباعتها على الوحدة الطرفية، يمكنك استخدام الكود التالي:

```cs
// معالجة الخيارات والحصول على حاوية النتيجة
var resultContainer = plugin.Process(options);

// الحصول على النتيجة الأولى من حاوية النتيجة
var result = resultContainer.ResultCollection[0];

// طباعة النتيجة
Console.WriteLine(result);
```
النتيجة ستحتوي على معلومات مثل مسارات ملفات الإخراج.

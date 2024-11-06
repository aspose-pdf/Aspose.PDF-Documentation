---
title: Optimizer 
type: docs
weight: 80
url: ar/net/plugins/optimizer/
description: كيفية تحسين ومعالجة ملفات PDF باستخدام Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

في هذا الفصل، سنستكشف كيفية استخدام [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) لتحسين حجم ملفات PDF وتدويرها في تطبيقات C# الخاصة بك.
هيا نغوص في التعلم خطوة بخطوة لكيفية أداء هذه المهام.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي يحتوي على بعض حقول النماذج

## تحسين ملفات PDF

يتضمن تحسين ملف PDF تقليص حجمه وتحسين أدائه. الأجزاء التالية تظهر كيفية تحقيق هذه المهمة. إليك كيف يمكنك تحسين ملف PDF:

* إنشاء مصدر بيانات ملف جديد لملف PDF الذي سيتم إدخاله.
* إنشاء مصدر بيانات ملف جديد لملف PDF المُحسن الناتج.
* إنشاء نسخة من `OptimizeOptions`.
* إضافة مصادر البيانات الإدخال والناتج إلى خيارات التحسين.
* أضف مصادر البيانات الإدخال والإخراج إلى خيارات التحسين.
* إنشاء نموذج من `Optimizer` ومعالجة التحسين باستخدام خيارات التحسين.

```cs
// إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
var inputDataSource = new FileDataSource(inputPath);

// إنشاء مصدر بيانات ملف جديد لملف PDF المُحسَن الناتج.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// إنشاء نموذج جديد من OptimizeOptions.
var options = new OptimizeOptions();

// أضف مصادر البيانات الإدخال والإخراج إلى خيارات التحسين.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// إنشاء نموذج جديد من Optimizer.
var optimizer = new Optimizer();

// معالجة التحسين باستخدام خيارات التحسين.
optimizer.Process(options);
```

## تغيير حجم ملفات PDF

يتضمن تغيير حجم ملف PDF تغيير حجم صفحته. يوضح الكود التالي كيفية تنفيذ هذه المهمة. اتبع هذه الخطوات لتغيير حجم ملف PDF:

* إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
* إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
* إنشاء مصدر بيانات ملف جديد لملف PDF الناتج المعدل الحجم.
* إنشاء نموذج من `ResizeOptions` وتحديد حجم الصفحة المطلوب.
* إضافة مصادر البيانات الإدخال والناتج إلى خيارات التغيير الحجم.
* إنشاء نموذج من `Optimizer` ومعالجة تغيير الحجم باستخدام خيارات التغيير الحجم.

```cs
// إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
var inputDataSource = new FileDataSource("sample.pdf");

// إنشاء مصدر بيانات ملف جديد لملف PDF الناتج المعدل الحجم.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// إنشاء نموذج جديد من ResizeOptions وتحديد حجم الصفحة المطلوب.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// إضافة مصادر البيانات الإدخال والناتج إلى خيارات التغيير الحجم.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// إنشاء نموذج جديد من Optimizer.
var optimizer = new Optimizer();

// معالجة تغيير الحجم باستخدام خيارات التغيير الحجم.
optimizer.Process(opt);
```

## Rotating PDF Pages
## تدوير صفحات PDF

يتيح لك تدوير صفحات PDF تغيير اتجاه الصفحات داخل مستند PDF. إليك كيف يمكنك تدوير صفحات PDF:

* إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
* إنشاء مصدر بيانات ملف جديد لملف PDF الإخراج.
* إنشاء نسخة من `RotateOptions` وتعيين قيمة التدوير.
* إضافة مصادر البيانات للإدخال والإخراج إلى خيارات التدوير.
* إنشاء نسخة من `Optimizer` ومعالجة التدوير باستخدام خيارات التدوير.

```cs
// إنشاء مصدر بيانات ملف جديد لملف PDF الإدخال.
var inputDataSource = new FileDataSource(inputPath);

// إنشاء مصدر بيانات ملف جديد لملف PDF الإخراج المحسن.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// إنشاء نسخة جديدة من OptimizeOptions.
var opt = new RotateOptions();

// إضافة مصادر البيانات للإدخال والإخراج إلى خيارات التحسين.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// تعيين قيمة التدوير
opt.Rotation = Rotation.on180;

// إنشاء نسخة جديدة من Optimizer.
var optimizer = new Optimizer();

// معالجة التحسين باستخدام خيارات التحسين.
optimizer.Process(opt)
```
## الخاتمة

لقد تعلمت كيفية تحسين، تغيير حجم، وتدوير ملفات PDF باستخدام إضافة Aspose.PDF Optimizer في C#. قم بدمج هذه التقنيات في تطبيقاتك للتعامل مع مستندات PDF بكفاءة وفقًا لمتطلباتك.

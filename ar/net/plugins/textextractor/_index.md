---
title: استخراج النص
type: docs
weight: 140
url: ar/net/plugins/textextractor/
description: يستخرج محتوى النص من مستند PDF.
lastmod: "2024-01-24"
---

هل لديك مستند PDF تحتاج إلى [استخراج النص منه برمجيًا](https://products.aspose.org/pdf/net/text-extractor/؟ مع Aspose.PDF لـ .NET، يمكنك تحقيق هذه المهمة بسهولة باستخدام فئة TextExtractor. في هذا المقال، سنقوم بشرح الخطوات الأساسية لإنشاء تطبيق استخراج نص في .NET، بما في ذلك إنشاء كائن TextExtractor، إضافة مصدر بيانات، وتشغيل عملية استخراج النص.

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي

بالإضافة إلى ذلك، يرجى التعرف على فئة `TextExtractorOptions` ووظائفها. يمكن العثور على معلومات مفصلة في [مرجع API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

الآن، دعونا نتعمق في الكود ونستكشف كيفية استخراج النص من مستند PDF.
الآن، دعونا نغوص في الكود ونستكشف كيفية استخراج النص من مستند PDF.

## شرح الكود

يوضح الكود التالي قدرات استخراج النص. دعونا نقوم بتفصيل الخطوات الرئيسية:

### 1. إنشاء كائن TextExtractor

يبدأ الكود بإنشاء نسخة جديدة من فئة `TextExtractor`. توفر هذه الفئة طرقًا لاستخراج النص من مستندات PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. إضافة مصدر البيانات

بعد ذلك، يتم إنشاء `FileDataSource` لملف PDF الذي سيتم استخراج النص منه.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. إنشاء TextExtractorOptions

يتم إنشاء كائن `TextExtractorOptions` لتكوين عملية استخراج النص. يتم إضافة مصدر الملف إلى الخيارات.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. تشغيل عملية استخراج النص

ثم يتم استدعاء طريقة `Process` على كائن `TextExtractor`، مع تمرير الخيارات المكونة.
يتم بعد ذلك استدعاء الطريقة `Process` على الكائن `TextExtractor`، مع تمرير الخيارات المُعدة.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

يمكنك رؤية الكود الكامل أدناه:

``````cs
using Aspose.Pdf.Plugins;
// ...

// إنشاء نموذج جديد من TextExtractor.
using TextExtractor extractor = new();

// إنشاء FileDataSource لملف PDF الإدخال.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// إنشاء TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// معالجة استخراج النص.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// طباعة النص المستخرج.
Console.WriteLine(results[0]);

```

---
title: مستخرج الصور
type: docs
weight: 80
url: /net/plugins/imageextractor/
description: استخراج الصور من ملفات PDF بسهولة مع إضافة ImageExtractor
lastmod: "2024-01-24"
draft: false
---

إذا كنت بحاجة من قبل لاستخراج الصور من ملف PDF باستخدام .NET، يوفر Aspose.PDF لـ .NET حلاً قويًا وبسيطًا. في هذا الدليل، سنتعرف على الخطوات الأساسية لإنشاء كائن، وإضافة مصدر بيانات، وتشغيل طريقة المعالجة باستخدام [مستخرج الصور Aspose.PDF](https://products.aspose.org/pdf/net/image-extractor/).

## المتطلبات الأساسية

ستحتاج إلى الآتي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 21.1 أو أحدث
* ملف PDF نموذجي

يمكنك تحميل مكتبة Aspose.PDF لـ .NET من الموقع الرسمي أو تثبيتها باستخدام مدير حزم NuGet في Visual Studio.
الآن، دعونا نغوص في الكود ونتعلم كيفية استخدام إضافة ImageExtractor.

## الخطوات

يوضح الكود المقدم استخدام إضافة `ImageExtractor` لاستخراج الصور من ملف PDF.
يوضح الكود المقدم استخدام إضافة `ImageExtractor` لاستخراج الصور من ملف PDF.

### 1. إنشاء كائن (ImageExtractor)

الخطوة الأولى تتضمن إنشاء مثيل لإضافة `ImageExtractor`. يتم تحقيق ذلك باستخدام الكود التالي:

```csharp
using var plugin = new ImageExtractor();
```

هنا، يضمن الأمر `using` التخلص الصحيح من الموارد عند اكتمال العملية.

### 2. إضافة مصدر البيانات

بعد ذلك، يتم إنشاء مثيل لفئة `ImageExtractorOptions` لتكوين عملية استخراج الصور. يتم إضافة مسار الملف الإدخالي إلى الخيارات باستخدام طريقة `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

تأكد من استبدال `"C:\Samples\"` و `"sample.pdf"` بالمسار واسم الملف المناسب لملف PDF الخاص بك.

### 3. تشغيل طريقة المعالجة

الخطوة الأخيرة هي معالجة استخراج الصور باستخدام الإضافة والخيارات:

```csharp
```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

تُخزن النتيجة في `resultContainer`، والتي تحتوي على الصورة/الصور المستخرجة.

### 4. التعامل مع الصور المستخرجة

بعد تشغيل العملية، يمكنك استرجاع الصورة/الصور المستخرجة من حاوية النتائج. يوضح الكود أدناه كيفية حفظ الصورة المستخرجة الأولى في موقع مؤقت:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

تأكد من تخصيص مسار الوجهة واسم الملف حسب تفضيلاتك.

يمكنك نسخ المثال الكامل أدناه:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // يوضح استخدام مكون ImageExtractor الإضافي لاستخراج الصور من ملف PDF.
    // </summary>
    internal static void Run()
    {
        // إنشاء نسخة من مكون ImageExtractor الإضافي.
        using var plugin = new ImageExtractor();

        // إنشاء نسخة من فئة ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // إضافة مسار الملف الإدخالي إلى الخيارات.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // معالجة استخراج الصورة باستخدام المكون الإضافي والخيارات.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // الحصول على الصورة المستخرجة من حاوية النتائج.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```


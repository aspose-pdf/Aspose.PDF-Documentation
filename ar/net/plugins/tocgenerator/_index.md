---
title: ToC Generator
type: docs
weight: 150
url: /ar/net/plugins/tocgenerator/
description: يُنشئ جدول محتويات باستخدام مولد جدول المحتويات Aspose.PDF لـ .NET
lastmod: "2024-01-24"
draft: false
---

هل تريد تعزيز مستندات PDF الخاصة بك بإضافة [جدول المحتويات (TOC)](https://products.aspose.org/pdf/net/toc-generator/) بشكل ديناميكي؟ يوفر Aspose.PDF لـ .NET فئة `TocGenerator` القوية التي تتيح لك إنشاء TOCs بسهولة. في هذا الدليل، سنمر بالخطوات الأساسية لإنشاء TOC في مستند PDF باستخدام Aspose.PDF، مع تغطية إنشاء كائن `TocGenerator`، وإضافة مسارات الإدخال/الخروج، وتشغيل عملية إنشاء TOC.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي

بالإضافة إلى ذلك، يُرجى التعرف على فئة `TocOptions` ووظائفها. يمكن العثور على معلومات مفصلة في [مرجع API Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

الآن، دعونا نغوص في الكود ونستكشف كيفية إنشاء جدول المحتويات لمستند PDF الخاص بك.
الآن، دعونا نغوص في الكود ونستكشف كيفية إنشاء جدول المحتويات لمستند PDF الخاص بك.

## شرح الكود

سنستخدم فئة `TocGeneratorDemo` مع طريقة `Run` لنوضح كيفية إنشاء جدول المحتويات. دعونا نفصل الخطوات الرئيسية:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // يشغل عرض توليد جدول المحتويات.
        internal static void Run()
        {
            // إنشاء نموذج جديد لفئة TocGenerator.
            TocGenerator generator = new();

            // إنشاء نموذج جديد لفئة TocOptions.
            TocOptions options = new();
            // إضافة مسارات الإدخال والإخراج إلى TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // معالجة توليد جدول المحتويات والحصول على حاوية النتائج.
            var resultContainer = generator.Process(options);

            // الحصول على النتائج من حاوية النتائج.
            var result = resultContainer.ResultCollection[0];

            // طباعة النتيجة إلى وحدة التحكم.
            Console.WriteLine(result);
        }
    }
}
```
### 1. إنشاء كائن TocGenerator

يبدأ الكود بإنشاء نموذج جديد من الفئة `TocGenerator`. توفر هذه الفئة طرقًا لإنشاء جداول المحتويات لمستندات PDF.

```csharp
TocGenerator generator = new();
```

### 2. إنشاء TocOptions

بعد ذلك، يتم إنشاء نموذج جديد من الفئة `TocOptions` لتكوين عملية إنشاء جدول المحتويات. يتم إضافة مسارات الملفات الواردة والناتجة إلى الخيارات.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. تشغيل عملية إنشاء جدول المحتويات

ثم يتم استدعاء الطريقة `Process` على كائن `TocGenerator`، مع تمرير الخيارات المكونة. يحتوي حاوية النتائج على جدول المحتويات المُنشأ، ويتم طباعتها في وحدة التحكم.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```

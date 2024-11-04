---
title: محول PNG
type: docs
weight: 110
url: /net/plugins/png/
description: تحويل مستندات PDF إلى صور PNG باستخدام إضافة Aspose.PDF PNG
lastmod: "2024-01-24"
---

إذا كنت تبحث عن [تحويل مستندات PDF إلى صور PNG](https://products.aspose.org/pdf/net/png-converter/) باستخدام .NET، فإن Aspose.PDF لـ .NET يوفر حلاً قوياً. في هذه المقالة، سنتناول الخطوات الأساسية لإنشاء كائن، إضافة مصدر بيانات، وتشغيل طريقة العملية باستخدام مكتبة Aspose.PDF.

## الشروط المسبقة

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.1 أو أحدث
* ملف PDF نموذجي

## شرح الكود

الكود أدناه يوضح عرض توضيحي لتحويل PNG باستخدام إضافة Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// إنشاء نسخة جديدة من فئة PngOptions.
var convertorOptions = new PngOptions();

// إضافة مسارات الإدخال والإخراج إلى PngOptions.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// تعيين دقة الإخراج إلى 300 DPI.
convertorOptions.OutputResolution = 300;

// إنشاء نسخة جديدة من فئة Png.
Png converter = new ();

// معالجة تحويل PNG والحصول على حاوية النتائج.
ResultContainer resultContainer = converter.Process(convertorOptions);

// طباعة النتيجة إلى وحدة التحكم.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
لنقم بتوضيح الخطوات الرئيسية:

1. **إنشاء كائن (PngOptions و Png)**

   يبدأ الكود بإنشاء مثال على فئة `PngOptions` لتكوين تحويل PNG. بالإضافة إلى ذلك، يتم إنشاء مثال على فئة `Png` لمزيد من المعالجة.

2. **إضافة مصدر البيانات**

   يتم إضافة مسار ملف PDF الإدخال إلى `PngOptions` باستخدام طريقة `AddInput`. بالمثل، يتم إضافة مسار الخروج لصور PNG باستخدام طريقة `AddOutput`.

3. **تعيين دقة الخروج**

   يقوم الكود بتعيين دقة الخروج إلى 300 DPI باستخدام خاصية `OutputResolution` لفئة `PngOptions`.

4. **تشغيل طريقة العملية**

   يتم بدء تحويل PNG عن طريق استدعاء طريقة `Process` على فئة `Png`، مع تمرير `PngOptions` المكونة. يتم تخزين النتيجة في `resultContainer`.

5. **التعامل مع النتيجة**

   يطبع الكود النتيجة إلى وحدة التحكم، مع عرض مسار الملف المحول.

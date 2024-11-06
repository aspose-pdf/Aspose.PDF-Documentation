---
title: مولد الجداول
type: docs
weight: 130
url: ar/net/plugins/tablegenerator/
description: يتيح إضافة/إدراج جدول في رقم الصفحة المحدد للمستند PDF.
lastmod: "2024-01-24"
draft: false
---

هل تحتاج إلى إنشاء جداول ديناميكية وجذابة بصريًا في مستندات PDF الخاصة بك باستخدام .NET؟ يوفر Aspose.PDF لـ .NET فئة TableGenerator قوية تبسط العملية. في هذا الفصل، سنتناول الخطوات لتوليد الجداول في مستند PDF باستخدام [مولد الجداول Aspose.PDF](https://products.aspose.org/pdf/net/table-generator/)، من إنشاء مستند تجريبي إلى توليد الجداول بفئة TableGenerator.
لنغوص في تعلم كيفية توليد الجداول خطوة بخطوة.

## المتطلبات الأساسية

ستحتاج إلى ما يلي:

* Visual Studio 2019 أو أحدث
* Aspose.PDF لـ .NET 24.3 أو أحدث
* ملف PDF نموذجي

## إنشاء مستند تجريبي

قبل أن نبدأ في توليد الجداول، دعونا نقوم بإنشاء مستند تجريبي بصفحات فارغة حيث سيتم إدراج جداولنا.
قبل أن نبدأ في إنشاء الجداول، دعنا نقوم بإنشاء مستند تجريبي بصفحات فارغة حيث سيتم إدراج الجداول.

* إنشاء مستند PDF جديد.
* إضافة صفحات فارغة إلى المستند.
* حفظ المستند في الملف المحدد.

```cs
// <summary>
// يقوم بإنشاء مستند تجريبي بصفحات فارغة.
//
// المعاملات:
// - fileName: المسار واسم الملف الناتج.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // إنشاء مستند PDF جديد.
    var document = new Aspose.Pdf.Document();

    // إضافة أربع صفحات فارغة إلى المستند.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // حفظ المستند في الملف المحدد.
    document.Save(fileName);
}
```

## إنشاء الجداول

بمجرد أن يكون مستندنا التجريبي جاهزًا، يمكننا البدء في إنشاء الجداول باستخدام فئة `TableGenerator`. يوضح الجزء التالي كيفية إنشاء جداول بأنواع وخيارات تنسيق مختلفة. إليك كيفية إنشاء الجداول:

* إنشاء نموذج جديد من فئة `TableGenerator`.
* قم بإنشاء نموذج جديد من فئة `TableGenerator`.
* قم بإنشاء خيارات الجدول وحدد مصادر بيانات الملفات الواردة والصادرة.
* أضف الجداول مع الصفوف والخلايا إلى الخيارات، مع تحديد المحتوى والتنسيق.
* قم بمعالجة توليد الجدول باستخدام طريقة `Process` واحصل على حاوية النتيجة.

### إنشاء الجداول

لإنشاء جدول باستخدام Aspose.PDF، اتبع الخطوات التالية:

```cs
// قم بإنشاء نموذج جديد من فئة TableGenerator.
var generator = new TableGenerator();

// قم بإنشاء خيارات الجدول وأضف جداول تجريبية.
var options = new TableOptions();

// أضف مصادر بيانات الملفات الواردة والصادرة إلى الخيارات.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// أضف الجدول الأول إلى الخيارات.
options
    .InsertPageAfter(1)
    .AddTable()
```

في الكود أعلاه، نقوم بإنشاء نموذج من `TableOptions` ونحدد مصادر بيانات الملفات الواردة والصادرة لمستند PDF.
في الكود أعلاه، نقوم بإنشاء نموذج من `TableOptions` ونحدد مصادر بيانات الملفات الداخلة والخارجة لمستند PDF.

### إضافة المحتوى إلى الجداول

بمجرد إنشاء الجدول، يمكنك تعبئته بالصفوف والخلايا التي تحتوي على أنواع مختلفة من المحتوى، مثل النصوص، HTML، الصور، إلخ. إليك كيفية إضافة محتوى إلى جدول:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Header 1</h1>")) // إضافة محتوى HTML إلى الخلية.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"));
```

في هذا المثال، نضيف صفًا إلى الجدول ونملأه بالخلايا التي تحتوي على أجزاء HTML التي تمثل العناوين.

طرق مفيدة:

* **InsertPageAfter**: يقوم بإدراج صفحة بعد رقم الصفحة المحدد.
* **InsertPageBefore**: يقوم بإدراج صفحة قبل رقم الصفحة المحدد.
* **AddTable**: يضيف جدولًا إلى المستند.
* **AddTable**: إضافة جدول إلى المستند.
* **AddRow**: إضافة صف إلى الجدول.
* **AddCell**: إضافة خلايا إلى الصف.
* **AddParagraph**: إضافة محتوى إلى الخلية.

يمكنك إضافة أنواع المحتوى التالية كفقرة:

* **HtmlFragment** - محتوى يعتمد على ترميز HTML
* **TeXFragment** - محتوى يعتمد على ترميز TeX/LaTeX
* **TextFragment** - محتوى نصي بسيط
* **Image** - الرسومات

## تنفيذ توليد الجدول

بعد إضافة المحتوى، يمكننا البدء في إنشاء الجدول.

```cs
// معالجة توليد الجدول والحصول على حاوية النتائج.
var resultContainer = generator.Process(options);

// طباعة عدد النتائج في مجموعة النتائج.            
Console.WriteLine(resultContainer.ResultCollection.Count);
```

تقوم الطريقة `Process` بتوليد الجدول. يمكن أيضاً إدراج هذه الطريقة داخل try-catch لمعالجة الأخطاء.

يمكنك مشاهدة الكود الكامل للمثال أدناه:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // يمثل فئة توضح استخدام توليد الجدول في Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // يشغل عرض توليد الجدول.
        // </summary>
        internal static void Run()
        {
            // إنشاء مستند تجريبي وتوليد جداول.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // ينشئ مستند تجريبي مع أربع صفحات فارغة.
        //
        // المعاملات:
        // - fileName: مسار واسم الملف الناتج.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // إنشاء مستند PDF جديد.
            var document = new Aspose.Pdf.Document();

            // إضافة أربع صفحات فارغة إلى المستند.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // حفظ المستند إلى الملف المحدد.
            document.Save(fileName);
        }

        // <summary>
        // يولد جداول باستخدام فئة TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // إنشاء نموذج جديد لفئة TableGenerator.
            var generator = new TableGenerator();

            // إنشاء خيارات الجدول وإضافة جداول تجريبية.
            var options = new TableOptions();

            // إضافة مصادر بيانات الملفات الداخلية والخارجية إلى الخيارات.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // إضافة الجدول الأول إلى الخيارات.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Header 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Header 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Header 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small The equation $E=mc^2$, discovered in 1905 by Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 1a"))
                            .AddParagraph(new TextFragment("Cell 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Cell 3 3"));

            // إضافة الجدول الثاني إلى الخيارات.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Header 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // معالجة توليد الجدول والحصول على حاوية النتائج.
            var resultContainer = generator.Process(options);

            // طباعة عدد النتائج في مجموعة النتائج.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```


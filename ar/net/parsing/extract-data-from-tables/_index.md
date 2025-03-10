---
title: استخراج البيانات من جدول في PDF باستخدام C#
linktitle: استخراج البيانات من الجدول
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج البيانات الجدولية من PDF باستخدام Aspose.PDF for .NET في C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from Table in PDF with C#",
    "alternativeHeadline": "Effortlessly Extract Tables from PDFs Using C#",
    "abstract": "اكتشف القدرة القوية على استخراج البيانات الجدولية من مستندات PDF باستخدام Aspose.PDF for .NET في C#. تسهل هذه الميزة عملية استرجاع ومعالجة الجداول من خلال السماح للمستخدمين بالوصول بسلاسة إلى الخلايا الفردية وتخزين البيانات المستخرجة في تنسيقات مثل CSV و Excel، مما يعزز إمكانية الوصول إلى البيانات وقابليتها للاستخدام",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "695",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-data-from-table-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-table-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج الجداول من PDF برمجيًا

استخراج الجداول من PDFs ليس مهمة بسيطة لأن الجدول يمكن أن يتم إنشاؤه بطرق مختلفة.

Aspose.PDF for .NET لديها أداة لتسهيل استرجاع الجداول. لاستخراج بيانات الجدول، يجب عليك تنفيذ الخطوات التالية:

1. فتح المستند - إنشاء كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إنشاء كائن [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. تحديد الصفحات التي سيتم تحليلها وتطبيق [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/visit) على الصفحات المطلوبة. سيتم مسح البيانات الجدولية وتخزين النتيجة في [TableList](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/properties/tablelist).
1. `TableList` هو قائمة من [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). للحصول على البيانات، قم بالتكرار عبر `TableList` وتعامل مع [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) و [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist).
1. كل [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) يحتوي على مجموعة من [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). يمكنك معالجتها لأغراضك الخاصة.

تعمل الشيفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تظهر المثال التالي استخراج الجدول من جميع الصفحات:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {                    
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.TableAbsorber absorber = new Aspose.Pdf.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                Console.WriteLine("Table");
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {                                 
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            Console.Write($"{sb.ToString()}|");
                        }                           
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## استخراج الجدول في منطقة محددة من صفحة PDF

كل جدول تم امتصاصه لديه خاصية [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) التي تصف موقع الجدول على الصفحة.

إذا كنت بحاجة إلى استخراج الجداول الموجودة في منطقة محددة، يجب عليك العمل مع إحداثيات محددة.

تعمل الشيفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تظهر المثال التالي كيفية استخراج الجدول المميز بتعليق مربع:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractMarkedTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    { 
        var page = document.Pages[1];
        var squareAnnotation =
            page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
            as Aspose.Pdf.Annotations.SquareAnnotation;


        var absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);

        foreach (var table in absorber.TableList)
        {
            var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
            (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
            (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
            (squareAnnotation.Rect.URY > table.Rectangle.URY);

            if (isInRegion)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            var text = sb.ToString();
                            Console.Write($"{text}|");
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## استخراج بيانات الجدول من PDF وتخزينها في ملف CSV

تظهر المثال التالي كيفية استخراج الجدول وتخزينه كملف CSV.
لرؤية كيفية تحويل PDF إلى جدول بيانات Excel، يرجى الرجوع إلى مقال [تحويل PDF إلى Excel](/pdf/ar/net/convert-pdf-to-excel/).

تعمل الشيفرة البرمجية التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableSaveExcel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSave Option object
        Aspose.Pdf.ExcelSaveOptions excelSave = new Aspose.Pdf.ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

        // Save the output in XLS format
        document.Save(dataDir + "ExtractTableSaveXLS_out.xlsx", excelSave);
    }
}
```
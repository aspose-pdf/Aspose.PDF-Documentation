---
title: إدراج صفحات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ar/net/insert-pdf-pages/
description: يشرح هذا القسم كيفية إدراج صفحات PDF باستخدام واجهات Aspose.PDF من خلال فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "قم بتحسين إدارة PDF الخاصة بك مع الميزة الجديدة التي تسمح للمستخدمين بإدراج صفحات محددة من PDF واحد إلى آخر باستخدام فئة PdfFileEditor. تدعم هذه الوظيفة إدراج الصفحات بناءً على النطاق والمصفوفة، مما يعزز كفاءة سير العمل من خلال دمج المستندات بسلاسة عبر مسارات الملفات أو التدفقات",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إدراج صفحات PDF بين رقمين باستخدام مسارات الملفات

يمكن إدراج نطاق معين من الصفحات من PDF واحد إلى آخر باستخدام [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). للقيام بذلك، تحتاج إلى ملف PDF مدخل تريد إدراج الصفحات فيه، وملف منفذ تحتاج الصفحات منه للإدراج، وموقع حيث يجب إدراج الصفحات، ونطاق من الصفحات من ملف المنفذ التي يجب إدراجها في ملف PDF المدخل. يتم تحديد هذا النطاق باستخدام معلمات الصفحة البداية والصفحة النهاية. أخيرًا، يتم حفظ ملف PDF الناتج مع النطاق المحدد من الصفحات المدخلة في الملف المدخل. يوضح لك مقتطف الكود التالي كيفية إدراج صفحات PDF بين رقمين باستخدام تدفقات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## إدراج مصفوفة من صفحات PDF باستخدام مسارات الملفات

إذا كنت ترغب في إدراج بعض الصفحات المحددة في ملف PDF آخر، يمكنك استخدام تحميل زائد من طريقة [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) التي تتطلب مصفوفة صحيحة من الصفحات. في هذه المصفوفة، يمكنك تحديد الصفحات المحددة التي ترغب في إدراجها في ملف PDF المدخل. للقيام بذلك، تحتاج إلى ملف PDF مدخل تريد إدراج الصفحات فيه، وملف منفذ تحتاج الصفحات منه للإدراج، وموقع حيث يجب إدراج الصفحات، ومصفوفة صحيحة من الصفحات من ملف المنفذ التي يجب إدراجها في ملف PDF المدخل. تحتوي هذه المصفوفة على قائمة من الصفحات المحددة التي ترغب في إدراجها في ملف PDF المدخل. أخيرًا، يتم حفظ ملف PDF الناتج مع المصفوفة المحددة من الصفحات المدخلة في الملف المدخل. يوضح لك مقتطف الكود التالي كيفية إدراج مصفوفة من صفحات PDF باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## إدراج صفحات PDF بين رقمين باستخدام التدفقات

إذا كنت ترغب في إدراج نطاق الصفحات باستخدام التدفقات، تحتاج فقط إلى استخدام تحميل زائد مناسب من طريقة [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). للقيام بذلك، تحتاج إلى تدفق PDF مدخل تريد إدراج الصفحات فيه، وتدفق منفذ تحتاج الصفحات منه للإدراج، وموقع حيث يجب إدراج الصفحات، ونطاق من الصفحات من التدفق المنفذ التي يجب إدراجها في تدفق PDF المدخل. يتم تحديد هذا النطاق باستخدام معلمات الصفحة البداية والصفحة النهاية. أخيرًا، يتم حفظ تدفق PDF الناتج مع النطاق المحدد من الصفحات المدخلة في التدفق المدخل. يوضح لك مقتطف الكود التالي كيفية إدراج صفحات PDF بين رقمين باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## إدراج مصفوفة من صفحات PDF باستخدام التدفقات

يمكنك أيضًا إدراج مصفوفة من الصفحات في ملف PDF آخر باستخدام التدفقات بمساعدة تحميل زائد مناسب من طريقة Insert التي تتطلب مصفوفة صحيحة من الصفحات. في هذه المصفوفة، يمكنك تحديد الصفحات المحددة التي ترغب في إدراجها في تدفق PDF المدخل. للقيام بذلك، تحتاج إلى تدفق PDF مدخل تريد إدراج الصفحات فيه، وتدفق منفذ تحتاج الصفحات منه للإدراج، وموقع حيث يجب إدراج الصفحات، ومصفوفة صحيحة من الصفحات من التدفق المنفذ التي يجب إدراجها في ملف PDF المدخل. تحتوي هذه المصفوفة على قائمة من الصفحات المحددة التي ترغب في إدراجها في تدفق PDF المدخل. أخيرًا، يتم حفظ تدفق PDF الناتج مع المصفوفة المحددة من الصفحات المدخلة في الملف المدخل. يوضح لك مقتطف الكود التالي كيفية إدراج مصفوفة من صفحات PDF باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```
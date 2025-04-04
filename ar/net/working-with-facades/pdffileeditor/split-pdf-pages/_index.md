---
title: تقسيم صفحات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/split-pdf-pages/
description: يشرح هذا القسم كيفية تقسيم صفحات PDF باستخدام Aspose.PDF Facades من خلال استخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "تتيح ميزة تقسيم صفحات PDF الجديدة في Aspose.PDF for .NET للمستخدمين تقسيم مستندات PDF بكفاءة إلى أقسام مختلفة باستخدام فئة PdfFileEditor. تدعم هذه الوظيفة تقسيم الصفحات من الصفحة الأولى إلى صفحة محددة، وتقسيمها إلى مجموعات كبيرة، وحتى عزل الصفحات الفردية، كل ذلك من خلال مسارات الملفات أو التدفقات، مما يوفر خيارات متعددة لمعالجة PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تقسيم صفحات PDF من البداية باستخدام مسارات الملفات

تتيح لك طريقة [SplitFromFirst](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم ملف PDF بدءًا من الصفحة الأولى وانتهاءً برقم الصفحة المحدد. إذا كنت ترغب في معالجة ملفات PDF من القرص، يمكنك تمرير مسارات الملفات لملفات PDF المدخلة والمخرجة إلى هذه الطريقة. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF من البداية باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## تقسيم صفحات PDF من البداية باستخدام تدفقات الملفات

تتيح لك طريقة [SplitFromFirst](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم ملف PDF بدءًا من الصفحة الأولى وانتهاءً برقم الصفحة المحدد. إذا كنت ترغب في معالجة ملفات PDF من التدفقات، يمكنك تمرير تدفقات PDF المدخلة والمخرجة إلى هذه الطريقة. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF من البداية باستخدام تدفقات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## تقسيم صفحات PDF إلى مجموعات كبيرة باستخدام مسارات الملفات

تتيح لك طريقة [SplitToBulks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم ملف PDF إلى مجموعات متعددة من الصفحات. في هذا المثال، نحتاج إلى مجموعتين من الصفحات (1، 2) و(5، 6). إذا كنت ترغب في الوصول إلى ملف PDF من القرص، تحتاج إلى تمرير ملف PDF المدخل كمسار ملف. ترجع هذه الطريقة مصفوفة من MemoryStream. يمكنك التكرار عبر هذه المصفوفة وحفظ مجموعات الصفحات الفردية كملفات منفصلة. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF إلى مجموعات كبيرة باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## تقسيم صفحات PDF إلى مجموعات كبيرة باستخدام التدفقات

تتيح لك طريقة [SplitToBulks](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم ملف PDF إلى مجموعات متعددة من الصفحات. في هذا المثال، نحتاج إلى مجموعتين من الصفحات (1، 2) و(5، 6). يمكنك تمرير تدفق إلى هذه الطريقة بدلاً من الوصول إلى الملف من القرص. ترجع هذه الطريقة مصفوفة من MemoryStream. يمكنك التكرار عبر هذه المصفوفة وحفظ مجموعات الصفحات الفردية كملفات منفصلة. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF إلى مجموعات كبيرة باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## تقسيم صفحات PDF إلى النهاية باستخدام مسارات الملفات

تتيح لك طريقة [SplitToEnd](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم PDF من رقم الصفحة المحدد إلى نهاية ملف PDF وحفظه كملف PDF جديد. للقيام بذلك، باستخدام مسارات الملفات، تحتاج إلى تمرير مسارات الملفات المدخلة والمخرجة ورقم الصفحة التي يجب أن يبدأ منها التقسيم. سيتم حفظ ملف PDF الناتج على القرص. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF إلى النهاية باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## تقسيم صفحات PDF إلى النهاية باستخدام التدفقات

تتيح لك طريقة [SplitToEnd](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تقسيم PDF من رقم الصفحة المحدد إلى نهاية ملف PDF وحفظه كملف PDF جديد. للقيام بذلك، باستخدام التدفقات، تحتاج إلى تمرير التدفقات المدخلة والمخرجة ورقم الصفحة التي يجب أن يبدأ منها التقسيم. سيتم حفظ ملف PDF الناتج إلى تدفق المخرجات. يوضح لك مقتطف الكود التالي كيفية تقسيم صفحات PDF إلى النهاية باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## تقسيم PDF إلى صفحات فردية باستخدام مسارات الملفات

{{% alert color="primary" %}}

يمكنك محاولة تقسيم مستند PDF وعرض النتائج عبر الإنترنت على هذا الرابط:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

لتقسيم ملف PDF إلى صفحات فردية، تحتاج إلى تمرير PDF كمسار ملف إلى طريقة [SplitToPages](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). ستعيد هذه الطريقة مصفوفة من MemoryStream تحتوي على الصفحات الفردية من ملف PDF. يمكنك التكرار عبر هذه المصفوفة من MemoryStream وحفظ الصفحات الفردية كملفات PDF فردية على القرص. يوضح لك مقتطف الكود التالي كيفية تقسيم PDF إلى صفحات فردية باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## تقسيم PDF إلى صفحات فردية باستخدام التدفقات

لتقسيم ملف PDF إلى صفحات فردية، تحتاج إلى تمرير PDF كتدفق إلى طريقة [SplitToPages](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). ستعيد هذه الطريقة مصفوفة من MemoryStream تحتوي على الصفحات الفردية من ملف PDF. يمكنك التكرار عبر هذه المصفوفة من MemoryStream وحفظ الصفحات الفردية كملفات PDF فردية على القرص، أو يمكنك الاحتفاظ بهذه الصفحات الفردية في تدفق الذاكرة لاستخدامها لاحقًا في تطبيقك. يوضح لك مقتطف الكود التالي كيفية تقسيم PDF إلى صفحات فردية باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```
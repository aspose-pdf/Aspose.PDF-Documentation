---
title: جعل NUp من ملفات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /ar/net/make-nup-of-pdf-files/
description: يوضح هذا المقال كيفية جعل NUp من ملفات PDF باستخدام واجهات Aspose.PDF من خلال استخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "تتيح ميزة NUp في Aspose.PDF for .NET للمستخدمين دمج عدة ملفات PDF بكفاءة في مستند إخراج واحد، مع تخصيص حجم الصفحة وتكوينات التخطيط. تدعم هذه الوظيفة كل من مسارات الملفات والتدفقات، مما يمكّن من دمج مرن في سير العمل المختلفة مع تحسين عرض المستند.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## جعل NUp من PDF باستخدام مسارات الملفات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من ملف PDF المدخل وحفظه في ملف PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية جعل NUP باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## جعل NUp باستخدام حجم الصفحة ومسارات الملفات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من ملف PDF المدخل وحفظه في ملف PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لملف PDF الناتج باستخدام هذه النسخة الزائدة. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام حجم الصفحة ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## جعل NUp من PDF باستخدام حجم الصفحة والقيم الأفقية والعمودية ومسارات الملفات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من ملف PDF المدخل وحفظه في ملف PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لملف PDF الناتج وعدد الصفحات الأفقية والعمودية على كل صفحة ناتجة باستخدام هذه النسخة الزائدة. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام حجم الصفحة والقيم الأفقية والعمودية ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## جعل NUp من PDF باستخدام مصفوفة من ملفات PDF ومسارات الملفات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من مصفوفة من ملفات PDF المدخلة وحفظها في ملف PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام مصفوفة من ملفات PDF ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## جعل NUp من PDF باستخدام التدفقات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام التدفقات بدلاً من مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## جعل NUp من PDF باستخدام حجم الصفحة والتدفقات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام التدفقات بدلاً من مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لتدفق PDF الناتج باستخدام هذه النسخة الزائدة. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام حجم الصفحة والتدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## جعل NUp من PDF باستخدام حجم الصفحة والقيم الأفقية والعمودية والتدفقات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام التدفقات بدلاً من مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لتدفق PDF الناتج وعدد الصفحات الأفقية والعمودية على كل صفحة ناتجة باستخدام هذه النسخة الزائدة. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام حجم الصفحة والقيم الأفقية والعمودية والتدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## جعل NUp من PDF باستخدام مصفوفة من ملفات PDF والتدفقات

[MakeNUp](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) طريقة من فئة [PdfFileEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileeditor) تتيح لك جعل NUp من مصفوفة من تدفقات PDF المدخلة وحفظها في تدفق PDF الناتج. تتيح لك هذه النسخة الزائدة جعل NUp باستخدام التدفقات بدلاً من مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية جعل NUp باستخدام مصفوفة من ملفات PDF باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```
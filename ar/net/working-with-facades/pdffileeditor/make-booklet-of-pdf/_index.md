---
title: إنشاء كتيب من PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/make-booklet-of-pdf/
description: يشرح هذا القسم كيفية إنشاء كتيب من PDF باستخدام Aspose.PDF Facades من خلال استخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "تتيح ميزة إنشاء كتيب من PDF في Aspose.PDF للمستخدمين إنشاء كتيبات من ملفات PDF بسهولة باستخدام فئة PdfFileEditor. تدعم هذه الوظيفة كل من مسارات الملفات والتدفقات، مما يمكّن من تخصيص أحجام الصفحات وتحديد الصفحات اليسرى واليمنى لتحسين التحكم في المخرجات. هذه الأداة القوية تبسط عملية إنشاء الكتيبات، مما يجعلها موردًا أساسيًا لمعالجة PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## إنشاء كتيب من PDF باستخدام مسارات الملفات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من ملف PDF المدخل وحفظه في ملف PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## إنشاء كتيب من PDF باستخدام حجم الصفحة ومسارات الملفات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من ملف PDF المدخل وحفظه في ملف PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لملف PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام حجم الصفحة ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## إنشاء كتيب من PDF باستخدام حجم الصفحة، والصفحات اليسرى واليمنى المحددة، ومسارات الملفات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من ملف PDF المدخل وحفظه في ملف PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لملف PDF الناتج وتحديد صفحات معينة للجانب الأيسر والأيمن من ملف PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام حجم الصفحة، والصفحات اليسرى واليمنى المحددة، ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## إنشاء كتيب من PDF باستخدام الصفحات اليسرى واليمنى المحددة، ومسارات الملفات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من ملف PDF المدخل وحفظه في ملف PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام مسارات الملفات. يمكنك أيضًا تحديد صفحات معينة للجانب الأيسر والأيمن من ملف PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام الصفحات اليسرى واليمنى المحددة ومسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## إنشاء كتيب من PDF باستخدام التدفقات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من تدفق PDF المدخل وحفظه في تدفقات PDF الناتجة. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام التدفقات بدلاً من مسارات الملفات. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## إنشاء كتيب من PDF باستخدام حجم الصفحة والتدفقات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام التدفقات بدلاً من مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لتدفق PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام حجم الصفحة والتدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## إنشاء كتيب من PDF باستخدام حجم الصفحة، والصفحات اليسرى واليمنى المحددة، والتدفقات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام التدفقات بدلاً من مسارات الملفات. يمكنك أيضًا تعيين حجم الصفحة لملف PDF الناتج وتحديد صفحات معينة للجانب الأيسر والأيمن من تدفق PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام حجم الصفحة، والصفحات اليسرى واليمنى المحددة، والتدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## إنشاء كتيب من PDF باستخدام الصفحات اليسرى واليمنى المحددة، والتدفقات

تتيح لك طريقة [MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) إنشاء كتيب من تدفق PDF المدخل وحفظه في تدفق PDF الناتج. يسمح لك هذا التحميل الزائد بإنشاء كتيب باستخدام التدفقات بدلاً من مسارات الملفات. يمكنك أيضًا تحديد صفحات معينة للجانب الأيسر والأيمن من تدفق PDF الناتج مع هذا التحميل الزائد. يوضح لك مقتطف الكود التالي كيفية إنشاء كتيب باستخدام الصفحات اليسرى واليمنى المحددة والتدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```
---
title: استخراج صفحات PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/extract-pdf-pages/
description: يشرح هذا القسم كيفية استخراج صفحات PDF باستخدام Aspose.PDF Facades من خلال فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "تتيح ميزة استخراج صفحات PDF في Aspose.PDF for .NET Facades للمستخدمين قدرات محسّنة لاستخراج الصفحات بشكل انتقائي من مستندات PDF. من خلال استخدام فئة PdfFileEditor، يمكن للمستخدمين استخراج نطاق محدد أو مجموعة من الصفحات عبر مسارات الملفات أو التدفقات، مما يجعل معالجة المستندات أكثر سلاسة ومرونة. هذه الوظيفة مفيدة بشكل خاص للمستخدمين الذين يتطلعون إلى تخصيص محتوى PDF الخاص بهم دون تغيير الملفات الأصلية.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات

تتيح لك طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) استخراج نطاق محدد من الصفحات من ملف PDF. يسمح لك هذا التحميل الزائد باستخراج الصفحات أثناء معالجة ملفات PDF من القرص. يتطلب هذا التحميل الزائد المعلمات التالية: مسار ملف الإدخال، الصفحة الأولى، الصفحة الأخيرة، ومسار ملف الإخراج. سيتم استخراج الصفحات من الصفحة الأولى إلى الصفحة الأخيرة وسيتم حفظ الإخراج على القرص. يوضح لك مقتطف الكود التالي كيفية استخراج صفحات PDF بين رقمين باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## استخراج مصفوفة من صفحات PDF باستخدام مسارات الملفات

إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة من صفحات معينة، فإن طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. يأخذ هذا التحميل الزائد من طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) المعلمات التالية: ملف PDF المدخل، مصفوفة صحيحة من الصفحات التي سيتم استخراجها، وملف PDF الناتج. يوضح لك مقتطف الكود التالي كيفية استخراج صفحات PDF باستخدام مسارات الملفات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## استخراج صفحات PDF بين رقمين باستخدام التدفقات

تتيح لك طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) من فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) استخراج نطاق من الصفحات باستخدام التدفقات. تحتاج إلى تمرير المعلمات التالية إلى هذا التحميل الزائد: تدفق الإدخال، الصفحة الأولى، الصفحة الأخيرة، وتدفق الإخراج. سيتم استخراج الصفحات المحددة بواسطة النطاق بين الصفحة الأولى والصفحة الأخيرة من تدفق الإدخال وحفظها في تدفق الإخراج. يوضح لك مقتطف الكود التالي كيفية استخراج صفحات PDF بين رقمين باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## استخراج مصفوفة من صفحات PDF باستخدام التدفقات

يمكن استخراج مصفوفة من الصفحات من تدفق PDF وحفظها في تدفق الإخراج باستخدام التحميل الزائد المناسب لطريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). إذا كنت لا ترغب في استخراج نطاق من الصفحات، بل مجموعة من صفحات معينة، فإن طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) تتيح لك القيام بذلك أيضًا. تحتاج أولاً إلى إنشاء مصفوفة صحيحة تحتوي على جميع أرقام الصفحات التي تحتاج إلى استخراجها. يأخذ هذا التحميل الزائد من طريقة [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) المعلمات التالية: تدفق الإدخال، مصفوفة صحيحة من الصفحات التي سيتم استخراجها وتدفق الإخراج. يوضح لك مقتطف الكود التالي كيفية استخراج صفحات PDF باستخدام التدفقات.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```
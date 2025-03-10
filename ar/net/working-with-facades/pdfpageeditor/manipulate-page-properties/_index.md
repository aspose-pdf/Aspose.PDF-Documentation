---
title: التلاعب بخصائص الصفحة
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/manipulate-page-properties/
description: يشرح هذا القسم كيفية التلاعب بخصائص الصفحة باستخدام واجهات Aspose.PDF من خلال فئة PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "تقديم فئة PdfPageEditor، أداة قوية لإدارة خصائص صفحات PDF مع واجهات Aspose.PDF for .NET. تتيح هذه الميزة للمطورين استرجاع وتعديل السمات الأساسية للصفحة مثل الدوران، مستويات التكبير، وأبعاد الصفحة، مما يوفر تحكمًا دقيقًا في عرض محتوى PDF. مع طرق بسيطة للحصول على الخصائص وتعيينها، بما في ذلك القدرة على تغيير حجم محتويات صفحة معينة، لم يكن تحسين مستندات PDF أسهل من ذلك.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## الحصول على خصائص صفحة PDF من ملف PDF موجود

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) يتيح لك العمل مع الصفحات الفردية من ملف PDF. يساعدك في الحصول على خصائص الصفحة الفردية مثل أحجام صناديق الصفحات المختلفة، دوران الصفحة، تكبير الصفحة، إلخ. للحصول على تلك الخصائص، تحتاج إلى إنشاء كائن [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، يمكنك استخدام طرق مختلفة للحصول على خصائص الصفحة مثل [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)، [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)، [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) إلخ.

تظهر الشيفرة البرمجية التالية كيفية الحصول على خصائص صفحة PDF من ملف PDF موجود.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## تعيين خصائص صفحة PDF في ملف PDF موجود

لتعيين خصائص الصفحة مثل دوران الصفحة، التكبير أو نقطة الأصل، تحتاج إلى استخدام فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). توفر هذه الفئة طرقًا وخصائص مختلفة لتعيين هذه الخصائص. أولاً، تحتاج إلى إنشاء كائن من فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). بعد ذلك، يمكنك استخدام هذه الطرق والخصائص لتعيين خصائص الصفحة. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

تظهر الشيفرة البرمجية التالية كيفية تعيين خصائص صفحة PDF في ملف PDF موجود.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## تغيير حجم محتويات الصفحة لصفحات معينة في ملف PDF

تسمح لك طريقة ResizeContents من فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) بتغيير حجم محتويات الصفحة في ملف PDF. تُستخدم فئة [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) لتحديد المعلمات التي سيتم استخدامها لتغيير حجم الصفحة (الصفحات) مثل الهوامش بالنسبة المئوية أو الوحدات، إلخ. يمكنك تغيير حجم جميع الصفحات أو تحديد مصفوفة من الصفحات لتغيير حجمها باستخدام طريقة ResizeContents.

تظهر الشيفرة البرمجية التالية كيفية تغيير حجم محتويات بعض الصفحات المحددة من ملف PDF.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```
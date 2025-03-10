---
title: تعديل الصفحات الفردية لملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: يشرح هذا القسم كيفية تعديل الصفحات الفردية لملف PDF باستخدام فئة PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Editing PDF individual pages",
    "alternativeHeadline": "Edit Individual Pages of PDF Easily with PdfPageEditor",
    "abstract": "تتيح فئة PdfPageEditor في Aspose.PDF for .NET للمستخدمين القدرة على التلاعب بكفاءة بالصفحات الفردية لملف PDF من خلال وظائف مثل التدوير والمحاذاة وتأثيرات الانتقال. تعزز هذه الأداة المتخصصة التحكم في عرض الصفحات وتنسيقها، مما يسمح بعرض مخصص لمحتوى PDF. استمتع بقدرات تحرير سلسة لتحسين كيفية عرض كل صفحة والتفاعل معها.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "593",
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
    "url": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تتيح مساحة أسماء Aspose.Pdf.Facades في [Aspose.PDF for .NET](/pdf/ar/net/) لك التلاعب بالصفحات الفردية في ملف PDF. تساعدك هذه الميزة في العمل مع عرض الصفحة والمحاذاة والانتقال وما إلى ذلك. تساعد فئة PdfpageEditor في تحقيق هذه الوظيفة. في هذه المقالة، سننظر في الخصائص والأساليب التي توفرها هذه الفئة وعمل هذه الأساليب أيضًا.

{{% /alert %}}

## الشرح

تختلف فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) عن فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) وفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). أولاً، نحتاج إلى فهم الفرق، ثم سنكون قادرين على فهم فئة PdfPageEditor بشكل أفضل. تتيح لك فئة PdfFileEditor التلاعب بجميع الصفحات في ملف مثل إضافة الصفحات أو حذفها أو دمجها، بينما تساعدك فئة PdfContentEditor في التلاعب بمحتويات الصفحة مثل النص والأشياء الأخرى. بينما تعمل فئة PdfPageEditor فقط مع الصفحة الفردية نفسها مثل التدوير والتكبير والمحاذاة وما إلى ذلك.

يمكننا تقسيم الميزات التي توفرها هذه الفئة إلى ثلاث فئات رئيسية وهي: الانتقال، والمحاذاة، والعرض. سنناقش هذه الفئات أدناه:

### الانتقال

تحتوي هذه الفئة على خاصيتين تتعلقان بالانتقال وهما [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) و [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). تحدد TransitionType نمط الانتقال الذي سيتم استخدامه عند الانتقال إلى هذه الصفحة من صفحة أخرى أثناء العرض. تحدد TransitionDuration مدة عرض الصفحات.

### المحاذاة

تدعم فئة PdfPageEditor كل من المحاذاة الأفقية والعمودية. توفر خاصيتين لخدمة هذا الغرض وهما [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) و [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). تُستخدم خاصية Alignment لمحاذاة المحتويات أفقيًا. تأخذ خاصية Alignment قيمة من AlignmentType، والتي تحتوي على ثلاث خيارات وهي: Center و Left و Right. تأخذ خاصية VerticalAlignment قيمة من VerticalAlignmentType، والتي تحتوي على ثلاث خيارات وهي: Bottom و Center و Top.

### العرض

تحت فئة العرض، يمكننا تضمين خصائص مثل PageSize و Rotation و Zoom و DisplayDuration. تحدد خاصية PageSize حجم الصفحة الفردية في الملف. تأخذ هذه الخاصية كائن PageSize كمدخل، والذي ي encapsulates حجم الصفحة المحدد مسبقًا مثل A0 و A1 و A2 و A3 و A4 و A5 و A6 و B5 و Letter و Ledger و P11x17. تُستخدم خاصية Rotation لتعيين تدوير الصفحة الفردية. يمكن أن تأخذ القيم 0 أو 90 أو 180 أو 270. تحدد خاصية Zoom معامل التكبير للصفحة، وتأخذ قيمة عائمة كمدخل. توفر هذه الفئة أيضًا طريقة للحصول على حجم الصفحة وتدوير الصفحة الفردية في الملف.

يمكنك العثور على عينات من الأساليب المذكورة أعلاه في مقتطف الشيفرة أدناه:



```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EditPdfPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create a new instance of PdfPageEditor class
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Specify an array of pages which need to be manipulated (pages can be multiple, here we have specified only one page)
        pdfPageEditor.ProcessPages = new int[] { 1 };

        // Alignment related code
        pdfPageEditor.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;

        // Specify transition type for the pages
        pdfPageEditor.TransitionType = 2;
        // Specify transition duration
        pdfPageEditor.TransitionDuration = 5;

        // Display related code

        // Select a page size from the enumeration and assign to property
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLedger;

        // Assign page rotation
        pdfPageEditor.Rotation = 90;

        // Specify zoom factor for the page
        pdfPageEditor.Zoom = 100;

        // Assign display duration for the page
        pdfPageEditor.DisplayDuration = 5;

        // Fetching methods

        // Methods provided by the class, page rotation specified already
        var rotation = pdfPageEditor.GetPageRotation(1);

        // Already specified page can be fetched
        var pageSize = pdfPageEditor.GetPageSize(1);

        // This method gets the page count
        var totalPages = pdfPageEditor.GetPages();

        // This method changes the origin from (0,0) to specified number
        pdfPageEditor.MovePosition(100, 100);

        // Save PDF document
        pdfPageEditor.Save(dataDir + "EditPdfPages_out.pdf");
    }
}
```

## الخاتمة

{{% alert color="primary" %}}
في هذه المقالة، نظرنا عن كثب إلى فئة [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). لقد أوضحنا الخصائص والأساليب التي توفرها هذه الفئة. يجعل التلاعب بالصفحات الفردية في الفئة مهمة سهلة وبسيطة للغاية.
{{% /alert %}}
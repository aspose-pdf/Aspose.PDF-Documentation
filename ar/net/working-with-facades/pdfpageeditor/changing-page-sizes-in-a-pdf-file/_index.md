---
title: تغيير أحجام الصفحات في ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/changing-page-sizes-in-a-pdf-file/
description: حاول تعلم كيفية تغيير أحجام الصفحات في ملف PDF باستخدام فئة PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "تتيح ميزة فئة PdfPageEditor في Aspose.Pdf للمستخدمين تغيير أحجام الصفحات بسهولة للصفحات الفردية أو المتعددة داخل ملف PDF. من خلال استخدام خاصية PageSize وخاصية Pages، يمكن للمستخدمين اختيار من بين أحجام الصفحات المحددة مسبقًا وتطبيقها بفعالية، مما يعزز مرونة وتخصيص تخطيطات مستندات PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة فحسب، بل يمكنه أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## تفاصيل التنفيذ

[PdfPageEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor) class in [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) contains a property named [PageSize](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) which can be used to change the page size of an individual page or multiple pages at once. The Pages property can be used to assign the numbers of the pages on which the new page size needs to be applied. PageSize class contains a list of different page sizes as its members. Any of the members of this class can be assigned to PageSize property of the [PdfPageEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor) class. You can also get page size of any page using GetPageSize method and passing the page number.

--> 
يمكن ترجمة الفقرة أعلاه إلى العربية كالتالي:

فئة [PdfPageEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor) في [فضاء الأسماء Aspose.Pdf.Facades](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) تحتوي على خاصية باسم [PageSize](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) والتي يمكن استخدامها لتغيير حجم صفحة فردية أو عدة صفحات دفعة واحدة. يمكن استخدام خاصية Pages لتعيين أرقام الصفحات التي سيتم تطبيق الحجم الجديد عليها. تحتوي فئة PageSize على قائمة بأحجام الصفحات المختلفة كأعضائها. يمكن تعيين أي من أعضاء هذه الفئة إلى خاصية PageSize لفئة [PdfPageEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor). يمكنك أيضاً الحصول على حجم أي صفحة باستخدام طريقة GetPageSize مع تمرير رقم الصفحة.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```
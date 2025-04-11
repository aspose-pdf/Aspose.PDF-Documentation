---
title: العمل مع تدوير الصفحات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/working-with-page-rotation/
description: يشرح هذا القسم كيفية العمل مع تدوير الصفحات باستخدام فئة PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Page Rotation",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with PdfPageEditor",
    "abstract": "اكتشف ميزة تدوير الصفحات القوية في فئة PdfPageEditor، مما يتيح التلاعب الدقيق بصفحات المستند من خلال زوايا تدوير قابلة للتخصيص. مع خيارات لتحديد تدويرات الصفحات الفردية أو تطبيق تدوير موحد عبر الصفحات المحددة، تعزز هذه الوظيفة قدرات تحرير PDF، مما يوفر مرونة أكبر وتحكم للمستخدمين.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "202",
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
    "url": "/net/working-with-page-rotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-page-rotation/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

فئة [PdfPageEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor) توفر إمكانية تدوير صفحة.

{{% /alert %}}

## تدوير الصفحة باستخدام PageRotations

لتدوير الصفحات في المستند يمكننا استخدام [PageRotations](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` تحتوي على رقم الصفحة ودرجة التدوير، المفتاح يمثل رقم الصفحة، وقيمة المفتاح تمثل التدوير بالدرجات.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void RotatePages1()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "sample.pdf");

         // Specify the page rotation dictionary
         editor.PageRotations = new System.Collections.Generic.Dictionary<int, int>
         {
             { 1, 90 },
             { 2, 180 },
             { 3, 270 }
         };

         // Save PDF document
         editor.Save(dataDir + "sample-rotate-a.pdf");
     }
 }
```

## تدوير الصفحة باستخدام Rotation

يمكننا أيضًا استخدام خاصية [Rotation](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). يجب أن يكون التدوير 0 أو 90 أو 180 أو 270

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotatePages2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Specify the pages to rotate and the rotation angle
        editor.ProcessPages = new int[] { 1, 3 };
        editor.Rotation = 90;

        // Save PDF document
        editor.Save(dataDir + "sample-rotate-a.pdf");
    }
}
```
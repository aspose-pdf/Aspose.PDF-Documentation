---
title: استخراج المرفقات من ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/extract-attachments/
description: اكتشف كيفية استخراج وإدارة المرفقات في مستندات PDF في .NET باستخدام Aspose.PDF لتحسين معالجة المستندات.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Attachments from PDF File",
    "alternativeHeadline": "Effortlessly Extract and Manage PDF Attachments",
    "abstract": "تتيح وظيفة استخراج المرفقات الجديدة في Aspose.PDF for .NET للمطورين استرجاع وإدارة مرفقات الملفات داخل مستندات PDF بسهولة. من خلال استخدام فئة PdfExtractor، يمكن للمستخدمين استخراج المرفقات والحصول على معلومات أساسية، مثل أسماء المرفقات والتفاصيل، مما يعزز قدرات معالجة المستندات.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "208",
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
    "url": "/net/extract-attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تعتبر استخراج المرفقات واحدة من الفئات الرئيسية ضمن قدرات الاستخراج في [مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades). توفر هذه الفئة مجموعة من الطرق، التي لا تساعد فقط في استخراج المرفقات ولكن أيضًا توفر الطرق التي يمكن أن تعطيك معلومات متعلقة بالمرفقات، أي أن طرق [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) و [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) توفر معلومات المرفقات واسم المرفق على التوالي. لاستخراج المرفقات ثم الحصول عليها، نستخدم طرق [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) و [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

تظهر لك الشيفرة البرمجية التالية كيفية استخدام طرق PdfExtractor:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Create the extractor
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "GetAlltheAttachments.pdf");

        // Extract attachments
        pdfExtractor.ExtractAttachment();

        // Get attachment names
        if (pdfExtractor.GetAttachNames().Count > 0)
        {
            Console.WriteLine("Extracting and storing...");

            // Get extracted attachments
            pdfExtractor.GetAttachment(dataDir + "GetAlltheAttachments_out.pdf");
        }
    }
}
```
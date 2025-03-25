---
title: تدوير الختم حول نقطة المركز
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/rotating-stamp-about-the-center-point/
description: يشرح هذا القسم كيفية تدوير الختم حول نقطة المركز باستخدام فئة الختم.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "تتيح الميزة في Aspose.PDF for .NET للمستخدمين تدوير الأختام داخل ملفات PDF بدقة حول نقطة مركزها. باستخدام فئة الختم، يمكن للمطورين بسهولة تعيين قيم التدوير من 0 إلى 360 درجة، مما يعزز مرونة وتخصيص وضع العلامات المائية في الوثائق. هذه الوظيفة مثالية لإنشاء ملفات PDF ديناميكية بصريًا مع اتجاهات ختم مخصصة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

[مساحة أسماء Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) في [Aspose.PDF for .NET](/pdf/ar/net/) تتيح لك إضافة ختم في ملف PDF موجود. أحيانًا، يحتاج المستخدمون إلى تدوير الختم. في هذه المقالة، سنرى كيفية تدوير الختم حول نقطة مركزه.

{{% /alert %}}

## تفاصيل التنفيذ

تتيح لك فئة [الختم](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) إضافة علامة مائية في ملف PDF. يمكنك تحديد الصورة التي سيتم إضافتها كختم باستخدام طريقة [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). تتيح لك طريقة [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) تعيين نقطة الأصل للختم المضاف؛ هذه النقطة هي إحداثيات الزاوية السفلى اليسرى للختم. يمكنك أيضًا تعيين حجم الصورة باستخدام طريقة [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

الآن، نرى كيف يمكن تدوير الختم حول مركز الختم. توفر فئة [الختم](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) خاصية تسمى Rotation. تقوم هذه الخاصية بتعيين أو الحصول على التدوير من 0 إلى 360 لمحتوى الختم. يمكننا تحديد أي قيمة تدوير من 0 إلى 360. من خلال تحديد قيمة التدوير، يمكننا تدوير الختم حول نقطة مركزه. إذا كان الختم كائنًا من نوع الختم، فيمكن تحديد قيمة التدوير كالتالي: aStamp.Rotation = 90. في هذه الحالة، سيتم تدوير الختم بزاوية 90 درجة حول مركز محتوى الختم. يوضح لك مقتطف الكود التالي كيفية تدوير الختم حول نقطة المركز:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```
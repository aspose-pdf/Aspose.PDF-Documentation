---
title: منصة البيانات الوصفية القابلة للتوسيع - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/working-with-extensible-metadata-platform-xmp/
description: يشرح هذا القسم كيفية العمل مع منصة البيانات الوصفية القابلة للتوسيع - XMP باستخدام فئة PdfXmpMetadata.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "تتيح وظيفة منصة البيانات الوصفية القابلة للتوسيع (XMP) في Aspose.PDF for .NET للمستخدمين تضمين البيانات الوصفية القياسية والملكية بكفاءة والتلاعب بها داخل ملفات PDF. من خلال استخدام فئة PdfXmpMetadata، تبسط هذه الميزة عملية تتبع التغييرات وتعزيز القدرات الدلالية لوثائق PDF، مما يجعلها أداة قيمة للمطورين الذين يتطلعون إلى دمج إدارة البيانات الوصفية المتقدمة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

{{% alert color="primary" %}}

تعتبر منصة البيانات الوصفية القابلة للتوسيع (XMP) معيارًا تم إنشاؤه بواسطة شركة أدوبي. تم تطوير هذا المعيار لمعالجة وتخزين البيانات الوصفية القياسية والملكية. يمكن تضمين هذه البيانات الوصفية في تنسيقات ملفات مختلفة، ولكن في هذه المقالة سنركز فقط على تنسيق ملف PDF. سنرى كيف يمكننا تضمين البيانات الوصفية في ملف PDF باستخدام مساحة أسماء Aspose.Pdf.Facades في Aspose.PDF for .NET. سنستخدم فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfxmpmetadata) للتلاعب بـ XMP في مستند PDF.

{{% /alert %}}

## الخلفية

يمر ملف PDF بالعديد من المراحل خلال فترة حياته. نقوم بإنشاء مستند PDF ثم نمرره إلى أشخاص أو أقسام أخرى لمزيد من المعالجة. ومع ذلك، خلال هذه العملية نحتاج إلى تتبع جوانب مختلفة من التغييرات التي تم إجراؤها. يخدم XMP هذا الغرض من تتبع التغييرات أو المعلومات الأخرى حول البيانات في الملف.

## الشرح

للتلاعب بـ XMP باستخدام Aspose.Pdf.Facades، سنستخدم فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class). سنستخدم هذه الفئة للتلاعب بخصائص البيانات الوصفية المحددة مسبقًا. تضيف فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) هذه الخصائص إلى ملف PDF. كما أنها تساعد في فتح وحفظ ملفات PDF التي نضيف فيها البيانات الوصفية. لذا، باستخدام فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class)، يمكننا بسهولة التلاعب بـ XMP في ملف PDF.
سيساعدك مقتطف الكود التالي على فهم كيفية استخدام فئة [PdfXmpMetadata](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfxmpmetadata) للعمل مع XMP:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## الخاتمة

{{% alert color="primary" %}}
في هذه المقالة، رأينا كيف يمكننا العمل مع XMP باستخدام Aspose.Pdf.Facades. تجعل فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) المستخدمة في هذه المقالة من السهل جدًا على المستخدم التلاعب بالبيانات الوصفية في مستند PDF. إذا تم استخدام فئة [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) بشكل صحيح، سيكون من السهل جدًا دمج الذكاء في ملفات PDF، مما يجعل الويب الدلالي أقرب قليلاً إلى التحقيق.
{{% /alert %}}
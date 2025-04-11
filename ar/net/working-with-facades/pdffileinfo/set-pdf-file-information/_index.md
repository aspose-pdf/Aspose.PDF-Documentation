---
title: تعيين معلومات ملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/set-pdf-file-information/
description: يشرح هذا القسم كيفية تعيين معلومات ملف PDF باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "قم بتحسين إدارة ملفات PDF الخاصة بك مع الوظيفة الجديدة في Aspose.PDF for .NET التي تتيح لك تعيين وتحديث المعلومات الخاصة بالملف بسهولة مثل المؤلف، العنوان، والكلمات الرئيسية. استخدم فئة PdfFileInfo لتعديل ملفات PDF الخاصة بك بكفاءة، مضيفًا بيانات وصفية قيمة لتحسين التنظيم وقابلية البحث. قم بتبسيط سير العمل الخاص بك من خلال حفظ هذه التحديثات بسلاسة باستخدام طريقة SaveNewInfo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

[PdfFileInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo) تتيح لك تعيين معلومات محددة لملف PDF. تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo) ثم تعيين خصائص مختلفة محددة للملف مثل المؤلف، العنوان، الكلمات الرئيسية، والمبدع، إلخ. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [SaveNewInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) لكائن [PdfFileInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo).

تظهر لك مقتطفات الكود التالية كيفية تعيين معلومات ملف PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## تعيين معلومات البيانات الوصفية

تتيح لك طريقة [SetMetaInfo](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) إضافة أي معلومات. في مثالنا، أضفنا حقلًا. تحقق من مقتطف الكود التالي:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```
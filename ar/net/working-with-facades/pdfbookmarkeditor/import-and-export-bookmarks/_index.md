---
title: استيراد وتصدير العلامات المرجعية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/import-and-export-bookmarks/
description: يشرح هذا القسم كيفية استيراد وتصدير العلامات المرجعية باستخدام Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Bookmarks",
    "alternativeHeadline": "Seamlessly Import and Export PDF Bookmarks with XML",
    "abstract": "اكتشف ميزة استيراد وتصدير العلامات المرجعية الجديدة في Aspose.PDF for .NET، والتي تمكن المستخدمين من استيراد العلامات المرجعية من ملفات XML إلى مستندات PDF الموجودة وتصدير العلامات المرجعية مرة أخرى إلى XML. تعزز هذه الوظيفة إدارة المستندات من خلال تبسيط دمج العلامات المرجعية، مما يوفر عملية مباشرة للحفاظ على الهيكل التنظيمي داخل ملفات PDF. قم بتحسين سير العمل الخاص بك ورفع قدرات التعامل مع PDF الخاصة بك مع هذه الإضافة القوية",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/import-and-export-bookmarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-bookmarks/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

## استيراد العلامات المرجعية من XML إلى ملف PDF موجود

تتيح لك طريقة [ImportBookmarksWithXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) استيراد العلامات المرجعية إلى ملف PDF من ملف XML. لاستيراد العلامات المرجعية، تحتاج إلى إنشاء كائن [PdfBookmarkEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfbookmarkeditor) وربط ملف PDF باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، تحتاج إلى استدعاء طريقة [ImportBookmarksWithXml](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/ar/net/aspose.pdf/document/methods/save). يوضح لك مقتطف الكود التالي كيفية استيراد العلامات المرجعية من ملف XML.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

        // Import bookmarks
        bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

        // Save PDF document
        bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportBookmarksFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ImportFromXML.pdf");

    // Import bookmarks
    bookmarkEditor.ImportBookmarksWithXML(dataDir + "bookmarks.xml");

    // Save PDF document
    bookmarkEditor.Save(dataDir + "ImportFromXML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## تصدير العلامات المرجعية إلى XML من ملف PDF موجود

تتيح لك طريقة ExportBookmarksToXml تصدير العلامات المرجعية من ملف PDF إلى ملف XML.

لتصدير العلامات المرجعية:

1. أنشئ كائن PdfBookmarkEditor واربط ملف PDF باستخدام طريقة BindPdf.
1. استدعِ طريقة ExportBookmarksToXml.
1. احفظ ملف PDF المحدث باستخدام طريقة Save.

يوضح لك مقتطف الكود التالي كيفية تصدير العلامات المرجعية إلى ملف XML.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using (var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor())
    {
        // Bind PDF document
        bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

        // Export bookmarks to an XML file
        bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportBookmarksToXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Bookmarks();

    // Create an instance of PdfBookmarkEditor
    using var bookmarkEditor = new Aspose.Pdf.Facades.PdfBookmarkEditor();

    // Bind PDF document
    bookmarkEditor.BindPdf(dataDir + "ExportToXML.pdf");

    // Export bookmarks to an XML file
    bookmarkEditor.ExportBookmarksToXML(dataDir + "bookmarks.xml");
}
```
{{< /tab >}}
{{< /tabs >}}
---
title: العمل مع بيانات التعريف لملف PDF في C#
linktitle: بيانات التعريف لملف PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 200
url: /ar/net/pdf-file-metadata/
description: استكشف كيفية استخراج وإدارة بيانات التعريف لملف PDF، مثل المؤلف والعنوان، في .NET باستخدام Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF File Metadata in C#",
    "alternativeHeadline": "Extracting and Managing PDF Metadata in C#",
    "abstract": "افتح قوة إدارة ملفات PDF مع ميزتنا الجديدة لمطوري C#، مما يتيح الوصول السلس إلى بيانات التعريف لملف PDF. احصل على رؤى حول خصائص الملف، واستخرج بيانات التعريف XMP، وقم بتحديث معلومات الوثيقة بسهولة، مما يبسط عملية التعامل مع مستنداتك. اختبر وظائف محسنة للحفاظ على بيانات التعريف لملف PDF والتلاعب بها بكفاءة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF file metadata, C# PDF manipulation, get PDF file information, set PDF file information, XMP metadata, Aspose.PDF for .NET, document properties, PDF metadata management",
    "wordcount": "834",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2024-11-25",
    "description": "تشرح هذه القسم كيفية الحصول على معلومات ملف PDF، كيفية الحصول على بيانات التعريف XMP من ملف PDF، تعيين معلومات ملف PDF."
}
</script>

تعمل مقتطفات الشيفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/) .

## الحصول على معلومات ملف PDF

للحصول على معلومات محددة عن ملف PDF، تحتاج أولاً إلى الحصول على كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) باستخدام خاصية [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) . بمجرد استرجاع كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) ، يمكنك الحصول على قيم الخصائص الفردية. يوضح مقتطف الشيفرة التالي كيفية الحصول على معلومات ملف PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;

        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPDFFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFileInfo.pdf"))
    {
        // Get document information
        var docInfo = document.Info;
        // Display document information
        Console.WriteLine("Author: {0}", docInfo.Author);
        Console.WriteLine("Creation Date: {0}", docInfo.CreationDate);
        Console.WriteLine("Keywords: {0}", docInfo.Keywords);
        Console.WriteLine("Modify Date: {0}", docInfo.ModDate);
        Console.WriteLine("Subject: {0}", docInfo.Subject);
        Console.WriteLine("Title: {0}", docInfo.Title);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## تعيين معلومات ملف PDF

Aspose.PDF for .NET يتيح لك تعيين معلومات محددة عن ملف PDF، مثل المؤلف، تاريخ الإنشاء، الموضوع، والعنوان. لتعيين هذه المعلومات:

1. أنشئ كائن [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) .
1. قم بتعيين قيم الخصائص.
1. احفظ المستند المحدث باستخدام طريقة Save لفئة Document.

يظهر مقتطف الشيفرة التالي كيفية تعيين معلومات ملف PDF.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFileInformation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFileInfo.pdf"))
    {
        // Specify document information
        var docInfo = new Aspose.Pdf.DocumentInfo(document);

        docInfo.Author = "Aspose";
        docInfo.CreationDate = DateTime.Now;
        docInfo.Keywords = "Aspose.Pdf, DOM, API";
        docInfo.ModDate = DateTime.Now;
        docInfo.Subject = "PDF Information";
        docInfo.Title = "Setting PDF Document Information";

        // Save PDF document
        document.Save(dataDir + "SetFileInfo_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## الحصول على بيانات التعريف XMP من ملف PDF

Aspose.PDF يتيح لك الوصول إلى بيانات التعريف XMP لملف PDF. للحصول على بيانات التعريف لملف PDF:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) وافتح ملف PDF المدخل.
1. احصل على بيانات التعريف للملف باستخدام خاصية [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) .

يظهر مقتطف الشيفرة التالي كيفية الحصول على بيانات التعريف من ملف PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXMPMetadata.pdf"))
    {
        // Get and display properties
        Console.WriteLine($"Create Date: {document.Metadata["xmp:CreateDate"]}");
        Console.WriteLine($"Nickname: {document.Metadata["xmp:Nickname"]}");
        Console.WriteLine($"Custom Property: {document.Metadata["xmp:CustomProperty"]}");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## تعيين بيانات التعريف XMP في ملف PDF

Aspose.PDF يتيح لك تعيين بيانات التعريف في ملف PDF. لتعيين بيانات التعريف:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .
1. قم بتعيين قيم بيانات التعريف باستخدام خاصية [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) .
1. احفظ المستند المحدث باستخدام طريقة [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) لكائن [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) .

يظهر مقتطف الشيفرة التالي كيفية تعيين بيانات التعريف في ملف PDF.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetXMPMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Set properties
        document.Metadata["xmp:CreateDate"] = DateTime.Now.ToString("o");
        document.Metadata["xmp:Nickname"] = "Nickname";
        document.Metadata["xmp:CustomProperty"] = "Custom Value";

        // Save PDF document
        document.Save(dataDir + "SetXMPMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## إدراج بيانات التعريف مع بادئة

بعض المطورين يحتاجون إلى إنشاء مساحة أسماء جديدة لبيانات التعريف مع بادئة. يوضح مقتطف الشيفرة التالي كيفية إدراج بيانات التعريف مع بادئة.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrefixMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetXMPMetadata.pdf"))
    {
        // Register a namespace URI for the 'xmp' prefix
        document.Metadata.RegisterNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");

        // Set the metadata property using the registered prefix
        document.Metadata["xmp:ModifyDate"] = DateTime.Now.ToString("o"); // ISO 8601 format for datetime

        // Save PDF document
        document.Save(dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
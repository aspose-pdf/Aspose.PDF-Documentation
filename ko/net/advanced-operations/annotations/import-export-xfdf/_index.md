---
title: XFDF로 주석 가져오기 및 내보내기
linktitle: XFDF로 주석 가져오기 및 내보내기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/import-export-xfdf/
description: C# 및 Aspose.PDF for .NET 라이브러리를 사용하여 XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Effortless XFDF Annotation Import and Export",
    "abstract": "Aspose.PDF for .NET 라이브러리의 XFDF에 대한 새로운 가져오기 및 내보내기 기능은 주석 데이터의 원활한 전송을 허용하여 PDF 문서 관리를 향상시킵니다. 이 기능은 사용자가 XFDF 파일에서 주석을 쉽게 통합하고 다시 내보낼 수 있도록 하여 PDF 양식에 대한 효율적인 데이터 교환 및 아카이빙 기능을 촉진합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Annotations, Export Annotations, XFDF Format, Aspose.PDF for .NET, PdfAnnotationEditor, ImportAnnotationFromXfdf, ExportAnnotationsXfdf, PDF Forms Manipulation",
    "wordcount": "670",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "C# 및 Aspose.PDF for .NET 라이브러리를 사용하여 XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다."
}
</script>

{{% alert color="primary" %}}

XFDF는 XML 양식 데이터 형식을 의미합니다. 이는 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 양식에 포함된 양식 데이터 또는 주석을 나타내는 데 사용됩니다. XFDF는 다양한 용도로 사용될 수 있지만, 우리의 경우에는 양식 데이터 또는 주석을 다른 컴퓨터나 서버 등으로 전송하거나 수신하는 데 사용되거나, 양식 데이터 또는 주석을 아카이브하는 데 사용될 수 있습니다. 이 기사에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려했는지와 XFDF 파일로 주석 데이터를 가져오고 내보내는 방법을 살펴보겠습니다.

{{% /alert %}}

**Aspose.PDF for .NET**는 PDF 문서를 편집할 때 기능이 풍부한 구성 요소입니다. XFDF는 PDF 양식 조작의 중요한 측면인 만큼, Aspose.PDF for .NET의 Aspose.Pdf.Facades 네임스페이스는 이를 잘 고려하여 XFDF 파일로 주석 데이터를 가져오고 내보내는 방법을 제공했습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내는 두 가지 메서드를 포함하고 있습니다. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 메서드는 PDF 문서에서 XFDF 파일로 주석을 내보내는 기능을 제공하며, [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 메서드는 기존 XFDF 파일에서 주석을 가져올 수 있게 해줍니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 이러한 유형은 열거형의 형태로 지정할 수 있으며, 이 열거형을 이러한 메서드 중 하나의 인수로 전달하면 됩니다. 이렇게 하면 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 주석을 XFDF 파일로 내보내는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAnnotationsToXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationDemo1.pdf");

        // Define the annotation types to export
        var annotType = new Aspose.Pdf.Annotations.AnnotationType[] { Aspose.Pdf.Annotations.AnnotationType.Line, Aspose.Pdf.Annotations.AnnotationType.Square };

        // Export annotations to XFDF file
        using (var fileStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
        }
    }
}
```

다음 코드 스니펫은 XFDF 파일에서 주석을 가져오는 방법을 설명합니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Define the export file name
            var exportFileName = dataDir + "exportannotations.xfdf";

            // Import annotations from the XFDF file
            annotationEditor.ImportAnnotationsFromXfdf(exportFileName);

            // Save PDF document
            document.Save(dataDir + "ImportAnnotationFromXfdf_out.pdf");
        }
    }
}
```

## 주석을 한 번에 내보내고 가져오는 또 다른 방법

아래 코드에서 ImportAnnotations 메서드는 다른 PDF 문서에서 직접 주석을 가져올 수 있게 해줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var documentFrom = new Aspose.Pdf.Document(dataDir + "some_doc.pdf"))
    {
        // Create PDF document
        using (var documentTo = new Aspose.Pdf.Document())
        {
            // Add page
            var page = documentTo.Pages.Add();

            // Export/import
            using (var ms = new MemoryStream())
            {
                documentFrom.ExportAnnotationsToXfdf(ms);
                documentTo.ImportAnnotationsFromXfdf(ms);
            }

            // Save PDF document
            documentTo.Save(dataDir + "AnnotationDemo3_out.pdf");
        }
    }
}
```

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
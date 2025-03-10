---
title: XFDF로 주석 가져오기 및 내보내기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/import-export-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 가져오고 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET은 XFDF로 주석을 가져오고 내보내는 강력한 기능을 소개하여 PDF 조작 기능을 향상시킵니다. 이 기능은 사용자가 XML Forms Data Format에서 주석 데이터를 선택적으로 전송할 수 있도록 하여 더 나은 문서 관리를 위한 원활한 통합 및 보관을 가능하게 합니다. 주석 유형을 지정하는 전용 메서드를 통해 사용자는 PDF 주석을 효율적으로 관리할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 다음 섹션에서 고급 사용자 및 개발자를 확인하세요."
}
</script>

XFDF는 XML Forms Data Format의 약자입니다. 이는 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 양식에 포함된 양식 데이터 또는 주석을 나타내는 데 사용됩니다. XFDF는 여러 가지 용도로 사용될 수 있지만, 우리의 경우 다른 컴퓨터나 서버 등으로 양식 데이터 또는 주석을 전송하거나 수신하는 데 사용되거나 양식 데이터 또는 주석을 보관하는 데 사용될 수 있습니다. 이 기사에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려했는지, 그리고 XFDF 파일로 주석 데이터를 가져오고 내보내는 방법을 살펴보겠습니다.

## XFDF로 주석 가져오기 및 내보내기

[Aspose.PDF for .NET](/pdf/ko/net/)는 PDF 문서를 편집할 때 기능이 풍부한 구성 요소입니다. XFDF는 PDF 양식 조작의 중요한 측면인 만큼, [Aspose.PDF for .NET](/pdf/ko/net/)의 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 이를 잘 고려하여 XFDF 파일로 주석 데이터를 가져오고 내보내는 메서드를 제공했습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내는 두 가지 메서드를 포함하고 있습니다. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 메서드는 PDF 문서에서 XFDF 파일로 주석을 내보내는 기능을 제공하며, [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 메서드는 기존 XFDF 파일에서 주석을 가져오는 기능을 제공합니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 이러한 유형은 열거형의 형태로 지정할 수 있으며, 이 열거형을 이러한 메서드 중 하나에 인수로 전달하면 됩니다. 이렇게 하면 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

다음 코드 스니펫은 XFDF 파일로 주석을 가져오는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

다음 코드 스니펫은 XFDF 파일로 주석을 가져오고 내보내는 방법을 설명합니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

이렇게 하면 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```
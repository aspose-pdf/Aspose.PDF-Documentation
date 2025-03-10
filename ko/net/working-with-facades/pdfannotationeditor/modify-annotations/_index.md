---
title: PDF에서 주석 수정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/modify-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일의 주석을 XFDF로 수정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modify Annotations in your PDF",
    "alternativeHeadline": "Enhance Your PDF Annotations with New Modifications",
    "abstract": "주석 수정 기능을 사용하면 사용자가 Aspose.PDF Facades를 사용하여 PDF 파일의 주석의 주요 속성을 쉽게 편집할 수 있습니다. 이 기능에는 주제, 저자, 색상 등을 변경하는 것과 주석 유형별로 주석을 삭제하는 옵션이 포함되어 있어 PDF 주석 관리 프로세스를 간소화합니다. 이러한 강력한 주석 수정 기능을 활용하여 PDF 워크플로를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "290",
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
    "url": "/net/modify-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modify-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 주석 수정

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) 메서드는 주석의 기본 속성인 주제, 수정 날짜, 저자, 주석 색상 및 열기 플래그를 변경할 수 있게 해줍니다. ModifyAnnotations 메서드를 사용하여 저자를 직접 설정할 수도 있습니다. 이 클래스는 주석을 삭제하는 두 개의 오버로드된 메서드도 제공합니다. 첫 번째 메서드인 DeleteAnnotations는 PDF 파일에서 모든 주석을 삭제합니다.  

예를 들어, 다음 코드에서는 [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor)를 사용하여 주석의 저자를 변경하는 것을 고려해 보세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotationsAuthor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Modify annotations author
        annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        // Save PDF document
        annotationEditor.Save(dataDir + "ModifyAnnotationsAuthor_out.pdf");
    }
}
```

두 번째 메서드는 주석을 수정할 수 있게 해줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        // Create PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Create a new object of type Annotation
            TextAnnotation newTextAnnotation = new TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
            newTextAnnotation.Title = "Updated title";
            newTextAnnotation.Subject = "Updated subject";
            newTextAnnotation.Contents = "Updated sample contents for the annotation";
            // Modify annotations in the PDF file
            annotationEditor.ModifyAnnotations(1, 1, newTextAnnotation);
            // Save PDF document
            annotationEditor.Save(dataDir + "ModifyAnnotations_out.pdf");
        }
    }
}
```
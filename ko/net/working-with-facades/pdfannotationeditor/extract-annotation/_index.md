---
title: PDF에서 주석 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/extract-annotation/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "새로운 주석 추출 기능을 통해 PDF 문서의 잠재력을 활용하세요. 이 기능은 Aspose.PDF for .NET을 사용하여 주석을 XFDF 형식으로 원활하게 추출할 수 있게 해줍니다. 이 기능은 특정 주석 유형을 쉽게 검색할 수 있게 하여 문서 관리 및 협업 효율성을 향상시킵니다. 중요한 주석 데이터를 손쉽게 추출하고 저장하여 PDF 워크플로를 간소화하는 방법을 알아보세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 메서드는 PDF 파일에서 주석을 추출할 수 있게 해줍니다. 주석을 추출하려면 [PdfAnnotationEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그 후, PDF 파일에서 추출할 주석 유형의 열거형을 생성해야 합니다.

그런 다음 [ExtractAnnotations](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 메서드를 사용하여 주석을 ArrayList로 추출할 수 있습니다. 그 후, 이 목록을 반복하여 개별 주석을 가져올 수 있습니다. 마지막으로, [PdfAnnotationEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor) 객체의 [Save](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 주석을 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```
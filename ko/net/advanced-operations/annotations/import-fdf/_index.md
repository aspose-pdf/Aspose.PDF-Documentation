---
title: C#를 통해 FDF 형식 주석을 PDF로 가져오기
linktitle: C#를 통해 FDF 형식 주석을 PDF로 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/import-fdf/
description: 기존 Form.ImportFdf() 또는 PdfAnnotationEditor.ImportAnnotationsFromFdf() 메서드를 사용하여 Aspose.PDF for .NET으로 FDF 형식 주석을 PDF로 가져옵니다.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "FDF 형식 주석을 PDF 파일로 원활하게 가져와 Aspose.PDF for .NET을 사용하여 PDF 관리 기능을 향상시킵니다. Form.ImportFdf() 및 PdfAnnotationEditor.ImportAnnotationsFromFdf() 메서드를 사용하면 경량 FDF 파일에서 양식 데이터와 주석을 PDF 문서에 손쉽게 통합하여 데이터 제출 및 주석 프로세스를 간소화할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

FDF (Forms Data Format)는 PDF 문서에서 양식 데이터와 주석을 저장하고 전송하는 파일 형식입니다. 이는 원본 PDF 파일의 전체 콘텐츠 없이 양식 필드 값이나 주석만 포함하는 경량 PDF 버전입니다. FDF 파일은 서버에 양식 데이터를 제출할 때나 전체 PDF 파일을 전송할 필요 없이 주석을 교환할 때 자주 사용됩니다. 이들은 PDF로 다시 가져와 양식 필드를 채우거나 주석을 적용할 수 있습니다.

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor/) 클래스는 FDF 파일에서 주석을 가져오는 작업을 위한 메서드를 포함하고 있습니다. [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) 메서드는 FDF 문서에서 PDF 파일로 주석을 가져오는 기능을 제공합니다.

또한, [Class Form](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/)에는 [Form.ImportFdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/importfdf/) 메서드가 포함되어 있으며, 이는 FDF 파일의 필드 내용을 가져와 새로운 PDF에 넣습니다.

다음 코드 스니펫은 Form.ImportFdf() 메서드를 사용하여 FDF 형식 주석을 PDF로 가져오는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

다음 코드 스니펫은 PdfAnnotationEditor.ImportAnnotationsFromFdf() 메서드를 사용하여 FDF 형식 주석을 PDF로 가져오는 방법을 보여줍니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```
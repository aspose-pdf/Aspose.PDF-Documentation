---
title: Import and Export Annotations to XFDF
linktitle: Import and Export Annotations to XFDF
type: docs
weight: 40
url: /net/import-export-xfdf/
description: XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다. C# 및 Aspose.PDF for .NET 라이브러리를 사용합니다.
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
    "alternativeHeadline": "XFDF 파일로 주석 데이터 가져오기 및 내보내기 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, XFDF로 가져오기 내보내기",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "XFDF 형식으로 주석을 가져오고 내보낼 수 있습니다. C# 및 Aspose.PDF for .NET 라이브러리를 사용합니다."
}
</script>
{{% alert color="primary" %}}

XFDF는 XML Forms Data Format를 의미합니다. 이는 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 양식에 포함된 양식 데이터나 주석을 표현하는 데 사용됩니다. XFDF는 여러 가지 목적으로 사용될 수 있지만, 우리의 경우에는 다른 컴퓨터나 서버 등으로 양식 데이터나 주석을 보내거나 받거나, 양식 데이터나 주석을 보관하는 데 사용될 수 있습니다. 이 글에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려하고 있으며 XFDF 파일로 주석 데이터를 가져오고 내보낼 수 있는 방법을 살펴볼 것입니다.

{{% /alert %}}

**Aspose.PDF for .NET**은 PDF 문서를 편집할 때 풍부한 기능을 제공하는 컴포넌트입니다. 우리가 알다시피, XFDF는 PDF 양식 조작의 중요한 측면이며, Aspose.PDF for .NET의 Aspose.Pdf.Facades 네임스페이스는 이를 매우 잘 고려하고 있으며, XFDF 파일로 주석 데이터를 가져오고 내보내는 메소드를 제공하고 있습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내는 두 가지 메소드를 포함하고 있습니다.
[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내는 두 가지 방법을 포함합니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 조각은 XFDF 파일로 주석을 내보내는 방법을 보여줍니다:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;


namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // 문서 디렉토리 경로입니다.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// XFDF 파일에서 주석 가져오기
        /// Adobe Acrobat에 의해 생성된 XML Forms Data Format (XFDF) 파일;
        /// 페이지 폼 요소의 설명과 그 값들, 예를 들어 텍스트 필드의 이름과 값들을 저장합니다;
        /// PDF 문서로 가져올 수 있는 양식 데이터를 저장하는 데 사용됩니다.
        /// PdfAnnotationEditor 클래스의 ImportAnnotationsFromXfdf 메소드를 사용하여 XFDF 파일에서 주석 데이터를 가져올 수 있습니다.
        /// </summary>       
   
        public static void ExportAnnotationXFDF()
        {
            // PdfAnnotationEditor 객체 생성
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // PDF 문서를 Annotation Editor에 바인드
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));
           
            // 주석 내보내기
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
다음 코드 스니펫은 XFDF 파일에 주석을 가져오는 방법을 설명합니다:

```csharp
public static void ImportAnnotationXFDF()
{
    // PdfAnnotationEditor 객체 생성
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // 새 PDF 문서 생성
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // 주석 가져오기
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // 출력 PDF 저장
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## 주석을 한 번에 내보내기/가져오기하는 또 다른 방법

아래 코드에서 ImportAnnotations 메소드는 다른 PDF 문서에서 직접 주석을 가져올 수 있습니다.

```csharp
        /// <summary>
        /// ImportAnnotations 메소드는 다른 PDF 문서에서 직접 주석을 가져올 수 있음
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // PdfAnnotationEditor 객체 생성
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // 새 PDF 문서 생성
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // Annotation Editor는 여러 PDF 문서에서 주석을 가져올 수 있지만,
            // 이 예제에서는 하나만 사용합니다.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // 출력 PDF 저장
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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
```


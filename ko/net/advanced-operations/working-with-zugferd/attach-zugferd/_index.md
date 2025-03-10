---
title: PDF/3-A 준수 PDF 생성 및 C#에서 ZUGFeRD 인보이스 첨부
linktitle: PDF에 ZUGFeRD 첨부
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/attach-zugferd/
description: ZUGFeRD와 함께 PDF 문서를 생성하는 방법을 배우세요 Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "개발자가 PDF/A-3B 준수 PDF 문서를 생성하고 C#을 사용하여 ZUGFeRD 인보이스를 원활하게 첨부할 수 있는 새로운 기능을 발견하세요. 이 기능은 PDF 파일에 인보이스 메타데이터를 포함하는 과정을 단순화하여 문서의 장기 보존과 전자 인보이스 표준 준수를 보장합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF에 ZUGFeRD 첨부

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

ZUGFeRD를 PDF에 첨부하기 위해 다음 단계를 권장합니다:

* 입력 및 출력 PDF 파일이 위치한 폴더를 가리키는 경로 변수를 정의합니다.
* 경로에서 기존 PDF 파일(예: "ZUGFeRD-test.pdf")을 로드하여 문서 객체를 생성합니다.
* ZUGFeRD 표준에 준하는 인보이스 메타데이터를 포함하는 "factur-x.xml"이라는 다른 파일의 경로와 설명을 제공하여 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) 객체를 생성합니다.
* 설명, MIME 유형 및 AF 관계와 같은 속성을 파일 사양 객체에 추가합니다. AF 관계는 포함된 파일이 PDF 문서와 어떻게 관련되는지를 나타냅니다. 이 경우 "Alternative"로 설정되어 있으며, 이는 포함된 파일이 PDF 콘텐츠의 대체 표현임을 의미합니다.
* 파일 사양 객체를 문서의 포함된 파일 컬렉션에 추가합니다. 파일 이름은 ZUGFeRD 표준에 따라 지정해야 하며, 예를 들어 "factur-x.xml"입니다.
* 문서를 PDF/A-3B 형식으로 변환합니다. PDF/A-3B는 전자 문서의 장기 보존을 보장하는 PDF의 하위 집합입니다. PDF/A-3B는 PDF 문서에 모든 형식의 파일을 포함할 수 있습니다.
* 변환된 문서를 새 PDF 파일(예: "ZUGFeRD-res.pdf")로 저장합니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

변환 메서드는 스트림, PDF 형식 및 변환 오류 작업을 매개변수로 사용합니다. 스트림 매개변수는 변환 로그를 저장하는 데 사용할 수 있습니다. 변환 오류 작업 매개변수는 변환 중 오류가 발생할 경우 수행할 작업을 지정합니다. 이 경우 "Delete"로 설정되어 있으며, 이는 PDF/A-3B 형식에 부합하지 않는 모든 요소가 문서에서 삭제됨을 의미합니다.
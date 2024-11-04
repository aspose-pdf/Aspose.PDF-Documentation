---
title: Fill AcroForm - Fill PDF Form using C#
linktitle: Fill AcroForm
type: docs
weight: 20
url: /net/fill-form/
keywords: Fill PDF Form C#
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 양식을 채울 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Fill AcroForm",
    "alternativeHeadline": "How to fill AcroForm in PDf",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, fill acroform",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 양식을 채울 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## PDF 문서에서 폼 필드 채우기

폼 필드를 채우려면 Document 객체의 Form 컬렉션에서 필드를 가져온 다음, 필드의 Value 속성을 사용하여 필드 값 설정합니다.

이 예제는 TextBoxField를 선택하고 Value 속성을 사용하여 그 값을 설정합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 문서 열기
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// 필드 가져오기
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// 필드 값 수정
textBoxField.Value = "필드에 채워질 값";
dataDir = dataDir + "FillFormField_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```


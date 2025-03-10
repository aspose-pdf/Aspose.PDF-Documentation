---
title: XFA 양식 작업하기
linktitle: XFA 양식
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/xfa-forms/
description: Aspose.PDF for .NET API를 사용하면 PDF 문서에서 XFA 및 XFA Acroform 필드와 작업할 수 있습니다. Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NET는 이제 XFA 양식 작업을 위한 고급 기능을 제공하여 개발자가 PDF 문서 내에서 XFA Acroform 필드를 채우고, 변환하고, 관리할 수 있도록 합니다. 이 기능은 동적 양식의 조작을 단순화하여 필드 값 및 속성에 원활하게 접근할 수 있도록 하며, XFA에서 표준 AcroForms로의 효율적인 변환을 제공합니다. 복잡한 양식 구조를 처리하기 위한 이 강력한 솔루션으로 PDF 처리 워크플로를 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET API를 사용하면 PDF 문서에서 XFA 및 XFA Acroform 필드와 작업할 수 있습니다. Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

동적 양식은 XFA로 알려진 XML 사양을 기반으로 하며, "XML 양식 아키텍처"입니다. 또한 동적 XFA 양식을 표준 Acroform으로 변환할 수 있습니다. 양식에 대한 정보(PDF와 관련하여)는 매우 모호합니다. 필드가 존재하며 속성과 JavaScript 이벤트가 있지만 렌더링에 대한 명시는 없습니다. XFA 양식의 객체는 문서를 로드할 때 그려집니다.

{{% /alert %}}

Form 클래스는 정적 AcroForm을 처리할 수 있는 기능을 제공하며, Form 클래스의 GetFieldFacade(..) 메서드를 사용하여 특정 필드 인스턴스를 가져올 수 있습니다. 그러나 XFA 필드는 Form.GetFieldFacade(..) 메서드를 통해 접근할 수 없습니다. 대신 [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa)를 사용하여 필드 값을 가져오거나 설정하고 XFA 필드 템플릿을 조작하십시오(필드 속성 설정).

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## XFA 필드 채우기

다음 코드 스니펫은 XFA 양식에서 필드를 채우는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## XFA를 Acroform으로 변환

{{% alert color="primary" %}}

온라인으로 시도하기
Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

동적 양식은 XFA로 알려진 XML 사양을 기반으로 하며, "XML 양식 아키텍처"입니다. 양식에 대한 정보(PDF와 관련하여)는 매우 모호합니다. 필드가 존재하며 속성과 JavaScript 이벤트가 있지만 렌더링에 대한 명시는 없습니다.

현재 PDF는 데이터와 PDF 양식을 통합하기 위한 두 가지 방법을 지원합니다:

- AcroForms(아크로뱃 양식이라고도 함), PDF 1.2 형식 사양에 도입되어 포함되었습니다.
- Adobe XML 양식 아키텍처(XFA) 양식, PDF 1.5 형식 사양에 선택적 기능으로 도입되었습니다( XFA 사양은 PDF 사양에 포함되어 있지 않으며, 단지 참조만 됩니다.)

XFA 양식의 페이지를 추출하거나 조작할 수 없습니다. 왜냐하면 양식 내용이 XFA 양식을 표시하거나 렌더링하려고 하는 애플리케이션 내에서 런타임에 생성되기 때문입니다. Aspose.PDF는 개발자가 XFA 양식을 표준 AcroForms로 변환할 수 있는 기능을 제공합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## XFA 필드 속성 가져오기

필드 속성에 접근하려면 먼저 Document.Form.XFA.Template를 사용하여 필드 템플릿에 접근하십시오. 다음 코드 스니펫은 XFA 양식 필드의 X 및 Y 좌표를 가져오는 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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
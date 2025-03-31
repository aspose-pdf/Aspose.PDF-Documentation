---
title: AcroForm 추출 - C#에서 PDF의 양식 데이터 추출
linktitle: AcroForm 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/extract-form/
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에서 양식을 추출합니다. PDF 파일의 개별 필드에서 값을 가져옵니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm - Extract Form Data from PDF in C#",
    "alternativeHeadline": "Effortlessly Extract PDF Form Data Using C#",
    "abstract": "Aspose.PDF for .NET의 새로운 AcroForm 추출 기능은 개발자가 PDF 문서에서 양식 데이터를 쉽게 추출할 수 있도록 합니다. 이 기능을 통해 사용자는 PDF 내의 개별 필드 또는 모든 필드에서 값을 검색할 수 있어 C# 애플리케이션에서 데이터 관리 및 조작 기능을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract form data, PDF in C#, Aspose.PDF for .NET, AcroForm extraction, get field values PDF, PDF form fields, individual field value, get fields in region, manipulate PDF forms, C# PDF library",
    "wordcount": "673",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에서 양식을 추출합니다. PDF 파일의 개별 필드에서 값을 가져옵니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 양식에서 데이터 추출

### PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오려면 모든 양식 필드를 탐색한 다음 Value 속성을 사용하여 값을 가져와야 합니다. Form 컬렉션에서 각 필드를 가져오고, 기본 필드 유형인 Field에 접근하여 그 Value 속성에 접근합니다.

다음 C# 코드 스니펫은 PDF 문서의 모든 필드에서 값을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValuesFromFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValuesFromAllFields.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

### PDF 문서의 개별 필드에서 값 가져오기

양식 필드의 Value 속성을 사용하면 특정 필드의 값을 가져올 수 있습니다. 값을 가져오려면 Document 객체의 Form 컬렉션에서 양식 필드를 가져옵니다. 이 C# 예제는 [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)를 선택하고 Value 속성을 사용하여 값을 검색합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValueFromField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get a field
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            // Get field value
            Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
            Console.WriteLine("Value : {0} ", textBoxField.Value);
        }
    }
}
```

제출 버튼의 URL을 가져오려면 다음 코드 줄을 사용하십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSubmitFormActionUrl()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get the SubmitFormAction from the form field
        if (document.Form[1].OnActivated is Aspose.Pdf.Annotations.SubmitFormAction act)
        {
            // Output the URL of the SubmitFormAction
            Console.WriteLine(act.Url.Name);
        }
    }
}
```

### PDF 파일의 특정 영역에서 양식 필드 가져오기

때때로 문서에서 양식 필드가 어디에 있는지 알 수 있지만 이름은 모를 수 있습니다. 예를 들어, 인쇄된 양식의 도면만 가지고 있는 경우입니다. Aspose.PDF for .NET를 사용하면 문제가 되지 않습니다. PDF 파일의 특정 영역에 어떤 필드가 있는지 확인할 수 있습니다. PDF 파일의 특정 영역에서 양식 필드를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 사용하여 PDF 파일을 엽니다.
1. 문서의 Forms 컬렉션에서 양식을 가져옵니다.
1. 직사각형 영역을 지정하고 Form 객체의 GetFieldsInRect 메서드에 전달합니다. Fields 컬렉션이 반환됩니다.
1. 이를 사용하여 필드를 조작합니다.

다음 C# 코드 스니펫은 PDF 파일의 특정 직사각형 영역에서 양식 필드를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldsFromRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf"))
    {
        // Create rectangle object to get fields in that area
        var rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

        // Get the PDF form
        var form = document.Form;

        // Get fields in the rectangular area
        var fields = form.GetFieldsInRect(rectangle);

        // Display Field names and values
        foreach (var field in fields)
        {
            // Display image placement properties for all placements
            Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
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
---
title: 버튼 옵션 값 가져오기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/get-button-option-value/
description: 이 섹션에서는 Form 클래스를 사용하여 Aspose.PDF Facades로 버튼 옵션 값을 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Aspose.PDF Facades를 사용하여 기존 PDF 파일에서 버튼 옵션 값을 효율적으로 검색하는 방법을 알아보세요. Form 클래스의 GetButtonOptionValues 및 GetButtonOptionCurrentValue 메서드를 사용하면 라디오 버튼의 모든 사용 가능한 옵션과 현재 선택된 값을 쉽게 얻을 수 있어 PDF 양식 관리 기능을 향상시킬 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에서 버튼 옵션 값 가져오기

라디오 버튼은 다양한 옵션을 표시하는 방법을 제공합니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 특정 라디오 버튼에 대한 모든 버튼 옵션 값을 가져올 수 있게 해줍니다. [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) 메서드를 사용하여 이러한 값을 가져올 수 있습니다. 이 메서드는 라디오 버튼의 이름을 입력 매개변수로 요구하며 Hashtable을 반환합니다. 이 Hashtable을 반복하여 옵션 값을 얻을 수 있습니다. 다음 코드 스니펫은 기존 PDF 파일에서 버튼 옵션 값을 가져오는 방법을 보여줍니다.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## 기존 PDF 파일에서 현재 버튼 옵션 값 가져오기

라디오 버튼은 옵션 값을 설정하는 방법을 제공하지만, 한 번에 하나만 선택할 수 있습니다. 현재 선택된 옵션 값을 가져오려면 [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) 메서드를 사용할 수 있습니다. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 클래스는 이 메서드를 제공합니다. [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) 메서드는 라디오 버튼 이름을 입력 매개변수로 요구하며 값을 문자열로 반환합니다. 다음 코드 스니펫은 기존 PDF 파일에서 현재 버튼 옵션 값을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```
---
title: AcroForm 채우기 - C#을 사용하여 PDF 양식 채우기
linktitle: AcroForm 채우기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/fill-form/
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
    "headline": "Fill AcroForm - Fill PDF Form using C#",
    "alternativeHeadline": "Effortlessly Fill PDF Forms with C# Integration",
    "abstract": "Aspose.PDF for .NET 라이브러리의 새로운 AcroForm 채우기 기능은 개발자가 C#을 사용하여 프로그래밍 방식으로 PDF 양식을 효율적으로 채울 수 있도록 합니다. 이 기능은 양식 필드를 채우는 과정을 간소화하여 PDF 문서 관리에서 생산성과 정확성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Fill PDF Form, AcroForm, Aspose.PDF for .NET, fill PDF forms C#, TextBoxField, PDF document generation, form field value, PDF manipulation library, fill form field, C# PDF library",
    "wordcount": "355",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2025-04-11",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 양식을 채울 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서에서 양식 필드 채우기

양식 필드를 채우려면 Document 객체의 Form 컬렉션에서 필드를 가져오고 필드 유형에 적합한 속성을 사용하여 값을 설정합니다(예: 텍스트 필드의 경우 Value, 체크 박스의 경우 Checked, 목록 상자의 경우 Selected).

이 예제에서는 다양한 필드를 선택하고 해당 속성을 설정합니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf"))
    {
        // Set value for TextBoxField
        var textBoxField = document.Form["textField"] as Aspose.Pdf.Forms.TextBoxField;
        textBoxField.Value = "Value to be filled in the field";

        // Add option for ListBoxField and select it
        var listBoxField = document.Form["listField"] as Aspose.Pdf.Forms.ListBoxField;
        listBoxField.AddOption("Orange");
        listBoxField.Selected = listBoxField.Options.Count;

        // Set check for CheckboxField
        var checkboxField = document.Form["checkField"] as Aspose.Pdf.Forms.CheckboxField;
        checkboxField.Checked = true;

        // Set check for first option of RadioButtonField
        var radioField = document.Form["radioGroup"] as Aspose.Pdf.Forms.RadioButtonField;
        radioField.Options[1].Selected = true;

        // Save PDF document
        document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
    }
}
```

{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf");

    // Set value for TextBoxField
    var textBoxField = document.Form.OfType<Aspose.Pdf.Forms.TextBoxField>().First();
    textBoxField.Value = "Value to be filled in the field";

    // Add option for ListBoxField and select it
    var listBoxField = document.Form.OfType<Aspose.Pdf.Forms.ListBoxField>().First();
    listBoxField.AddOption("Orange");
    listBoxField.Selected = listBoxField.Options.Count;

    // Set check for CheckboxField
    var checkboxField = document.Form.OfType<Aspose.Pdf.Forms.CheckboxField>().First();
    checkboxField.Checked = true;

    // Set check for first option of RadioButtonField
    var radioField = document.Form.OfType<Aspose.Pdf.Forms.RadioButtonField>().First();
    radioField.Options[1].Selected = true;

    // Save PDF document
    document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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
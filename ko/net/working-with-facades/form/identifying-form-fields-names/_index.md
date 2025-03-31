---
title: 양식 필드 이름 식별
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades를 사용하면 Form 클래스를 통해 양식 필드 이름을 식별할 수 있습니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "Aspose.PDF for .NET의 기능은 PDF 문서에서 양식 필드 이름을 식별하는 과정을 단순화합니다. Form 클래스와 그 속성을 활용하여 사용자는 필드 이름을 쉽게 검색하고 해당 필드와 함께 표시할 수 있어 PDF 양식 작성 및 편집을 간소화합니다. 이 기능은 Adobe Designer와 같은 외부 도구에서 생성된 양식 작업 시 정확한 필드 조작을 보장하여 사용자 경험을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[Aspose.PDF for .NET](/pdf/ko/net/)은 이미 생성된 PDF 양식을 만들고, 편집하고, 채울 수 있는 기능을 제공합니다. [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades) 네임스페이스에는 [Form](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form) 클래스가 포함되어 있으며, 이 클래스에는 [FillField](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/methods/fillfield/index)라는 함수가 있어 두 개의 인수, 즉 필드 이름과 필드 값을 받습니다. 따라서 양식 필드를 채우기 위해서는 정확한 양식 필드 이름을 알고 있어야 합니다.

## 구현 세부사항

우리는 종종 Adobe Designer와 같은 도구에서 생성된 양식을 채워야 하는 상황에 직면하게 되며, 이때 양식 필드 이름이 무엇인지 확실하지 않을 수 있습니다. 따라서 양식 필드를 채우기 위해 먼저 모든 PDF 양식 필드의 이름을 읽어야 합니다. [Form](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form) 클래스는 모든 필드의 이름을 반환하는 [FieldNames](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/properties/fieldnames)라는 속성을 제공하며, PDF에 필드가 없으면 null을 반환합니다. 그러나 이 속성을 사용할 때 PDF 양식의 모든 필드 이름을 얻지만, 어떤 이름이 어떤 필드에 해당하는지 확실하지 않을 수 있습니다.

이 문제에 대한 해결책으로 각 필드의 외관 속성을 사용할 것입니다. Form 클래스에는 [GetFieldFacade](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/methods/getfieldfacade)라는 함수가 있어 위치, 색상, 테두리 스타일, 글꼴, 목록 항목 등을 포함한 속성을 반환합니다. 이러한 값을 저장하기 위해 [FormFieldFacade](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/FormFieldFacade) 클래스를 사용해야 하며, 이 클래스는 필드의 시각적 속성을 기록하는 데 사용됩니다. 이러한 속성을 얻으면 각 필드 아래에 필드 이름을 표시하는 텍스트 필드를 추가할 수 있습니다.

{{% alert color="primary" %}}
이 시점에서 "텍스트 필드를 추가할 위치를 어떻게 결정할 것인가?"라는 질문이 제기됩니다.
{{% /alert %}}

{{% alert color="primary" %}}
이 문제에 대한 해결책은 [FormFieldFacade](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/FormFieldFacade) 클래스의 Box 속성으로, 이 속성은 필드의 위치를 보유합니다. 이러한 값을 사각형 유형의 배열에 저장하고 이 값을 사용하여 새 텍스트 필드를 추가할 위치를 식별해야 합니다.
{{% /alert %}}

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades) 네임스페이스에는 PDF 양식을 조작할 수 있는 [FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/FormEditor)라는 클래스가 있습니다. PDF 양식을 열고, 기존 양식 필드 아래에 텍스트 필드를 추가하고, 새 이름으로 PDF 양식을 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```
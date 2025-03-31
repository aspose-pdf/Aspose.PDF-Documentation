---
title: 필드 외관 및 속성
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/changing-field-appearance-and-attributes/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 필드 외관 및 속성을 변경하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "Aspose.Pdf.Facades 네임스페이스의 FormEditor 클래스에서 도입된 기능은 사용자가 PDF의 양식 필드의 외관과 속성을 모두 사용자 정의할 수 있도록 합니다. SetFieldAppearance 및 SetFieldAttributes와 같은 메서드를 활용하여 개발자는 필드 한계를 포함한 시각적 요소와 동작을 쉽게 수정하여 사용자 상호작용 및 데이터 입력 효율성을 향상시킬 수 있습니다. 이 기능은 특정 애플리케이션 요구에 맞게 설계된 양식 필드의 유연성을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/FormEditor) 클래스는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades)의 양식 필드의 외관뿐만 아니라 필드의 동작을 변경할 수 있게 해줍니다. 이 기사에서는 FormEditor 클래스를 사용하여 필드 외관, 필드 속성 및 필드 한계를 변경하는 방법을 살펴보겠습니다.

{{% /alert %}}

## 구현 세부정보

[SetFieldAppearance](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) 메서드는 양식 필드의 외관을 변경하는 데 사용됩니다. 이 메서드는 AnnotationFlag를 매개변수로 사용합니다. AnnotationFlag는 Hidden 또는 NoRotate와 같은 다양한 멤버를 가진 열거형입니다.

[SetFieldAttributes](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) 메서드는 양식 필드의 속성을 변경하는 데 사용됩니다. 이 메서드에 전달되는 매개변수는 ReadOnly 또는 Required와 같은 멤버를 포함하는 PropertyFlag 열거형입니다.

[FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/FormEditor) 클래스는 필드 한계를 설정하는 메서드도 제공합니다. 이 메서드는 필드가 얼마나 많은 문자를 채울 수 있는지를 알려줍니다. 아래 코드 스니펫은 이러한 모든 메서드를 사용하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```
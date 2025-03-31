---
title: 텍스트 상자 필드에서 텍스트 정렬
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/justify-text-in-a-textbox-field/
description: 이 문서에서는 Form Class를 사용하여 텍스트 상자 필드에서 텍스트를 정렬하는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "이 기능은 사용자가 Aspose.Pdf.Facades 네임스페이스의 FormEditor 클래스를 사용하여 PDF 문서의 텍스트 상자 필드 내에서 텍스트를 정렬할 수 있도록 합니다. AlignJustified 옵션을 활용하여 사용자는 기능성을 유지하면서도 시각적으로 매력적인 텍스트 정렬을 달성할 수 있습니다. 활성 입력 중에는 정렬된 정렬이 지원되지 않지만, 이는 PDF 파일의 양식 데이터 프레젠테이션을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

이 문서에서는 PDF 파일의 텍스트 상자 필드에서 텍스트를 정렬하는 방법을 보여줍니다.

{{% /alert %}}

## 구현 세부사항

[FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor) 클래스는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades) 에서 PDF 양식 필드를 장식할 수 있는 기능을 제공합니다. 이제 텍스트 상자 필드에서 텍스트를 정렬해야 하는 경우, [FormFieldFacade](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formfieldfacade) 열거형의 [AlignJustified](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) 값을 사용하고 [FormEditor.DecorateField](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/decoratefield/index) 메서드를 호출하여 쉽게 달성할 수 있습니다. 아래 예제에서는 먼저 [Form](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form) 클래스의 [FillField](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/form/methods/fillfield/index) 메서드를 사용하여 텍스트 상자 필드를 채운 후, FormEditor 클래스를 사용하여 텍스트 상자 필드의 텍스트를 정렬합니다. 다음 코드 조각은 텍스트 상자 필드에서 텍스트를 정렬하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
PDF에서는 정렬된 정렬이 지원되지 않기 때문에 텍스트 상자 필드에 텍스트를 입력할 때 텍스트가 왼쪽으로 정렬됩니다. 그러나 필드가 비활성 상태일 때 텍스트는 정렬됩니다.
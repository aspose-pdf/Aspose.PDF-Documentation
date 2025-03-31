---
title: FormEditor 클래스의 기능 탐색
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/exploring-features-of-formeditor-class/
description: Aspose.PDF for .NET 라이브러리를 사용하여 FormEditor 클래스의 기능을 탐색하는 세부 정보를 배울 수 있습니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Exploring features of FormEditor class",
    "alternativeHeadline": "Enhancing PDF Forms with FormEditor Class",
    "abstract": "상호작용 PDF 양식을 손쉽게 조작할 수 있도록 설계된 Aspose.PDF for .NET 라이브러리 내에서 FormEditor 클래스의 향상된 기능을 발견하십시오. 이 기능은 개발자가 양식 필드를 원활하게 추가, 편집 및 구성할 수 있도록 하여 수정 프로세스를 간소화하는 사용자 친화적인 방법을 제공합니다. FormEditor의 포괄적인 기능을 활용하여 PDF 양식 처리를 최적화하고 문서 워크플로를 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "358",
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
    "url": "/net/exploring-features-of-formeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/exploring-features-of-formeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

PDF 문서에는 때때로 AcroForm으로 알려진 상호작용 양식이 포함되어 있습니다. 이는 웹 페이지에서 사용되는 양식과 유사합니다. 이러한 양식에는 텍스트 상자, 체크 박스 및 버튼 등 다양한 유형의 컨트롤이 포함되어 있습니다. PDF 파일로 작업하는 개발자는 때때로 이러한 양식을 편집해야 할 수도 있습니다. 이 기사에서는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)가 이를 가능하게 하는 방법에 대해 자세히 살펴보겠습니다.

{{% /alert %}}

## 구현 세부정보

개발자는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)를 사용하여 PDF 문서에 새로운 양식 및 양식 필드를 추가할 뿐만 아니라 기존 필드를 편집할 수 있습니다. 이 기사의 범위는 양식 편집과 관련된 [Aspose.PDF for .NET](/pdf/ko/net/)의 기능으로 제한됩니다.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스는 개발자가 양식 필드를 편집할 수 있도록 하는 대부분의 메서드와 속성을 포함하고 있습니다. 새로운 필드를 추가할 뿐만 아니라 기존 필드를 제거하고, 한 필드를 다른 위치로 이동하고, 필드 이름이나 속성을 변경하는 등의 작업을 수행할 수 있습니다. 이 클래스에서 제공하는 기능 목록은 매우 포괄적이며, 이 클래스를 사용하여 양식 필드로 작업하는 것은 매우 쉽습니다.

이러한 메서드는 두 가지 주요 범주로 나눌 수 있으며, 하나는 필드를 조작하는 데 사용되고, 다른 하나는 이러한 필드의 새로운 속성을 설정하는 데 사용됩니다. 첫 번째 범주에 포함될 수 있는 메서드는 AddField, AddListItem, RemoveListItem, CopyInnerField, CopyOuterField, DelListItem, MoveField, RemoveField 및 RenameField 등이 있습니다. 두 번째 범주에는 SetFieldAlignment, SetFieldAppearance, SetFieldAttribute, SetFieldLimit, SetFieldScript 메서드가 포함될 수 있습니다. 다음 코드 스니펫은 FormEditor 클래스의 일부 메서드가 작동하는 모습을 보여줍니다:


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExploringFormEditorFeatures()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "inFile.pdf"))
    {
        // Create instance of FormEditor
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            // Add field in the PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "field1", 1, 300, 500, 350, 525);

            // Add List field in PDF file
            editor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225);

            // Add list items
            editor.AddListItem("field2", "item 1");
            editor.AddListItem("field2", "item 2");

            // Add submit button
            editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http:// Testwebsite.com/testpage", 200, 200, 250, 225);

            // Delete list item
                editor.DelListItem("field2", "item 1");

            // Move field to new position
            editor.MoveField("field1", 10, 10, 50, 50);

            // Remove existing field from the PDF
            editor.RemoveField("field1");

            // Rename an existing field
            editor.RenameField("field1", "newfieldname");

            // Reset all visual attributes to empty value
            editor.ResetFacade();

            // Set the alignment style of a text field
            editor.SetFieldAlignment("field1", Aspose.Pdf.Facades.FormFieldFacade.AlignLeft);

            // Set appearance of the field
            editor.SetFieldAppearance("field1", Aspose.Pdf.Annotations.AnnotationFlags.NoRotate);

            // Set field attributes i.e. ReadOnly, Required
            editor.SetFieldAttribute("field1", Aspose.Pdf.Facades.PropertyFlag.ReadOnly);

            // Set field limit
            editor.SetFieldLimit("field1", 25);

            // Save modifications in the output file
            editor.Save(dataDir + "FormEditorFeatures2_out.pdf");                    
        }
    }
}
```
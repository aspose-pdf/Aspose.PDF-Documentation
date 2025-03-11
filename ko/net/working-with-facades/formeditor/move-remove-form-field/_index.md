---
title: 양식 필드 이동 및 제거
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/move-remove-form-field/
description: PDF에서 양식 필드를 관리하는 방법을 탐색하고, 이를 이동하거나 제거하는 방법을 Aspose.PDF for .NET을 사용하여 알아보세요.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "FormEditor 클래스의 양식 필드 이동 및 제거 기능은 사용자가 기존 PDF 문서 내에서 양식 필드를 원활하게 재배치하고 제거할 수 있도록 합니다. MoveField 및 RemoveField 메서드를 활용하여 사용자는 양식을 효율적으로 사용자 정의하고, 사용성과 문서 관리를 향상시킬 수 있습니다. 이 기능은 사용자가 광범위한 기술 전문 지식 없이도 PDF 레이아웃을 최적화할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에서 양식 필드를 새 위치로 이동하기

양식 필드를 새 위치로 이동하려면 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) 메서드를 사용할 수 있습니다. 필드 이름과 이 필드의 새 위치만 [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) 메서드에 제공하면 됩니다. 또한 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에서 양식 필드를 새 위치로 이동하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## 기존 PDF 파일에서 양식 필드 삭제하기

기존 PDF 파일에서 양식 필드를 삭제하려면 FormEditor 클래스의 RemoveField 메서드를 사용할 수 있습니다. 이 메서드는 필드 이름이라는 하나의 인수만 필요합니다. FormEditor 클래스의 객체를 생성하고, [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) 메서드를 호출하여 PDF에서 특정 필드를 제거한 다음 Save 메서드를 호출하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 양식 필드를 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## PDF에서 양식 필드 이름 변경하기

또한 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) 메서드를 사용하여 필드 이름을 변경할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```
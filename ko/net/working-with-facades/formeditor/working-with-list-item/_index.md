---
title: 목록 항목 작업
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/working-with-list-item/
description: 이 섹션에서는 FormEditor 클래스를 사용하여 Aspose.PDF Facades로 목록 항목 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Aspose.PDF for .NET의 목록 항목 기능으로 PDF 양식을 개선하세요. FormEditor 클래스를 사용하여 ListBox 필드에서 항목을 쉽게 추가하거나 삭제할 수 있어 동적이고 사용자 정의 가능한 입력이 가능합니다. 이 기능은 양식 관리를 간소화하여 귀하의 필요에 맞게 콘텐츠를 조정하는 것을 더 쉽게 만듭니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에 목록 항목 추가

[AddListItem](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/addlistitem) 메서드는 [ListBox](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/listboxfield) 필드에 항목을 추가할 수 있게 해줍니다. 첫 번째 인자는 필드 이름이고 두 번째 인자는 필드 항목입니다. 단일 필드 항목을 전달하거나 항목 목록을 포함하는 문자열 배열을 전달할 수 있습니다. 이 메서드는 [FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 PDF 파일에 목록 항목을 추가하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## 기존 PDF 파일에서 목록 항목 삭제

[DelListItem](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor/methods/dellistitem) 메서드는 [ListBox](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/listboxfield)에서 특정 항목을 삭제할 수 있게 해줍니다. 첫 번째 매개변수는 필드 이름이고 두 번째 매개변수는 목록에서 삭제하려는 항목입니다. 이 메서드는 [FormEditor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/formeditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 PDF 파일에서 목록 항목을 삭제하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```
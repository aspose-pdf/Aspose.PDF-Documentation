---
title: PDF 양식 필드 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/add-form-fields/
description: 이 주제는 FormEditor 클래스를 사용하여 Aspose.PDF Facades와 함께 양식 필드 작업하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "FormEditor 클래스를 사용하여 양식 필드를 추가함으로써 PDF 문서에 동적 상호작용을 향상시킵니다. 이 기능을 통해 텍스트 필드, URL이 있는 제출 버튼 및 푸시 버튼에 JavaScript 기능을 손쉽게 통합하여 PDF에서 사용자 입력 및 데이터 제출을 간소화할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일에 양식 필드 추가

기존 PDF 파일에 양식 필드를 추가하려면 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 메서드를 사용해야 합니다. 이 메서드는 추가하려는 필드의 유형과 필드의 이름 및 위치를 지정해야 합니다. [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 클래스의 객체를 생성하고, [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 메서드를 사용하여 PDF에 새 필드를 추가합니다. 또한 [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) 메서드를 사용하여 필드의 문자 수에 제한을 지정할 수 있으며, 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 기존 PDF 파일에 양식 필드를 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## 기존 PDF 파일에 제출 버튼 URL 추가

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 메서드는 PDF 파일에서 제출 버튼의 URL을 설정할 수 있게 해줍니다. 이는 제출 버튼이 클릭될 때 데이터가 게시되는 URL입니다. 예제 코드에서는 URL, 필드의 이름, 추가할 페이지 번호 및 버튼 배치 좌표를 지정합니다. [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 메서드는 제출 버튼 필드의 이름과 URL을 요구합니다. 이 메서드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 제출 버튼 URL을 설정하는 방법을 보여줍니다.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## 푸시 버튼에 JavaScript 추가

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) 메서드는 PDF 파일의 푸시 버튼에 JavaScript를 추가할 수 있게 해줍니다. 이 메서드는 푸시 버튼의 이름과 JavaScript를 요구합니다. 이 메서드는 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 클래스에서 제공됩니다. 다음 코드 스니펫은 푸시 버튼에 JavaScript를 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```
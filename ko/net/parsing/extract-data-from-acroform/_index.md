---
title: AcroForm에서 C#을 사용하여 데이터 추출
linktitle: AcroForm에서 데이터 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/extract-data-from-acroform/
description: Aspose.PDF는 PDF 파일에서 양식 필드 데이터를 쉽게 추출할 수 있게 해줍니다. AcroForms에서 데이터를 추출하고 JSON, XML 또는 FDF 형식으로 저장하는 방법을 알아보세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "PDF 문서의 AcroForms에서 양식 필드 데이터를 추출하는 기능을 단순화하는 Aspose.PDF for .NET의 새로운 기능을 발견하세요. JSON, XML, FDF 및 XFDF 형식으로 데이터를 내보낼 수 있는 기능을 통해 사용자는 간결한 코드 예제를 활용하여 애플리케이션에 원활하게 통합하면서 양식 데이터를 효율적으로 관리할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 문서에서 양식 필드 추출

양식 필드를 생성하고 양식 필드를 채우는 것뿐만 아니라, Aspose.PDF for .NET은 PDF 파일에서 양식 필드 데이터 또는 양식 필드에 대한 정보를 쉽게 추출할 수 있게 해줍니다.

아래 샘플 코드에서는 PDF의 각 페이지를 반복하여 PDF의 모든 AcroForm에 대한 정보와 양식 필드 값을 추출하는 방법을 보여줍니다. 이 샘플 코드는 양식 필드의 이름을 미리 알지 못한다고 가정합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
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

양식 필드의 이름을 알고 있다면 Documents.Form 컬렉션의 인덱서를 사용하여 이 데이터를 빠르게 검색할 수 있습니다. 이 기능을 사용하는 방법에 대한 샘플 코드는 이 문서 하단을 참조하세요.

## 제목으로 양식 필드 값 검색

양식 필드의 Value 속성을 사용하면 특정 필드의 값을 가져올 수 있습니다. 값을 가져오려면 Document 객체의 Form 컬렉션에서 양식 필드를 가져옵니다. 이 예제에서는 TextBoxField를 선택하고 Value 속성을 사용하여 값을 검색합니다.

## PDF 문서에서 JSON으로 양식 필드 추출

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## PDF 파일에서 XML로 데이터 추출

Form 클래스는 ExportXml 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. XML로 데이터를 내보내려면 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXml 메서드를 호출해야 합니다. 마지막으로 FileStream 객체를 닫고 Form 객체를 폐기할 수 있습니다. 다음 코드 스니펫은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## PDF 파일에서 FDF로 데이터 내보내기

Form 클래스는 ExportFdf 메서드를 사용하여 PDF 파일에서 FDF 파일로 데이터를 내보낼 수 있게 해줍니다. FDF로 데이터를 내보내려면 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportFdf 메서드를 호출해야 합니다. 마지막으로 Form 클래스의 Save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 FDF 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## PDF 파일에서 XFDF로 데이터 내보내기

Form 클래스는 ExportXfdf 메서드를 사용하여 PDF 파일에서 XFDF 파일로 데이터를 내보낼 수 있게 해줍니다. XFDF로 데이터를 내보내려면 Form 클래스의 객체를 생성한 다음 FileStream 객체를 사용하여 ExportXfdf 메서드를 호출해야 합니다. 마지막으로 Form 클래스의 Save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 XFDF 파일로 데이터를 내보내는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```
---
title: AcroForm 수정
linktitle: AcroForm 수정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/modifing-form/
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 파일의 양식을 수정합니다. 기존 양식에서 필드를 추가하거나 제거하고, 필드 제한을 가져오고 설정하는 등의 작업을 수행할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "Aspose.PDF for .NET 라이브러리의 새로운 AcroForm 수정 기능을 통해 사용자는 기존 PDF 양식에서 필드를 원활하게 추가하거나 제거할 수 있습니다. 이 기능은 필드 제한 설정 및 사용자 경험을 개선하기 위한 글꼴 모양 사용자 지정을 포함하여 PDF 양식 관리 및 상호 작용을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 파일의 양식을 수정합니다. 기존 양식에서 필드를 추가하거나 제거하고, 필드 제한을 가져오고 설정하는 등의 작업을 수행할 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 필드 제한 가져오기 또는 설정하기

FormEditor 클래스의 SetFieldLimit(field, limit) 메서드를 사용하면 필드 제한, 즉 필드에 입력할 수 있는 최대 문자 수를 설정할 수 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFieldLimit()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save PDF document
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

유사하게, Aspose.PDF에는 DOM 접근 방식을 사용하여 필드 제한을 가져오는 메서드가 있습니다. 다음 코드 스니펫은 그 단계를 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
    {
        // Get the field and its maximum limit
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            Console.WriteLine("Limit: " + textBoxField.MaxLen);
        }
    }
}
```

다음 코드 스니펫을 사용하여 *Aspose.Pdf.Facades* 네임스페이스를 통해 동일한 값을 가져올 수도 있습니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingFacades()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## 양식 필드에 사용자 정의 글꼴 설정하기

Adobe PDF 파일의 양식 필드는 특정 기본 글꼴을 사용하도록 구성할 수 있습니다. Aspose.PDF의 초기 버전에서는 14개의 기본 글꼴만 지원되었습니다. 이후 릴리스에서는 개발자가 모든 글꼴을 적용할 수 있도록 허용했습니다. 양식 필드에 사용되는 기본 글꼴을 설정하고 업데이트하려면 DefaultAppearance(Font font, double size, Color color) 클래스를 사용하십시오. 이 클래스는 Aspose.Pdf.InteractiveFeatures 네임스페이스 아래에 있습니다. 이 객체를 사용하려면 Field 클래스의 DefaultAppearance 속성을 사용하십시오.

다음 코드 스니펫은 PDF 양식 필드에 대한 기본 글꼴을 설정하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFormFieldFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
    {
        // Get particular form field from document
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            // Create font object
            var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

            // Set the font information for form field
            field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
        }

        // Save PDF document
        document.Save(dataDir + "FormFieldFont14_out.pdf");
    }
}
```

## 기존 양식에서 필드 추가/제거하기

모든 양식 필드는 Document 객체의 Form 컬렉션에 포함되어 있습니다. 이 컬렉션은 Delete 메서드를 포함하여 양식 필드를 관리하는 다양한 메서드를 제공합니다. 특정 필드를 삭제하려면 Delete 메서드에 필드 이름을 매개변수로 전달한 다음 업데이트된 PDF 문서를 저장하십시오. 다음 코드 스니펫은 PDF 문서에서 특정 필드를 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
    {
        // Delete a particular field by name
        document.Form.Delete("textbox1");

        // Save PDF document
        document.Save(dataDir + "DeleteFormField_out.pdf");
    }
}
```

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
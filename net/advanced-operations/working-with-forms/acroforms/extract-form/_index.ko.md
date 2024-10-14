---
title: Extract AcroForm - PDF에서 AcroForm 데이터 추출하기 C#
linktitle: Extract AcroForm
type: docs
weight: 30
url: /net/extract-form/
keywords: extract form data from pdf c#
description: Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에서 양식을 추출하세요. PDF 파일의 개별 필드에서 값을 가져옵니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "PDF에서 AcroForm 추출하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, extract acroform",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에서 양식을 추출하세요. PDF 파일의 개별 필드에서 값을 가져옵니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 양식에서 데이터 추출

### PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오려면 모든 양식 필드를 탐색한 후 Value 속성을 사용하여 값을 가져와야 합니다. Form 컬렉션에서 각 필드를 가져오고, Field라고 하는 기본 필드 유형에서 Value 속성에 액세스합니다.

다음 C# 코드 스니펫은 PDF 문서의 모든 필드의 값을 가져오는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// 모든 필드에서 값 가져오기
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("필드 이름 : {0} ", formField.PartialName);
    Console.WriteLine("값 : {0} ", formField.Value);
}
```
### PDF 문서의 개별 필드에서 값 가져오기

폼 필드의 Value 속성을 사용하여 특정 필드의 값을 가져올 수 있습니다. 값을 가져오려면 Document 객체의 Form 컬렉션에서 폼 필드를 가져옵니다. 이 C# 예제에서는 [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield)를 선택하고 Value 속성을 사용하여 그 값을 검색합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// 필드 가져오기
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// 필드 값 가져오기
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

제출 버튼의 URL을 가져오려면 다음 코드 줄을 사용하세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### PDF 파일의 특정 지역에서 폼 필드 가져오기

문서에서 폼 필드가 어디에 있는지는 알지만 이름은 모를 때가 있습니다. 예를 들어, 인쇄된 양식의 도면만 가지고 있는 경우입니다. Aspose.PDF for .NET을 사용하면 문제가 되지 않습니다. PDF 파일의 주어진 영역에 어떤 필드가 있는지 알 수 있습니다. PDF 파일의 특정 지역에서 폼 필드를 가져오려면:

1. [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 사용하여 PDF 파일을 엽니다.
1. 문서의 Forms 컬렉션에서 폼을 가져옵니다.
1. 직사각형 영역을 지정하고 Form 객체의 GetFieldsInRect 메소드에 전달합니다. Fields 컬렉션이 반환됩니다.
1. 이를 사용하여 필드를 조작합니다.

다음 C# 코드 스니펫은 PDF 파일의 특정 직사각형 영역에서 폼 필드를 가져오는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// PDF 파일 열기
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// 해당 영역에서 필드를 가져오기 위한 사각형 객체 생성
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// PDF 폼 가져오기
Aspose.Pdf.Forms.Form form = doc.Form;

// 직사각형 영역에서 필드 가져오기
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// 필드 이름과 값을 표시
foreach (Field field in fields)
{
    // 모든 배치에 대한 이미지 배치 속성 표시
    Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 라이브러리",
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "영어"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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
```


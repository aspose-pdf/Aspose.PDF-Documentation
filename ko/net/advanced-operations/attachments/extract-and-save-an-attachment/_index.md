---
title: 첨부 파일 추출 및 저장
linktitle: 첨부 파일 추출 및 저장
type: docs
weight: 20
url: ko/net/extract-and-save-an-attachment/
description: Aspose.PDF for .NET은 PDF 문서에서 모든 첨부 파일을 가져올 수 있습니다. 또한 문서에서 개별 첨부 파일을 가져올 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "첨부 파일 추출 및 저장",
    "alternativeHeadline": "첨부 파일을 추출하고 저장하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 첨부 파일 저장, 첨부 파일 추출",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET은 PDF 문서에서 모든 첨부 파일을 가져올 수 있습니다. 또한 문서에서 개별 첨부 파일을 가져올 수 있습니다."
}
</script>

## 모든 첨부 파일 가져오기

Aspose.PDF를 사용하면 PDF 문서에서 모든 첨부 파일을 가져올 수 있습니다. 이는 PDF에서 문서를 별도로 저장하고자 할 때나 PDF에서 첨부 파일을 제거해야 할 필요가 있을 때 유용합니다.

PDF 파일에서 모든 첨부 파일을 가져오는 방법:

1. [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션을 순회합니다. [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션에는 모든 첨부 파일이 포함되어 있습니다. 이 컬렉션의 각 요소는 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 나타냅니다. [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션을 순회하는 각 foreach 루프 반복은 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 반환합니다.
다음 코드 조각은 PDF 문서에서 모든 첨부 파일을 가져오는 방법을 보여줍니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// 내장 파일 컬렉션 가져오기
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// 내장된 파일의 수를 가져옵니다
Console.WriteLine("총 파일 수 : {0}", embeddedFiles.Count);

int count = 1;

// 모든 첨부 파일을 얻기 위해 컬렉션을 반복합니다.
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("이름: {0}", fileSpecification.Name);
    Console.WriteLine("설명: {0}",
    fileSpecification.Description);
    Console.WriteLine("MIME 유형: {0}", fileSpecification.MIMEType);

    // 매개변수 객체가 매개변수를 포함하는지 확인
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("체크섬: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("생성 날짜: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("수정 날짜: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("크기: {0}", fileSpecification.Params.Size);
    }

    // 첨부 파일을 가져와 파일이나 스트림에 쓰기
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## 개별 첨부 파일 가져오기

개별 첨부 파일을 가져오기 위해 Document 인스턴스의 `EmbeddedFiles` 객체에서 첨부 파일의 인덱스를 지정할 수 있습니다. 다음 코드 스니펫을 사용해 보세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// 특정 내장 파일 가져오기
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// 파일 속성 가져오기
Console.WriteLine("이름: {0}", fileSpecification.Name);
Console.WriteLine("설명: {0}", fileSpecification.Description);
Console.WriteLine("Mime 유형: {0}", fileSpecification.MIMEType);

// 매개변수 객체가 매개변수를 포함하는지 확인
if (fileSpecification.Params != null)
{
    Console.WriteLine("체크섬: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("생성 날짜: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("수정 날짜: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("크기: {0}", fileSpecification.Params.Size);
}

// 첨부 파일을 가져와 파일 또는 스트림에 쓰기
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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


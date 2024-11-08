---
title: PDF 파일 메타데이터 작업 | C#
linktitle: PDF 파일 메타데이터
type: docs
weight: 140
url: /ko/net/pdf-file-metadata/
description: 이 섹션에서는 PDF 파일 정보를 얻는 방법, PDF 파일에서 XMP 메타데이터를 얻는 방법, PDF 파일 정보를 설정하는 방법에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 파일 메타데이터 작업 | C#",
    "alternativeHeadline": "PDF 파일 메타데이터 얻는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf 파일 메타데이터",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 PDF 파일 정보를 얻는 방법, PDF 파일에서 XMP 메타데이터를 얻는 방법, PDF 파일 정보를 설정하는 방법에 대해 설명합니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

## PDF 파일 정보 얻기

PDF 파일의 특정 정보를 얻으려면, 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) 속성을 사용하여 [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) 객체를 가져와야 합니다. [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) 객체를 검색하면 개별 속성의 값을 얻을 수 있습니다. 다음 코드 조각은 PDF 파일 정보를 얻는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// 문서 정보 가져오기
DocumentInfo docInfo = pdfDocument.Info;
// 문서 정보 표시
Console.WriteLine("작성자: {0}", docInfo.Author);
Console.WriteLine("생성 날짜: {0}", docInfo.CreationDate);
Console.WriteLine("키워드: {0}", docInfo.Keywords);
Console.WriteLine("수정 날짜: {0}", docInfo.ModDate);
Console.WriteLine("주제: {0}", docInfo.Subject);
Console.WriteLine("제목: {0}", docInfo.Title);
```
## PDF 파일 정보 설정

Aspose.PDF for .NET을 사용하면 PDF의 파일별 정보를 설정할 수 있습니다. 저자, 생성 날짜, 주제, 제목과 같은 정보를 설정할 수 있습니다. 이 정보를 설정하려면:

1. [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) 객체를 생성합니다.
1. 속성의 값을 설정합니다.
1. Document 클래스의 Save 메서드를 사용하여 업데이트된 문서를 저장합니다.

{{% alert color="primary" %}}

*Application* 및 *Producer* 필드에 대한 값을 설정할 수 없음을 유의하십시오. 이 필드에는 Aspose Ltd. 및 Aspose.PDF for .NET x.x.x가 표시됩니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// 문서 정보 지정
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "PDF Information";
docInfo.Title = "Setting PDF Document Information";

dataDir = dataDir + "SetFileInfo_out.pdf";
// 출력 문서 저장
pdfDocument.Save(dataDir);
```
## PDF 파일에서 XMP 메타데이터 가져오기

Aspose.PDF를 사용하면 PDF 파일의 XMP 메타데이터에 접근할 수 있습니다. PDF 파일의 메타데이터를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 입력 PDF 파일을 엽니다.
1. [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) 속성을 사용하여 파일의 메타데이터를 가져옵니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 가져오는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// 속성 가져오기
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## PDF 파일에 XMP 메타데이터 설정하기

Aspose.PDF를 사용하면 PDF 파일에 메타데이터를 설정할 수 있습니다.
Aspose.PDF를 사용하여 PDF 파일에 메타데이터를 설정할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata) 속성을 사용하여 메타데이터 값을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일에 메타데이터를 설정하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// 속성 설정
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// 문서 저장
pdfDocument.Save(dataDir);
```
## 접두사가 있는 메타데이터 삽입

일부 개발자는 접두사가 있는 새 메타데이터 네임스페이스를 생성해야 할 수 있습니다. 다음 코드 스니펫은 접두사가 있는 메타데이터를 삽입하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 참조하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Xmlns 접두사가 제거되었습니다
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// 문서 저장
pdfDocument.Save(dataDir);
```


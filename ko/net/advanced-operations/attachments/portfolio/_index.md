---
title: PDF 포트폴리오 작업
linktitle: 포트폴리오
type: docs
weight: 40
url: ko/net/portfolio/
description: C#을 사용하여 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성해야 합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 포트폴리오 작업",
    "alternativeHeadline": "PDF 문서에서 포트폴리오 생성",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 포트폴리오",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "C#을 사용하여 PDF 포트폴리오를 만드는 방법. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성해야 합니다."
}
</script>

## PDF 포트폴리오 생성 방법

Aspose.PDF를 사용하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 포트폴리오 문서를 만들 수 있습니다. [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 클래스로 가져온 후 파일을 Document.Collection 객체에 추가하세요. 파일이 추가되면 Document 클래스의 Save 메소드를 사용하여 포트폴리오 문서를 저장하세요.

다음 예제는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래 코드는 다음 포트폴리오를 결과로 합니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

### Aspose.PDF로 생성된 PDF 포트폴리오

![Aspose.PDF로 생성된 PDF 포트폴리오](working-with-pdf-portfolio_1.jpg)

```csharp
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Document 객체 인스턴스화
Document doc = new Document();

// 문서 컬렉션 객체 인스턴스화
doc.Collection = new Collection();

// 포트폴리오에 추가할 파일 가져오기
FileSpecification excel = new FileSpecification(dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification(dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// 파일의 설명 제공
excel.Description = "Excel 파일";
word.Description = "Word 파일";
image.Description = "이미지 파일";

// 문서 컬렉션에 파일 추가
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// 포트폴리오 문서 저장
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## PDF 포트폴리오에서 파일 추출하기

PDF 포트폴리오를 사용하면 다양한 출처(예: PDF, Word, Excel, JPEG 파일)의 콘텐츠를 하나의 통합 컨테이너로 모을 수 있습니다. 각각의 원본 파일은 개별적인 신원을 유지하지만 PDF 포트폴리오 파일로 조립됩니다. 사용자는 다른 구성 파일과 독립적으로 각 구성 파일을 열고, 읽고, 편집하고, 형식을 지정할 수 있습니다.

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. 또한 PDF 포트폴리오에서 파일을 추출할 수 있는 기능도 제공합니다.

다음 코드 스니펫은 PDF 포트폴리오에서 파일을 추출하는 단계를 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// 원본 PDF 포트폴리오를 로드합니다.
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// 내장된 파일의 컬렉션을 가져옵니다.
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// 포트폴리오의 개별 파일을 반복 처리합니다.
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // 첨부 파일을 가져와 파일이나 스트림에 쓰기
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // 추출된 파일을 특정 위치에 저장합니다.
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // 스트림 객체를 닫습니다.
    fileStream.Close();
}
```
![PDF 포트폴리오에서 파일 추출](working-with-pdf-portfolio_2.jpg)

## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 줄을 사용해보세요.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉터리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// 소스 PDF 포트폴리오 로드
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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



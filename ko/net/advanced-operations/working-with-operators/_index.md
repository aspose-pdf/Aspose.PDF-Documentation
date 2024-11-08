---
title: 연산자 사용하기
linktitle: 연산자 사용하기
type: docs
weight: 170
url: /ko/net/operators/
description: 이 주제는 Aspose.PDF에서 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-operators/
    - /net/operator/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "연산자 사용하기",
    "alternativeHeadline": "PDF 연산자 사용 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서 연산자, pdf 연산자 사용",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "이 주제는 Aspose.PDF에서 연산자를 사용하는 방법을 설명합니다. 연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다."
}
</script>
## PDF 연산자와 그 사용법 소개

연산자는 페이지에 그래픽 모양을 그리는 등의 동작을 지정하는 PDF 키워드입니다. 연산자 키워드는 초기 고체 문자(2Fh)가 없기 때문에 명명된 객체와 구별됩니다. 연산자는 내용 스트림 내에서만 의미가 있습니다.

내용 스트림은 페이지에 그려질 그래픽 요소를 설명하는 지시사항으로 구성된 데이터를 가진 PDF 스트림 객체입니다. PDF 연산자에 대한 자세한 내용은 [PDF 사양](https://opensource.adobe.com/dc-acrobat-sdk-docs/)에서 확인할 수 있습니다.

### 구현 세부사항

이 주제는 Aspose.PDF에서 연산자를 사용하는 방법을 설명합니다.
이 주제는 Aspose.PDF와 연산자를 사용하는 방법에 대해 설명합니다.

- **GSave** 연산자는 PDF의 현재 그래픽 상태를 저장합니다.
- **ConcatenateMatrix** (행렬 연결) 연산자는 이미지가 PDF 페이지에 어떻게 배치될지 정의하는 데 사용됩니다.
- **Do** 연산자는 페이지에 이미지를 그립니다.
- **GRestore** 연산자는 그래픽 상태를 복원합니다.

PDF 파일에 이미지를 추가하는 방법:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 입력 PDF 문서를 엽니다.
1. 이미지가 추가될 특정 페이지를 가져옵니다.
1. 이미지를 페이지의 Resources 컬렉션에 추가합니다.
1. 다음 연산자를 사용하여 페이지에 이미지를 배치합니다:
   - 먼저, GSave 연산자를 사용하여 현재 그래픽 상태를 저장합니다.
   - 그 다음 ConcatenateMatrix 연산자를 사용하여 이미지가 배치될 위치를 지정합니다.
   - Do 연산자를 사용하여 페이지에 이미지를 그립니다.
1. 마지막으로, GRestore 연산자를 사용하여 업데이트된 그래픽 상태를 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 조각은 PDF 연산자 사용 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// 문서 열기
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// 좌표 설정
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// 이미지를 추가할 페이지 가져오기
Page page = pdfDocument.Pages[1];
// 이미지를 스트림으로 로드
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// 페이지 리소스의 이미지 컬렉션에 이미지 추가
page.Resources.Images.Add(imageStream);
// GSave 연산자 사용: 이 연산자는 현재 그래픽 상태를 저장합니다
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Rectangle과 Matrix 객체 생성
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// ConcatenateMatrix (행렬 연결) 연산자 사용: 이미지가 배치되는 방식을 정의합니다
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Do 연산자 사용: 이 연산자는 이미지를 그립니다
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// GRestore 연산자 사용: 이 연산자는 그래픽 상태를 복원합니다
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```
changefreq: "monthly"
type: docs
## 페이지에서 연산자를 사용하여 XForm 그리기

이 주제에서는 GSave/GRestore 연산자, ContatenateMatrix 연산자를 사용하여 xForm의 위치를 설정하고 Do 연산자를 사용하여 페이지에 xForm을 그리는 방법을 설명합니다.

아래 코드는 PDF 파일의 기존 내용을 GSave/GRestore 연산자 쌍으로 감싸는 방법을 보여줍니다. 이 방법은 기존 내용의 끝에 초기 그래픽 상태를 얻는 데 도움이 됩니다. 이 접근 방식이 없으면 기존 연산자 체인의 끝에 원치 않는 변형이 남을 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // 예제는 다음을 보여줍니다.
    // GSave/GRestore 연산자 사용
    // xForm 위치 설정을 위한 ContatenateMatrix 연산자 사용
    // 페이지에 xForm를 그리기 위한 Do 연산자 사용

    // 기존 내용을 GSave/GRestore 연산자 쌍으로 감싸기
    //        이는 기존 내용 끝에 초기 그래픽 상태를 얻기 위함입니다.
    //        그렇지 않으면 기존 연산자 체인 끝에 원치 않는 변형이 남을 수 있습니다.
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // 새 명령 후 그래픽 상태를 제대로 지우기 위해 그래픽 상태 저장 연산자 추가
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region xForm 생성

    // xForm 생성
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // 이미지 너비와 높이 정의
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // 이미지를 스트림으로 로드
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // XForm 리소스의 이미지 컬렉션에 이미지 추가
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Do 연산자 사용: 이 연산자는 이미지를 그립니다.
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // x=100 y=500 좌표에 폼 배치
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Do 연산자로 폼 그리기
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // x=100 y=300 좌표에 폼 배치
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Do 연산자로 폼 그리기
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // GSave 이후 GRestore로 그래픽 상태 복원
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## 연산자 클래스를 사용하여 그래픽 객체 제거

연산자 클래스는 PDF 조작을 위한 훌륭한 기능을 제공합니다. PDF 파일에 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) 메소드를 사용하여 제거할 수 없는 그래픽이 포함되어 있을 경우, 대신 연산자 클래스를 사용하여 제거할 수 있습니다.

다음 코드 스니펫은 그래픽을 제거하는 방법을 보여줍니다. PDF 파일에 그래픽의 텍스트 레이블이 포함되어 있는 경우, 이 접근 방식을 사용하면 PDF 파일에 그대로 남아 있을 수 있으므로, 이러한 이미지를 삭제하기 위해 그래픽 연산자를 검색하십시오.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// 사용된 경로-페인팅 연산자들
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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


---
title: C#을 사용하여 PDF 크기 최적화, 압축 또는 축소
linktitle: PDF 최적화
type: docs
weight: 30
url: /ko/net/optimize-pdf/
keywords: "optimize pdf c#"
description: PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 임베드되지 않은 글꼴 제거, C#을 사용하여 사용되지 않는 객체 제거.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/changing-page-sizes-in-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용한 PDF 최적화",
    "alternativeHeadline": ".NET을 이용한 PDF 최적화 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, optimize pdf",
    "wordcount": "302",
    "proficiencyLevel":"초급",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "PDF 파일 최적화, 모든 이미지 축소, PDF 크기 줄이기, 임베드되지 않은 글꼴 제거, C#을 사용하여 사용되지 않는 객체 제거."
}
</script>
PDF 문서에는 때때로 추가 데이터가 포함되어 있을 수 있습니다. PDF 파일의 크기를 줄이면 네트워크 전송 및 저장 공간을 최적화할 수 있습니다. 이는 웹 페이지에 게시하거나 소셜 네트워크에 공유하거나 이메일로 보내거나 저장소에 보관하는 경우 특히 유용합니다. PDF를 최적화하기 위해 여러 기술을 사용할 수 있습니다:

- 온라인 탐색에 맞게 페이지 콘텐츠 최적화
- 모든 이미지 축소 또는 압축
- 페이지 콘텐츠 재사용 활성화
- 중복 스트림 병합
- 포함되지 않은 글꼴
- 사용되지 않는 객체 제거
- 평면화 폼 필드 제거
- 주석 제거 또는 평면화

{{% alert color="primary" %}}

 최적화 방법에 대한 자세한 설명은 최적화 방법 개요 페이지에서 확인할 수 있습니다.

{{% /alert %}}

## 웹용 PDF 문서 최적화

웹용 최적화 또는 선형화는 웹 브라우저를 사용하여 온라인 탐색에 적합한 PDF 파일을 만드는 과정을 말합니다. 파일을 웹 표시용으로 최적화하려면:

1. [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체에서 입력 문서를 엽니다.
1.
1. 최적화된 문서를 [저장](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 저장하세요.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

다음 코드 스니펫은 웹용 PDF 문서를 최적화하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");

// 웹용 최적화
pdfDocument.Optimize();

dataDir = dataDir + "OptimizeDocument_out.pdf";

// 출력 문서 저장
pdfDocument.Save(dataDir);
```

## PDF 크기 줄이기

[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) 메소드를 사용하면 필요하지 않은 정보를 제거함으로써 문서 크기를 줄일 수 있습니다.
[OptimizeResources()](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/optimizeresources) 메소드를 사용하면 불필요한 정보를 제거하여 문서 크기를 줄일 수 있습니다.

- 문서 페이지에서 사용되지 않는 리소스는 제거됩니다
- 동등한 리소스는 하나의 객체로 합쳐집니다
- 사용되지 않는 객체는 삭제됩니다

아래 스니펫은 예제입니다. 그러나 이 메서드가 문서 축소를 보장할 수 없다는 점에 유의하세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "ShrinkDocument.pdf");
// PDF 문서 최적화. 그러나 이 메서드가 문서 축소를 보장할 수 없다는 점에 유의하세요
pdfDocument.OptimizeResources();
dataDir = dataDir + "ShrinkDocument_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```

## 최적화 전략 관리

최적화 전략을 사용자 정의할 수도 있습니다.
우리는 최적화 전략을 사용자 정의할 수도 있습니다.

### 모든 이미지 축소 또는 압축

이미지를 다루는 두 가지 방법이 있습니다: 이미지 품질을 줄이거나 해상도를 변경합니다. 어떤 경우든 [ImageCompressionOptions](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions)를 적용해야 합니다. 다음 예제에서는 [ImageQuality](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality)를 50으로 줄여 이미지를 축소합니다.

`ImageQuality`는 JPEG 품질과 유사하게 작동하며, 값 0은 최저이고 값 100은 최고입니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET을 참조하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// 문서 열기
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// OptimizationOptions 초기화
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImages 옵션 설정
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQuality 옵션 설정
optimizeOptions.ImageCompressionOptions.ImageQuality = 50;
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "Shrinkimage_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```
다른 방법은 이미지를 낮은 해상도로 크기를 조정하는 것입니다. 이 경우, ResizeImages를 true로 설정하고 MaxResolution을 적절한 값으로 설정해야 합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 시간 초기화
var time = DateTime.Now.Ticks;
// 문서 디렉토리 경로
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// 문서 열기
Document pdfDocument = new Document(dataDir + "ResizeImage.pdf");
// OptimizationOptions 초기화
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImages 옵션 설정
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQuality 옵션 설정
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// ResizeImage 옵션 설정
optimizeOptions.ImageCompressionOptions.ResizeImages = true;
// MaxResolution 옵션 설정
optimizeOptions.ImageCompressionOptions.MaxResolution = 300;
// OptimizationOptions 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "ResizeImages_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```
또 다른 중요한 문제는 실행 시간입니다. 하지만 이 설정도 관리할 수 있습니다. 현재 우리는 두 가지 알고리즘 - 표준과 빠른 -을 사용할 수 있습니다. 실행 시간을 제어하려면 [버전](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/imagecompressionoptions/properties/version) 속성을 설정해야 합니다. 다음 스니펫은 빠른 알고리즘을 보여줍니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 시간 초기화
var time = DateTime.Now.Ticks;
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();
// 문서 열기
Document pdfDocument = new Document(dataDir + "Shrinkimage.pdf");
// OptimizationOptions 초기화
var optimizeOptions = new Pdf.Optimization.OptimizationOptions();
// CompressImages 옵션 설정
optimizeOptions.ImageCompressionOptions.CompressImages = true;
// ImageQuality 옵션 설정
optimizeOptions.ImageCompressionOptions.ImageQuality = 75;
// 이미지 압축 버전을 빠르게 설정
optimizeOptions.ImageCompressionOptions.Version = Pdf.Optimization.ImageCompressionVersion.Fast;
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "FastShrinkImages_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
```
### 사용되지 않는 객체 제거

PDF 문서에는 문서의 다른 객체에서 참조하지 않는 PDF 객체가 포함되어 있을 수 있습니다. 예를 들어, 문서 페이지 트리에서 페이지가 제거되었지만 페이지 객체 자체는 제거되지 않은 경우가 이에 해당합니다. 이러한 객체를 제거하면 문서가 유효하지 않게 되는 것이 아니라 문서의 크기가 줄어듭니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// RemoveUsedObject 옵션 설정
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedObjects = true
};
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```

### 사용되지 않는 스트림 제거

문서에는 사용되지 않는 리소스 스트림이 포함되어 있을 때가 있습니다.
문서에는 가끔 사용하지 않는 리소스 스트림이 포함되어 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// RemoveUsedStreams 옵션 설정
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    RemoveUnusedStreams = true
};
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```

### 중복 스트림 연결

일부 문서는 여러 개의 동일한 리소스 스트림(예를 들어 이미지와 같은)을 포함할 수 있습니다.
어떤 문서들은 여러 개의 동일한 리소스 스트림(예를 들어 이미지와 같은)을 포함할 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 으로 이동해 주세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// LinkDuplcateStreams 옵션 설정
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    LinkDuplcateStreams = true
};
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
dataDir = dataDir + "OptimizeDocument_out.pdf";
// 업데이트된 문서 저장
pdfDocument.Save(dataDir);
```

또한, [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) 설정을 사용할 수 있습니다.
추가적으로, [AllowReusePageContent](https://reference.aspose.com/pdf/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent) 설정을 사용할 수 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// AllowReusePageContent 옵션 설정
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    AllowReusePageContent = true
};
Console.WriteLine("시작");
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
// 업데이트된 문서 저장
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("완료");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("원본 파일 크기: {0}. 줄어든 파일 크기: {1}", fi1.Length, fi2.Length);
```
### 글꼴 임베딩 해제

문서가 임베딩된 글꼴을 사용하는 경우, 모든 글꼴 데이터가 문서에 저장됩니다. 이점은 사용자의 기기에 글꼴이 설치되어 있지 않아도 문서를 볼 수 있다는 것입니다. 하지만 글꼴을 임베딩하면 문서의 크기가 커집니다. 글꼴 임베딩 해제 방법은 모든 임베딩된 글꼴을 제거합니다. 따라서 문서 크기가 줄어들지만, 올바른 글꼴이 설치되어 있지 않으면 문서가 읽을 수 없게 될 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// 글꼴 임베딩 해제 옵션 설정
var optimizeOptions = new Pdf.Optimization.OptimizationOptions
{
    UnembedFonts = true
};
Console.WriteLine("시작");
// OptimizationOptions를 사용하여 PDF 문서 최적화
pdfDocument.OptimizeResources(optimizeOptions);
// 업데이트된 문서 저장
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("완료");
var fi1 = new System.IO.FileInfo(dataDir + "OptimizeDocument.pdf");
var fi2 = new System.IO.FileInfo(dataDir + "OptimizeDocument_out.pdf");
Console.WriteLine("원본 파일 크기: {0}. 줄어든 파일 크기: {1}", fi1.Length, fi2.Length);
```
최적화 리소스는 이러한 방법을 문서에 적용합니다. 이러한 방법 중 하나라도 적용되면 문서 크기가 대체로 감소할 것입니다. 이러한 방법 중 어느 것도 적용되지 않으면 문서 크기는 변하지 않을 것입니다.

## PDF 문서 크기를 줄이는 추가 방법

### 주석 제거 또는 평탄화

주석은 필요하지 않을 때 삭제할 수 있습니다. 편집이 필요하지 않지만 필요할 때는 평탄화할 수 있습니다. 이러한 기술은 파일 크기를 줄입니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// 문서 열기
Document pdfDocument = new Document(dataDir + "OptimizeDocument.pdf");
// 주석 평탄화
foreach (var page in pdfDocument.Pages)
{
    foreach (var annotation in page.Annotations)
    {
        annotation.Flatten();
    }

}
// 업데이트된 문서 저장
pdfDocument.Save(dataDir + "OptimizeDocument_out.pdf");
```
### 양식 필드 제거

PDF 문서에 AcroForm이 포함되어 있는 경우, 양식 필드를 평탄화하여 파일 크기를 줄일 수 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 소스 PDF 양식 로드
Document doc = new Document(dataDir + "input.pdf");

// 평탄화 양식
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// 업데이트된 문서 저장
doc.Save(dataDir);
```

### RGB 색공간의 PDF를 회색조로 변환

PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다.
PDF 파일은 텍스트, 이미지, 첨부 파일, 주석, 그래프 및 기타 객체로 구성됩니다.

```csharp
// 전체 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 를 방문하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// 원본 PDF 파일 로드
using (Document document = new Document(dataDir + "input.pdf"))
{
    Aspose.Pdf.RgbToDeviceGrayConversionStrategy strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();
    for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
    {
        // PDF 내 특정 페이지의 인스턴스를 가져옵니다.
        Page page = document.Pages[idxPage];
        // RGB 컬러스페이스 이미지를 그레이스케일 컬러스페이스로 변환
        strategy.Convert(page);
    }
    // 결과 파일 저장
    document.Save(dataDir + "Test-gray_out.pdf");
}
```

### FlateDecode 압축

{{% alert color="primary" %}}

이 기능은 버전 18.12 이상에서 지원됩니다.

{{% /alert %}}

Aspose.PDF for .NET은 PDF 최적화 기능을 위한 FlateDecode 압축 지원을 제공합니다.
Aspose.PDF for .NET은 PDF 최적화 기능에 대해 FlateDecode 압축 지원을 제공합니다.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-FlateDecodeCompression-1.cs" >}}

### **XImageCollection에 이미지 저장**

Aspose.PDF for .NET은 FlateDecode 압축으로 **XImageCollection**에 새 이미지를 저장할 수 있는 기능을 제공합니다. 이 옵션을 사용하려면 **ImageFilterType.Flate** 플래그를 사용할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다:

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-StoreImageInXImageCollection-1.cs" >}}

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



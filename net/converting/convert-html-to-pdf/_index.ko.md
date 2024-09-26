---
title: .NET에서 HTML을 PDF로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: /net/convert-html-to-pdf/
lastmod: "2021-11-01"
description: 이 주제에서는 Aspose.PDF를 사용하여 HTML을 PDF 및 MHTML을 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
## 개요

이 기사에서는 **C#을 사용하여 HTML을 PDF로 변환하는 방법**을 설명합니다. 다음 주제들을 다룹니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

_포맷_: **HTML**
- [C# HTML을 PDF로 변환](#csharp-html-to-pdf)
- [C# HTML을 PDF로 변환하기](#csharp-html-to-pdf)
- [C# HTML을 PDF로 어떻게 변환하나요](#csharp-html-to-pdf)

_포맷_: **MHTML**
- [C# MHTML을 PDF로 변환](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 변환하기](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 어떻게 변환하나요](#csharp-mhtml-to-pdf)

_포맷_: **웹페이지**
- [C# 웹페이지를 PDF로 변환](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 변환하기](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 어떻게 변환하나요](#csharp-webpage-to-pdf)

## C# HTML에서 PDF로 변환
## C# HTML을 PDF로 변환

**Aspose.PDF for .NET**은 기존 HTML 문서를 PDF로 원활하게 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 사용자 정의할 수 있습니다.

## HTML을 PDF로 변환

다음 C# 코드 샘플은 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

<a name="csharp-html-to-pdf"><strong>단계: C#에서 HTML을 PDF로 변환</strong></a>

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/) 클래스의 인스턴스를 생성합니다.
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 객체를 초기화합니다.
3. **Document.Save()** 메소드를 호출하여 출력 PDF 문서를 저장합니다.

```csharp
public static void ConvertHTMLtoPDF()
{
    HtmlLoadOptions options= new HtmlLoadOptions();
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

{{% alert color="success" %}}
**온라인에서 HTML을 PDF로 변환해 보세요**

Aspose는 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 살펴볼 수 있습니다.
Aspose가 무료로 제공하는 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf) 온라인 애플리케이션을 소개합니다. 여기서 기능과 품질을 테스트해 볼 수 있습니다.

[![Aspose.PDF 변환 HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)

## HTML에서 PDF로의 고급 변환

HTML 변환 엔진은 변환 과정을 제어할 수 있는 여러 옵션을 가지고 있습니다.

### 미디어 쿼리 지원

미디어 쿼리는 다양한 장치에 맞춤형 스타일 시트를 제공하는 인기 있는 기술입니다. [`HtmlMediaType`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/htmlmediatype) 속성을 사용하여 장치 유형을 설정할 수 있습니다.

```csharp
public static void ConvertHTMLtoPDFAdvanced_MediaType()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        // 인쇄 또는 화면 모드 설정
        HtmlMediaType = HtmlMediaType.Print
    };
    Document pdfDocument = new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```
### 폰트 삽입 활성화(비활성화)

HTML 페이지는 종종 폰트(예: 로컬 폴더의 폰트, Google 폰트 등)를 사용합니다. [`IsEmbedFonts`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/properties/isembedfonts) 속성을 사용하여 문서에서 폰트의 삽입을 제어할 수도 있습니다.

```csharp
public static void ConvertHTMLtoPDFAdvanced_EmbedFonts()
{
    // 폰트 삽입 비활성화
    HtmlLoadOptions options = new HtmlLoadOptions {IsEmbedFonts = false};
    Document pdfDocument= new Document(_dataDir + "test_fonts.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}
```

### 외부 리소스 로딩 관리

변환 엔진은 HTML 문서와 관련된 특정 리소스의 로딩을 제어할 수 있는 메커니즘을 제공합니다.
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 클래스는 리소스 로더의 동작을 정의할 수 있는 속성 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)를 가지고 있습니다.
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 클래스는 리소스 로더의 동작을 정의할 수 있는 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources) 속성을 가지고 있습니다.
모든 PNG 이미지를 `test.jpg` 이미지로 교체하고 다른 리소스의 외부 URL을 내부 URL로 교체해야 한다고 가정합시다.
이를 위해 `SamePictureLoader`라는 사용자 정의 로더를 정의하고 이 이름을 [`CustomLoaderOfExternalResources`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/customloaderofexternalresources)에 지정할 수 있습니다.

```csharp
public static void ConvertHTMLtoPDFAdvanced_DummyImage()
{
    HtmlLoadOptions options = new HtmlLoadOptions
    {
        CustomLoaderOfExternalResources = SamePictureLoader
    };
    Document pdfDocument= new Document(_dataDir + "test.html", options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static LoadOptions.ResourceLoadingResult SamePictureLoader(string resourceURI)
{
    LoadOptions.ResourceLoadingResult result;

    if (resourceURI.EndsWith(".png"))
    {
        byte[] resultBytes = File.ReadAllBytes(_dataDir + "test.jpg");
        result = new LoadOptions.ResourceLoadingResult(resultBytes)
        {
            //MIME 타입 설정
            MIMETypeIfKnown = "image/jpeg"
        };
    }
    else
    {
        result = new LoadOptions.ResourceLoadingResult(GetContentFromUrl(resourceURI));
    }
    return result;
}

private static byte[] GetContentFromUrl(string url)
{
    var httpClient = new HttpClient();
    return httpClient.GetByteArrayAsync(url).GetAwaiter().GetResult();
}
```
## 웹 페이지를 PDF로 변환

웹 페이지를 변환하는 것은 로컬 HTML 문서를 변환하는 것과 약간 다릅니다. 웹 페이지 내용을 PDF 형식으로 변환하려면 먼저 HttpClient 인스턴스를 사용하여 HTML 페이지 내용을 가져오고, Stream 객체를 생성하고, 내용을 Document 객체에 전달한 다음 PDF 형식으로 출력을 렌더링할 수 있습니다.

웹서버에 호스팅된 웹 페이지를 PDF로 변환할 때:

<a name="csharp-webpage-to-pdf"><strong>단계: C#에서 웹페이지를 PDF로 변환</strong></a>

1. HttpClient 객체를 사용하여 페이지의 내용을 읽습니다.
1. [HtmlLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 객체를 인스턴스화하고 기본 URL을 설정합니다.
1. Stream 객체를 전달하면서 Document 객체를 초기화합니다.
1. 선택적으로 페이지 크기 및/또는 방향을 설정합니다.

```csharp
public static void ConvertHTMLtoPDFAdvanced_WebPage()
{
    const string url = "https://en.wikipedia.org/wiki/Aspose_API";
    // 페이지 크기 A3 및 가로 방향 설정;
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        PageInfo = {Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### 웹 페이지에서 PDF 변환을 위한 자격 증명 제공

때로는 인증과 접근 권한이 필요한 HTML 파일을 변환해야 할 필요가 있습니다. 이러한 경우에는 인증된 사용자만 페이지 내용을 가져올 수 있습니다. 또한 HTML 내부에서 참조하는 일부 리소스/데이터가 인증이 필요한 외부 서버에서 가져오는 시나리오도 포함됩니다. 이러한 요구사항을 충족하기 위해 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions) 클래스에 [`ExternalResourcesCredentials`](https://reference.aspose.com/pdf/net/aspose.pdf/htmlloadoptions/fields/externalresourcescredentials) 속성이 추가되었습니다. 다음 코드 스니펫은 HTML 및 해당 리소스에 자격 증명을 전달하는 단계를 보여줍니다. HTML 파일을 PDF로 변환할 때입니다.

```csharp
public static void ConvertHTMLtoPDFAdvanced_Authorized()
{
    const string url = "http://httpbin.org/basic-auth/user1/password1";
    var credentials = new NetworkCredential("user1", "password1");
    HtmlLoadOptions options = new HtmlLoadOptions(url)
    {
        ExternalResourcesCredentials = credentials
    };
    Document pdfDocument= new Document(GetContentFromUrlAsStream(url, credentials), options);
    pdfDocument.Save(_dataDir + "html_test.PDF");
}

private static Stream GetContentFromUrlAsStream(string url, ICredentials credentials = null)
{
    using (var handler = new HttpClientHandler { Credentials = credentials })
    using (var httpClient = new HttpClient(handler))
    {
        return httpClient.GetStreamAsync(url).GetAwaiter().GetResult();
    }
}
```
### 단일 페이지에 모든 HTML 콘텐츠 렌더링

Aspose.PDF for .NET은 HTML 파일을 PDF 형식으로 변환할 때 모든 콘텐츠를 단일 페이지에 렌더링할 수 있는 기능을 제공합니다. 예를 들어, 출력 크기가 한 페이지보다 큰 HTML 콘텐츠가 있는 경우, 출력 데이터를 단일 PDF 페이지로 렌더링하기 위한 옵션을 사용할 수 있습니다. 이 옵션을 사용하기 위해 HtmlLoadOptions 클래스는 IsRenderToSinglePage 플래그로 확장되었습니다. 아래의 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// HTMLLoadSave 옵션 초기화
HtmlLoadOptions options = new HtmlLoadOptions();
// 단일 페이지로 렌더링 설정
options.IsRenderToSinglePage = true;
// 문서 로드
Document pdfDocument= new Document(dataDir + "HTMLToPDF.html", options);
// 저장
pdfDocument.Save(dataDir + "RenderContentToSamePage.pdf");
```

### SVG 데이터를 포함한 HTML 렌더링

### HTML을 SVG 데이터로 렌더링

Aspose.PDF for .NET은 HTML 페이지를 PDF 문서로 변환할 수 있는 기능을 제공합니다. HTML은 페이지 내에 SVG 그래픽 요소를 태그로 추가할 수 있기 때문에, Aspose.PDF는 이러한 데이터를 결과 PDF 파일로 변환하는 것을 지원합니다. 다음 코드 조각은 SVG 그래픽 태그가 포함된 HTML 파일을 태그가 지정된 PDF 문서로 변환하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하십시오.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// 입력 파일 경로 설정
string inFile = dataDir + "HTMLSVG.html";
// 출력 파일 경로 설정
string outFile = dataDir + "RenderHTMLwithSVGData.pdf";
// HtmlLoadOptions 초기화
HtmlLoadOptions options = new HtmlLoadOptions(Path.GetDirectoryName(inFile));
// Document 객체 초기화
Document pdfDocument = new Document(inFile, options);
// 저장
pdfDocument.Save(outFile);
```

## MHTML을 PDF로 변환

{{% alert color="success" %}}
**MHTML을 PDF로 온라인 변환 시도**
**MHTML을 PDF로 온라인 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["MHTML을 PDF로"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)를 제공합니다. 여기서 해당 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF를 사용한 MHTML에서 PDF로의 변환 무료 앱](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>은 MIME HTML의 약자로, 웹 페이지 아카이브 형식으로 사용되어 HTML 코드와 함께 일반적으로 외부 링크(예: 이미지, 플래시 애니메이션, 자바 애플릿, 오디오 파일)로 표현되는 리소스를 단일 파일로 결합합니다.
<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, MIME HTML의 약자로, 외부 링크(예: 이미지, 플래시 애니메이션, 자바 애플릿, 오디오 파일 등)에 의해 일반적으로 표현되는 자원들을 HTML 코드와 함께 단일 파일로 결합하는 웹 페이지 아카이브 형식입니다.

<a name="csharp-mhtml-to-pdf"><strong>단계: C#에서 MHTML을 PDF로 변환</strong></a>

1. [MhtLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mhtloadoptions/) 클래스의 인스턴스를 생성합니다.
2. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 객체를 초기화합니다.
3. **Document.Save()** 메서드를 호출하여 출력된 PDF 문서를 저장합니다.

```csharp
public static void ConvertMHTtoPDF()
{
    MhtLoadOptions options = new MhtLoadOptions()
    {
        PageInfo = { Width = 842, Height = 1191, IsLandscape = true}
    };
    Document pdfDocument= new Document(_dataDir + "fileformatinfo.mht", options);
    pdfDocument.Save(_dataDir + "mhtml_test.PDF");
}
```

## 참고

이 글은 이러한 주제들도 다룹니다.
이 문서는 다음 주제도 다룹니다.

_형식_: **HTML**
- [C# HTML을 PDF로 변환하는 코드](#csharp-html-to-pdf)
- [C# HTML을 PDF로 변환하는 API](#csharp-html-to-pdf)
- [C# HTML을 PDF로 프로그래밍 방식으로 변환](#csharp-html-to-pdf)
- [C# HTML을 PDF로 변환하는 라이브러리](#csharp-html-to-pdf)
- [C# HTML을 PDF로 저장](#csharp-html-to-pdf)
- [C# HTML에서 PDF 생성](#csharp-html-to-pdf)
- [C# HTML에서 PDF 생성](#csharp-html-to-pdf)
- [C# HTML을 PDF로 변환하는 변환기](#csharp-html-to-pdf)

_형식_: **MHTML**
- [C# MHTML을 PDF로 변환하는 코드](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 변환하는 API](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 프로그래밍 방식으로 변환](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 변환하는 라이브러리](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 저장](#csharp-mhtml-to-pdf)
- [C# MHTML에서 PDF 생성](#csharp-mhtml-to-pdf)
- [C# MHTML에서 PDF 생성](#csharp-mhtml-to-pdf)
- [C# MHTML을 PDF로 변환하는 변환기](#csharp-mhtml-to-pdf)

_형식_: **웹페이지**
- [C# 웹페이지를 PDF로 변환하는 코드](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 변환하는 API](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 프로그래밍 방식으로 변환](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 프로그래밍 방식으로 변환](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 변환하는 라이브러리](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 저장](#csharp-webpage-to-pdf)
- [C# 웹페이지에서 PDF 생성](#csharp-webpage-to-pdf)
- [C# 웹페이지에서 PDF 생성하기](#csharp-webpage-to-pdf)
- [C# 웹페이지를 PDF로 변환하는 컨버터](#csharp-webpage-to-pdf)

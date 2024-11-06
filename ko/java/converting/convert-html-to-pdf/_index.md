---
title: 자바에서 HTML을 PDF 파일로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: ko/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 HTML 및 MHTML 형식을 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 개요

이 문서는 자바를 사용하여 HTML을 PDF로 변환하는 방법을 설명합니다. 코드는 매우 간단하며, HTML을 Document 클래스에 로드하고 출력 PDF로 저장하기만 하면 됩니다. 자바에서 MHTML을 PDF로 변환하는 것도 유사합니다. 다음 주제를 다룹니다.

- [Java HTML에서 PDF로](#convert-html-to-pdf)
- [Java MHTML에서 PDF로](#convert-mhtml-to-pdf)
- [Java에서 HTML을 PDF로 변환](#convert-html-to-pdf)
- [Java에서 MHTML을 PDF로 변환](#convert-mhtml-to-pdf)
- [Java에서 HTML로부터 PDF](#convert-html-to-pdf)
- [Java에서 MHTML로부터 PDF](#convert-mhtml-to-pdf)
- [Java HTML에서 PDF 변환기 - 웹 페이지를 PDF로 변환하는 방법](#convert-html-to-pdf)

- [Java HTML에서 PDF 라이브러리, API 또는 코드로 프로그래밍 방식으로 HTML에서 PDF를 렌더링, 저장, 생성 또는 만들기](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java**는 기존의 HTML 문서를 PDF로 원활하게 변환할 수 있는 PDF 조작 API입니다. HTML을 PDF로 변환하는 과정은 유연하게 사용자 정의할 수 있습니다.

## Convert HTML to PDF

다음 Java 코드 샘플은 HTML 문서를 PDF로 변환하는 방법을 보여줍니다.

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 클래스의 인스턴스를 생성합니다.
1. [Document](https://reference.aspose.com/page/java/com.aspose.page/document) 객체를 초기화합니다.
1. **Document.save(String)** 메서드를 호출하여 출력 PDF 문서를 저장합니다.

```java
// 소스 PDF 문서를 엽니다.
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// HTML SaveOptions 객체를 인스턴스화합니다.
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// 문서를 저장합니다.
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**온라인에서 HTML을 PDF로 변환해보세요**

Aspose는 ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## HTML에서 PDF로의 고급 변환

HTML 변환 엔진은 변환 프로세스를 제어할 수 있는 여러 옵션을 제공합니다.

### 미디어 쿼리 지원

1. HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)를 생성합니다.
1. 인쇄 또는 화면 모드를 설정합니다.
1. [문서 객체](<https://reference.aspose.com/page/java/com.aspose.page/document>)를 초기화합니다.
1. 출력 PDF 문서를 저장합니다.

미디어 쿼리는 다양한 장치에 맞춘 스타일 시트를 제공하기 위한 인기 있는 기술입니다. 우리는 [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType) 속성을 사용하여 장치 유형을 설정할 수 있습니다.

```java
// Create a HTML LoadOptions
HtmlLoadOptions options = new HtmlLoadOptions();

// Set Print or Screen mode
options.setHtmlMediaType(HtmlMediaType.Print);

// Initialize document object
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Save output PDF document
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### 글꼴 임베딩 활성화 (비활성화)

1. 새로운 Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 추가.
1. 글꼴 임베딩 활성화/비활성화.
1. 새로운 문서 저장.

HTML 페이지는 종종 글꼴을 사용합니다 (예: 로컬 폴더의 글꼴, Google Fonts 등). 우리는 [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--) 속성을 사용하여 문서에서 글꼴의 임베딩을 제어할 수 있습니다.

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// 글꼴 임베딩 활성화/비활성화
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### 외부 리소스 로딩 관리

변환 엔진은 HTML 문서와 관련된 특정 리소스의 로딩을 제어할 수 있는 메커니즘을 제공합니다.

[HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) 클래스는 [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) 속성을 가지고 있으며, 이를 통해 리소스 로더의 동작을 정의할 수 있습니다.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // 교체를 위한 명확한 템플릿 리소스 생성:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // i.imgur.com 서버의 경우 빈 바이트 배열 반환
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // 기본 리소스 로더로 리소스 처리
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## MHTML을 PDF로 변환

{{% alert color="success" %}}
**MHTML을 PDF로 온라인에서 변환해 보세요**


Aspose.PDF for Java는 온라인 무료 애플리케이션 ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)를 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion MHTML to PDF using Free App](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>은 MIME HTML의 약자로, 일반적으로 외부 링크(예: 이미지, 플래시 애니메이션, 자바 애플릿 및 오디오 파일)로 표현되는 리소스를 HTML 코드와 결합하여 단일 파일로 만드는 웹 페이지 아카이브 형식입니다. MHTML 파일의 내용은 MIME 타입 multipart/related를 사용하여 HTML 이메일 메시지처럼 인코딩됩니다.

다음 코드 스니펫은 Java를 사용하여 MHTML 파일을 PDF 형식으로 변환하는 방법을 보여줍니다:

```java
// MHTML 파일의 로드 옵션을 지정하기 위해 MhtLoadOptions의 인스턴스를 생성합니다.
MhtLoadOptions options = new MhtLoadOptions();

// MHTML 파일의 경로를 설정합니다.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// MHTML 파일을 Document 객체에 로드합니다.
Document document = new Document(mhtmlFileName, options);

// 문서를 PDF 파일로 저장합니다.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// 문서를 닫습니다.
document.close();
```
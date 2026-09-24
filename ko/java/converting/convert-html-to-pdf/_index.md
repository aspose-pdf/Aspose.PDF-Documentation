---
title: Java에서 HTML을 PDF로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: 미디어 설정, CSS 페이지 규칙, 글꼴 포함, SVG 콘텐츠 및 단일 페이지 출력을 포함하여 Aspose.PDF를 사용하여 Java에서 HTML, MHTML 및 웹 페이지를 PDF로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Aspose.PDF를 사용하여 Java에서 HTML을 PDF로 변환하는 방법
Abstract: 이 문서에서는 Java용 Aspose.PDF를 사용하여 HTML 및 MHTML 파일을 PDF로 변환하는 방법을 설명합니다. 기본적인 HTML-to-PDF 작업 과정을 다루고 미디어 유형, CSS 페이지 규칙 우선 순위, 포함된 글꼴, SVG 콘텐츠, 단일 페이지 출력 및 라이브 웹 페이지에서 직접 변환을 사용하여 렌더링을 제어하는 ​​방법을 보여줍니다.
---
Java용 Aspose.PDF는 로컬 HTML 파일, 보관된 MHTML 콘텐츠 및 라이브 웹 페이지를 PDF 문서로 변환할 수 있습니다. `HtmlLoadOptions` 및 `MhtLoadOptions`을 사용하여 변환 파이프라인을 제어하여 레이아웃 크기 조정, CSS 미디어 처리, 페이지 규칙 우선 순위, 글꼴 포함, 리소스 해상도 및 단일 페이지 렌더링 동작에 영향을 줄 수 있습니다.


## 
HTML을 PDF로 변환



로컬 HTML 파일을 PDF 문서로 직접 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 생성하여 가져오는 동안 HTML 소스가 해석되는 방식을 구성합니다.

1. 
[`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/)을 `ScaleToPageWidth`으로 설정하면 넓은 HTML 콘텐츠가 잘리는 대신 대상 PDF 페이지 너비에 맞게 조정됩니다.
1. 해당 경로와 구성된 로드 옵션을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 소스 HTML 파일을 엽니다.

1. 
생성된 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 대상 출력 경로에 PDF 파일로 저장합니다.


```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
미디어 유형 옵션을 사용하여 HTML을 PDF로 변환



HTML 변환 중에 CSS 미디어 유형 처리를 제어해야 하는 경우 이 예를 사용하십시오.


1. 
변환 설정을 위한 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 생성합니다.
1. 인쇄 매체 대신 화면 표시용 CSS 규칙을 사용하여 HTML을 렌더링해야 하는 경우 [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/)을 `Screen`으로 설정합니다.

1. 
변환 중에 미디어 쿼리 종속 스타일이 적용되도록 구성된 로드 옵션으로 HTML 파일을 엽니다.

1. 
결과 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 PDF 파일로 저장합니다.


```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
CSS 페이지 규칙 우선순위를 사용하여 HTML을 PDF로 변환



CSS `@page` 규칙이 최종 PDF 페이지 레이아웃에 영향을 미쳐야 하는 경우 이 예를 사용하십시오.

1. HTML 파일을 열기 전에 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 생성하세요.

1. 
다른 레이아웃 설정이 소스 마크업의 CSS `@page` 선언보다 우선해야 하는 경우 `setPriorityCssPageRule(false)`을 구성합니다.

1. 
가져오는 동안 페이지 레이아웃이 확인되도록 구성된 옵션을 사용하여 HTML 콘텐츠를 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 로드합니다.

1. 
생성된 PDF 파일을 저장합니다.


```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
내장된 글꼴을 사용하여 HTML을 PDF로 변환

출력 PDF에 HTML 글꼴을 포함하여 유지해야 하는 경우 이 예를 사용하십시오.


1. 
HTML 가져오기 구성을 위한 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 만듭니다.

1. 
`setEmbedFonts(true)`을 활성화하면 HTML 렌더링 중에 확인된 글꼴이 출력 PDF에 저장됩니다.

1. 
최종 문서에서 원래의 타이포그래피를 계속 사용할 수 있도록 이러한 로드 옵션을 사용하여 HTML 소스를 엽니다.

1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 포함된 글꼴 리소스가 포함된 PDF로 저장하세요.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 단일 PDF 페이지에서 HTML 콘텐츠 렌더링



긴 HTML 콘텐츠를 여러 페이지에 걸쳐 흐르는 대신 하나의 PDF 페이지에 보관해야 하는 경우 이 예를 사용하십시오.


1. 
변환 설정을 위한 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 만듭니다.

1. 
`setRenderToSinglePage(true)`을 활성화하면 가져온 HTML이 여러 페이지에 걸쳐 분할되지 않고 하나의 PDF 페이지에 배치됩니다.

1. 
구성된 로드 옵션으로 소스 HTML을 열고 Aspose.PDF가 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에서 페이지 레이아웃을 구축하도록 합니다.
1. 출력 PDF 파일을 저장합니다.


```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
인라인 SVG가 포함된 HTML 변환



PDF에서 렌더링해야 하는 인라인 SVG 데이터가 HTML 소스에 포함된 경우 이 예를 사용하십시오.


1. 
변환 중에 관련 리소스를 일관되게 확인할 수 있도록 HTML 파일의 상위 디렉터리를 기본 경로로 사용하여 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 만듭니다.

1. 
소스 경로 및 로드 옵션을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 인라인 SVG 마크업이 포함된 HTML 파일을 엽니다.
1. Aspose.PDF가 포함된 SVG 요소와 함께 HTML DOM을 PDF 페이지 콘텐츠로 렌더링하도록 합니다.

1. 
생성된 PDF 문서를 저장합니다.


```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
웹페이지를 PDF로 변환



라이브 웹 URL을 렌더링하고 PDF 문서로 저장해야 하는 경우 이 예를 사용하세요.


1. 
스타일시트 및 이미지와 같은 상대 리소스를 해당 주소에 대해 확인할 수 있도록 대상 URL을 사용하여 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 인스턴스를 만듭니다.
1. URL 문자열을 `URL` 개체로 변환하고 입력 스트림을 열어 라이브 HTML 콘텐츠를 가져옵니다.

1. 
응답 스트림과 구성된 로드 옵션에서 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 생성하여 다운로드한 페이지가 올바른 기본 URL로 처리되도록 합니다.

1. 
렌더링된 웹 페이지를 PDF 파일로 저장하고 try-with-resources를 사용하여 스트림 리소스를 자동으로 닫습니다.


```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 
MHTML을 PDF로 변환



보관된 MHTML 파일을 PDF 문서로 변환해야 하는 경우 이 예를 사용하십시오.

1. [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) 인스턴스를 만들어 Aspose.PDF에게 소스를 MIME HTML 콘텐츠로 로드하도록 지시합니다.

1. 
해당 경로와 MHTML 로드 옵션을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 `.mht` 또는 `.mhtml` 파일을 엽니다.

1. 
Aspose.PDF는 보관된 HTML 콘텐츠와 포함된 리소스를 PDF 문서 모델로 구문 분석합니다.

1. 
생성된 PDF 파일을 저장합니다.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

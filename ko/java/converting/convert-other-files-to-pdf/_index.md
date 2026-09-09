---
title: Java에서 다른 파일 형식을 PDF로 변환
linktitle: 다른 파일 형식을 PDF로 변환
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: Aspose.PDF를 사용하여 Java에서 EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD 및 TeX 파일을 PDF로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java에서 다른 파일 형식을 PDF로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 여러 소스 파일 형식을 PDF로 변환하는 방법을 설명합니다. 필요한 경우 형식별 로드 옵션과 전처리 단계를 사용하여 EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, 텍스트, XML, XPS 및 XSL-FO 변환 워크플로를 다룹니다.
---
Aspose.PDF for Java는 문서, 마크업, 페이지 설명 형식을 PDF로 변환하는 기능을 지원합니다.


## 
OFD를 PDF로 변환



OFD 문서를 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
파일 경로와 [`OfdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 OFD 소스를 엽니다.

1. 
Aspose.PDF가 OFD 패키지를 PDF 문서 모델로 구문 분석하도록 합니다.
1. 결과 PDF를 대상 출력 경로에 저장합니다.


```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## 
TeX를 PDF로 변환



TeX 콘텐츠를 PDF로 직접 렌더링해야 하는 경우 이 예를 사용하세요.


1. 
파일 경로와 [`TeXLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 TeX 소스를 엽니다.

1. 
Aspose.PDF가 TeX 마크업을 해석하고 로딩 중에 PDF 레이아웃을 구축하도록 하세요.
1. 생성된 PDF를 저장합니다.


```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
포스트스크립트를 PDF로 변환



PostScript 파일을 PDF 문서로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에서 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/)을 사용하여 PostScript 소스를 엽니다.

1. 
Aspose.PDF는 PostScript 페이지 설명 스트림을 PDF 문서 모델로 변환합니다.
1. 변환된 PDF 파일을 저장합니다.


```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
EPS를 PDF로 변환



캡슐화된 PostScript 파일을 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
EPS는 동일한 PostScript 기반 로드 경로를 따르므로 [`PsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/)으로 EPS 소스를 엽니다.

1. 
가져오는 동안 페이지 설명 내용이 변환되도록 파일을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에 로드합니다.
1. 출력 PDF를 저장합니다.


```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
EPUB를 PDF로 변환



EPUB eBook을 PDF로 변환해야 하는 경우 이 예를 사용하세요.


1. 
파일 경로와 [`EpubLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 EPUB 소스를 엽니다.

1. 
Aspose.PDF가 전자책 구조를 로드하고 PDF 페이지로 변환하도록 하세요.
1. 변환된 PDF를 저장합니다.


```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
마크다운을 PDF로 변환



Markdown 콘텐츠를 PDF로 렌더링하고 저장해야 하는 경우 이 예를 사용하세요.


1. 
파일 경로와 [`MdLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 마크다운 소스를 엽니다.

1. 
Aspose.PDF가 Markdown 콘텐츠를 해석하여 PDF 페이지 콘텐츠로 렌더링하도록 합니다.
1. 출력 PDF 파일을 저장합니다.


```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
간단한 작업 과정을 통해 텍스트를 PDF로 변환



일반 텍스트 파일을 PDF로 신속하게 변환해야 하는 경우 이 예를 사용하십시오.


1. 
UTF-8 디코딩으로 일반 텍스트 소스를 읽어 텍스트 콘텐츠를 Java 문자열로 사용할 수 있습니다.

1. 
빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만들고 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가합니다.
1. 텍스트를 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)으로 래핑하고 페이지 단락 컬렉션에 추가합니다.

1. 
생성된 PDF를 저장합니다.


```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
고급 옵션을 사용하여 텍스트를 PDF로 변환



추가 레이아웃 또는 인코딩 옵션을 사용하여 일반 텍스트를 변환해야 하는 경우 이 예를 사용하십시오.


1. 
변환 중에 페이지 구분 표시를 검사할 수 있도록 입력 파일에서 모든 텍스트 줄을 읽습니다.
1. 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만들고 여백과 기본 텍스트 상태로 각 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 구성합니다.

1. 
[`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/)을 통해 고정 폭 글꼴을 해결하고 각 줄을 [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)으로 추가합니다.

1. 
페이지 작성 루프가 완료된 후 출력 파일을 저장합니다.


```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PCL을 PDF로 변환



PCL 인쇄 스트림을 PDF로 변환해야 하는 경우 이 예를 사용하십시오.

1. 관대한 가져오기 동작이 필요한 경우 [`PclLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/)을 만들고 구문 분석 오류 억제를 활성화합니다.

1. 
파일 경로 및 로드 옵션을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 PCL 소스를 엽니다.

1. 
결과를 PDF로 저장하세요.


```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
XSLT 및 HTML을 통해 XML을 PDF로 변환



최종 PDF 생성 전에 XML 데이터를 변환해야 하는 경우 이 예를 사용하십시오.

1. 전용 변환 메서드를 호출하여 XSLT 파일이 포함된 XML 소스를 임시 HTML 파일로 변환합니다.

1. 
생성된 HTML 파일을 기존 HTML-PDF 변환 기능에 전달하여 최종 PDF가 표준 [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) 워크플로우를 사용하도록 합니다.

1. 
변환이 완료된 후 `finally` 블록의 임시 HTML 파일을 삭제하세요.

1. 
생성된 PDF 파일을 저장합니다.


```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## 
XPS를 PDF로 변환

XPS 문서를 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
파일 경로와 [`XpsLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 XPS 소스를 엽니다.

1. 
문서를 로드하는 동안 Aspose.PDF가 XPS 페이지 설명을 해석하도록 합니다.

1. 
변환된 PDF를 저장합니다.


```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
XSL-FO를 PDF로 변환

XSL-FO 컨텐츠를 PDF로 렌더링해야 하는 경우 이 예를 사용하십시오.


1. 
로드 중에 XML 소스가 변환될 수 있도록 XSLT 경로를 사용하여 [`XslFoLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/)을 만듭니다.

1. 
잘못된 XSL-FO가 발견되면 즉시 발생하도록 구문 분석 오류 처리 모드를 구성합니다.

1. 
해당 로드 옵션을 사용하여 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)에서 XML 소스를 엽니다.

1. 
결과 PDF 문서를 저장합니다.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## XML을 중간 HTML로 변환



최종 PDF 변환 단계 전에 XML 데이터를 HTML로 변환해야 하는 경우 이 방법을 사용하십시오.


1. 
XML 및 XSLT 입력 파일을 변환 소스로 엽니다.

1. 
XSLT 스타일시트에서 `Transformer`을 만들고 XML 소스에 대해 실행합니다.

1. 
다운스트림 PDF 변환 기능이 로드할 수 있도록 변환된 HTML 파일을 디스크에 씁니다.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```

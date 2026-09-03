---
title: Java에서 PDF를 EPUB, 텍스트, XPS 등으로 변환
linktitle: PDF를 다른 형식으로 변환
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Aspose.PDF를 사용하여 Java에서 PDF 파일을 EPUB, LaTeX, Markdown, 텍스트, XPS 및 MobiXML로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java에서 PDF를 다른 형식으로 변환하는 방법
Abstract: 이 문서에서는 필요한 경우 형식별 저장 옵션과 함께 Java용 Aspose.PDF를 사용하여 PDF 파일을 EPUB, TeX, Markdown, 텍스트, XPS 및 MobiXML 형식으로 변환하는 방법을 설명합니다.
---
Java용 Aspose.PDF는 PDF 문서를 텍스트, 전자책, 인쇄 및 마크업 지향 출력 형식으로 내보낼 수 있습니다.


## 
PDF를 EPUB로 변환



PDF 문서를 EPUB 전자책 형식으로 내보내야 하는 경우 이 예를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/)을 생성하고 인식 모드를 `Flow`로 설정하세요.
1. PDF 콘텐츠를 리플로우 가능한 EPUB 마크업으로 내보내려면 `document.save(outputFile.toString(), saveOptions)`으로 전화하세요.

1. 
변환된 EPUB 파일을 저장합니다.


```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 
PDF를 TeX로 변환



PDF 내용을 TeX 마크업으로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. TeX 직렬화를 위해 [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/)을 만듭니다.

1. 
`document.save(outputFile.toString(), saveOptions)`을 호출하면 PDF 콘텐츠가 TeX 마크업으로 내보내집니다.

1. 
결과 TeX 파일을 저장합니다.


```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 일반 텍스트로 변환



PDF 문서를 텍스트 파일로 내보내야 하는 경우 이 예를 사용하십시오.

1. [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
PDF 페이지에서 텍스트 콘텐츠를 추출하려면 [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/)을 만드세요.

1. 
첫 번째 페이지를 일반 텍스트로 작성하려면 `device.process(document.getPages().get_Item(1), outputFile.toString())`을 호출하세요.

1. 
텍스트 출력 파일을 저장합니다.


```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 XPS로 변환

PDF 문서를 XPS 형식으로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/)을 만들고 내장된 트루타입 글꼴을 활성화하세요.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF가 포함된 글꼴 리소스가 있는 XPS로 직렬화됩니다.

1. 
변환된 XPS 파일을 저장합니다.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF를 마크다운으로 변환



PDF 콘텐츠를 Markdown으로 내보내야 하는 경우 이 예를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/)을 만들고 이미지 리소스 디렉터리와 HTML 이미지 태그 출력을 구성합니다.

1. 
`document.save(outputFile.toString(), saveOptions)`으로 전화하면 PDF 콘텐츠가 외부 이미지 리소스와 함께 Markdown으로 내보내집니다.
1. 생성된 Markdown 파일을 저장합니다.


```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PDF를 Mobi XML로 변환



PDF 컨텐츠를 Mobi 호환 XML로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
대상 직렬화 형식으로 [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml`을 선택합니다.
1. `document.save(outputFile.toString(), SaveFormat.MobiXml)`으로 전화하면 PDF가 Mobi 호환 XML로 내보내집니다.

1. 
변환된 파일을 저장합니다.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

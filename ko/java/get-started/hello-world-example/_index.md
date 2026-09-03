---
title: Java를 사용한 Hello World의 예
linktitle: Hello World 예시
type: docs
weight: 20
url: /java/hello-world-example/
description: 이 샘플은 Java용 Aspose.PDF를 사용하여 스타일이 지정된 Hello World 텍스트가 포함된 간단한 PDF 문서를 만드는 방법을 보여줍니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 통한 Hello World 예제
Abstract: 이 문서에서는 Java용 Aspose.PDF에 대한 Hello World 예제를 제공합니다. 이 예제에서는 새 PDF 문서를 만들고, 페이지를 추가하고, 사용자 정의 위치, 글꼴 및 색상이 포함된 TextFragment를 만들고, TextBuilder를 사용하여 페이지에 텍스트를 추가하고, 결과를 PDF 파일로 저장합니다.
---
"Hello World" 예제는 기본 PDF 생성 작업 흐름을 이해하는 가장 짧은 경로입니다. 이 문서의 예제에서는 새 PDF를 만들고, 스타일이 지정된 텍스트 조각을 페이지에 배치하고, 출력 파일을 저장합니다.



Java 예제는 다음 단계를 따릅니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 개체를 만듭니다.

1. 
문서에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
`Hello, world!` 텍스트를 사용하여 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 만듭니다.
1. [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) 프래그먼트를 통해 [위치](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), 글꼴, 글꼴 크기, 배경색, 전경색을 설정합니다.

1. 
페이지에 대한 [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/)를 만듭니다.

1. 
[텍스트 조각](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)을 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 추가합니다.

1. 
PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.



다음 Java 코드는 `GetStartedExamples.java`을 기반으로 합니다.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

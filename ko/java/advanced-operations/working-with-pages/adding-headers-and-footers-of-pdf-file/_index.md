---
title: Java에서 PDF 머리글 및 바닥글 추가
linktitle: PDF에 머리글 및 바닥글 추가
type: docs
weight: 50
url: /java/add-headers-and-footers-of-pdf-file/
description: 텍스트, 이미지 및 구조화된 콘텐츠를 사용하여 Java에서 PDF 파일에 머리글과 바닥글을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 머리글 및 바닥글 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 머리글과 바닥글을 추가하는 방법을 보여줍니다. 텍스트, 페이지 번호 매기기, HTML, 이미지, 표, LaTeX 기반 머리글 및 바닥글 콘텐츠를 다룹니다.
---

Aspose.PDF for Java를 사용하면 `HeaderFooter` 개체를 각 페이지에 할당하고 다양한 콘텐츠 유형으로 채울 수 있습니다.


## 
텍스트 머리글 및 바닥글 추가



각 페이지의 상단과 하단에 간단한 텍스트 콘텐츠가 필요한 경우 이 예를 사용하세요.


1. 
[HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 개체를 만들고 텍스트 조각을 추가합니다.

1. 
머리글과 바닥글의 여백을 구성합니다.

1. 
원본 PDF의 각 페이지에 적용하고 결과를 저장합니다.


```java
public static void addHeaderAndFooterAsText(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Demo header"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Demo footer"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
페이지 번호 매기기를 사용하여 머리글 및 바닥글 추가



머리글이나 바닥글에 현재 페이지 번호와 총 페이지 수가 표시되어야 하는 경우 이 예를 사용하세요.


1. 
페이지 번호 매기기 자리 표시자가 있는 [HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 개체를 만듭니다.

1. 
두 개체 모두에 대한 여백을 구성합니다.

1. 
이를 각 페이지에 적용하고 업데이트된 PDF를 저장하세요.


```java
public static void usingHeaderAndFooterForPageNumbering(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new TextFragment("Page $p from $P"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new TextFragment("Page $p / $P"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
HTML 머리글 및 바닥글 추가



머리글 및 바닥글 내용에 인라인 HTML 형식이 포함되어야 하는 경우 이 예를 사용하십시오.


1. 
[HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 개체를 생성하고 [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) 콘텐츠를 추가합니다.

1. 
배치를 위한 여백을 구성합니다.

1. 
각 페이지에 머리글과 바닥글을 지정하고 문서를 저장하세요.


```java
public static void addHeaderAndFooterAsHtml(Path inputFile, Path outputFile) {
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(new HtmlFragment("This is an HTML <strong>Header</strong>"));

    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(new HtmlFragment("Powered by <i>Aspose.PDF</i>"));

    MarginInfo margin = new MarginInfo();
    margin.setLeft(50);
    margin.setTop(20);
    header.setMargin(margin);
    footer.setMargin(margin);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
이미지 머리글 및 바닥글 추가



머리글과 바닥글이 모든 페이지에 이미지를 표시해야 하는 경우 이 예를 사용하세요.


1. 
[이미지](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 개체를 생성하고 머리글 및 바닥글 컨테이너에 추가합니다.

1. 
여백을 구성하고 각 페이지에 컨테이너를 할당합니다.

1. 
업데이트된 PDF를 저장합니다.


```java
public static void addHeaderAndFooterAsImage(Path inputFile, Path imageFile, Path outputFile) {
    Image headerImage = new Image();
    headerImage.setFile(imageFile.toString());
    HeaderFooter header = new HeaderFooter();
    header.getParagraphs().add(headerImage);

    Image footerImage = new Image();
    footerImage.setFile(imageFile.toString());
    HeaderFooter footer = new HeaderFooter();
    footer.getParagraphs().add(footerImage);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            MarginInfo margin = new MarginInfo();
            margin.setLeft(50);
            header.setMargin(margin);
            footer.setMargin(margin);
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
표 기반 머리글 및 바닥글 추가



머리글과 바닥글 내용이 표 레이아웃과 텍스트 스타일을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
필요한 텍스트 스타일과 테이블 개체를 만듭니다.

1. 
[HeaderFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerfooter/) 컨테이너에 테이블을 추가합니다.

1. 
각 페이지에 머리글과 바닥글을 적용하고 문서를 저장하세요.


```java
public static void addHeaderAndFooterAsTable(Path inputFile, Path outputFile) {
    TextState textStateHeader = new TextState();
    textStateHeader.setFont(FontRepository.findFont("Arial"));
    textStateHeader.setFontSize(12);
    textStateHeader.setHorizontalAlignment(HorizontalAlignment.Center);

    TextState textStateFooter = new TextState();
    textStateFooter.setFont(FontRepository.findFont("Arial"));
    textStateFooter.setFontSize(12);
    textStateFooter.setHorizontalAlignment(HorizontalAlignment.Left);

    HeaderFooter header = new HeaderFooter();
    HeaderFooter footer = new HeaderFooter();

    Table tableHeader = new Table();
    tableHeader.setColumnWidths(String.valueOf(594 - header.getMargin().getLeft() - header.getMargin().getRight()));
    tableHeader.getRows().add().getCells().add("This is a Table Header", textStateHeader);

    Table table = new Table();
    table.setColumnWidths(String.valueOf(594 - footer.getMargin().getLeft() - footer.getMargin().getRight()));
    table.getRows().add().getCells().add("Powered by Aspose.PDF", textStateFooter);

    header.getParagraphs().add(tableHeader);
    footer.getParagraphs().add(table);
    footer.getMargin().setLeft(150);

    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getPages().size(); i++) {
            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

## 
LaTeX 머리글 및 바닥글 추가



머리글과 바닥글이 TeX 또는 LaTeX 콘텐츠를 렌더링해야 하는 경우 이 예제를 사용하세요.


1. 
원본 PDF를 열고 총 페이지 수를 확인합니다.

1. 
각 페이지의 머리글과 바닥글에 대한 [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) 콘텐츠를 만듭니다.

1. 
콘텐츠를 할당하고 문서를 저장합니다.

```java
public static void addHeaderAndFooterAsLatex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int pageCount = document.getPages().size();
        for (int i = 1; i <= pageCount; i++) {
            HeaderFooter header = new HeaderFooter();
            header.getParagraphs().add(new TeXFragment("This is a LaTeX Header. \\today\\", true));

            HeaderFooter footer = new HeaderFooter();
            footer.getParagraphs().add(new TeXFragment("\\copyright\\ 2025 My Company -- Page \\thepage\\ is " + pageCount, true));

            document.getPages().get_Item(i).setHeader(header);
            document.getPages().get_Item(i).setFooter(footer);
        }
        document.save(outputFile.toString());
    }
}
```

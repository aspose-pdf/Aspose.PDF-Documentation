---
title: Java를 사용한 기본 텍스트 추출
linktitle: 기본 텍스트 추출
type: docs
weight: 10
url: /java/basic-text-extraction/
description: 모든 페이지, 특정 페이지 또는 단락 구조별로 Aspose.PDF를 사용하여 Java의 PDF 문서에서 텍스트를 추출하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

기본 텍스트 추출은 Java에서 PDF 콘텐츠를 읽기 위한 시작점입니다. Aspose.PDF는 두 가지 일반적인 접근 방식을 제공합니다.


- 
문서나 페이지에서 일반 텍스트 결과가 필요한 경우 `TextAbsorber`을 사용하세요.
- 페이지, 섹션, 단락, 줄 및 조각 그룹화를 유지해야 하는 경우 `ParagraphAbsorber`을 사용하세요.



PDF 페이지는 워드 프로세서 문서처럼 텍스트를 저장하지 않으므로 추출된 순서는 페이지 콘텐츠 스트림 및 레이아웃에 따라 달라집니다. 지역별 추출, 형상 세부정보, 다중 열 레이아웃, 주석, 강조 표시된 텍스트 또는 위 첨자 및 아래 첨자 감지의 경우 이 섹션의 관련 추출 기사를 사용하세요.


## 
모든 페이지에서 텍스트 추출



전체 문서에서 일반 텍스트 스트림을 수집하여 파일에 쓰려면 `TextAbsorber`을 사용하세요. 읽을 수 있는 텍스트 콘텐츠만 필요하고 단락 경계나 좌표는 필요하지 않은 경우 가장 간단한 옵션입니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 만들어 문서 전체에 걸쳐 텍스트를 축적하세요.

1. 
`document.getPages().accept(textAbsorber)`으로 전화하면 흡수체가 모든 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 방문하게 됩니다.

1. 
추출된 텍스트 버퍼를 출력 파일에 씁니다.


```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
특정 페이지에서 텍스트 추출



필요한 페이지에만 흡수체를 적용하십시오. `Document` 페이지 컬렉션의 페이지 번호는 1부터 시작하므로 `get_Item(1)`은 첫 번째 페이지를 읽습니다.

1. [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
단일 페이지 추출을 위해 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 만듭니다.

1. 
페이지 번호로 선택한 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 `accept(textAbsorber)`을 호출합니다.

1. 
추출된 텍스트 버퍼를 출력 파일에 씁니다.


```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
단락 구조별로 텍스트 추출

단일 일반 텍스트 스트림 대신 구조적 그룹화가 필요한 경우 `ParagraphAbsorber`을 사용하세요. 섹션, 단락, 줄 및 `TextFragment` 개체가 포함된 페이지 마크업을 반환합니다. 이는 출력에서 ​​텍스트의 논리적 블록을 유지해야 할 때 유용합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/)를 생성하고 전체 문서를 방문하여 페이지 마크업 결과를 구축하세요.

1. 
흡수체에 의해 노출된 페이지 마크업, 섹션, 단락, 줄 및 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 개체를 반복합니다.

1. 
구조적 그룹화가 유지되도록 명시적인 페이지, 섹션 및 단락 번호 매기기를 사용하여 출력 텍스트를 작성합니다.
1. 추출된 단락 텍스트를 출력 파일에 씁니다.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```

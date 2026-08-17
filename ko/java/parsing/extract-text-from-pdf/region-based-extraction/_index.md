---
title: Java를 사용한 지역 기반 추출
linktitle: 지역 기반 추출
type: docs
weight: 20
url: /java/region-based-extraction/
description: Java용 Aspose.PDF를 사용하여 특정 페이지 영역에서 텍스트를 추출하거나 PDF 문서의 단락 형상을 검사하는 방법을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
직사각형 페이지 영역에서 텍스트 추출



페이지의 정의된 영역으로 추출을 제한하려면 `TextSearchOptions`을 `Rectangle`과 함께 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
선택한 페이지 영역의 텍스트를 수집하려면 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 생성하세요.

1. 
대상 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)에 대해 [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/)를 만들고 `setLimitToPageBounds(true)`을 활성화하면 추출이 표시되는 페이지 상자 내에 유지됩니다.

1. 
구성된 검색 옵션을 흡수체에 적용하고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 방문합니다.

1. 
추출된 텍스트 버퍼를 출력 파일에 씁니다.


```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## 
기하학 정보가 포함된 단락 추출



추출된 텍스트와 함께 섹션 직사각형 및 단락 다각형을 검사하려면 `ParagraphAbsorber`을 사용하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/)를 생성하고 대상 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 방문하여 페이지 마크업 정보를 구축합니다.

1. 
첫 번째 페이지 마크업 결과를 읽고 해당 섹션과 단락을 반복합니다.

1. 
[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 라인에서 재구성된 각 섹션 직사각형, 단락 다각형 및 단락 텍스트를 수집합니다.

1. 
기하학과 추출된 텍스트 세부정보를 사용하여 출력 보고서를 작성합니다.

1. 
추출된 세부정보를 출력 파일에 씁니다.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```

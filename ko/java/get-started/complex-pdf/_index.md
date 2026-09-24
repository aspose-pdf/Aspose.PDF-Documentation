---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
weight: 30
url: /java/complex-pdf-example/
description: Aspose.PDF for Java를 사용하면 이미지, 텍스트 조각 및 테이블을 하나의 파일에 포함하는 보다 복잡한 PDF 문서를 만들 수 있습니다.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 복잡한 PDF 만들기
Abstract: 이 문서에서는 Aspose.PDF를 사용하여 Java에서 보다 복잡한 PDF를 만드는 방법을 보여줍니다. 이 예에서는 이미지, 서식이 지정된 제목, 설명 텍스트 블록, 스타일이 지정된 머리글 셀과 생성된 일람표 행이 포함된 테이블을 추가한 다음 결과를 PDF 문서로 저장합니다.
---
[Hello World](/pdf/java/hello-world-example/) 예제는 가장 간단한 PDF 생성 경로를 다룹니다. 이 예는 해당 워크플로를 기반으로 그래픽, 텍스트 및 표 형식의 콘텐츠를 결합하는 보다 풍부한 문서를 만듭니다.



Java로 더 복잡한 PDF 문서를 생성하려면:


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 생성하고 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 추가하세요.

1. 
`page.addImage(...)` 및 대상 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 사용하여 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)에 이미지를 추가합니다.

1. 
헤더 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 만들고 글꼴, 크기, 정렬 및 [위치](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/)를 설정합니다.
1. 설명 단락에 대한 두 번째 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)를 만듭니다.

1. 
테두리, 패딩, 머리글 스타일을 적용하여 [표](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)를 만드세요.

1. 
생성된 일정 행을 [테이블](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)에 추가합니다.

1. 
[페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 단락에 [표](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)를 추가합니다.

1. 
출력된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

다음 Java 코드는 `GetStartedExamples.java`을 기반으로 합니다.


```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```


동일한 예에서는 도우미 메서드를 사용하여 헤더 형식 및 생성된 출발 시간이 포함된 일정 테이블을 준비합니다.

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```

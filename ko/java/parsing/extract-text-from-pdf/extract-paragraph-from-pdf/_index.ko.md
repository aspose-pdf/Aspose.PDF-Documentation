---
title: PDF에서 단락 추출 
linktitle: 단락 추출
type: docs
weight: 20
url: /java/extract-paragraph-from-pdf/
description: 이 기사는 Aspose.PDF에서 텍스트를 추출하는 특별한 도구인 ParagraphAbsorber를 사용하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 단락 형태로 PDF 문서에서 텍스트 추출

특정 텍스트("일반 텍스트" 또는 "정규 표현식" 사용)를 단일 페이지 또는 전체 문서에서 검색하여 PDF 문서에서 텍스트를 얻을 수 있으며, 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 얻을 수 있습니다.
 때때로 PDF 문서에서 단락을 추출하거나 텍스트를 단락 형태로 추출해야 하는 경우가 있습니다. 우리는 PDF 문서 페이지의 텍스트에서 섹션과 단락을 검색하는 기능을 구현했습니다. 우리는 PDF 문서에서 단락을 추출하는 데 사용할 수 있는 ParagraphAbsorber 클래스를 도입했습니다 (TextFragmentAbsorber 및 TextAbsorber와 유사). ParagraphAbsorber를 사용할 수 있는 두 가지 방법이 있습니다:

**1- PDF 페이지에서 텍스트의 섹션과 단락의 경계를 그리는 방법:**

```java
public static void ExtractParagraph() {
    // 문서 디렉토리의 경로.
    Document doc = new Document(_dataDir + "input.pdf");
    Page page = doc.getPages().get_Item(2);

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.visit(page);

    PageMarkup markup = absorber.getPageMarkups().get(0);

    for (MarkupSection section : markup.getSections()) {
        DrawRectangleOnPage(section.getRectangle(), page);
        for (MarkupParagraph paragraph : section.getParagraphs()) {
            DrawPolygonOnPage(paragraph.getPoints(), page);
        }
    }

    doc.save(_dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page) {
    page.getContents().add(new GSave());
    page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.getContents().add(new SetRGBColorStroke(0, 1, 0));
    page.getContents().add(new SetLineWidth(2));
    page.getContents().add(new Re(rectangle.getLLX(), rectangle.getLLY(), rectangle.getWidth(), rectangle.getHeight()));
    page.getContents().add(new ClosePathStroke());
    page.getContents().add(new GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page) {
    page.getContents().add(new GSave());
    page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.getContents().add(new SetRGBColorStroke(0, 0, 1));
    page.getContents().add(new SetLineWidth(1));
    page.getContents().add(new MoveTo(polygon[0].getX(), polygon[0].getY()));
    for (int i = 1; i < polygon.length; i++) {
        page.getContents().add(new LineTo(polygon[i].getX(), polygon[i].getY()));
    }
    page.getContents().add(new LineTo(polygon[0].getX(), polygon[0].getY()));
    page.getContents().add(new ClosePathStroke());
    page.getContents().add(new GRestore());
}
```

**2- 단락 컬렉션을 반복하고 그들의 텍스트를 얻음으로써:**

```java
public static void ExtractParagraph02() {
        // 기존 PDF 파일 열기
        Document doc = new Document(_dataDir + "input.pdf");
        // ParagraphAbsorber 인스턴스화
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(doc);

        for (PageMarkup markup : absorber.getPageMarkups()) {
            int i = 1;
            for (MarkupSection section : markup.getSections()) {
                int j = 1;

                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();

                    for (java.util.List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    paragraphText.append("\r\n");

                    System.out.println("단락 "+j+" 섹션 "+ i + " 페이지에서"+ ":"+markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
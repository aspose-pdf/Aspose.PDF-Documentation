---
title: PDF에서 단락 추출
linktitle: 단락 추출
type: docs
weight: 20
url: ko/androidjava/extract-paragraph-from-pdf/
description: 이 문서에서는 Aspose.PDF의 특별한 도구인 ParagraphAbsorber를 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에서 단락 형태로 텍스트 추출하기

특정 텍스트("일반 텍스트" 또는 "정규 표현식" 사용)를 단일 페이지 또는 전체 문서에서 검색하여 PDF 문서에서 텍스트를 가져오거나, 단일 페이지, 페이지 범위 또는 전체 문서의 모든 텍스트를 가져올 수 있습니다.
 일부 경우에는 PDF 문서에서 단락을 추출하거나 단락 형식의 텍스트를 필요로 합니다. 우리는 PDF 문서 페이지의 텍스트에서 섹션과 단락을 검색하는 기능을 구현했습니다. 우리는 ParagraphAbsorber 클래스를 소개했으며 (TextFragmentAbsorber 및 TextAbsorber와 유사), 이를 사용하여 PDF 문서에서 단락을 추출할 수 있습니다. ParagraphAbsorber를 사용할 수 있는 두 가지 방법이 있습니다:

**1- PDF 페이지의 텍스트 섹션과 단락의 경계를 그리기:**

```java
public static void ExtractParagraph() {
        // 문서 디렉토리 경로.
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
        page.getContents()
                .add(new Re(rectangle.getLLX(), rectangle.getLLY(), rectangle.getWidth(), rectangle.getHeight()));
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

**2- 단락 모음을 반복하여 그들의 텍스트를 얻기:**

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

                    System.out.println("섹션 " + i + "의 단락 " + j + " 페이지" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
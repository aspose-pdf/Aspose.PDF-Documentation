---
title: Извлечь абзац из PDF
linktitle: Извлечь абзац
type: docs
weight: 20
url: /ru/androidjava/extract-paragraph-from-pdf/
description: Узнайте, как извлекать конкретные абзацы из PDF‑документа в Android/Java с помощью Aspose.PDF для извлечения содержимого.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечь текст из PDF‑документа в виде абзацев

Мы можем получить текст из PDF‑документа, ищя определённый текст (using "plain text" or "regular expressions") на одной странице или во всём документе, либо получить полный текст одной страницы, диапазона страниц или всего документа. Однако в некоторых случаях вам требуется извлекать абзацы из PDF‑документа или текст в виде абзацев. Мы реализовали функциональность поиска разделов и абзацев в тексте страниц PDF‑документов. Мы представили класс ParagraphAbsorber (как TextFragmentAbsorber и TextAbsorber), который можно использовать для извлечения абзацев из PDF‑документов. Существует два следующих способа использования ParagraphAbsorber:

**1- По рисованию границы разделов и абзацев текста на странице PDF:**

```java
public static void ExtractParagraph() {
        // The path to the documents directory.
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

**2- Итерация по коллекции абзацев и получение их текста:**

```java
 public static void ExtractParagraph02() {
        // Open an existing PDF file
        Document doc = new Document(_dataDir + "input.pdf");
        // Instantiate ParagraphAbsorber
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

                    System.out.println("Paragraph " + j + " of section " + i + " on page" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```


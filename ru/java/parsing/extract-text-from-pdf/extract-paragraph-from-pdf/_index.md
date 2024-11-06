---
title: Извлечение абзаца из PDF
linktitle: Извлечение абзаца
type: docs
weight: 20
url: ru/java/extract-paragraph-from-pdf/
description: В этой статье описывается, как использовать ParagraphAbsorber - специальный инструмент в Aspose.PDF для извлечения текста из PDF-документов.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста из PDF-документа в форме абзацев

Мы можем получить текст из PDF-документа, осуществляя поиск определенного текста (используя "простой текст" или "регулярные выражения") на одной странице или во всем документе, или мы можем получить полный текст одной страницы, диапазона страниц или всего документа.
 Однако в некоторых случаях вам необходимо извлечь абзацы из PDF-документа или текст в виде абзацев. Мы реализовали функциональность для поиска разделов и абзацев в тексте страниц PDF-документа. Мы представили класс ParagraphAbsorber (как TextFragmentAbsorber и TextAbsorber), который может быть использован для извлечения абзацев из PDF-документов. Существует два способа использования ParagraphAbsorber:

**1- Отрисовка границ разделов и абзацев текста на странице PDF:**

```java
public static void ExtractParagraph() {
    // Путь к каталогу с документами.
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

**2- Путем итерации через коллекцию абзацев и получения их текста:**

```java
public static void ExtractParagraph02() {
        // Открыть существующий PDF файл
        Document doc = new Document(_dataDir + "input.pdf");
        // Создать экземпляр ParagraphAbsorber
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

                    System.out.println("Абзац "+j+" раздела "+ i + " на странице"+ ":"+markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
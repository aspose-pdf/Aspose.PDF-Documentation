---
title: Extrair Parágrafo de PDF
linktitle: Extrair Parágrafo
type: docs
weight: 20
url: /pt/androidjava/extract-paragraph-from-pdf/
description: Saiba como extrair parágrafos específicos de um documento PDF em Android/Java usando Aspose.PDF para extração de conteúdo.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de documento PDF em forma de Parágrafos

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "plain text" ou "regular expressions") em uma única página ou em todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou do documento completo. No entanto, em alguns casos, você precisa extrair parágrafos de um documento PDF ou texto na forma de Parágrafos. Implementamos funcionalidade para pesquisar seções e parágrafos no texto das páginas de documentos PDF. Introduzimos a classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF. Existem duas maneiras a seguir nas quais você pode usar o ParagraphAbsorber:

**1- Desenhando a borda das seções e parágrafos de texto na página PDF:**

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

**2- Iterando pela coleção de parágrafos e obtendo o texto deles:**

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


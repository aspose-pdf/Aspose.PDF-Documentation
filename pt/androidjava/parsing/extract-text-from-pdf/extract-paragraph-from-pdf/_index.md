---
title: Extrair Parágrafo de PDF
linktitle: Extrair Parágrafo
type: docs
weight: 20
url: /pt/androidjava/extract-paragraph-from-pdf/
description: Este artigo descreve como usar o ParagraphAbsorber - uma ferramenta especial no Aspose.PDF para extrair texto de documentos PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de documento PDF em forma de Parágrafos

Podemos obter texto de um documento PDF pesquisando um texto específico (usando "texto simples" ou "expressões regulares") de uma única página ou de todo o documento, ou podemos obter o texto completo de uma única página, intervalo de páginas ou documento completo.
 Porém, em alguns casos, você precisa extrair parágrafos de um documento PDF ou texto na forma de Parágrafos. Implementamos a funcionalidade para pesquisar seções e parágrafos no texto das páginas do documento PDF. Introduzimos a Classe ParagraphAbsorber (como TextFragmentAbsorber e TextAbsorber), que pode ser usada para extrair parágrafos de documentos PDF. Existem duas maneiras a seguir nas quais você pode usar o ParagraphAbsorber:

**1- Desenhando a borda das seções e parágrafos de texto na página do PDF:**

```java
public static void ExtractParagraph() {
        // O caminho para o diretório de documentos.
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
        page.getContents().add(new ConcatenateMatrix(1, 0, 1, 0, 0, 0));
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

**2- Ao iterar pela coleção de parágrafos e obter o texto deles:**

```java
 public static void ExtractParagraph02() {
        // Abrir um arquivo PDF existente
        Document doc = new Document(_dataDir + "input.pdf");
        // Instanciar ParagraphAbsorber
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

                    System.out.println("Parágrafo " + j + " da seção " + i + " na página" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
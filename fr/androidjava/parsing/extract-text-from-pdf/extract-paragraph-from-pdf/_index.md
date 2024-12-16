---
title: Extraire un Paragraphe d'un PDF
linktitle: Extraire un Paragraphe
type: docs
weight: 20
url: /fr/androidjava/extract-paragraph-from-pdf/
description: Cet article décrit comment utiliser ParagraphAbsorber - un outil spécial dans Aspose.PDF pour extraire du texte des documents PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du Texte d'un document PDF sous forme de Paragraphes

Nous pouvons obtenir du texte d'un document PDF en recherchant un texte particulier (en utilisant du "texte brut" ou des "expressions régulières") à partir d'une seule page ou de l'ensemble du document, ou nous pouvons obtenir le texte complet d'une seule page, d'une plage de pages ou de l'ensemble du document.
 Cependant, dans certains cas, vous devez extraire des paragraphes d'un document PDF ou du texte sous forme de paragraphes. Nous avons implémenté une fonctionnalité pour rechercher des sections et des paragraphes dans le texte des pages de documents PDF. Nous avons introduit la classe ParagraphAbsorber (comme TextFragmentAbsorber et TextAbsorber), qui peut être utilisée pour extraire des paragraphes de documents PDF. Il existe deux façons suivantes d'utiliser ParagraphAbsorber :

**1- En dessinant la bordure des sections et paragraphes de texte sur la page PDF :**

```java
public static void ExtractParagraph() {
        // Le chemin vers le répertoire des documents.
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

**2- En itérant à travers la collection de paragraphes et en obtenant leur texte :**

```java
 public static void ExtractParagraph02() {
        // Ouvrir un fichier PDF existant
        Document doc = new Document(_dataDir + "input.pdf");
        // Instancier ParagraphAbsorber
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

                    System.out.println("Paragraphe " + j + " de la section " + i + " sur la page" + ":" + markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
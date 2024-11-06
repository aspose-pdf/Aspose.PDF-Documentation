---
title: Extraer Párrafo de PDF 
linktitle: Extraer Párrafo
type: docs
weight: 20
url: es/java/extract-paragraph-from-pdf/
description: Este artículo describe cómo usar ParagraphAbsorber - una herramienta especial en Aspose.PDF para extraer texto de documentos PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de un documento PDF en forma de Párrafos

Podemos obtener texto de un documento PDF buscando un texto particular (usando "texto sin formato" o "expresiones regulares") de una sola página o de todo el documento, o podemos obtener el texto completo de una sola página, rango de páginas o documento completo.
 Sin embargo, en algunos casos, necesitas extraer párrafos de un documento PDF o texto en forma de párrafos. Hemos implementado una funcionalidad para buscar secciones y párrafos en el texto de las páginas de documentos PDF. Hemos introducido la Clase ParagraphAbsorber (como TextFragmentAbsorber y TextAbsorber), que se puede usar para extraer párrafos de documentos PDF. Hay dos formas en las que puedes usar ParagraphAbsorber:

**1- Dibujando el borde de las secciones y párrafos de texto en la página PDF:**

```java
public static void ExtractParagraph() {
    // La ruta al directorio de documentos.
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

**2- Iterando a través de la colección de párrafos y obteniendo el texto de ellos:**

```java
public static void ExtractParagraph02() {
        // Abrir un archivo PDF existente
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

                    System.out.println("Párrafo "+j+" de la sección "+ i + " en la página"+ ":"+markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
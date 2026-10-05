---
title: Extracción basada en regiones usando Java
linktitle: Extracción basada en regiones
type: docs
weight: 20
url: /es/java/region-based-extraction/
description: Aprenda cómo extraer texto de una región específica de la página o inspeccionar la geometría de los párrafos en documentos PDF con Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extraer texto de una región rectangular de la página

Utilice `TextSearchOptions` con un `Rectangle` para restringir la extracción a un área definida en una página.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para recopilar texto del área de página seleccionada.
1. Cree [`TextSearchOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) para el objetivo [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) y habilite `setLimitToPageBounds(true)` para que la extracción permanezca dentro del cuadro de página visible.
1. Aplique las opciones de búsqueda configuradas al absorber y visite el objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Escriba el búfer de texto extraído en el archivo de salida.

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

## Extraer párrafos con información de geometría

Utilice `ParagraphAbsorber` para inspeccionar los rectángulos de sección y los polígonos de párrafo junto con el texto extraído.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`ParagraphAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) y visite el objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para generar información de marcado de página.
1. Lea el primer resultado de marcado de página y recorra sus secciones y párrafos.
1. Recopile cada rectángulo de sección, polígono de párrafo y el texto del párrafo reconstruido a partir de su [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) líneas.
1. Construya el informe de salida con geometría y detalles del texto extraído.
1. Escriba los detalles extraídos en el archivo de salida.

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

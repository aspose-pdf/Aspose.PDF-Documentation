---
title: Extracción basada en regiones usando Java
linktitle: Extracción basada en regiones
type: docs
weight: 20
url: /java/region-based-extraction/
description: Aprenda a extraer texto de una región de página específica o inspeccionar la geometría de párrafos en documentos PDF con Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
Extraer texto de una región de página rectangular



Utilice `TextSearchOptions` con `Rectangle` para restringir la extracción a un área definida en una página.

1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para recopilar texto del área de la página seleccionada.

1. Cree [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) para el [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) de destino y habilite `setLimitToPageBounds(true)` para que la extracción permanezca dentro del cuadro de página visible.

1. Aplique las opciones de búsqueda configuradas al absorbente y visite la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

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

## Extraer párrafos con información de geometría.



Utilice `ParagraphAbsorber` para inspeccionar rectángulos de sección y polígonos de párrafo junto con el texto extraído.


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) y visite la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino para crear información de marcado de página.

1. Lea el resultado del marcado de la primera página y repita sus secciones y párrafos.
1. Recopile cada rectángulo de sección, polígono de párrafo y el texto del párrafo reconstruido a partir de sus líneas [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. Cree el informe de salida con geometría y detalles de texto extraídos.

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

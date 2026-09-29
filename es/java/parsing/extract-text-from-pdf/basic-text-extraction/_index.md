---
title: Extracción básica de texto usando Java
linktitle: Extracción básica de texto
type: docs
weight: 10
url: /es/java/basic-text-extraction/
description: Aprenda cómo extraer texto de documentos PDF en Java con Aspose.PDF de todas las páginas, de una página específica o por estructura de párrafos.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
La extracción básica de texto es el punto de partida para leer el contenido PDF en Java. Aspose.PDF ofrece dos enfoques comunes:

- Utilice `TextAbsorber` cuando necesita un resultado de texto plano de un documento o página.
- Utilice `ParagraphAbsorber` cuando necesita preservar la agrupación de página, sección, párrafo, línea y fragmento.

Las páginas PDF no almacenan texto como lo hace un documento de procesamiento de textos, por lo que el orden extraído depende del flujo de contenido y el diseño de la página. Para extracción específica de regiones, detalles de geometría, diseños de varias columnas, anotaciones, texto resaltado o detección de superíndice y subíndice, utilice los artículos de extracción relacionados en esta sección.

## Extraer texto de todas las páginas

Utilice `TextAbsorber` para recopilar una secuencia de texto plano de todo el documento y escribirla en un archivo. Esta es la opción más simple cuando solo necesita el contenido de texto legible y no necesita los límites de párrafo o las coordenadas.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para acumular texto a lo largo de todo el documento.
1. Llame `document.getPages().accept(textAbsorber)` así cada [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) es visitado por el absorbente.
1. Escriba el búfer de texto extraído en el archivo de salida.

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extraer texto de una página específica

Aplique el absorbedor solo en la página que necesita. Números de página en el `Document` la colección de páginas es de base 1, así que `get_Item(1)` lee la primera página.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`TextAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para la extracción de una sola página.
1. Llame `accept(textAbsorber)` en el objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) seleccionado por número de página.
1. Escriba el búfer de texto extraído en el archivo de salida.

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## Extraer texto por estructura de párrafo

Utilice `ParagraphAbsorber` cuando necesita agrupación estructural en lugar de un solo flujo de texto plano. Devuelve marcas de página con secciones, párrafos, líneas y `TextFragment` objetos, lo cual es útil cuando la salida debe preservar bloques lógicos de texto.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`ParagraphAbsorber`](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) y recorra todo el documento para crear resultados de marcado de página.
1. Itere a través de las marcas de página, secciones, párrafos, líneas y [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos expuestos por el absorber.
1. Construya el texto de salida con numeración explícita de página, sección y párrafo para que se preserve la agrupación estructural.
1. Escriba el texto del párrafo extraído en el archivo de salida.

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```

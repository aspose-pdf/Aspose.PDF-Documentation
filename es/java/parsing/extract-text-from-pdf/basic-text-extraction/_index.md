---
title: Extracción básica de texto usando Java
linktitle: Extracción básica de texto
type: docs
weight: 10
url: /es/java/basic-text-extraction/
description: Aprende cómo extraer texto de documentos PDF en Java con Aspose.PDF de todas las páginas, de una página específica o por estructura de párrafos.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
La extracción básica de texto es el punto de partida para leer contenido PDF en Java. Aspose.PDF ofrece dos enfoques comunes:

- Usar `TextAbsorber` cuando necesitas un resultado de texto plano de un documento o página.
- Usar `ParagraphAbsorber` cuando necesitas preservar la agrupación de página, sección, párrafo, línea y fragmento.

Las páginas PDF no almacenan texto como lo hace un documento de procesamiento de textos, por lo que el orden extraído depende del flujo de contenido y el diseño de la página. Para extracción específica de regiones, detalles geométricos, diseños de múltiples columnas, anotaciones, texto resaltado, o detección de superíndices y subíndices, utilice los artículos de extracción relacionados en esta sección.

## Extraer texto de todas las páginas

Usar `TextAbsorber` para recopilar un flujo de texto plano de todo el documento y escribirlo en un archivo. Esta es la opción más sencilla cuando solo necesita el contenido de texto legible y no necesita los límites de los párrafos ni las coordenadas.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para acumular texto en todo el documento.
1. Llamar `document.getPages().accept(textAbsorber)` así cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) es visitado por el absorbente.
1. Escribe el búfer de texto extraído al archivo de salida.

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

Aplicar el absorbente solo a la página que necesites. Números de página en el `Document` La colección de páginas es basada en 1, por lo que `get_Item(1)` lee la primera página.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para extracción de una sola página.
1. Llamar `accept(textAbsorber)` en el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) seleccionado por número de página.
1. Escribe el búfer de texto extraído al archivo de salida.

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

Usar `ParagraphAbsorber` cuando necesite agrupación estructural en lugar de una sola secuencia de texto plano. Devuelve marcas de página con secciones, párrafos, líneas y `TextFragment` objetos, lo cual es útil cuando la salida debe preservar bloques lógicos de texto.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) y visite todo el documento para crear resultados de marcado de página.
1. Iterar a través de los marcados de página, secciones, párrafos, líneas y [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos expuestos por el absorbente.
1. Construya el texto de salida con numeración explícita de página, sección y párrafo para que se preserve la agrupación estructural.
1. Escribe el texto del párrafo extraído en el archivo de salida.

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

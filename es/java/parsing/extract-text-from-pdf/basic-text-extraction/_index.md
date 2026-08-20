---
title: Extracción de texto básico usando Java
linktitle: Extracción de texto básico
type: docs
weight: 10
url: /java/basic-text-extraction/
description: Aprenda a extraer texto de documentos PDF en Java con Aspose.PDF de todas las páginas, de una página específica o por estructura de párrafos.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La extracción de texto básica es el punto de partida para leer contenido PDF en Java. Aspose.PDF proporciona dos enfoques comunes:


- 
Utilice `TextAbsorber` cuando necesite un resultado de texto sin formato de un documento o página.
- Utilice `ParagraphAbsorber` cuando necesite conservar la agrupación de páginas, secciones, párrafos, líneas y fragmentos.



Las páginas PDF no almacenan texto como un documento de procesamiento de textos, por lo que el orden extraído depende del flujo de contenido y el diseño de la página. Para extracción específica de región, detalles de geometría, diseños de varias columnas, anotaciones, texto resaltado o detección de superíndices y subíndices, utilice los artículos de extracción relacionados en esta sección.


## 
Extraer texto de todas las páginas.



Utilice `TextAbsorber` para recopilar un flujo de texto plano de todo el documento y escribirlo en un archivo. Esta es la opción más sencilla cuando solo necesita contenido de texto legible y no necesita límites ni coordenadas de párrafo.


1. 
Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para acumular texto en todo el documento.

1. 
Llame a `document.getPages().accept(textAbsorber)` para que el absorbente visite cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Escriba el búfer de texto extraído en el archivo de salida.


```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
Extraer texto de una página específica



Aplique el absorbente solo a la página que necesita. Los números de página en la colección de páginas `Document` están basados ​​en 1, por lo que `get_Item(1)` lee la primera página.

1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) para la extracción de una sola página.

1. 
Llame a `accept(textAbsorber)` en la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino seleccionada por el número de página.

1. 
Escriba el búfer de texto extraído en el archivo de salida.


```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 
Extraer texto por estructura de párrafo

Utilice `ParagraphAbsorber` cuando necesite agrupación estructural en lugar de una única secuencia de texto sin formato. Devuelve marcas de página con secciones, párrafos, líneas y objetos `TextFragment`, lo cual es útil cuando la salida debe preservar bloques lógicos de texto.


1. 
Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) y visite el documento completo para generar resultados de marcado de página.

1. 
Itere a través de las marcas de página, secciones, párrafos, líneas y objetos [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) expuestos por el absorbente.

1. 
Cree el texto de salida con numeración explícita de páginas, secciones y párrafos para conservar la agrupación estructural.
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

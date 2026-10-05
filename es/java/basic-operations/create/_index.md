---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: /es/java/create-document/
description: Aprenda cómo crear un documento PDF desde cero en Java usando Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generar archivos PDF con Aspose.PDF for Java
Abstract: Este artículo muestra cómo crear un archivo PDF en Java usando Aspose.PDF. El ejemplo crea un nuevo objeto Document, añade una página, inserta un TextFragment con texto de muestra y guarda el resultado como un archivo PDF.
---
Crear archivos PDF mediante código es una necesidad común para informes, facturas y documentos empresariales generados. Aspose.PDF for Java proporciona una forma directa de construir un documento desde cero.

## Crear un archivo PDF en Java

Para crear un documento PDF programáticamente:

1. Cree un objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Agregue un [`TextFragment`](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) a los párrafos de la página.
1. Guarde el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a un archivo de salida.

## Crear un documento PDF simple

El siguiente ejemplo de Java se basa en `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

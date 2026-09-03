---
title: Crear documento PDF de forma programática
linktitle: Crear PDF
type: docs
weight: 10
url: /es/java/create-document/
description: Aprenda cómo crear un documento PDF desde cero en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generando archivos PDF con Aspose.PDF for Java
Abstract: Este artículo muestra cómo crear un archivo PDF en Java usando Aspose.PDF. El ejemplo crea un nuevo objeto Document, agrega una página, inserta un TextFragment con texto de muestra y guarda el resultado como un archivo PDF.
---
Crear archivos PDF mediante código es un requisito común para informes, facturas y documentos empresariales generados. Aspose.PDF for Java ofrece una forma directa de construir un documento desde cero.

## Cómo crear un archivo PDF en Java

Para crear un documento PDF programáticamente:

1. Crear un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objeto.
1. Agregar un [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Agregar un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) a los párrafos de la página.
1. Guardar el [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a un archivo de salida.

## Crear un documento PDF sencillo

El siguiente ejemplo en Java se basa en `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

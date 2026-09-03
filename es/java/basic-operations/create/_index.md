---
title: Crear documento PDF mediante programación
linktitle: Crear PDF
type: docs
weight: 10
url: /java/create-document/
description: Aprenda a crear un documento PDF desde cero en Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Generando archivos PDF con Aspose.PDF para Java
Abstract: Este artículo muestra cómo crear un archivo PDF en Java usando Aspose.PDF. El ejemplo crea un nuevo objeto Documento, agrega una página, inserta un TextFragment con texto de muestra y guarda el resultado como un archivo PDF.
---
La creación de archivos PDF en código es un requisito común para informes, facturas y documentos comerciales generados. Aspose.PDF para Java proporciona una forma directa de crear un documento desde cero.


## 
Cómo crear un archivo PDF en Java



Para crear un documento PDF mediante programación:


1. Cree un objeto [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al documento.
1. Agregue un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) a los párrafos de la página.

1. Guarde el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) en un archivo de salida.


## 
Crea un documento PDF sencillo



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

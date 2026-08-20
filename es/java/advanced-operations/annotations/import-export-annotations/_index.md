---
title: Importar y exportar anotaciones usando Java
linktitle: Importar y exportar anotaciones
type: docs
weight: 80
url: /java/import-export-annotations/
description: Aprenda a copiar anotaciones de un documento PDF a otro documento PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfiera anotaciones PDF entre documentos en Java.
Abstract: Este artículo explica cómo copiar anotaciones de un PDF de origen y exportarlas a un nuevo documento PDF usando Aspose.PDF para Java. El flujo de trabajo carga el archivo de origen, crea el documento de destino, agrega una página, copia las anotaciones de la primera página de origen y guarda el resultado.
---
## Copie anotaciones de un PDF a otro


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al [Documento] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue cada [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) a la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Lea o repita los elementos de [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) en la página de destino.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Enumere los elementos de [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) en la primera página de origen y agregue cada uno a la página de destino.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```

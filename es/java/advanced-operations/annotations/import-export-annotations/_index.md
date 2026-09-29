---
title: Importar y exportar anotaciones usando Java
linktitle: Importar y exportar anotaciones
type: docs
weight: 80
url: /es/java/import-export-annotations/
description: Aprenda cómo copiar anotaciones de un documento PDF a otro documento PDF usando Aspose.PDF for Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfiera anotaciones PDF entre documentos en Java.
Abstract: Este artículo explica cómo copiar anotaciones de un PDF de origen y exportarlas a un nuevo documento PDF usando Aspose.PDF for Java. El flujo de trabajo carga el archivo de origen, crea el documento de destino, agrega una página, copia las anotaciones de la primera página de origen y guarda el resultado.
---
## Copiar anotaciones de un PDF a otro

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue un [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al destino [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregue cada [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) al objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Lea o iterar a través del [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) elementos en la página de destino.
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumere el [`Annotation`](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) elementos en la primera página de origen y agregue cada uno a la página de destino.

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

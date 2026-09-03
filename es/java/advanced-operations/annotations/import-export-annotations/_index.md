---
title: Importar y exportar anotaciones usando Java
linktitle: Importar y exportar anotaciones
type: docs
weight: 80
url: /es/java/import-export-annotations/
description: Aprenda cómo copiar anotaciones de un documento PDF a otro documento PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transferir anotaciones PDF entre documentos en Java.
Abstract: Este artículo explica cómo copiar anotaciones de un PDF de origen y exportarlas a un nuevo documento PDF usando Aspose.PDF for Java. El flujo de trabajo carga el archivo de origen, crea el documento de destino, añade una página, copia las anotaciones de la primera página de origen y guarda el resultado.
---
## Copiar anotaciones de un PDF a otro

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar un [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al destino [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Agregar cada [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) al objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Leer o iterar a través del [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) elementos en la página de destino.
1. Guardar el PDF actualizado [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerar el [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) elementos en la primera página de origen y agregar cada uno a la página de destino.

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

---
title: Importar y exportar anotaciones usando Java
linktitle: Importar y exportar anotaciones
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: Aprenda a copiar anotaciones de un documento PDF a otro documento PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Transferir anotaciones PDF entre documentos en Java
Abstract: Este artículo explica cómo copiar anotaciones de un PDF de origen y exportarlas a un nuevo documento PDF usando Java. El flujo de trabajo carga el archivo de origen, crea el documento de destino, agrega una página, copia las anotaciones de la primera página de origen y guarda el resultado.
---
## Copie anotaciones de un PDF a otro


1. Abra el PDF de origen y cree un nuevo documento de destino con una página de destino.

2. Enumere las anotaciones en la primera página de origen y agregue cada una a la página de destino.

3. Guarde el documento de destino para conservar las anotaciones copiadas.

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

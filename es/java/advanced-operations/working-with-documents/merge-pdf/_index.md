---
title: Fusionar archivos PDF en Java
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /java/merge-pdf-documents/
description: Aprenda a fusionar varios archivos PDF en un solo documento en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine documentos completos, rangos seleccionados y páginas alternas con Java
Abstract: Este artículo explica cómo fusionar documentos PDF usando Aspose.PDF para Java. Cubre la combinación de dos archivos, la combinación de varios documentos, la selección de rangos de páginas, la inserción de un documento en otro en una posición específica, la alternancia de páginas y la creación de resultados combinados con marcadores de sección.
---
Aspose.PDF para Java admite varias estrategias de fusión dependiendo de cómo se debe ensamblar la salida.


## 
Fusionar dos documentos PDF



Utilice este enfoque cuando necesite el flujo de fusión más simple y desee adjuntar un documento completo a otro.


1. 
Abra ambos objetos PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Agregue la colección [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del segundo documento al primer documento.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```

## 
Copiar un rango de páginas seleccionado entre documentos



Este método auxiliar mantiene la lógica de combinación de rangos de páginas en un solo lugar para que otros ejemplos puedan reutilizar la misma rutina de copia validada.


1. 
Abra o reciba los objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origen y destino.

1. 
Normalice el rango de páginas solicitado para que permanezca dentro de la colección [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible.
1. Agregue cada página del rango validado al documento de destino.


```java
private static void appendPageRange(Document sourceDocument, Document destinationDocument, int startPage, int endPage) {
    int totalPages = sourceDocument.getPages().size();
    if (totalPages == 0) {
        return;
    }

    int start = Math.max(1, startPage);
    int end = Math.min(endPage, totalPages);
    if (start > end) {
        return;
    }

    for (int pageNumber = start; pageNumber <= end; pageNumber++) {
        destinationDocument.getPages().add(sourceDocument.getPages().get_Item(pageNumber));
    }
}
```

## 
Fusionar varios documentos PDF en un solo archivo



Utilice este patrón cuando necesite combinar una lista de archivos de entrada en un único documento de salida en secuencia.


1. 
Cree un [Documento] PDF de salida vacío(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Abra cada archivo de entrada uno a la vez y copie su rango completo de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en el documento de salida.
1. Guarde el resultado combinado después de que se hayan procesado todos los archivos fuente.


```java
public static void mergeMultipleDocuments(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                appendPageRange(sourceDocument, outputDocument, 1, sourceDocument.getPages().size());
            }
        }
        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionar la página seleccionada abarca desde dos documentos



Este ejemplo crea un archivo de salida personalizado tomando solo rangos de páginas específicos de cada documento fuente.


1. 
Abra ambos objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origen y cree un nuevo documento de salida.

1. 
Agregue solo los rangos de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requeridos de cada documento fuente.
1. Guarde el documento de salida ensamblado.


```java
public static void mergeSelectedPageRanges(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        appendPageRange(document1, outputDocument, 1, 2);
        appendPageRange(document2, outputDocument, 2, 3);
        outputDocument.save(outputFile.toString());
    }
}
```

## 
Insertar un documento PDF en otro en una posición específica



Utilice este enfoque cuando un documento deba aparecer dentro de otro en lugar de solo antes o después de él.


1. 
Abra los objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) base e insertados y cree un nuevo documento de salida.

1. 
Copie la primera parte del documento base, luego agregue el documento insertado completo y finalmente agregue el rango base restante de la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Guarde el resultado reordenado en un archivo nuevo.


```java
public static void mergeInsertDocumentAtPosition(Path inputFile1, Path inputFile2, int insertAfterPage, Path outputFile) {
    try (Document baseDocument = new Document(inputFile1.toString());
         Document insertDocument = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int baseTotalPages = baseDocument.getPages().size();
        int insertIndex = Math.max(0, Math.min(insertAfterPage, baseTotalPages));

        appendPageRange(baseDocument, outputDocument, 1, insertIndex);
        appendPageRange(insertDocument, outputDocument, 1, insertDocument.getPages().size());
        appendPageRange(baseDocument, outputDocument, insertIndex + 1, baseTotalPages);

        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionar dos documentos PDF alternando páginas



Este ejemplo intercala páginas de dos documentos, lo que resulta útil cuando ambas entradas deben contribuir página por página al resultado final.


1. 
Abra ambos objetos PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) de origen y cree un nuevo documento de salida.

1. 
Recorra el recuento máximo de páginas disponibles y agregue cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible del primer y segundo documento por turno.
1. Guarde el documento de salida intercalado.


```java
public static void mergeAlternatingPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString());
         Document outputDocument = new Document()) {
        int document1Pages = document1.getPages().size();
        int document2Pages = document2.getPages().size();
        int maxPages = Math.max(document1Pages, document2Pages);

        for (int pageNumber = 1; pageNumber <= maxPages; pageNumber++) {
            if (pageNumber <= document1Pages) {
                outputDocument.getPages().add(document1.getPages().get_Item(pageNumber));
            }
            if (pageNumber <= document2Pages) {
                outputDocument.getPages().add(document2.getPages().get_Item(pageNumber));
            }
        }

        outputDocument.save(outputFile.toString());
    }
}
```

## 
Fusionar documentos con páginas separadoras y marcadores



Utilice este patrón cuando el archivo combinado deba seguir siendo fácil de navegar y mostrar claramente dónde comienza cada documento fuente.


1. 
Cree un [Documento] PDF de salida vacío(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra cada archivo fuente por turno.

1. 
Agregue un separador [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) con un encabezado y luego cree un marcador [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) para esa sección.
1. Agregue las páginas de origen, opcionalmente agregue un marcador que apunte a la primera página de contenido y guarde el documento combinado final.

```java
public static void mergeWithSectionSeparatorsAndBookmarks(List<Path> inputFiles, Path outputFile) {
    try (Document outputDocument = new Document()) {
        int sectionIndex = 1;
        for (Path inputFile : inputFiles) {
            try (Document sourceDocument = new Document(inputFile.toString())) {
                int sourcePageCount = sourceDocument.getPages().size();

                Page separatorPage = outputDocument.getPages().add();
                separatorPage.getParagraphs().add(new TextFragment(
                        "Section " + sectionIndex + ": " + inputFile.getFileName()));

                OutlineItemCollection sectionBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                sectionBookmark.setTitle("Section " + sectionIndex);
                sectionBookmark.setAction(new GoToAction(separatorPage));
                outputDocument.getOutlines().add(sectionBookmark);

                int firstContentPageNumber = outputDocument.getPages().size() + 1;
                appendPageRange(sourceDocument, outputDocument, 1, sourcePageCount);

                if (sourcePageCount > 0 && firstContentPageNumber <= outputDocument.getPages().size()) {
                    OutlineItemCollection contentBookmark = new OutlineItemCollection(outputDocument.getOutlines());
                    contentBookmark.setTitle("Section " + sectionIndex + " Content");
                    contentBookmark.setAction(new GoToAction(outputDocument.getPages().get_Item(firstContentPageNumber)));
                    sectionBookmark.add(contentBookmark);
                }
            }
            sectionIndex++;
        }

        outputDocument.save(outputFile.toString());
    }
}
```

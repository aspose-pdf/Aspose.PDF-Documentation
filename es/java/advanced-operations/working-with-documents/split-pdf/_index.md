---
title: Dividir archivos PDF en Java
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /es/java/split-pdf-document/
description: Aprenda cómo dividir páginas PDF en archivos PDF separados en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida documentos PDF por páginas, rangos, grupos y patrones de nombres de archivo usando Java
Abstract: Este artículo explica cómo dividir documentos PDF usando Aspose.PDF for Java. Cubre la división en páginas individuales, en dos o tres partes, páginas impares y pares, fragmentos de tamaño fijo, rangos personalizados, la primera o última página más el resto, grupos de páginas personalizados y la generación de nombres de archivo estables.
---
Aspose.PDF for Java admite varios patrones de división más allá de la salida de una página por archivo.

## Dividir un PDF en archivos de una sola página

Utilice este enfoque cuando cada página de origen deba convertirse en un documento de salida separado.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) quieres exportar.
1. Agregar lo seleccionado [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al nuevo documento.
1. Guardar cada PDF de salida [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void splitDocuments(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve("Page_" + pageNumber + ".pdf").toString());
            }
        }
    }
}
```

## Dividir un PDF en dos partes

Este ejemplo divide el documento fuente en dos archivos de salida secuenciales basados en el punto medio.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Calcule el punto medio del disponible [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) colección.
1. Copie la primera mitad de las páginas en un documento de salida y las páginas restantes en otro.
1. Guarda ambos documentos de resultado.

```java
public static void splitDocumentsIntoTwoParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int midPoint = totalPages / 2;

        try (Document firstDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= midPoint; pageNumber++) {
                firstDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            firstDocument.save(outputDir.resolve("Part_1.pdf").toString());
        }

        try (Document secondDocument = new Document()) {
            for (int pageNumber = midPoint + 1; pageNumber <= totalPages; pageNumber++) {
                secondDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            secondDocument.save(outputDir.resolve("Part_2.pdf").toString());
        }
    }
}
```

## Dividir un PDF en grupos de páginas de tamaño fijo

Utilice este patrón cuando cada archivo de salida deba contener el mismo número de páginas, excepto posiblemente la última parte.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Recorrer el [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) colección en grupos de `pagesPerPart`.
1. Cree un nuevo documento de salida para cada grupo y copie el rango de páginas calculado en él.
1. Guarde cada parte con un nombre de archivo generado.

```java
public static void splitDocumentsEveryNPages(Path inputFile, Path outputDir, int pagesPerPart) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        int partIndex = 1;

        for (int startPage = 1; startPage <= totalPages; startPage += pagesPerPart) {
            int endPage = Math.min(startPage + pagesPerPart - 1, totalPages);
            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Every_" + pagesPerPart + "_Part_" + partIndex + ".pdf").toString());
            }
            partIndex++;
        }
    }
}
```

## Dividir un PDF por rangos de página personalizados

Este ejemplo le permite definir páginas de inicio y fin explícitas para cada documento de salida.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Defina lo requerido [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rangos en una matriz o en otra colección.
1. Valide cada rango respecto al recuento de páginas de origen y copie las páginas coincidentes en un nuevo documento.
1. Guarde cada archivo de salida basado en rangos.

```java
public static void splitDocumentsByPageRanges(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        Integer[][] ranges = {{1, 3}, {4, 6}, {7, null}};

        for (int index = 0; index < ranges.length; index++) {
            int startPage = ranges[index][0];
            Integer endPage = ranges[index][1];
            if (startPage > totalPages) {
                continue;
            }

            int effectiveEnd = endPage == null ? totalPages : Math.min(endPage, totalPages);
            if (startPage > effectiveEnd) {
                continue;
            }

            try (Document rangeDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= effectiveEnd; pageNumber++) {
                    rangeDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                rangeDocument.save(outputDir.resolve(
                        "Range_" + (index + 1) + "_" + startPage + "_to_" + effectiveEnd + ".pdf").toString());
            }
        }
    }
}
```

## Dividir la primera página y las páginas restantes

Utilice este enfoque cuando la página de portada deba exportarse por separado del resto del documento.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y confirme que contiene páginas.
1. Crear un documento de salida para el primero [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Cree otro documento para el rango de páginas restante cuando haya más de una página disponible.
1. Guarda ambos resultados.

```java
public static void splitDocumentsFirstPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document firstPageDocument = new Document()) {
            firstPageDocument.getPages().add(document.getPages().get_Item(1));
            firstPageDocument.save(outputDir.resolve("First_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        try (Document remainingPagesDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber++) {
                remainingPagesDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            remainingPagesDocument.save(outputDir.resolve("Remaining_Pages.pdf").toString());
        }
    }
}
```

## Dividir la última página y las páginas anteriores

Este ejemplo separa la página final del resto del documento, lo que es útil para extraer páginas de resumen o de firma.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y verifica que no esté vacío.
1. Copiar el último [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en un nuevo documento de salida.
1. Elimina esa página del documento original cuando aún queden páginas anteriores.
1. Guarda la última página y las páginas restantes como archivos separados.

```java
public static void splitDocumentsLastPageAndRest(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        try (Document lastPageDocument = new Document()) {
            lastPageDocument.getPages().add(document.getPages().get_Item(totalPages));
            lastPageDocument.save(outputDir.resolve("Last_Page.pdf").toString());
        }

        if (totalPages == 1) {
            return;
        }

        document.getPages().delete(totalPages);
        document.save(outputDir.resolve("Previous_Pages.pdf").toString());
    }
}
```

## Dividir un PDF en tres partes

Utilice este patrón cuando el documento debe dividirse en tres secciones consecutivas de tamaño aproximadamente igual.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y determinar el número total de páginas.
1. Calcule el tamaño aproximado de cada parte de salida.
1. Cree hasta tres documentos y copie lo que coincida [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) rangos.
1. Guarda cada parte generada.

```java
public static void splitDocumentsIntoThreeParts(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        if (totalPages == 0) {
            return;
        }

        int partSize = Math.max(1, (totalPages + 2) / 3);
        for (int partIndex = 0; partIndex < 3; partIndex++) {
            int startPage = partIndex * partSize + 1;
            int endPage = Math.min((partIndex + 1) * partSize, totalPages);
            if (startPage > totalPages) {
                break;
            }

            try (Document partDocument = new Document()) {
                for (int pageNumber = startPage; pageNumber <= endPage; pageNumber++) {
                    partDocument.getPages().add(document.getPages().get_Item(pageNumber));
                }
                partDocument.save(outputDir.resolve("Three_Parts_" + (partIndex + 1) + ".pdf").toString());
            }
        }
    }
}
```

## Dividir un PDF en grupos de páginas personalizados

Este ejemplo muestra cómo crear archivos de salida a partir de conjuntos de páginas no secuenciales en lugar de rangos continuos.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Definir grupos personalizados de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) números.
1. Cree un nuevo documento de salida para cada grupo y añada solo las páginas válidas de ese grupo.
1. Guarde cada documento de grupo que no esté vacío.

```java
public static void splitDocumentsCustomPageGroups(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();
        List<List<Integer>> groups = List.of(
                List.of(1, 2, 5),
                List.of(3, 4, 6, 7));

        int groupIndex = 1;
        for (List<Integer> group : groups) {
            try (Document groupDocument = new Document()) {
                for (Integer pageNumber : group) {
                    if (pageNumber >= 1 && pageNumber <= totalPages) {
                        groupDocument.getPages().add(document.getPages().get_Item(pageNumber));
                    }
                }
                if (groupDocument.getPages().size() > 0) {
                    groupDocument.save(outputDir.resolve("Custom_Group_" + groupIndex + ".pdf").toString());
                }
            }
            groupIndex++;
        }
    }
}
```

## Dividir un PDF en páginas individuales con nombres de archivo estables

Utiliza esta versión cuando los nombres de salida deben permanecer ordenables léxicamente, por ejemplo en canalizaciones automatizadas.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crea un documento de salida para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Guarde cada archivo con un número de página con ceros a la izquierda.

```java
public static void splitDocumentsWithStableFilenames(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            try (Document newDocument = new Document()) {
                newDocument.getPages().add(document.getPages().get_Item(pageNumber));
                newDocument.save(outputDir.resolve(String.format("Page_%03d.pdf", pageNumber)).toString());
            }
        }
    }
}
```

## Dividir un PDF en páginas impares y pares

Este ejemplo crea dos salidas separando las páginas según la paridad de su número de página.

1. Abrir el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crea un documento de salida para impares [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) números y otro para los números de página pares.
1. Iterar a través de las páginas de origen con el incremento requerido para cada documento de salida.
1. Guarde los resultados de página impar y página par por separado.

```java
public static void splitDocumentsOddEvenPages(Path inputFile, Path outputDir) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        try (Document oddDocument = new Document()) {
            for (int pageNumber = 1; pageNumber <= totalPages; pageNumber += 2) {
                oddDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            oddDocument.save(outputDir.resolve("Odd_Pages.pdf").toString());
        }

        try (Document evenDocument = new Document()) {
            for (int pageNumber = 2; pageNumber <= totalPages; pageNumber += 2) {
                evenDocument.getPages().add(document.getPages().get_Item(pageNumber));
            }
            evenDocument.save(outputDir.resolve("Even_Pages.pdf").toString());
        }
    }
}
```

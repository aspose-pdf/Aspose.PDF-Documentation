---
title: Dividir archivos PDF en Java
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /java/split-pdf-document/
description: Aprenda a dividir páginas PDF en archivos PDF separados en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Divida documentos PDF por páginas, rangos, grupos y patrones de nombres de archivos usando Java
Abstract: Este artículo explica cómo dividir documentos PDF usando Aspose.PDF para Java. Cubre la división en páginas individuales, dos o tres partes, páginas pares e impares, fragmentos de tamaño fijo, rangos personalizados, primera o última página más el resto, grupos de páginas personalizados y generación estable de nombres de archivos.
---
Aspose.PDF para Java admite varios patrones de división más allá de la salida de una página por archivo.


## 
Dividir un PDF en archivos de una sola página



Utilice este enfoque cuando cada página de origen deba convertirse en un documento de salida independiente.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) que desee exportar.
1. Agregue la [Página] seleccionada(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al nuevo documento.

1. 
Guarde cada [Documento] PDF de salida(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


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

## 
Dividir un PDF en dos partes



Este ejemplo divide el documento fuente en dos archivos de salida secuenciales según el punto medio.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Calcule el punto medio de la colección [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) disponible.

1. 
Copie la primera mitad de las páginas en un documento de salida y las páginas restantes en otro.

1. 
Guarde ambos documentos de resultados.


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

## 
Dividir un PDF en grupos de páginas de tamaño fijo



Utilice este patrón cuando cada archivo de salida deba contener el mismo número de páginas, excepto posiblemente la última parte.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Recorra la colección [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en grupos de `pagesPerPart`.

1. 
Cree un nuevo documento de salida para cada grupo y copie en él el rango de páginas calculado.

1. 
Guarde cada parte con un nombre de archivo generado.


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

## 
Dividir un PDF por rangos de páginas personalizados

Este ejemplo le permite definir páginas de inicio y finalización explícitas para cada documento de salida.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Defina los rangos de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requeridos en una matriz u otra colección.

1. 
Valide cada rango con el recuento de páginas de origen y copie las páginas coincidentes en un documento nuevo.

1. 
Guarde cada archivo de salida basado en rango.

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

## Dividir la primera página y las páginas restantes.



Utilice este enfoque cuando la portada deba exportarse por separado del resto del documento.


1. 
Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y confirme que contiene páginas.

1. 
Cree un documento de salida para la primera [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Cree otro documento para el rango de páginas restante cuando haya más de una página disponible.
1. Guarde ambos resultados.


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

## 
Dividir la última página y las páginas anteriores.



Este ejemplo separa la página final del resto del documento, lo que resulta útil para extraer páginas de resumen o firmas.


1. 
Abra el [Documento] PDF de origen(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y compruebe que no esté vacío.

1. 
Copie la última [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) en un nuevo documento de salida.
1. Elimine esa página del documento original cuando aún queden páginas anteriores.

1. 
Guarde la última página y las páginas restantes como archivos separados.


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

## 
Dividir un PDF en tres partes



Utilice este patrón cuando el documento deba dividirse en tres secciones consecutivas de aproximadamente el mismo tamaño.


1. 
Abra el [Documento] PDF de origen (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y determine el número total de páginas.
1. Calcule el tamaño aproximado de cada parte de salida.

1. 
Cree hasta tres documentos y copie los rangos de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) coincidentes.

1. 
Guarde cada parte generada.


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

## 
Dividir un PDF en grupos de páginas personalizados



Este ejemplo muestra cómo crear archivos de salida a partir de conjuntos de páginas no secuenciales en lugar de rangos continuos.

1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Defina grupos personalizados de números de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Cree un nuevo documento de salida para cada grupo y agregue solo las páginas válidas de ese grupo.

1. 
Guarde cada documento de grupo que no esté vacío.


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

## 
Divida un PDF en páginas individuales con nombres de archivo estables

Utilice esta versión cuando los nombres de salida deban permanecer léxicamente ordenables, por ejemplo, en canalizaciones automatizadas.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un documento de salida para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Guarde cada archivo con un número de página rellenado con ceros.


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

## 
Dividir un PDF en páginas pares e impares

Este ejemplo crea dos salidas separando las páginas según su paridad de número de página.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un documento de salida para números de [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) impares y otro para números de páginas pares.

1. 
Itere a través de las páginas de origen con el incremento requerido para cada documento de salida.

1. 
Guarde los resultados de las páginas pares y impares por separado.

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

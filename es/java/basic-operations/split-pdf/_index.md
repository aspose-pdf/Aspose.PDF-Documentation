---
title: Dividir archivos PDF en Java
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /es/java/split-pdf/
description: Aprenda cómo dividir un PDF en archivos PDF de una sola página en Java usando Aspose.PDF.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividir páginas PDF usando Java
Abstract: Este artículo muestra cómo dividir un documento PDF en archivos PDF de una sola página en Java usando Aspose.PDF. El ejemplo abre el documento original, recorre sus páginas, crea un nuevo documento para cada página y guarda cada página como un archivo PDF individual.
---
Dividir un PDF en archivos separados es útil cuando necesita exportar cada página para revisión, almacenamiento o procesamiento posterior.

## Ejemplo en vivo

[Divisor de Aspose.PDF](https://products.aspose.app/pdf/splitter) es una aplicación en línea gratuita para probar la división de PDF en un navegador.

[![Dividir PDF de Aspose](splitter.png)](https://products.aspose.app/pdf/splitter)

Este ejemplo usa el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) clase para abrir un archivo PDF e iterar a través de sus páginas. Para cada [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), crea un nuevo documento, agrega la página a él, y guarda el resultado como un archivo PDF separado.

Para dividir un PDF en archivos de página individuales en Java:

1. Abra el PDF fuente con el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Iterar a través del [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos devueltos por `document.getPages()`.
1. Crear un nuevo vacío [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) para cada página.
1. Agregar el actual [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) al nuevo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Guarda el nuevo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con un nombre de archivo único.
1. Cierra ambos [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) objetos cuando el procesamiento esté completo.

## Dividir PDF en archivos de una sola página

El siguiente ejemplo de Java se basa en `SplitDocumentExamples.java` y guarda páginas como `Page_1.pdf`, `Page_2.pdf`, y así sucesivamente.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```

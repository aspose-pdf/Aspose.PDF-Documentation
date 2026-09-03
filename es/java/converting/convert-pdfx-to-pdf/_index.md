---
title: Convertir PDF/A y PDF/UA a PDF en Java
linktitle: Convertir PDF/A y PDF/UA a PDF
type: docs
weight: 120
url: /es/java/convert-pdf_x-to-pdf/
lastmod: "2026-09-03"
description: Aprenda cómo eliminar la conformidad PDF/A y PDF/UA de archivos PDF basados en estándares en Java y guardarlos como documentos PDF estándar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF/A y PDF/UA a PDF estándar en Java
Abstract: Este artículo explica cómo eliminar la conformidad PDF/A y PDF/UA de documentos PDF basados en estándares usando Aspose.PDF for Java, y luego guardar el resultado como un archivo PDF estándar.
---
Aspose.PDF for Java puede convertir variantes PDF que cumplen con los estándares de vuelta a un documento PDF normal.

## Convertir PDF/A a PDF estándar

Utilice este ejemplo cuando un documento PDF/A de archivo deba degradarse a un PDF estándar.

1. Abra el archivo PDF/A fuente en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Llamada `removePdfaCompliance()` desvincular el perfil de cumplimiento archivístico del documento cargado.
1. Guarde el archivo PDF estándar resultante sin establecer la restricción PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Convertir PDF/UA a PDF estándar

Utilice este ejemplo cuando un documento PDF/UA accesible deba convertirse de nuevo a un PDF estándar.

1. Abra el archivo PDF/UA de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Llamada `removePdfUaCompliance()` para eliminar el perfil de cumplimiento de accesibilidad de los metadatos y los requisitos de estructura del documento.
1. Guarde el documento PDF resultante como un archivo PDF normal.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```

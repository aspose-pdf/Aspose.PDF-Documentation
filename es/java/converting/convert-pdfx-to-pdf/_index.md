---
title: Convierta PDF/A y PDF/UA a PDF en Java
linktitle: Convertir PDF/A y PDF/UA a PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Aprenda a eliminar la compatibilidad con PDF/A y PDF/UA de archivos PDF basados en estándares en Java y guardarlos como documentos PDF estándar.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF/A y PDF/UA a PDF estándar en Java
Abstract: Este artículo explica cómo eliminar la compatibilidad con PDF/A y PDF/UA de documentos PDF basados en estándares utilizando Aspose.PDF para Java y luego guardar el resultado como un archivo PDF estándar.
---
Aspose.PDF para Java puede convertir variantes de PDF que cumplen con los estándares en un documento PDF normal.


## 
Convertir PDF/A a PDF estándar



Utilice este ejemplo cuando un documento PDF/A de archivo deba degradarse a un PDF estándar.


1. 
Abra el archivo PDF/A de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Llame a `removePdfaCompliance()` para separar el perfil de cumplimiento de archivos del documento cargado.
1. Guarde el archivo PDF estándar resultante sin el conjunto de restricciones PDF/A.


```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## 
Convertir PDF/UA a PDF estándar



Utilice este ejemplo cuando un documento PDF/UA accesible deba volver a convertirse a un PDF estándar.


1. 
Abra el archivo PDF/UA de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Llame a `removePdfUaCompliance()` para eliminar el perfil de cumplimiento de accesibilidad de los metadatos del documento y los requisitos de estructura.
1. Guarde el documento PDF resultante como un archivo PDF normal.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```

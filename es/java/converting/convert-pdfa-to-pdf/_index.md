---
title: Convertir PDF/A a formato PDF 
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /es/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con la biblioteca Java. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir documento PDF/A a PDF

Convertir un documento PDF/A a PDF significa eliminar la restricción <abbr title="Portable Document Format Archive">PDF/A</abbr> del documento original. La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tiene el método RemovePdfaCompliance(..) para eliminar
la información de cumplimiento PDF del archivo de entrada/origen.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Crear objeto Document
    Document document = new Document(pdfaDocumentFileName);

    // Eliminar información de cumplimiento PDF/A
    document.removePdfaCompliance();

    // Guardar salida en formato XML
    document.save(documentFileName);
    document.close();
}
```


Esta información también se elimina si realizas cambios en el documento (por ejemplo, añadir páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad con PDF/A después de añadir la página.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Crear objeto Document
    Document document = new Document(pdfaDocumentFileName);

    // Añadir una nueva página (vacía) elimina la información de conformidad con PDF/A.
    document.getPages().add();

    // Guardar documento actualizado
    document.save(documentFileName);
    document.close();
}
```
---
title: Convertir PDF/A a PDF
linktitle: Convertir PDF/A a PDF
type: docs
weight: 350
url: /es/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-06-30"
description: Para convertir PDF/A a PDF deberías eliminar las restricciones del documento original. Aspose.PDF for Android via Java te permite resolver este problema de manera fácil y sencilla.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convertir un documento PDF/A a PDF significa eliminar \u003Cabbr title=\u0022Portable Document Format Archive
>PDF/A</abbr> restricción del documento original. Clase [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tiene el método RemovePdfaCompliance(..) para eliminar
la información de cumplimiento PDF del archivo de entrada/origen.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

Esta información también se elimina si haces cualquier cambio en el documento (p. ej., agregas páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad PDF/A después de añadir la página.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```





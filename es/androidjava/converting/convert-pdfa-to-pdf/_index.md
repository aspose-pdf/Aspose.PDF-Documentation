---
title: Convertir PDF/A a PDF 
linktitle: Convertir PDF/A a PDF
type: docs
weight: 350
url: es/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: Para convertir PDF/A a PDF, debe eliminar las restricciones del documento original. Aspose.PDF para Android a través de Java le permite resolver este problema de manera fácil y simple.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convertir un documento PDF/A a PDF significa eliminar la restricción de <abbr title="Portable Document Format Archive
">PDF/A</abbr> del documento original. La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tiene el método RemovePdfaCompliance(..) para eliminar
la información de cumplimiento PDF del archivo de entrada/origen.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Crear objeto Document
            document = new Document(pdfaDocumentFileName);

            // Eliminar información de cumplimiento PDF/A
            document.removePdfaCompliance();

            // Guardar salida en formato XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


Esta información también se elimina si realizas cambios en el documento (por ejemplo, agregar páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad con PDF/A después de agregar la página.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Crear objeto Document
        document = new Document(pdfaDocumentFileName);

        // Agregar una nueva página (vacía) elimina la información de conformidad con PDF/A.
        document.getPages().add();

        // Guardar documento actualizado
        document.save(pdfDocumentFileName);
    }
```
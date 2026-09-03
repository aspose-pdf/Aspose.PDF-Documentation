---
title: Crear PDF compatible con PDF/3-A y adjuntar factura ZUGFeRD en Java
linktitle: Adjunte ZUGFeRD a PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Aprenda cómo adjuntar XML de factura ZUGFeRD a un PDF y convertirlo a PDF/A-3A en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adjunte XML de factura ZUGFeRD a un documento PDF con Java
Abstract: Este artículo explica cómo crear un documento de factura compatible con PDF/A-3A utilizando Aspose.PDF para Java. Cubre cómo adjuntar el XML de la factura como un archivo incrustado, configurar el tipo MIME y la relación del archivo asociado, convertir el PDF a PDF/A-3A y guardar el documento final listo para ZUGFeRD.
---
Utilice las API `Document` y `FileSpecification` cuando necesite empaquetar XML de facturas dentro de un PDF para flujos de trabajo estilo ZUGFeRD.


## 
Adjunte XML de factura ZUGFeRD a un PDF


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree la [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para el archivo de factura XML.

1. Configure los metadatos del archivo incrustado, incluido el tipo MIME y [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Agregue [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) a la colección de archivos incrustados del documento.

1. Convierta el documento a [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.

1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```

---
title: Crear un PDF conforme a PDF/A-3A y adjuntar una factura ZUGFeRD en Java
linktitle: Adjuntar ZUGFeRD a PDF
type: docs
weight: 10
url: /es/java/attach-zugferd/
description: Aprenda cómo adjuntar el XML de la factura ZUGFeRD a un PDF y convertirlo a PDF/A-3A en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adjunte el XML de la factura ZUGFeRD a un documento PDF con Java
Abstract: Este artículo explica cómo crear un documento de factura compatible con PDF/A-3A utilizando Aspose.PDF for Java. Cubre la incorporación del XML de la factura como un archivo incrustado, la configuración del tipo MIME y la relación de archivo asociado, la conversión del PDF a PDF/A-3A y el guardado del documento final listo para ZUGFeRD.
---
Usa el `Document` y `FileSpecification` APIs cuando necesitas empaquetar XML de factura dentro de un PDF para flujos de trabajo estilo ZUGFeRD.

## Adjuntar XML de factura ZUGFeRD a un PDF

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear el [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para el archivo XML de la factura.
1. Establecer los metadatos del archivo incrustado, incluido el tipo MIME y [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Agregar el [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) a la colección de archivos incrustados del documento.
1. Convertir el documento a [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Guarda el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

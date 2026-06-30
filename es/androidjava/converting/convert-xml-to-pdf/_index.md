---
title: Convertir XML a PDF
linktitle: Convertir XML a PDF
type: docs
weight: 320
url: /es/androidjava/convert-xml-to-pdf/
lastmod: "2026-06-30"
description: La biblioteca Aspose.PDF presenta varias formas de convertir XML a PDF. Puedes usar XslFoLoadOptions o hacerlo con una estructura de archivo incorrecta.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

El formato XML se utiliza para almacenar datos estructurados. Hay varias formas de convertir <abbr title="Extensible Markup Language">XML</abbr> a PDF en Aspose.PDF.

Considere la opción de usar un documento XML basado en el estándar XSL-FO.

## Convertir XSL-FO a PDF

La conversión de archivos XSL-FO a PDF puede implementarse usando [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) objeto con [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  pero a veces puedes encontrarte con una estructura de archivo incorrecta. 

```java
// Convert XML to PDF
    public void convertXMLtoPDF() {
        // Initialize document object
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Save resultant PDF file
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```
    

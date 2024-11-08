---
title: Convertir XML a PDF 
linktitle: Convertir XML a PDF
type: docs
weight: 320
url: /es/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: La biblioteca Aspose.PDF presenta varias maneras de convertir XML a PDF. Puedes usar las XslFoLoadOptions o hacerlo con una estructura de archivo incorrecta.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Prueba en línea. Puedes verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

El formato XML se utiliza para almacenar datos estructurados. Hay varias maneras de convertir <abbr title="Extensible Markup Language">XML</abbr> a PDF en Aspose.PDF.

Considera la opción de usar un documento XML basado en el estándar XSL-FO.

## Convertir XSL-FO a PDF

La conversión de archivos XSL-FO a PDF se puede implementar usando el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) con [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions), pero a veces puedes encontrar una estructura de archivo incorrecta.
 
// Convertir XML a PDF
    public void convertXMLtoPDF() {
        // Inicializar objeto documento
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Guardar archivo PDF resultante
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```
---
title: Convertir XML en PDF
linktitle: Convertir XML en PDF
type: docs
weight: 320
url: /fr/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: La bibliothèque Aspose.PDF propose plusieurs manières de convertir XML en PDF. Vous pouvez utiliser XslFoLoadOptions ou le faire avec une structure de fichier incorrecte.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Le format XML utilisé pour stocker des données structurées. Il existe plusieurs façons de convertir <abbr title="Extensible Markup Language">XML</abbr> vers PDF dans Aspose.PDF.

Envisagez l'option d'utiliser un document XML basé sur la norme XSL-FO.

## Convertir XSL-FO en PDF

La conversion des fichiers XSL-FO en PDF peut être implémentée à l'aide de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) objet avec [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  mais parfois vous pouvez rencontrer une structure de fichier incorrecte. 

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
    

---
title: Convertir XML en PDF 
linktitle: Convertir XML en PDF
type: docs
weight: 320
url: /fr/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: La bibliothèque Aspose.PDF présente plusieurs façons de convertir XML en PDF. Vous pouvez utiliser les XslFoLoadOptions ou le faire avec une structure de fichier incorrecte.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Le format XML est utilisé pour stocker des données structurées. Il existe plusieurs façons de convertir <abbr title="Extensible Markup Language">XML</abbr> en PDF dans Aspose.PDF.

Considérez l'option d'utilisation d'un document XML basé sur la norme XSL-FO.

## Convertir XSL-FO en PDF

La conversion de fichiers XSL-FO en PDF peut être mise en œuvre en utilisant l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) avec [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions), mais parfois vous pouvez rencontrer une structure de fichier incorrecte.
 
// Convertir XML en PDF
    public void convertXMLtoPDF() {
        // Initialiser l'objet document
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Enregistrer le fichier PDF résultant
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```
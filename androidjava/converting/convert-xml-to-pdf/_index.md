---
title: Convert XML to PDF 
linktitle: Convert XML to PDF
type: docs
weight: 320
url: /androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF library presents several ways to convert XML to PDF. You can use the XslFoLoadOptions or do this with an incorrect file structure.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

The XML format used to store structured data. There are several ways to convert <abbr title="Extensible Markup Language">XML</abbr> to PDF in Aspose.PDF.

Consider option using XML document based on XSL-FO standard.

## Convert XSL-FO to PDF

The conversion of XSL-FO files to PDF can be implemented using [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) object with [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  but sometimes you can meet with the incorrect file structure. 

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
    
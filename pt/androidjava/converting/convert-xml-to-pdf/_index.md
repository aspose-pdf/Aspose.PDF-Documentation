---
title: Converter XML para PDF
linktitle: Converter XML para PDF
type: docs
weight: 320
url: /pt/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: A biblioteca Aspose.PDF apresenta várias maneiras de converter XML para PDF. Você pode usar o XslFoLoadOptions ou fazer isso com uma estrutura de arquivo incorreta.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

O formato XML usado para armazenar dados estruturados. Existem várias maneiras de converter <abbr title="Extensible Markup Language">XML</abbr> para PDF no Aspose.PDF.

Considere a opção de usar documento XML baseado no padrão XSL-FO.

## Converter XSL-FO para PDF

A conversão de arquivos XSL-FO para PDF pode ser implementada usando [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) objeto com [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  mas às vezes você pode encontrar uma estrutura de arquivo incorreta. 

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
    

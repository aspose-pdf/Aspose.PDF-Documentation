---
title: Konversi XML ke PDF
linktitle: Konversi XML ke PDF
type: docs
weight: 320
url: /id/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: Pustaka Aspose.PDF menyediakan beberapa cara untuk mengonversi XML ke PDF. Anda dapat menggunakan XslFoLoadOptions atau melakukan ini dengan struktur file yang tidak benar.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Format XML yang digunakan untuk menyimpan data terstruktur. Ada beberapa cara untuk mengonversi <abbr title="Extensible Markup Language">XML</abbr> ke PDF di Aspose.PDF.

Pertimbangkan opsi menggunakan dokumen XML berdasarkan standar XSL-FO.

## Konversi XSL-FO ke PDF

Konversi file XSL-FO ke PDF dapat diimplementasikan menggunakan [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) objek dengan [XslFoLoadOptions,](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  tetapi kadang-kadang Anda dapat menemui struktur file yang tidak tepat. 

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
    

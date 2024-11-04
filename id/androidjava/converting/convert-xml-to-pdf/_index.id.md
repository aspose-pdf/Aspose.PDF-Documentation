---
title: Mengonversi XML ke PDF 
linktitle: Mengonversi XML ke PDF
type: docs
weight: 320
url: /androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Pustaka Aspose.PDF menyajikan beberapa cara untuk mengonversi XML ke PDF. Anda dapat menggunakan XslFoLoadOptions atau melakukannya dengan struktur file yang tidak benar.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

Format XML digunakan untuk menyimpan data terstruktur. Ada beberapa cara untuk mengonversi <abbr title="Extensible Markup Language">XML</abbr> ke PDF dalam Aspose.PDF.

Pertimbangkan opsi menggunakan dokumen XML berdasarkan standar XSL-FO.

## Mengonversi XSL-FO ke PDF

Konversi file XSL-FO ke PDF dapat diimplementasikan menggunakan objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) dengan [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions), tetapi terkadang Anda dapat menghadapi struktur file yang tidak benar.
 
// Mengubah XML ke PDF
    public void convertXMLtoPDF() {
        // Inisialisasi objek dokumen
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Simpan file PDF hasil
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
```
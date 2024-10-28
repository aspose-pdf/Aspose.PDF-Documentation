---
title: Buat Dokumen Hello World PDF melalui XML dan XSLT
linktitle: Buat Dokumen Hello World PDF melalui XML dan XSLT
type: docs
weight: 10
url: /java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF untuk Java memberikan kesempatan untuk mengkonversi file XML menjadi dokumen PDF dengan syarat file XML input harus mengikuti Skema XSD Aspose.PDF Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Kadang-kadang Anda mungkin memiliki file XML yang sudah ada yang berisi data aplikasi dan Anda ingin menghasilkan laporan PDF menggunakan file ini. Anda dapat menggunakan XSLT untuk mengubah dokumen XML Anda yang ada menjadi dokumen XML yang kompatibel dengan Aspose.Pdf dan kemudian menghasilkan file PDF. Ada 3 langkah untuk menghasilkan PDF menggunakan XML dan XSLT.

Silakan ikuti langkah-langkah ini untuk mengkonversi file XML menjadi dokumen PDF menggunakan XSLT:

* Buat instance dari kelas PDF yang mewakili dokumen PDF

* Jika Anda telah membeli lisensi maka Anda juga harus menyematkan kode untuk menggunakan lisensi tersebut dengan bantuan kelas License dalam namespace Aspose.Pdf
* Ikat file input XML dan XSLT ke instance kelas PDF dengan memanggil metode BindXML-nya
* Simpan XML yang terikat dengan instance PDF sebagai dokumen PDF

## File Input XML

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## File Input XSLT

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```


## Membuat Hello World menggunakan XML dan Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```
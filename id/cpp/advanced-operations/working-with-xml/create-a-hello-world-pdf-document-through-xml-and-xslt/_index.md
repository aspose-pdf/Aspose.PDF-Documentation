---
title: Membuat PDF dari XML menggunakan XSLT 
linktitle: Membuat PDF dari XML menggunakan XSLT
type: docs
weight: 10
url: /id/cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Perpustakaan C++ menyediakan kemampuan untuk mengonversi file XML menjadi dokumen PDF dengan syarat file XML input harus mengikuti Skema Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Terkadang Anda mungkin memiliki file XML yang sudah ada yang berisi data aplikasi dan Anda ingin menghasilkan laporan PDF menggunakan file-file ini. Anda dapat menggunakan XSLT untuk mengubah dokumen XML Anda yang ada ke dokumen XML yang kompatibel dengan Aspose.Pdf dan kemudian menghasilkan file PDF. Ada 3 langkah untuk menghasilkan PDF menggunakan XML dan XSLT.

Silakan ikuti langkah-langkah ini untuk mengonversi file XML menjadi dokumen PDF menggunakan XSLT:

* Buat instance dari kelas PDF yang mewakili dokumen PDF
* Jika Anda telah membeli lisensi maka Anda juga harus menyematkan kode untuk menggunakan lisensi tersebut dengan bantuan kelas License di namespace Aspose.Pdf

* Hubungkan file XML dan XSLT input ke instance dari kelas PDF dengan memanggil metode BindXML-nya
* Simpan XML terikat dengan instance PDF sebagai dokumen PDF

## File XML Masukan

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## File XSLT Masukan

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
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

```cpp
using namespace System;
using namespace Aspose::Pdf;

static System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString);

void WorkingWithXML::CreatingPDFfromXMLusingXSLT()
{
 String _dataDir("C:\\Samples\\");
 //Buat dokumen pdf
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Mengikat file XML dan XSLT ke dokumen
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Simpan dokumen
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```
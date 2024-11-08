---
title: Menghasilkan PDF dari XML
linktitle: Menghasilkan PDF dari XML
type: docs
weight: 10
url: /id/java/generate-pdf-from-xml
description: Aspose.PDF untuk Java menyediakan kesempatan untuk mengonversi file XML menjadi dokumen PDF dengan syarat bahwa file XML input harus mengikuti Skema Aspose.PDF untuk Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Menghasilkan dokumen PDF dari dokumen XML bukanlah tugas yang mudah karena dokumen XML dapat menggambarkan konten yang berbeda. Aspose.PDF untuk Java memiliki beberapa cara untuk menghasilkan PDF berdasarkan dokumen XML:

- menggunakan transformasi XSLT
- menggunakan markup XSL-FO (XSL Formatting Objects)
- menggunakan Skema XML Aspose.PDF sendiri

## Menghasilkan dokumen PDF menggunakan transformasi XSLT

XSL (eXtensible Stylesheet Language) adalah bahasa styling untuk mentransformasi dokumen XML menjadi dokumen XML lain atau HTML. Dalam kasus kami, kami dapat menggunakan transformasi XML ke HTML dan kemudian membuat PDF berdasarkan data HTML.

Misalkan kita memiliki file XML dengan katalog CD sederhana (lihat di bawah).

```xml
<?xml version="1.0" encoding="utf-8" ?>
<catalog>
  <cd>
    <title>Empire Burlesque</title>
    <artist>Bob Dylan</artist>
    <country>USA</country>
    <company>Columbia</company>
    <price>10.90</price>
    <year>1985</year>
  </cd>
  <cd>
    <title>Hide your heart</title>
    <artist>Bonnie Tyler</artist>
    <country>UK</country>
    <company>CBS Records</company>
    <price>9.90</price>
    <year>1988</year>
  </cd>
  <cd>
    <title>Greatest Hits</title>
    <artist>Dolly Parton</artist>
    <country>USA</country>
    <company>RCA</company>
    <price>9.90</price>
    <year>1982</year>
  </cd>
  <cd>
    <title>Still got the blues</title>
    <artist>Gary Moore</artist>
    <country>UK</country>
    <company>Virgin records</company>
    <price>10.20</price>
    <year>1990</year>
  </cd>
  <cd>
    <title>Eros</title>
    <artist>Eros Ramazzotti</artist>
    <country>EU</country>
    <company>BMG</company>
    <price>9.90</price>
    <year>1997</year>
  </cd>
  <cd>
    <title>One night only</title>
    <artist>Bee Gees</artist>
    <country>UK</country>
    <company>Polydor</company>
    <price>10.90</price>
    <year>1998</year>
  </cd>
  <cd>
    <title>Sylvias Mother</title>
    <artist>Dr.Hook</artist>
    <country>UK</country>
    <company>CBS</company>
    <price>8.10</price>
    <year>1973</year>
  </cd>
  <cd>
    <title>Maggie May</title>
    <artist>Rod Stewart</artist>
    <country>UK</country>
    <company>Pickwick</company>
    <price>8.50</price>
    <year>1990</year>
  </cd>
  <cd>
    <title>Romanza</title>
    <artist>Andrea Bocelli</artist>
    <country>EU</country>
    <company>Polydor</company>
    <price>10.80</price>
    <year>1996</year>
  </cd>
  <cd>
    <title>When a man loves a woman</title>
    <artist>Percy Sledge</artist>
    <country>USA</country>
    <company>Atlantic</company>
    <price>8.70</price>
    <year>1987</year>
  </cd>
  <cd>
    <title>Black angel</title>
    <artist>Savage Rose</artist>
    <country>EU</country>
    <company>Mega</company>
    <price>10.90</price>
    <year>1995</year>
  </cd>
  <cd>
    <title>1999 Grammy Nominees</title>
    <artist>Many</artist>
    <country>USA</country>
    <company>Grammy</company>
    <price>10.20</price>
    <year>1999</year>
  </cd>
  <cd>
    <title>For the good times</title>
    <artist>Kenny Rogers</artist>
    <country>UK</country>
    <company>Mucik Master</company>
    <price>8.70</price>
    <year>1995</year>
  </cd>
  <cd>
    <title>Big Willie style</title>
    <artist>Will Smith</artist>
    <country>USA</country>
    <company>Columbia</company>
    <price>9.90</price>
    <year>1997</year>
  </cd>
  <cd>
    <title>Tupelo Honey</title>
    <artist>Van Morrison</artist>
    <country>UK</country>
    <company>Polydor</company>
    <price>8.20</price>
    <year>1971</year>
  </cd>
  <cd>
    <title>Soulsville</title>
    <artist>Jorn Hoel</artist>
    <country>Norway</country>
    <company>WEA</company>
    <price>7.90</price>
    <year>1996</year>
  </cd>
  <cd>
    <title>The very best of</title>
    <artist>Cat Stevens</artist>
    <country>UK</country>
    <company>Island</company>
    <price>8.90</price>
    <year>1990</year>
  </cd>
  <cd>
    <title>Stop</title>
    <artist>Sam Brown</artist>
    <country>UK</country>
    <company>A and M</company>
    <price>8.90</price>
    <year>1988</year>
  </cd>
  <cd>
    <title>Bridge of Spies</title>
    <artist>T`Pau</artist>
    <country>UK</country>
    <company>Siren</company>
    <price>7.90</price>
    <year>1987</year>
  </cd>
  <cd>
    <title>Private Dancer</title>
    <artist>Tina Turner</artist>
    <country>UK</country>
    <company>Capitol</company>
    <price>8.90</price>
    <year>1983</year>
  </cd>
  <cd>
    <title>Midt om natten</title>
    <artist>Kim Larsen</artist>
    <country>EU</country>
    <company>Medley</company>
    <price>7.80</price>
    <year>1983</year>
  </cd>
  <cd>
    <title>Pavarotti Gala Concert</title>
    <artist>Luciano Pavarotti</artist>
    <country>UK</country>
    <company>DECCA</company>
    <price>9.90</price>
    <year>1991</year>
  </cd>
  <cd>
    <title>The dock of the bay</title>
    <artist>Otis Redding</artist>
    <country>USA</country>
    <company>Stax Records</company>
    <price>7.90</price>
    <year>1968</year>
  </cd>
  <cd>
    <title>Picture book</title>
    <artist>Simply Red</artist>
    <country>EU</country>
    <company>Elektra</company>
    <price>7.20</price>
    <year>1985</year>
  </cd>
  <cd>
    <title>Red</title>
    <artist>The Communards</artist>
    <country>UK</country>
    <company>London</company>
    <price>7.80</price>
    <year>1987</year>
  </cd>
  <cd>
    <title>Unchain my heart</title>
    <artist>Joe Cocker</artist>
    <country>USA</country>
    <company>EMI</company>
    <price>8.20</price>
    <year>1987</year>
  </cd>
</catalog>
```


Untuk mengubah file ini menjadi PDF, kita harus membuat XSL dengan tata letak HTML. Mari kita render data kita dalam tabel. File XSL yang akan membantu kita melakukan ini mungkin terlihat seperti ini:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Koleksi CD Saya</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">Judul</th>
            <th style="text-align:left">Artis</th>
          </tr>
          <xsl:for-each select="catalog/cd">
            <tr>
              <td>
                <xsl:value-of select="title"/>
              </td>
              <td>
                <xsl:value-of select="artist"/>
              </td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

Jadi, kita perlu mengubah XML dan memuatnya ke dalam dokumen PDF.
 Contoh berikut menunjukkan cara ini:

```java

package com.aspose.pdf.examples;

import javax.xml.transform.*;

import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;


public class WorkingWithXML {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
  public static void ExampleXSLTtoPDF() throws TransformerException {
        String xslFile = _dataDir + "XMLFile1.xml", xmlFile = _dataDir +  "XSLTFile1.xslt";  
        TransformerFactory factory = TransformerFactory.newInstance();
        Transformer transformer = 
            factory.newTransformer( new StreamSource( xslFile ) );
        StreamSource xmlsource = new StreamSource( xmlFile );
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        StreamResult output = new StreamResult( baos );
        transformer.transform( xmlsource, output );
        com.aspose.pdf.HtmlLoadOptions options = new com.aspose.pdf.HtmlLoadOptions();
        ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
        com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(bais, options);        
        pdfDocument.save(_dataDir + "data_xml.pdf");
  }
}
```

## Menghasilkan dokumen PDF menggunakan markup XSL-FO

XSL-FO adalah bahasa markup berbasis XML yang menggambarkan pemformatan data XML untuk output ke layar, kertas, atau media lainnya. Aspose.PDF memiliki kelas khusus yang memungkinkan penerapan markup XSL-FO dan mendapatkan dokumen PDF.

Mari kita ambil contoh. Berikut adalah file XML dengan data sampel karyawan.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<employees>
    <companyname>ABC Inc.</companyname>
    <employee>
        <id>101</id>
        <name>Andrew</name>
        <designation>Manager</designation>
    </employee>

    <employee>
        <id>102</id>
        <name>Eduard</name>
        <designation>Executive</designation>
    </employee>

    <employee>
        <id>103</id>
        <name>Peter</name>
        <designation>Executive</designation>
    </employee>
</employees>
```

Mari kita buat file lain - file markup XSL-FO untuk mengubah data karyawan menjadi tabel.

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fo="http://www.w3.org/1999/XSL/Format" exclude-result-prefixes="fo">
    <xsl:template match="employees">
        <fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
            <fo:layout-master-set>
                <fo:simple-page-master master-name="simpleA4" page-height="29.7cm" page-width="21cm" margin-top="2cm" margin-bottom="2cm" margin-left="2cm" margin-right="2cm">
                    <fo:region-body/>
                </fo:simple-page-master>
            </fo:layout-master-set>
            <fo:page-sequence master-reference="simpleA4">
                <fo:flow flow-name="xsl-region-body">
                    <fo:block font-size="16pt" font-weight="bold" space-after="5mm">
                        Nama Perusahaan: <xsl:value-of select="companyname"/>
                    </fo:block>
                    <fo:block font-size="10pt">
                        <fo:table table-layout="fixed" width="100%" border-collapse="separate">
                            <fo:table-column column-width="4cm"/>
                            <fo:table-column column-width="4cm"/>
                            <fo:table-column column-width="5cm"/>
                            <fo:table-body>
                                <xsl:apply-templates select="employee"/>
                            </fo:table-body>
                        </fo:table>
                    </fo:block>
                </fo:flow>
            </fo:page-sequence>
        </fo:root>
    </xsl:template>
    <xsl:template match="employee">
        <fo:table-row>
            <xsl:if test="designation = 'Manager'">
                <xsl:attribute name="font-weight">bold</xsl:attribute>
            </xsl:if>
            <fo:table-cell>
                <fo:block>
                    <xsl:value-of select="id"/>
                </fo:block>
            </fo:table-cell>

            <fo:table-cell>
                <fo:block>
                    <xsl:value-of select="name"/>
                </fo:block>
            </fo:table-cell>
            <fo:table-cell>
                <fo:block>
                    <xsl:value-of select="designation"/>
                </fo:block>
            </fo:table-cell>
        </fo:table-row>
    </xsl:template>
</xsl:stylesheet>
```


Aspose.PDF memiliki kelas khusus [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XslFoLoadOptions) yang memungkinkan untuk menerapkan transformasi XSL-FO. Cuplikan berikut menunjukkan cara menggunakan kelas ini dengan file contoh yang dijelaskan di atas.

```java
public static void Example_XSLFO_to_PDF() {
    // Memperkenalkan objek XslFoLoadOption
    com.aspose.pdf.XslFoLoadOptions options = new com.aspose.pdf.XslFoLoadOptions(_dataDir+"employees.xslt");
    // Membuat objek Document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(_dataDir+"employees.xml", options);
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

## Menghasilkan dokumen PDF berdasarkan Skema XML Aspose.PDF

Cara lain untuk membuat dokumen PDF dari XML adalah dengan menggunakan Skema XML Aspose.PDF. Menggunakan diagram ini, Anda dapat mendeskripsikan tata letak halaman dengan cara yang sama seolah-olah Anda menggunakan tata letak tabel dalam HTML. Mari kita pertimbangkan pekerjaan metode ini secara lebih rinci.

### Mendefinisikan halaman

Mari kita definisikan halaman dengan parameter default.
 Halaman kami akan memiliki ukuran halaman A4 dan hanya berisi satu bagian teks.

```xml
<?xml versi="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <TextFragment>
      <TextSegment>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla odio lorem, luctus in lorem vitae, accumsan semper lectus. Cras a auctor leo, et tincidunt lacus.</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

Untuk menghasilkan dokumen PDF, kita akan menggunakan metode [bindXml](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#bindXml--).

```java
public static void Example_XML_to_PDF() {
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    pdfDocument.bindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

Untuk mendefinisikan ukuran halaman baru, kita harus menambahkan elemen `PageInfo`. Dalam contoh berikut, kami mengatur ukuran halaman A5 dan margin 25mm dan 10mm.

```xml
<?xml versi="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="true" Height="595" Width="420">
      <Margin Top="70.8661" Bottom="70.8661" Left="28.3465" Right="28.3465" />           
    </PageInfo>
    <TextFragment>
      <TextSegment>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla odio lorem, luctus in lorem vitae, accumsan semper lectus. Cras a auctor leo, et tincidunt lacus.</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

### Menambahkan elemen HtmlFragment dalam file XML

Karena HTML mengandung tag yang mirip dengan XML, ketika Anda menulis HTML di dalam tag XML apa pun, parser memperlakukannya sebagai markup XML dan mereka tidak dapat dikenali sebagai tag XML. Masalah ini dapat diatasi dengan menggunakan Bagian "CDATA" dalam XML. Bagian CDATA berisi teks yang tidak diurai oleh parser atau dengan kata lain, tidak diperlakukan sebagai markup XML. Template XML contoh berikut menunjukkan cara menambahkan HtmlFragment di dalam markup XML dengan menggunakan CDATA.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">Ini adalah String Html.</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### Menambahkan elemen Table dalam file XML

Elemen `Table`, `Row`, `Cell` digunakan untuk mendeskripsikan tabel. Cuplikan berikut menunjukkan penggunaan tabel sederhana. Dalam contoh ini beberapa sel memiliki atribut `Alignment` dan atribut ini memiliki nilai numerik:

1. Rata kiri
1. Rata tengah
1. Rata kanan.
1. Rata kanan-kiri. Teks akan diratakan pada margin kiri dan kanan.
1. Rata kanan-kiri penuh. Mirip dengan perataan 'Rata kanan-kiri', kecuali bahwa baris terakhir hanya akan diratakan kiri dalam mode 'Rata kanan-kiri', sementara dalam mode 'Rata kanan-kiri penuh' semua baris akan diratakan kiri dan kanan.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">JADWAL DI RUTE GREENTOWN-BLUEBERG</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | GREENTOWN → BLUEBERG</TextSegment>
    </TextFragment>
    <Table ColumnAdjustment="AutoFitToWindow" ColumnWidths ="10 10 10 10">
      <DefaultCellPadding Top="5" Left="0" Right="0" Bottom="5" />
      <Border>
        <Top Color="Black"></Top>
        <Bottom Color="Black"></Bottom>
        <Left Color="Black"></Left>
        <Right Color="Black"></Right>
      </Border>
      <Margin Top="15" />
      <Row BackgroundColor="LightGray" MinRowHeight="20">
        <Border>
          <Bottom Color="Black"></Bottom>
        </Border>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>Keberangkatan</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Kedatangan</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Hari Kerja</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Kapal</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>07.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>09.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Sen-Sab</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Star</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>10.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>12.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megastar</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>13.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>15.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Star</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>16.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>18.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megastar</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>19.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>21.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Star</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>22.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>00.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Sen-Jum, Min</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megastar</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```


Tables digunakan untuk tata letak dokumen. Misalnya, kita dapat menyesuaikan header halaman. Dalam hal ini, tabel digunakan untuk membagi header menjadi 2 kolom.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <Header>
        <Margin Top="20" />
        <Table ColumnAdjustment="AutoFitToWindow">
            <Row>
                <Cell Alignment="1">
                    <TextFragment>
                        <TextSegment>Tanggal: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>Halaman $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">JADWAL DI RUTE GREENTOWN-BLUEBERG</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | GREENTOWN → BLUEBERG</TextSegment>
    </TextFragment>
    <Table ColumnAdjustment="AutoFitToWindow" ColumnWidths ="10 10 10 10">
      <DefaultCellPadding Top="5" Left="0" Right="0" Bottom="5" />
      <Border>
        <Top Color="Black"></Top>
        <Bottom Color="Black"></Bottom>
        <Left Color="Black"></Left>
        <Right Color="Black"></Right>
      </Border>
      <Margin Top="15" />
      <Row BackgroundColor="LightGray" MinRowHeight="20">
        <Border>
          <Bottom Color="Black"></Bottom>
        </Border>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>Keberangkatan</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Kedatangan</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Hari Kerja</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Kapal</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>07.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>09.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Sen-Sab</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Bintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>10.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>12.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megabintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>13.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>15.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Bintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>16.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>18.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megabintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>19.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>21.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>setiap hari</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Bintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
      <Row>
        <Cell Alignment="2">
          <TextFragment>
            <TextSegment>22.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>00.30</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Sen-Jum, Min</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Megabintang</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```


### Memperbarui konten secara dinamis

Metode BindXML() menawarkan fitur untuk memuat konten file XML dan metode Document.save() dapat digunakan untuk menyimpan output dalam format PDF. Namun selama konversi, kita juga dapat mengakses elemen individu di dalam XML dan menggunakan XML sebagai template. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengakses TextSegments dari file XML.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <TextFragment>
      <TextSegment id="boldHtml">segment1</TextSegment>
    </TextFragment> 
    <TextFragment>
      <TextSegment id="strongHtml">segment2</TextSegment>
    </TextFragment>
  </Page>
</Document>
```

```java
public static void UpdatingContentDynamically() {
    // Instansiasi objek Document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    // Mengikat file XML sumber
    pdfDocument.bindXml(_dataDir + "log.xml");
    
    // Dapatkan referensi TextSegment pertama dengan ID boldHtml
    TextSegment segment = (TextSegment)pdfDocument.getObjectById("boldHtml");
    segment.setText("Demo 1");
    // Dapatkan referensi TextSegment kedua dengan ID strongHtml
    segment = (TextSegment)pdfDocument.getObjectById("strongHtml");
    segment.setText("Demo 2");
    // Simpan file PDF hasil
    pdfDocument.save(_dataDir + "XMLToPDF_out.pdf");
}
```


### Menambahkan elemen grafis ke halaman

Kita dapat menambahkan elemen tambahan lainnya ke dokumen XML: objek Gambar atau Grafik. Cuplikan berikut menunjukkan cara menambahkan elemen tersebut ke dokumen

```xml
<Graph Width="20" Height="20">    
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Menetapkan Jalur Gambar Saat Mengonversi XML ke PDF

Template XML berikut berisi tag `<Image>` dengan ID "testImg". Jika Anda ingin menetapkan jalur gambar dari kode Anda, Anda dapat mengakses elemen Gambar dari template XML selama proses konversi dan menetapkan jalur ke alamat yang Anda inginkan untuk gambar.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
 <Page id="mainSection">
    <PageInfo IsLandscape="true">
        <Margin Left="20" Right="20" Top="10" Bottom="30" />
    </PageInfo>
    <Header>
        <Margin Top="20" />
        <Table ColumnAdjustment="AutoFitToWindow">
            <Row>
                <Cell Alignment="1">
                    <Image File="logo.png" Id = "testImg"></Image>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>Page $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <Table ColumnAdjustment="AutoFitToWindow" ColumnWidths="8 10">
    <DefaultCellPadding Top="0" Left="0" Right="0" Bottom="0" />
    <Margin Top="15" />
    <Row>
        <Cell Alignment="1">
        <!--Logo-->
            <TextFragment>
                <TextSegment> Request ID</TextSegment>
                <TextState FontSize="14" ForegroundColor="#0e4f9c" FontStyle="1" /> 
            </TextFragment>
            <TextFragment>
                <TextSegment></TextSegment>
            </TextFragment>
            <TextFragment>
                <TextSegment id="boldtext">Some Bold Text</TextSegment>
                <TextState FontSize="14" FontStyle="1"></TextState>
            </TextFragment>
        </Cell>
    </Row>
    </Table>
 </Page>
</Document>
```


Code untuk mengatur jalur gambar dalam template XML adalah sebagai berikut:

```java
public static void Example_XML_to_PDF_01(){
    String inXml = _dataDir + "input.xml";
    String inFile = _dataDir + "aspose-logo.jpg";
    String outFile = _dataDir + "output_out.pdf";
    com.aspose.pdf.Document doc = new com.aspose.pdf.Document();
    doc.bindXml(inXml);
    com.aspose.pdf.Image image = (com.aspose.pdf.Image)doc.getObjectById("testImg");
    image.setFile(inFile);
    doc.save(outFile);
}
```
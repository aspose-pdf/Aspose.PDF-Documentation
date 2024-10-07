---
title: Generate PDF from XML
linktitle: Generate PDF from XML
type: docs
weight: 10
url: /net/generate-pdf-from-xml
description: Aspose.PDF untuk .NET menyediakan beberapa cara untuk mengonversi file XML menjadi dokumen PDF yang memerlukan file XML input.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate PDF from XML",
    "alternativeHeadline": "Convert XML into PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, generate pdf form xml, convert xml to pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/generate-pdf-from-xml",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-pdf-from-xml"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET menyediakan beberapa cara untuk mengonversi file XML menjadi dokumen PDF yang memerlukan file XML input."
}
</script>

Berikut cuplikan kode juga bekerja dengan [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

Menghasilkan dokumen PDF dari dokumen XML bukanlah tugas yang sepele karena dokumen XML dapat menggambarkan konten yang berbeda. Aspose.PDF untuk .NET memiliki beberapa cara untuk menghasilkan PDF berdasarkan dokumen XML:

- menggunakan transformasi XSLT
- menggunakan markup XSL-FO (XSL Formatting Objects)
- menggunakan Skema XML Aspose.PDF sendiri

## Menghasilkan dokumen PDF menggunakan transformasi XSLT

XSL (eXtensible Stylesheet Language) adalah bahasa styling untuk mengubah dokumen XML menjadi dokumen XML lainnya atau HTML. Dalam kasus kami, kami dapat menggunakan transformasi XML ke HTML dan kemudian membuat PDF berdasarkan data HTML.

Asumsikan kita memiliki file XML dengan katalog CD sederhana (lihat di bawah).

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
To convert this file to PDF kita harus membuat XSL dengan layout HTML. Mari kita render data kita dalam tabel. File XSL yang akan membantu kita melakukan ini mungkin terlihat seperti ini:

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
 
Jadi, kita perlu mengubah XML dan memuatnya ke dalam dokumen PDF.

```csharp
private static void ExampleXSLTtoPDF()
{
    var _dataDir = @"C:\tmp\";
    var XmlContent = File.ReadAllText(@"XMLFile1.xml");
    var XsltContent = File.ReadAllText(@"XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();
    // set page size to A5
    options.PageInfo.Height = 595;
    options.PageInfo.Width = 420;
    var pdfDocument = new Aspose.Pdf.Document(TransformXmltoHtml(XmlContent, XsltContent), options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}

public static MemoryStream TransformXmltoHtml(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();
    using (var reader = XmlReader.Create(new StringReader(xsltString)))
    {
        transform.Load(reader);
    }
    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);
    using (var reader = XmlReader.Create(new StringReader(inputXml)))
    {
        transform.Transform(reader, null, results);
    }
    memoryStream.Position = 0;
    return memoryStream;
}
```
## Menghasilkan dokumen PDF menggunakan markup XSL-FO

XSL-FO adalah bahasa markup berbasis XML yang menggambarkan pemformatan data XML untuk output ke layar, kertas, atau media lainnya. Aspose.PDF memiliki kelas khusus yang memungkinkan untuk menerapkan markup XSL-FO dan mendapatkan dokumen PDF.

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
Aspose.PDF memiliki kelas khusus [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) yang memungkinkan untuk menerapkan transformasi XSL-FO.
Potongan kode berikut menunjukkan cara menggunakan kelas ini dengan file sampel yang dijelaskan di atas.

```csharp
public static void Example_XSLFO_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    // Instansiasi objek XslFoLoadOption
    var options = new Pdf.XslFoLoadOptions("employees.xslt");
    // Buat objek Document
    var pdfDocument = new Aspose.Pdf.Document("employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

### Menghasilkan dokumen PDF menggunakan markup XSL-FO dan parameter XSL

Terkadang kita perlu menggunakan [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param). Elemen `<xsl:param>` menetapkan parameter berdasarkan nama dan, opsional, nilai default untuk parameter tersebut.

Mari kita ambil contoh yang sama seperti pada kasus sebelumnya, tetapi dengan sedikit perubahan (menambahkan parameter). File XML dengan data sampel tetap tidak berubah, ...

```xml
```xml
<?xml version="1.0" encoding="utf-8" ?>
<employees>
    <companyname>ABC Inc.</companyname>
    <employee>
        <id>101</id>
        <name>Andrew</name>
        <designation>Manajer</designation>
    </employee>

    <employee>
        <id>102</id>
        <name>Eduard</name>
        <designation>Eksekutif</designation>
    </employee>

    <employee>
        <id>103</id>
        <name>Peter</name>
        <designation>Eksekutif</designation>
    </employee>
</employees>
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fo="http://www.w3.org/1999/XSL/Format" exclude-result-prefixes="fo">

 <xsl:param name="isBoldName"></xsl:param>

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
   <xsl:if test="designation = 'Manajer'">
    <xsl:attribute name="font-weight">bold</xsl:attribute>
   </xsl:if>
   <fo:table-cell>
    <fo:block>
     <xsl:value-of select="id"/>
    </fo:block>
   </fo:table-cell>

   <fo:table-cell>
    <xsl:if test="$isBoldName='yes'">
     <xsl:attribute name="font-weight">bold</xsl:attribute>
    </xsl:if>
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
 
 
Untuk menambahkan parameter XSL, kita perlu membuat [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) sendiri dan
menetapkannya sebagai properti dalam [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions).
Cuplikan berikut menunjukkan cara menggunakan kelas ini dengan file contoh yang dijelaskan di atas.

```csharp
public static void Example_XSLFO_to_PDF_Param_21_7()
{
  string xmlInputFile = Path.Combine(_dataDir, "employees.xml");
  string xsltInputFile = Path.Combine(_dataDir, "employees.xslt");
  string outputFile = Path.Combine(_dataDir, "out.pdf");

  XslFoLoadOptions options = new XslFoLoadOptions(xsltInputFile);

  options.XsltArgumentList = new XsltArgumentList();
  options.XsltArgumentList.AddParam("isBoldName", "", "yes");

  Document document = new Document(xmlInputFile, options);
  document.Save(outputFile);
}
```

Jika Anda menggunakan versi lebih awal dari 21.7, silakan gunakan teknik berikut:

```csharp
  public static void Example_XSLFO_to_PDF_Param_21_6()
  {
      var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
      var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

      var options = new Aspose.Pdf.XslFoLoadOptions();
      var pdfDocument = new Aspose.Pdf.Document(TransformXSL(XmlContent, XsltContent), options);
      pdfDocument.Save(_dataDir + "data_xml.pdf");
  }

  public static MemoryStream TransformXSL(string inputXml, string xsltString)
  {
      var transform = new XslCompiledTransform();

      //Buat XsltArgumentList sendiri
      XsltArgumentList argsList = new XsltArgumentList();
      argsList.AddParam("isBoldName", "", "no");
      //---------------------

      using (var reader = XmlReader.Create(new StringReader(xsltString)))
      {
          transform.Load(reader);
      }
      var memoryStream = new MemoryStream();

      var results = new StreamWriter(memoryStream);
      using (var reader = XmlReader.Create(new StringReader(inputXml)))
      {
          transform.Transform(reader, argsList, results);
      }

      memoryStream.Position = 0;
      return memoryStream;
  }
}
```
## Menghasilkan Dokumen PDF berdasarkan Skema XML Aspose.PDF

Cara lain untuk membuat dokumen PDF dari XML adalah menggunakan Skema XML Aspose.PDF. Menggunakan diagram ini, Anda dapat menjelaskan tata letak halaman dengan cara yang sama seperti jika Anda menggunakan tata letak tabel di HTML. Mari kita pertimbangkan cara kerja metode ini lebih detail.

### Mendefinisikan halaman

Mari kita definisikan halaman dengan parameter default. Halaman kita akan memiliki ukuran halaman A4 dan hanya berisi satu bagian teks.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <TextFragment>
      <TextSegment>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla odio lorem, luctus in lorem vitae, accumsan semper lectus. Cras a auctor leo, et tincidunt lacus.</TextSegment>
    </TextFragment>
  </Page>
</Document>
```

Untuk menghasilkan dokumen PDF kita akan menggunakan metode [BindXml](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/bindxml/index).

```csharp
private static void Example_XML_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    var pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.BindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

Untuk mendefinisikan ukuran halaman baru, kita harus menambahkan elemen `PageInfo`. Dalam contoh berikut, kami menetapkan ukuran halaman A5 dan margin 25mm dan 10mm.

```xml
<?xml version="1.0" encoding="utf-8" ?>
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

Karena HTML mengandung tag yang mirip dengan XML, jadi ketika Anda menulis HTML di dalam tag XML apa pun, parser memperlakukannya sebagai markup XML dan mereka tidak dapat dikenali sebagai tag XML.
```

Karena HTML mengandung tag yang mirip dengan XML, ketika Anda menulis HTML di dalam tag XML, parser memperlakukannya sebagai markup XML dan mereka tidak dapat dikenali sebagai tag XML.

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

### Menambahkan elemen Tabel dalam file XML

Elemen `Table`, `Row`, `Cell` digunakan untuk mendeskripsikan tabel. Cuplikan berikut menunjukkan penggunaan tabel sederhana. Dalam contoh ini beberapa sel memiliki atribut `Alignment` dan atribut ini memiliki nilai numerik:

1. Perataan kiri
1. Perataan tengah
1. Perataan kanan.
1. Perataan justify. Teks akan diratakan pada margin kiri dan kanan.
1.
```
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
Tables digunakan untuk tata letak dokumen. Sebagai contoh, kita bisa menyesuaikan header halaman. Dalam hal ini, tabel digunakan untuk membagi header menjadi 2 kolom.

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

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instansiasi objek Dokumen
Document doc = new Document();
// Mengikat file XML sumber
doc.BindXml(dataDir + "log.xml");
// Dapatkan referensi objek halaman dari XML
Page page = (Page)doc.GetObjectById("mainSection");
// Dapatkan referensi TextSegment pertama dengan ID boldHtml
TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
// Dapatkan referensi TextSegment kedua dengan ID strongHtml
segment = (TextSegment)doc.GetObjectById("strongHtml");
// Simpan file PDF yang dihasilkan
doc.Save(dataDir + "XMLToPDF_out.pdf");
```
### Menambahkan elemen grafis ke halaman

Kita dapat menambahkan elemen tambahan lainnya ke dokumen XML: objek Gambar atau Grafik. Cuplikan berikut menunjukkan cara menambahkan elemen-elemen tersebut ke dalam dokumen

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Merah" FillColor="Biru"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Mengatur Jalur Gambar Saat Mengonversi XML ke PDF

Templat XML berikut mengandung tag `<Image>` di dalamnya dengan ID "testImg". Jika Anda ingin mengatur jalur gambar dari kode Anda, Anda dapat mengakses elemen Gambar dari templat XML selama proses konversi dan mengatur jalur ke alamat yang Anda inginkan untuk gambar.

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
                        <TextSegment>Halaman $p / $P</TextSegment>
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
                <TextSegment> ID Permintaan</TextSegment>
                <TextState FontSize="14" ForegroundColor="#0e4f9c" FontStyle="1" />
            </TextFragment>
            <TextFragment>
                <TextSegment></TextSegment>
            </TextFragment>
            <TextFragment>
                <TextSegment id="boldtext">Beberapa Teks Tebal</TextSegment>
                <TextState FontSize="14" FontStyle="1"></TextState>
            </TextFragment>
        </Cell>
    </Row>
    </Table>
 </Page>
</Document>
```
Code untuk mengatur jalur gambar dalam template XML adalah sebagai berikut:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
string inXml = dataDir + "input.xml";
string inFile = dataDir + "aspose-logo.jpg";
string outFile = dataDir + "output_out.pdf";
Document doc = new Document();
doc.BindXml(inXml);
Image image = (Image)doc.GetObjectById("testImg");
image.File = inFile;
doc.Save(outFile);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

---
id: "create-plugin"
title: "Membuat Plugin"
sidebar_label: "Membuat Plugin"
changefreq: "monthly"
type: docs
---

### Pengantar

Membuat plugin memungkinkan Anda untuk menambahkan fungsionalitas khusus ke aplikasi Anda.

### Langkah-langkah Membuat Plugin

1. **Buat Direktori Plugin:**

   Buat direktori baru di dalam folder `plugins` proyek Anda. Nama direktori ini harus sesuai dengan nama plugin Anda.

   ```bash
   mkdir plugins/nama-plugin-anda
   ```

2. **Buat File Utama Plugin:**

   Di dalam direktori plugin, buat file utama untuk plugin Anda. Biasanya, file ini dinamakan `index.js` atau `main.js`.

   ```javascript
   // plugins/nama-plugin-anda/index.js
   module.exports = function() {
     console.log("Plugin Anda telah berhasil diinisialisasi!");
   };
   ```

3. **Tambahkan Konfigurasi Plugin:**

   Tambahkan konfigurasi plugin di file konfigurasi utama aplikasi Anda, biasanya `config.js` atau `app.js`.

   ```javascript
   const namaPluginAnda = require('./plugins/nama-plugin-anda');

   namaPluginAnda();
   ```

### Contoh Plugin

Berikut adalah contoh plugin sederhana yang menambahkan middleware ke aplikasi Express.js.

```javascript
// plugins/logger/index.js
module.exports = function(app) {
  app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
  });
};
```

Untuk menggunakan plugin ini dalam aplikasi Express.js Anda:

```javascript
const express = require('express');
const logger = require('./plugins/logger');

const app = express();

logger(app);

app.get('/', (req, res) => {
  res.send('Hello, world!');
});

app.listen(3000, () => {
  console.log('Server berjalan di port 3000');
});
```

### Kesimpulan

Dengan mengikuti langkah-langkah di atas, Anda dapat membuat dan mengintegrasikan plugin ke dalam aplikasi Anda. Plugin dapat membantu memisahkan logika spesifik dari kode utama aplikasi Anda, membuatnya lebih modular dan mudah dikelola.
```

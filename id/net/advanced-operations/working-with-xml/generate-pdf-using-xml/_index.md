---
title: Menghasilkan PDF dari XML
linktitle: Menghasilkan PDF dari XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/generate-pdf-from-xml
description: Aspose.PDF for .NET menyediakan beberapa cara untuk mengonversi file XML menjadi dokumen PDF yang memerlukan file XML input.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate PDF from XML",
    "alternativeHeadline": "Generate PDF directly from XML data",
    "abstract": "Aspose.PDF for .NET sekarang menghasilkan PDF langsung dari data XML menggunakan beberapa metode: transformasi XSLT, markup XSL-FO, dan skema XML Aspose.PDF kustom. Fungsionalitas baru ini menawarkan pembuatan PDF yang fleksibel dari berbagai struktur XML, menyederhanakan alur kerja pembuatan dokumen",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3834",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET menyediakan beberapa cara untuk mengonversi file XML menjadi dokumen PDF yang memerlukan file XML input."
}
</script>

Potongan kode berikut juga bekerja dengan [Aspose.PDF.Drawing](/pdf/id/net/drawing/) pustaka.

Menghasilkan dokumen PDF dari dokumen XML bukanlah tugas yang sepele karena dokumen XML dapat menggambarkan konten yang berbeda. Aspose.PDF for .NET memiliki beberapa cara untuk menghasilkan PDF berdasarkan dokumen XML:

- menggunakan transformasi XSLT
- menggunakan markup XSL-FO (XSL Formatting Objects)
- menggunakan skema XML Aspose.PDF sendiri

## Menghasilkan dokumen PDF menggunakan transformasi XSLT

XSL (eXtensible Stylesheet Language) adalah bahasa gaya untuk mengubah dokumen XML menjadi dokumen XML lain atau HTML. Dalam kasus kami, kami dapat menggunakan transformasi XML ke HTML dan kemudian membuat PDF berdasarkan data HTML.

Misalkan kami memiliki file XML dengan katalog CD sederhana (lihat di bawah).

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

Untuk mengonversi file ini ke PDF, kami harus membuat XSL dengan tata letak HTML. Mari kita render data kami dalam tabel. File XSL yang akan membantu kami melakukan ini mungkin terlihat seperti ini:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>My CD Collection</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">Title</th>
            <th style="text-align:left">Artist</th>
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

Jadi, kami perlu mengubah XML dan memuatnya ke dalam dokumen PDF. Contoh berikut menunjukkan cara ini:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXsltToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var XmlContent = File.ReadAllText(dataDir + "XMLFile1.xml");
    var XsltContent = File.ReadAllText(dataDir + "XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // set page size to A5
    options.PageInfo.Height = 595;
    options.PageInfo.Width = 420;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(TransformXmlToHtml(XmlContent, XsltContent), options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLT_out.pdf");
    }
}

public static MemoryStream TransformXmlToHtml(string inputXml, string xsltString)
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
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXsltToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var XmlContent = File.ReadAllText(dataDir + "XMLFile1.xml");
    var XsltContent = File.ReadAllText(dataDir + "XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // set page size to A5
    options.PageInfo.Height = 595;
    options.PageInfo.Width = 420;

    // Open PDF document
    using var document = new Aspose.Pdf.Document(TransformXmlToHtml(XmlContent, XsltContent), options);

    // Save PDF document
    document.Save(dataDir + "XSLT_out.pdf");
}

public static MemoryStream TransformXmlToHtml(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    using var reader1 = XmlReader.Create(new StringReader(xsltString));
    transform.Load(reader1);

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using var reader2 = XmlReader.Create(new StringReader(inputXml));
    transform.Transform(reader2, null, results);

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}
{{< /tabs >}}

## Menghasilkan dokumen PDF menggunakan markup XSL-FO

XSL-FO adalah bahasa markup berbasis XML yang menggambarkan pemformatan data XML untuk output ke layar, kertas, atau media lainnya. Aspose.PDF memiliki kelas khusus yang memungkinkan penerapan markup XSL-FO dan mendapatkan dokumen PDF.

Mari kita ambil contoh. Berikut adalah file XML dengan data contoh karyawan.

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

Mari kita buat satu file lagi - file markup XSL-FO untuk mengubah data karyawan menjadi tabel.

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
                        Company Name: <xsl:value-of select="companyname"/>
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

Aspose.PDF memiliki [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) kelas khusus yang memungkinkan penerapan transformasi XSL-FO.
Potongan berikut menunjukkan cara menggunakan kelas ini dengan file contoh yang dijelaskan di atas.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    // Open XML file
    using (var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    // Open XML file
    using var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Menghasilkan dokumen PDF menggunakan markup XSL-FO dan parameter XSL

Terkadang kami perlu menggunakan [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param). Elemen `<xsl:param>` menetapkan parameter berdasarkan nama dan, jika perlu, nilai default untuk parameter tersebut.

Mari kita ambil contoh yang sama seperti pada kasus sebelumnya, tetapi dengan perubahan kecil (menambahkan parameter). File XML dengan data contoh tetap tidak tersentuh, ...

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

tetapi dalam file markup XSL-FO kami akan menambahkan parameter: `<xsl:param name="isBoldName"></xsl:param>` dan akan menerapkannya ke kolom `Name`.

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
      Company Name: <xsl:value-of select="companyname"/>
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

Untuk menambahkan parameter XSL, kami perlu membuat [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) sendiri dan
mengatur sebagai properti di [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions).
Potongan berikut menunjukkan cara menggunakan kelas ini dengan file contoh yang dijelaskan di atas.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_7()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open XML file
    using (var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_7()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open XML file
    using var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Jika Anda menggunakan versi lebih awal dari 21.7, silakan gunakan teknik berikut:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_6()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var xmlContent = File.ReadAllText(dataDir + "employees.xml");
    var xsltContent = File.ReadAllText(dataDir + "employees.xslt");

    var options = new Aspose.Pdf.XslFoLoadOptions();

    // Open XML file
    using (var document = new Aspose.Pdf.Document(TransformXsl(xmlContent, xsltContent), options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}

public static MemoryStream TransformXsl(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    // Create own XsltArgumentList
    var argsList = new XsltArgumentList();
    argsList.AddParam("isBoldName", "", "no");

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
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf_Param_21_6()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var xmlContent = File.ReadAllText(dataDir + "employees.xml");
    var xsltContent = File.ReadAllText(dataDir + "employees.xslt");

    var options = new Aspose.Pdf.XslFoLoadOptions();

    // Open XML file
    using var document = new Aspose.Pdf.Document(TransformXsl(xmlContent, xsltContent), options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}

public static MemoryStream TransformXsl(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    // Create own XsltArgumentList
    var argsList = new XsltArgumentList();
    argsList.AddParam("isBoldName", "", "no");

    using var reader1 = XmlReader.Create(new StringReader(xsltString));
    transform.Load(reader1);

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using var reader2 = XmlReader.Create(new StringReader(inputXml));
    transform.Transform(reader2, argsList, results);

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}
{{< /tabs >}}

## Menghasilkan dokumen PDF berdasarkan Skema XML Aspose.PDF

Cara lain untuk membuat dokumen PDF dari XML adalah menggunakan Skema XML Aspose.PDF. Menggunakan diagram ini, Anda dapat menggambarkan tata letak halaman dengan cara yang sama seolah-olah Anda menggunakan tata letak tabel dalam HTML. Mari kita pertimbangkan cara kerja metode ini lebih detail.

### Mendefinisikan halaman

Mari kita definisikan halaman dengan parameter default. Halaman kami akan memiliki ukuran halaman A4 dan hanya berisi satu potong teks.

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

Untuk menghasilkan dokumen PDF, kami akan menggunakan metode [BindXml](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/bindxml/index).

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXmlToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file to the document
        document.BindXml(dataDir + "aspose_pdf_demo.xml");

        // Save PDF document
        document.Save(dataDir + "XML_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXmlToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    //Bind XML file to the document
    document.BindXml(dataDir + "aspose_pdf_demo.xml");

    // Save PDF document
    document.Save(dataDir + "XML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Untuk mendefinisikan ukuran halaman baru, kami harus menambahkan elemen `PageInfo`. Dalam contoh berikut, kami mengatur ukuran halaman A5 dan margin 25mm dan 10mm.

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

Karena HTML mengandung tag yang mirip dengan XML, ketika Anda menulis HTML di dalam tag XML mana pun, parser memperlakukannya sebagai markup XML dan mereka tidak dapat dikenali sebagai tag XML. Masalah ini dapat diatasi dengan menggunakan "Bagian CDATA" dalam XML. Bagian CDATA berisi teks yang tidak diparsing oleh parser atau dengan kata lain, tidak diperlakukan sebagai markup XML. Template XML contoh berikut menunjukkan cara menambahkan HtmlFragment di dalam markup XML dengan menggunakan CDATA.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">This is Html String.</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### Menambahkan elemen Tabel dalam file XML

Elemen `Table`, `Row`, `Cell` digunakan untuk menggambarkan tabel. Potongan berikut menunjukkan penggunaan tabel sederhana. Dalam contoh ini, beberapa sel memiliki atribut `Alignment` dan atribut ini memiliki nilai numerik:

1. Penyelarasan kiri
1. Penyelarasan tengah
1. Penyelarasan kanan.
1. Penyelarasan justify. Teks akan disejajarkan di kedua margin kiri dan kanan.
1. Justifikasi penuh. Mirip dengan penyelarasan 'Justify', kecuali bahwa baris terakhir hanya akan disejajarkan ke kiri dalam mode 'Justify', sementara dalam mode 'FullJustify' semua baris akan disejajarkan ke kiri dan kanan.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">TIMETABLES ON GREENTOWN-BLUEBERG ROUTE</h1>
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
            <TextSegment>Departure</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Arrival</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Weekday</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Ship</TextSegment>
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
            <TextSegment>Mon-Sat</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>Mon-Fri, Sun</TextSegment>
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

Tabel digunakan untuk tata letak dokumen. Misalnya, kami dapat menyesuaikan header halaman. Dalam hal ini, tabel digunakan untuk membagi header menjadi 2 kolom.

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
                        <TextSegment>Date: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>Page $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">TIMETABLES ON GREENTOWN-BLUEBERG ROUTE</h1>
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
            <TextSegment>Departure</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Arrival</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Weekday</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Ship</TextSegment>
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
            <TextSegment>Mon-Sat</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>Mon-Fri, Sun</TextSegment>
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

Metode BindXML() menawarkan fitur untuk memuat konten file XML dan metode Document.save() dapat digunakan untuk menyimpan output dalam format PDF. Namun selama konversi, kami juga dapat mengakses elemen individu di dalam XML dan menggunakan XML sebagai template. Potongan kode berikut menunjukkan langkah-langkah untuk mengakses TextSegments dari file XML.

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

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file
        document.BindXml(dataDir + "log.xml");

        // Get reference of page object from XML
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get reference of first TextSegment with ID boldHtml
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");

        // Get reference of second TextSegment with ID strongHtml
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "XMLToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Bind XML file
    document.BindXml(dataDir + "log.xml");

    // Get reference of page object from XML
    var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

    // Get reference of first TextSegment with ID boldHtml
    var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");

    // Get reference of second TextSegment with ID strongHtml
    segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

    // Save PDF document
    document.Save(dataDir + "XMLToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Menambahkan elemen grafis ke halaman

Kami dapat menambahkan elemen tambahan lainnya ke dokumen XML: objek Gambar atau Grafik. Potongan berikut menunjukkan cara menambahkan elemen tersebut ke dokumen

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Mengatur Jalur Gambar Saat Mengonversi XML ke PDF

Template XML berikut berisi tag `<Image>` di dalamnya dengan ID "testImg". Jika Anda ingin mengatur jalur gambar dari kode Anda, Anda dapat mengakses elemen Gambar dari template XML selama proses konversi dan mengatur jalur ke alamat yang Anda inginkan untuk gambar.

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

Kode untuk mengatur jalur gambar dalam template XML adalah sebagai berikut:

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file
        document.BindXml(dataDir + "input.xml");

        // Get reference of Image with ID testImg
        var image = (Aspose.Pdf.Image)document.GetObjectById("testImg");

        // Set image file
        image.File = dataDir + "aspose-logo.jpg";

        // Save PDF document
        document.Save(dataDir + "output_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Bind XML file
    document.BindXml(dataDir + "input.xml");

    // Get reference of Image with ID testImg
    var image = (Aspose.Pdf.Image)document.GetObjectById("testImg");

    // Set image file
    image.File = dataDir + "aspose-logo.jpg";

    // Save PDF document
    document.Save(dataDir + "output_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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
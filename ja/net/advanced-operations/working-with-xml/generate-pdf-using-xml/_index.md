---
title: Generate PDF from XML
linktitle: Generate PDF from XML
type: docs
weight: 10
url: /ja/net/generate-pdf-from-xml
description: Aspose.PDF for .NETは、入力XMLファイルを必要とするPDFドキュメントに変換するいくつかの方法を提供します。
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
    "description": "Aspose.PDF for .NETは、入力XMLファイルを必要とするPDFドキュメントに変換するいくつかの方法を提供します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

XMLドキュメントからPDFドキュメントを生成することは簡単な作業ではありません。なぜなら、XMLドキュメントは異なる内容を記述することができるからです。Aspose.PDF for .NETは、XMLドキュメントに基づいてPDFを生成するためのいくつかの方法を提供しています：

- XSLT変換を使用する
- XSL-FO（XSL Formatting Objects）マークアップを使用する
- 独自のAspose.PDF XML Schemaを使用する

## XSLT変換を使用してPDFドキュメントを生成する

XSL（eXtensible Stylesheet Language）は、XMLドキュメントを他のXMLドキュメントやHTMLに変換するためのスタイリング言語です。私たちの場合、XMLをHTMLに変換し、そのHTMLデータに基づいてPDFを作成することができます。

仮に、シンプルなCDカタログを含むXMLファイルがあるとします（以下を参照）。

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

このファイルをPDFに変換するには、HTMLレイアウトのXSLを作成する必要があります。データをテーブルにレンダリングしましょう。これを行うのに役立つXSLファイルは次のようになります：

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>私のCDコレクション</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">タイトル</th>
            <th style="text-align:left">アーティスト</th>
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

したがって、XMLを変換してPDFドキュメントにロードする必要があります。
```

つまり、XMLを変換してPDFドキュメントにロードする必要があります。

```csharp
private static void ExampleXSLTtoPDF()
{
    var _dataDir = @"C:\tmp\";
    var XmlContent = File.ReadAllText(@"XMLFile1.xml");
    var XsltContent = File.ReadAllText(@"XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();
    // ページサイズをA5に設定
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
## PDFドキュメントをXSL-FOマークアップを使用して生成する

XSL-FOは、XMLデータのフォーマットを画面、紙、その他のメディアに出力するためのXMLベースのマークアップ言語です。Aspose.PDFには、XSL-FOマークアップを適用してPDFドキュメントを取得する特別なクラスがあります。

例を見てみましょう。以下は、従業員のサンプルデータを含むXMLファイルです。

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

従業員のデータをテーブルに変換するためのXSL-FOマークアップファイルをもう一つ作成しましょう。

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
Aspose.PDFには、XSL-FO変換を適用するための特別な[XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions)クラスがあります。
以下のスニペットは、上記のサンプルファイルを使用してこのクラスを使用する方法を示しています。

```csharp
public static void Example_XSLFO_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    // Instantiate XslFoLoadOption object
    var options = new Pdf.XslFoLoadOptions("employees.xslt");
    // Create Document object
    var pdfDocument = new Aspose.Pdf.Document("employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

### XSL-FOマークアップとXSLパラメータを使用してPDFドキュメントを生成する

時には[XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param)を使用する必要があります。`<xsl:param>`要素は、名前とオプションでそのパラメータのデフォルト値を設定します。

前回と同じ例を取り上げますが、少し変更（パラメータの追加）を加えます。サンプルデータを含むXMLファイルはそのままにして、...
```xml
<?xml version="1.0" encoding="utf-8"?>
<employees>
    <companyname>ABC株式会社</companyname>
    <employee>
        <id>101</id>
        <name>アンドリュー</name>
        <designation>マネージャー</designation>
    </employee>

    <employee>
        <id>102</id>
        <name>エドゥアルド</name>
        <designation>エグゼクティブ</designation>
    </employee>

    <employee>
        <id>103</id>
        <name>ピーター</name>
        <designation>エグゼクティブ</designation>
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
      会社名: <xsl:value-of select="companyname"/>
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
To add XSL params we need to create own [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) and
set as property in [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions).
The following snippet shows how to use this class with the sample files described above.

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

バージョン21.7より前を使用している場合は、次の技術を使用してください:

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

      //Create own XsltArgumentList
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
## Aspose.PDF XML Schemaに基づくPDFドキュメントの生成

XMLからPDFドキュメントを作成する別の方法は、Aspose.PDF XML Schemaを使用することです。この図を使用して、HTMLのテーブルレイアウトを使用しているかのようにページレイアウトを記述できます。この方法の作業をより詳細に検討しましょう。

### ページの定義

デフォルトのパラメータでページを定義しましょう。私たちのページはA4サイズで、1つのテキスト部分のみを含みます。

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

PDFドキュメントを生成するには、[BindXml](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/bindxml/index) メソッドを使用します。

```csharp
private static void Example_XML_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    var pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.BindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
To define a new page size we should add a `PageInfo` element. In the following example, we were set A5 page size and margins 25mm and 10mm.

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

### XMLファイルにHtmlFragment要素を追加する

HTMLはXMLに似たタグを含むため、任意のXMLタグ内にHTMLを書き込むと、パーサーはそれをXMLマークアップとして扱い、単にXMLタグとして認識することはできません。

HTMLにはXMLに似たタグが含まれているため、任意のXMLタグ内にHTMLを書き込むと、パーサーはそれをXMLマークアップとして扱い、単にXMLタグとして認識することができません。

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

### XMLファイルにTable要素を追加する

要素 `Table`、`Row`、`Cell` はテーブルを記述するために使用されます。以下のスニペットは、シンプルなテーブルを使用する方法を示しています。この例では、一部のセルに `Alignment` 属性があり、この属性には数値が設定されています:

1. 左揃え
1. 中央揃え
1. 右揃え
1. 両端揃え。テキストは左と右の両方の余白に揃えられます。
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
        <h1 style="font-family:Tahoma; font-size:16pt;">グリーンタウン-ブルーバーグルートの時刻表</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | グリーンタウン → ブルーバーグ</TextSegment>
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
            <TextSegment>出発</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>到着</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>平日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>船</TextSegment>
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
            <TextSegment>月-土</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>月-金、日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```
Tables are used for layout of documents. For example, we can customize a page header. In this case, table were used to divide the header into 2 columns.

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
                        <TextSegment>日付: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>ページ $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">グリーンタウン-ブルーバーグルートの時刻表</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | グリーンタウン → ブルーバーグ</TextSegment>
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
            <TextSegment>出発</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>到着</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>曜日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>船</TextSegment>
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
            <TextSegment>月-土</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
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
            <TextSegment>毎日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>スター</TextSegment>
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
            <TextSegment>月-金、日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>メガスター</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```
### コンテンツの動的な更新

BindXML() メソッドは XML ファイルの内容を読み込み、Document.save() メソッドを使用して出力を PDF 形式で保存する機能を提供します。しかし、変換中に XML 内の個々の要素にアクセスし、XML をテンプレートとして使用することもできます。次のコードスニペットは、XML ファイルから TextSegments にアクセスする手順を示しています。

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
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instantiate Document object
Document doc = new Document();
// Bind source XML file
doc.BindXml( dataDir + "log.xml");
// Get reference of page object from XML
Page page = (Page)doc.GetObjectById("mainSection");
// Get reference of first TextSegment with ID boldHtml
TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
// Get reference of second TextSegment with ID strongHtml
segment = (TextSegment)doc.GetObjectById("strongHtml");
// Save resultant PDF file
doc.Save(dataDir + "XMLToPDF_out.pdf");
```
### ページにグラフィック要素を追加する

XMLドキュメントに他の追加要素を追加できます: Image または Graph オブジェクト。以下のスニペットは、それらの要素をドキュメントに追加する方法を示しています。

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### XMLをPDFに変換する際の画像パスの設定

以下のXMLテンプレートには、IDが "testImg" の `<Image>` タグが含まれています。コードから画像パスを設定したい場合は、変換プロセス中にXMLテンプレートからImage要素にアクセスし、画像のパスを希望のアドレスに設定できます。

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
コードをXMLテンプレートに設定する方法は以下の通りです:

```csharp
// ドキュメントディレクトリへのパス。
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
title: "Introduction"
sidebar_label: "Introduction"
slug: "/"
---

This documentation will guide you through the process of setting up, configuring, and deploying our software. Whether you are a novice or an experienced user, you will find the necessary information to get started.

## Prerequisites

Before you begin, ensure you have the following:

- A compatible operating system (Windows, macOS, or Linux)
- Administrative privileges on your machine
- An active internet connection

## Installation

Follow these steps to install the software:

1. Download the installer from our official website.
2. Run the installer and follow the on-screen instructions.
3. Once installation is complete, open the software to ensure it is working correctly.

## Configuration

To configure the software, follow these instructions:

1. Open the settings menu.
2. Adjust the preferences according to your needs.
3. Save your changes and restart the software for the new settings to take effect.

## Deployment

Deploying the software involves the following steps:

1. Set up your deployment environment.
2. Transfer the necessary files to the server.
3. Run the deployment script.

## Troubleshooting

If you encounter any issues, refer to the troubleshooting section of this documentation or contact our support team for assistance.

---

changefreq: "monthly"
type: docs
---

---
title: "紹介"
sidebar_label: "紹介"
slug: "/"
---

このドキュメントは、ソフトウェアの設定、構成、およびデプロイのプロセスをガイドします。初心者でも経験豊富なユーザーでも、始めるために必要な情報を見つけることができます。

## 前提条件

始める前に、以下を確認してください：

- 互換性のあるオペレーティングシステム（Windows、macOS、またはLinux）
- マシン上での管理者権限
- アクティブなインターネット接続

## インストール

以下の手順に従ってソフトウェアをインストールします：

1. 公式ウェブサイトからインストーラをダウンロードします。
2. インストーラを実行し、画面の指示に従います。
3. インストールが完了したら、ソフトウェアを開き、正しく動作することを確認します。

## 設定

ソフトウェアを設定するには、以下の手順に従います：

1. 設定メニューを開きます。
2. ニーズに応じて設定を調整します。
3. 変更を保存し、新しい設定を有効にするためにソフトウェアを再起動します。

## デプロイ

ソフトウェアをデプロイするには、以下の手順を行います：

1. デプロイ環境を設定します。
2. 必要なファイルをサーバーに転送します。
3. デプロイスクリプトを実行します。

## トラブルシューティング

問題が発生した場合、このドキュメントのトラブルシューティングセクションを参照するか、サポートチームに連絡して支援を受けてください。

---

changefreq: "monthly"
type: docs
---
```

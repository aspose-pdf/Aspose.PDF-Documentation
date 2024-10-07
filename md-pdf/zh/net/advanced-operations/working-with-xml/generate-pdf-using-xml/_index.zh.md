---
title: 从XML生成PDF
linktitle: 从XML生成PDF
type: docs
weight: 10
url: /net/generate-pdf-from-xml
description: Aspose.PDF for .NET 提供了多种方法将XML文件转换为PDF文档，要求输入的XML文件。
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
    "headline": "从XML生成PDF",
    "alternativeHeadline": "将XML转换为PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, c#, 生成 pdf 从 xml, 将 xml 转换为 pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
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
    "description": "Aspose.PDF for .NET 提供了多种方法将XML文件转换为PDF文档，要求输入的XML文件。"
}
</script>

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

从XML文档生成PDF文档并不是一项简单的任务，因为XML文档可以描述不同的内容。Aspose.PDF for .NET 有几种基于XML文档生成PDF的方法：

- 使用XSLT转换
- 使用XSL-FO（XSL格式化对象）标记
- 使用自己的Aspose.PDF XML Schema

## 使用XSLT转换生成PDF文档

XSL（可扩展样式表语言）是一种用于将XML文档转换为其他XML文档或HTML的样式语言。在我们的情况下，我们可以使用XML到HTML的转换，然后基于HTML数据创建PDF。

假设我们有一个简单的CD目录的XML文件（见下文）。

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

要将此文件转换为PDF，我们应该创建一个带有HTML布局的XSL。让我们将数据渲染在表格中。帮助我们做到这一点的XSL文件可能看起来像这样：

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>我的CD收藏</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">标题</th>
            <th style="text-align:left">艺术家</th>
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

因此，我们需要转换XML并加载到PDF文档中。 以下示例展示了这种方式：

```csharp
private static void ExampleXSLTtoPDF()
{
    var _dataDir = @"C:\tmp\";
    var XmlContent = File.ReadAllText(@"XMLFile1.xml");
    var XsltContent = File.ReadAllText(@"XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();
    // 设置页面大小为A5
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
## 使用 XSL-FO 标记生成 PDF 文档

XSL-FO 是一种基于 XML 的标记语言，用于描述 XML 数据的格式，以输出到屏幕、纸张或其他媒体。Aspose.PDF 有一个特殊的类，可以应用 XSL-FO 标记并生成 PDF 文档。

让我们来看一个例子。这是一个包含员工示例数据的 XML 文件。

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

让我们创建另一个文件——XSL-FO 标记文件，将员工数据转换为表格。

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
                        公司名称: <xsl:value-of select="companyname"/>
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

Aspose.PDF 有一个特殊的 [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) 类，它允许应用 XSL-FO 转换。以下代码片段展示了如何使用上述示例文件中的这个类。

```csharp
public static void Example_XSLFO_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    // 实例化 XslFoLoadOption 对象
    var options = new Pdf.XslFoLoadOptions("employees.xslt");
    // 创建 Document 对象
    var pdfDocument = new Aspose.Pdf.Document("employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

### 使用 XSL-FO 标记和 XSL 参数生成 PDF 文档

有时我们需要使用 [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param)。`<xsl:param>` 元素通过名称建立一个参数，并可选择为该参数设定一个默认值。

让我们使用与前一个案例相同的示例，但做一些小改动（添加参数）。包含示例数据的 XML 文件保持不变，...

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

在 XSL-FO 标记文件中，我们将添加参数：`<xsl:param name="isBoldName"></xsl:param>` 并将其应用到 `Name` 列。

要添加 XSL 参数，我们需要创建自己的 [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) 并在 [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) 中设置为属性。以下代码片段展示了如何使用上述示例文件的该类。

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

如果您使用的是 21.7 之前的版本，请使用以下技术：

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

      //创建自己的 XsltArgumentList
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

## 基于 Aspose.PDF XML Schema 生成 PDF 文档

另一种从 XML 创建 PDF 文档的方法是使用 Aspose.PDF XML Schema。使用此图表，您可以像在 HTML 中使用表格布局一样描述页面布局。让我们更详细地考虑此方法的工作原理。

### 定义页面

让我们定义默认参数的页面。我们的页面将具有 A4 页面大小，并且只包含一段文本。

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

要生成 PDF 文档，我们将使用 [BindXml](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/bindxml/index) 方法。

```csharp
private static void Example_XML_to_PDF()
{
    var _dataDir = @"C:\tmp\";
    var pdfDocument = new Aspose.Pdf.Document();
    pdfDocument.BindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```

要定义新的页面大小，我们应该添加一个 `PageInfo` 元素。在下面的示例中，我们设置了 A5 页面大小和边距 25mm 和 10mm。

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

### 在 XML 文件中添加 HtmlFragment 元素

由于 HTML 包含类似于 XML 的标签，因此当您在任何 XML 标签内编写 HTML 时，解析器将其视为 XML 标记，并且它们不能被识别为 XML 标签。 问题可以通过在 XML 中使用 "CDATA" 部分来解决。CDATA 部分包含的文本不会被解析器解析，换句话说，它不被视为 XML 标记。以下示例 XML 模板展示了如何通过使用 CDATA 在 XML 标记中添加 HtmlFragment。

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

### 在 XML 文件中添加表格元素

元素 `Table`、`Row`、`Cell` 用于描述表格。以下代码段展示了如何使用一个简单的表格。在此示例中，某些单元格具有 `Alignment` 属性，并且该属性具有数值：

1. 左对齐
1. 居中对齐
1. 右对齐
1. 两端对齐。文本将同时对齐到左边距和右边距。 完全对齐。类似于“对齐”模式，除了在“对齐”模式下最后一行仅为左对齐，而在“完全对齐”模式下所有行将左右对齐。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">绿镇到蓝山路线的时间表</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | 绿镇 → 蓝山</TextSegment>
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
            <TextSegment>出发</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>到达</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>工作日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>船只</TextSegment>
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
            <TextSegment>周一至周六</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>巨星</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>巨星</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>周一至周五，周日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>巨星</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```
表格用于文档布局。例如，我们可以自定义页面页眉。在这种情况下，表格用于将页眉分为两列。

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
                        <TextSegment>日期: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>页 $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">格林镇-蓝堡路线时刻表</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | 格林镇 → 蓝堡</TextSegment>
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
            <TextSegment>出发</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>到达</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>工作日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>船只</TextSegment>
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
            <TextSegment>周一至周六</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>超级明星</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>超级明星</TextSegment>
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
            <TextSegment>每天</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>星号</TextSegment>
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
            <TextSegment>周一至周五，周日</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>超级明星</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```

### 动态更新内容

BindXML() 方法提供了加载 XML 文件内容的功能，并且可以使用 Document.save() 方法将输出保存为 PDF 格式。然而，在转换过程中，我们还可以访问 XML 内部的各个元素，并将 XML 用作模板。以下代码片段展示了从 XML 文件访问 TextSegments 的步骤。

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
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 实例化 Document 对象
Document doc = new Document();
// 绑定源 XML 文件
doc.BindXml( dataDir + "log.xml");
// 从 XML 获取页面对象的引用
Page page = (Page)doc.GetObjectById("mainSection");
// 获取 ID 为 boldHtml 的第一个 TextSegment 的引用
TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
// 获取 ID 为 strongHtml 的第二个 TextSegment 的引用
segment = (TextSegment)doc.GetObjectById("strongHtml");
// 保存结果 PDF 文件
doc.Save(dataDir + "XMLToPDF_out.pdf");
```

### 向页面添加图形元素

我们可以向 XML 文档添加其他附加元素：图像或图形对象。以下代码片段显示了如何将这些元素添加到文档中

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### 在将 XML 转换为 PDF 时设置图像路径

以下 XML 模板中包含一个 ID 为 "testImg" 的 `<Image>` 标签。如果您希望从代码中设置图像路径，可以在转换过程中从 XML 模板中访问 Image 元素，并将路径设置为您想要的图像地址。

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

将图像路径设置在XML模板中的代码如下：

```csharp
// 文档目录的路径。
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
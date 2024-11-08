---
title: XMLからPDFを生成
linktitle: XMLからPDFを生成
type: docs
weight: 10
url: /ja/cpp/generate-pdf-from-xml
description: Aspose.PDF for C++は、入力XMLファイルが必要なPDFドキュメントにXMLファイルを変換するためのいくつかの方法を提供します。
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XMLドキュメントからPDFドキュメントを生成することは簡単な作業ではありません。XMLドキュメントは異なるコンテンツを記述できるため、Aspose.PDF for C++はXMLドキュメントに基づいてPDFを生成するためのいくつかの方法を提供しています。

- XSLT変換を使用
- XSL-FO（XSLフォーマットオブジェクト）マークアップを使用
- 独自のAspose.PDF XMLスキーマを使用

## XSLT変換を使用してPDFドキュメントを生成

XSL（拡張スタイルシート言語）は、XMLドキュメントを他のXMLドキュメントまたはHTMLに変換するためのスタイリング言語です。この場合、XMLをHTMLに変換し、その後HTMLデータに基づいてPDFを作成することができます。

単純なCDカタログを含むXMLファイルがあると仮定します（下記参照）。

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

このファイルをPDFに変換するには、HTMLレイアウトを持つXSLを作成する必要があります。データをテーブルにレンダリングしましょう。これを手伝ってくれるXSLファイルは次のようになるかもしれません：

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

したがって、XMLを変換し、PDFドキュメントにロードする必要があります。 以下の例はこの方法を示しています:

```cpp
void WorkingWithXML::ExampleXSLTtoPDF()
{
 String _dataDir("C:\\Samples\\");

 auto XmlContent = System::IO::File::ReadAllText(u"XMLFile1.xml");
 auto XsltContent = System::IO::File::ReadAllText(u"XSLTFile1.xslt");

 auto options = MakeObject<Aspose::Pdf::HtmlLoadOptions>();
 // ページサイズをA5に設定
 options->get_PageInfo()->set_Height(595);
 options->get_PageInfo()->set_Width(420);
 auto pdfDocument = MakeObject<Aspose::Pdf::Document>(TransformXmltoHtml(XmlContent, XsltContent), options);
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}

System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString)
{
 auto transform = MakeObject<System::Xml::Xsl::XslCompiledTransform>();

 auto reader = System::Xml::XmlReader::Create(MakeObject<System::IO::StringReader>(xsltString));
 transform->Load(reader);

 auto memoryStream = MakeObject<System::IO::MemoryStream>();
 auto results = System::Xml::XmlWriter::Create(memoryStream);

 auto reader2 = System::Xml::XmlReader::Create(MakeObject<System::IO::StringReader>(inputXml));

 transform->Transform(reader2,nullptr,results);

 memoryStream->set_Position (0);
 return memoryStream;
}
```
## XSL-FOマークアップを使用してPDFドキュメントを生成する

XSL-FOは、XMLデータの画面、紙、またはその他のメディアへの出力用フォーマットを記述するXMLベースのマークアップ言語です。Aspose.PDFには、XSL-FOマークアップを適用してPDFドキュメントを取得するための特別なクラスがあります。

例を見てみましょう。以下は、従業員のサンプルデータを持つXMLファイルです。

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

Aspose.PDFには、XSL-FO変換を適用するための特別な[XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/)クラスがあります。
以下のスニペットは、上記で説明したサンプルファイルとこのクラスを使用する方法を示しています。

```cpp
void WorkingWithXML::Example_XSLFO_to_PDF()
{
 String _dataDir("C:\\Samples\\");
 // XslFoLoadOptionオブジェクトをインスタンス化
 auto options = MakeObject<Aspose::Pdf::XslFoLoadOptions>(u"employees.xslt");
 // Documentオブジェクトを作成
 auto pdfDocument = MakeObject<Aspose::Pdf::Document>(u"employees.xml", options);
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

### XSL-FOマークアップとXSLパラメータを使用したPDFドキュメントの生成

時々、[XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param)を使用する必要があります。`<xsl:param>`要素は、名前とオプションでそのパラメータのデフォルト値によってパラメータを確立します。

前のケースと同じ例を取り上げましょうが、少し変更を加えます（パラメータの追加）。 The XMLファイルに含まれるサンプルデータはそのままにしておきますが、XSL-FO マークアップファイルにパラメータを追加します: `<xsl:param name="isBoldName"></xsl:param>` そしてそれを `Name` 列に適用します。
XSLパラメータを追加するには、独自の 'XsltArgumentList' を作成し、[XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/) のプロパティとして設定する必要があります。以下のスニペットは、上記で説明したサンプルファイルを使用する方法を示しています。

```cpp
void WorkingWithXML::Example_XSLFO_to_PDF_Param_21_7()
{
 String _dataDir("C:\\Samples\\");
 String xmlInputFile(_dataDir + u"employees.xml");
 String xsltInputFile(_dataDir + u"employees.xslt");
 String outputFile(_dataDir + u"out.pdf");

 auto options = MakeObject<Aspose::Pdf::XslFoLoadOptions>(xsltInputFile);

 options->set_XsltArgumentList(MakeObject<System::Xml::Xsl::XsltArgumentList>());
 auto value = System::ObjectExt::Box(System::String(u"yes"));
 options->get_XsltArgumentList()->AddParam(u"isBoldName", u"", value);

 auto document = MakeObject<Document>(xmlInputFile, options);
 document->Save(outputFile);
}
```

## Aspose.PDF XML スキーマに基づいてPDFドキュメントを生成する

XMLからPDFドキュメントを作成する別の方法は、Aspose.PDF XMLスキーマを使用することです。 この図を使用すると、HTMLでテーブルレイアウトを使用するのと同じようにページレイアウトを説明できます。この方法の作業をより詳細に考察しましょう。

### ページの定義

デフォルトのパラメータでページを定義しましょう。私たちのページはA4サイズで、1つのテキスト片のみを含みます。

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

PDFドキュメントを生成するために、BindXml() メソッドを使用します。

```cpp
void WorkingWithXML::Example_XML_to_PDF()
{
 String _dataDir("C:\\Samples\\");

 auto pdfDocument = MakeObject<Document>();
 pdfDocument->BindXml(_dataDir + u"aspose_pdf_demo.xml");
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

新しいページサイズを定義するには、`PageInfo` 要素を追加する必要があります。 以下の例では、A5のページサイズと余白を25mmと10mmに設定しました。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="true" Height="595" Width="420">
      <Margin Top="70.8661" Bottom="70.8661" Left="28.3465" Right="28.3465" />
    </PageInfo>
    <TextFragment>
      <TextSegment>ロレム・イプサム・ドロール・シット・アメット、コンセクテトゥア・アディピシシング・エリット。ヌラ・オディオ・ロレム、ルクツス・イン・ロレム・ヴィタエ、アクムサン・センペル・レクトゥス。クラス・ア・アウクター・レオ、エト・ティンキュンディト・ラクス。</TextSegment>
    </TextFragment>
  </Page>
</Document>
```

### XMLファイルにHtmlFragment要素を追加する

HTMLにはXMLに似たタグが含まれているため、任意のXMLタグ内にHTMLを書き込むと、パーサーはそれをXMLマークアップとして扱い、XMLタグとして認識することはできません。 問題は、XMLで "CDATA" セクションを使用することで克服できます。CDATA セクションには、パーサーによって解析されないテキストが含まれています。言い換えれば、XML マークアップとして扱われません。以下のサンプル XML テンプレートは、CDATA を使用して XML マークアップ内に HtmlFragment を追加する方法を示しています。

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

### XMLファイルにテーブル要素を追加

要素 `Table`、`Row`、`Cell` はテーブルを説明するために使用されます。以下のスニペットは、単純なテーブルの使用法を示しています。この例では、いくつかのセルが `Alignment` 属性を持ち、この属性には数値の値があります：

1. 左揃え
1. 中央揃え
1. 右揃え
1. 両端揃え。テキストは左右の余白に揃えられます。
1. 両端揃え。'Justify'配置と似ていますが、'Justify'モードでは最後の行のみが左揃えになりますが、'FullJustify'モードではすべての行が左右に揃えられます。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">GREENTOWN-BLUEBERGルートの時刻表</h1>
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
Tablesはドキュメントのレイアウトに使用されます。例えば、ページヘッダーをカスタマイズすることができます。この場合、ヘッダーを2つの列に分割するためにテーブルが使用されました。

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
        <h1 style="font-family:Tahoma; font-size:16pt;">GREENTOWN-BLUEBERGルートの時刻表</h1>
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

### コンテンツを動的に更新する

BindXML() メソッドは、XML ファイルの内容をロードする機能を提供し、Document.save() メソッドを使用して PDF 形式で出力を保存できます。ただし、変換中に XML 内の個々の要素にアクセスし、XML をテンプレートとして使用することもできます。次のコード スニペットは、XML ファイルから TextSegments にアクセスする手順を示しています。

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

```cpp
void WorkingWithXML::UpdatingontentDynamically() {

 String _dataDir("C:\\Samples\\");

 // Document オブジェクトをインスタンス化する
 auto doc = MakeObject<Document>();
 // ソース XML ファイルをバインドする
 doc->BindXml(_dataDir + u"log.xml");
 // XML からページ オブジェクトの参照を取得する
 auto page = System::DynamicCast<Page>(doc->GetObjectById(u"mainSection"));
 // ID boldHtml を持つ最初の TextSegment の参照を取得する
 auto segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"boldHtml"));
 // ID strongHtml を持つ2番目の TextSegment の参照を取得する
 segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"strongHtml"));
 // 結果の PDF ファイルを保存する
 doc->Save(_dataDir + u"XMLToPDF_out.pdf");
}
```

### ページにグラフィック要素を追加する

XMLドキュメントに他の追加要素を加えることができます: ImageまたはGraphオブジェクト。以下のスニペットは、これらの要素をドキュメントに追加する方法を示しています。

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### XMLをPDFに変換する際の画像パスの設定

以下のXMLテンプレートには、ID「testImg」を持つ`<Image>`タグが含まれています。コードから画像パスを設定したい場合、変換プロセス中にXMLテンプレートからImage要素にアクセスし、画像の希望するアドレスにパスを設定することができます。

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

コードをXMLテンプレートで画像パスを設定する方法は以下の通りです：

```cpp
void WorkingWithXML::UpdatingontentDynamically2() {

 String _dataDir("C:\\Samples\\");
 String inFile = _dataDir + u"aspose-logo.jpg";
 String outFile = _dataDir + u"output_out.pdf";

 // Documentオブジェクトをインスタンス化する
 auto doc = MakeObject<Document>();
 // ソースXMLファイルをバインドする
 doc->BindXml(_dataDir + u"input.xml");

 auto image = System::DynamicCast<Image>(doc->GetObjectById(u"testImg"));

 image->set_File(inFile);
 doc->Save(outFile);
}
```
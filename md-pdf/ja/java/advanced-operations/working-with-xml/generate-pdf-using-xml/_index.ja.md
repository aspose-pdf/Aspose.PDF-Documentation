---
title: XMLからPDFを生成する
linktitle: XMLからPDFを生成する
type: docs
weight: 10
url: /java/generate-pdf-from-xml
description: Aspose.PDF for Javaは、入力XMLファイルがAspose.PDF for Java Schemaに従っていることを要求し、XMLファイルをPDFドキュメントに変換する機能を提供します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XMLドキュメントからPDFドキュメントを生成することは簡単な作業ではありません。なぜなら、XMLドキュメントはさまざまなコンテンツを説明できるからです。Aspose.PDF for Javaは、XMLドキュメントに基づいてPDFを生成するいくつかの方法を提供しています:

- XSLT変換を使用
- XSL-FO (XSL Formatting Objects) マークアップを使用
- 独自のAspose.PDF XML Schemaを使用

## XSLT変換を使用してPDFドキュメントを生成する

XSL (eXtensible Stylesheet Language) は、XMLドキュメントを他のXMLドキュメントやHTMLに変換するためのスタイリング言語です。この場合、XMLをHTMLに変換し、そのHTMLデータに基づいてPDFを作成することができます。

以下に、シンプルなCDカタログを含むXMLファイルの例を示します。

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


このファイルをPDFに変換するには、HTMLレイアウトを持つXSLを作成する必要があります。データをテーブルにレンダリングしましょう。これを実現するためのXSLファイルは次のようになります:

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

したがって、XMLを変換してPDFドキュメントに読み込む必要があります。
 次の例はこの方法を示しています：

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

## XSL-FOマークアップを使用したPDFドキュメントの生成

XSL-FOは、XMLデータのフォーマットをスクリーン、紙、または他のメディアに出力するためのXMLベースのマークアップ言語です。Aspose.PDFには、XSL-FOマークアップを適用してPDFドキュメントを取得するための特別なクラスがあります。

例を見てみましょう。こちらは従業員のサンプルデータを含むXMLファイルです。

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

従業員のデータをテーブルに変換するための、もう一つのファイルであるXSL-FOマークアップファイルを作成しましょう。

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


Aspose.PDFには特別な[XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XslFoLoadOptions)クラスがあり、XSL-FO変換を適用することができます。以下のスニペットは、上記のサンプルファイルでこのクラスを使用する方法を示しています。

```java
public static void Example_XSLFO_to_PDF() {
    // XslFoLoadOptionオブジェクトをインスタンス化
    com.aspose.pdf.XslFoLoadOptions options = new com.aspose.pdf.XslFoLoadOptions(_dataDir+"employees.xslt");
    // Documentオブジェクトを作成
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(_dataDir+"employees.xml", options);
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

## Aspose.PDF XML Schemaに基づくPDFドキュメントの生成

XMLからPDFドキュメントを作成するもう一つの方法は、Aspose.PDF XML Schemaを使用することです。この図を使用すると、HTMLのテーブルレイアウトを使用するのと同じ方法でページレイアウトを記述できます。この方法の動作をより詳細に考えてみましょう。

### ページの定義

デフォルトのパラメータでページを定義してみましょう。
 私たちのページはA4サイズで、1つのテキストのみを含みます。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <TextFragment>
      <TextSegment>ロレム・イプサム・ドロール・シット・アメット、コンセクトゥル・アディピシング・エリット。ヌッラ・オーディオ・ロレム、ルクトゥス・イン・ロレム・ヴィタエ、アクムサン・センペル・レクトゥス。クラス・ア・アウクトル・レオ、エト・ティンキトゥンド・ラカス。</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

PDFドキュメントを生成するために、[bindXml](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#bindXml--) メソッドを使用します。

```java
public static void Example_XML_to_PDF() {
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    pdfDocument.bindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

新しいページサイズを定義するために、`PageInfo` 要素を追加する必要があります。以下の例では、A5ページサイズとマージンを25mmと10mmに設定しました。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="true" Height="595" Width="420">
      <Margin Top="70.8661" Bottom="70.8661" Left="28.3465" Right="28.3465" />           
    </PageInfo>
    <TextFragment>
      <TextSegment>ロレム・イプサム・ドロール・シット・アメット、コンセクトゥル・アディピシング・エリット。ヌッラ・オーディオ・ロレム、ルクトゥス・イン・ロレム・ヴィタエ、アクムサン・センペル・レクトゥス。クラス・ア・アウクトル・レオ、エト・ティンキトゥンド・ラカス。</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

### XMLファイルにHtmlFragment要素を追加する

HTMLはXMLに似たタグを含むため、XMLタグ内にHTMLを書き込むと、パーサーはそれをXMLマークアップとして扱い、単にXMLタグとして認識されません。この問題は、XMLで「CDATA」セクションを使用することで解決できます。CDATAセクションには、パーサーによって解析されないテキストが含まれており、言い換えれば、XMLマークアップとして扱われません。以下のサンプルXMLテンプレートは、CDATAを使用してXMLマークアップ内にHtmlFragmentを追加する方法を示しています。

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">これはHTML文字列です。</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### XMLファイルにTable要素を追加する

要素 `Table`、`Row`、`Cell` はテーブルを記述するために使用されます。次のスニペットは、シンプルなテーブルを使用する方法を示しています。この例では、一部のセルが `Alignment` 属性を持ち、この属性には数値が設定されています。

1. 左揃え
1. 中央揃え
1. 右揃え
1. 両端揃え。テキストは左端と右端の両方に揃えられます。
1. 完全両端揃え。「両端揃え」モードでは最後の行は左揃えのみですが、「完全両端揃え」モードではすべての行が左端と右端に揃えられます。

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
            <TextSegment>月-金, 日</TextSegment>
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


ドキュメントのレイアウトにはテーブルが使用されます。例えば、ページのヘッダーをカスタマイズできます。この場合、ヘッダーを2つの列に分けるためにテーブルが使用されました。

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


### コンテンツの動的更新

BindXML() メソッドは XML ファイルの内容をロードする機能を提供し、Document.save() メソッドを使用して出力を PDF 形式で保存できます。ただし、変換中に XML 内の個々の要素にアクセスし、XML をテンプレートとして使用することもできます。以下のコードスニペットは、XML ファイルから TextSegments にアクセスする手順を示しています。

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
    // Document オブジェクトをインスタンス化
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    // ソース XML ファイルをバインド
    pdfDocument.bindXml(_dataDir + "log.xml");
    
    // ID が boldHtml の最初の TextSegment の参照を取得
    TextSegment segment = (TextSegment)pdfDocument.getObjectById("boldHtml");
    segment.setText("Demo 1");
    // ID が strongHtml の2番目の TextSegment の参照を取得
    segment = (TextSegment)pdfDocument.getObjectById("strongHtml");
    segment.setText("Demo 2");
    // 結果の PDF ファイルを保存
    pdfDocument.save(_dataDir + "XMLToPDF_out.pdf");
}
```


### ページにグラフィック要素を追加する

XMLドキュメントに他の追加要素を追加できます：イメージまたはグラフオブジェクト。以下のスニペットは、これらの要素をドキュメントに追加する方法を示しています。

```xml
<Graph Width="20" Height="20">    
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### XMLをPDFに変換する際の画像パスの設定

以下のXMLテンプレートには、ID "testImg"を持つ`<Image>`タグが含まれています。コードから画像パスを設定したい場合、変換プロセス中にXMLテンプレートのImage要素にアクセスして、画像の希望するアドレスへのパスを設定できます。

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
        <!--ロゴ-->
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


Code to set image path in XML template is as follows:

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

XMLテンプレートで画像パスを設定するコードは以下の通りです。
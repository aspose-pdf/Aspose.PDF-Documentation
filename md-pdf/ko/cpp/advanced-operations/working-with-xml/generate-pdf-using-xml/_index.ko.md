---
title: XML에서 PDF 생성
linktitle: XML에서 PDF 생성
type: docs
weight: 10
url: /cpp/generate-pdf-from-xml
description: Aspose.PDF for C++는 입력 XML 파일을 필요로 하여 XML 파일을 PDF 문서로 변환하는 여러 가지 방법을 제공합니다.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XML 문서에서 PDF 문서를 생성하는 것은 간단한 작업이 아닙니다. XML 문서는 다양한 콘텐츠를 설명할 수 있기 때문에 Aspose.PDF for C++는 XML 문서를 기반으로 PDF를 생성하는 여러 가지 방법을 제공합니다:

- XSLT 변환을 사용하여
- XSL-FO (XSL Formatting Objects) 마크업을 사용하여
- 자체 Aspose.PDF XML 스키마를 사용하여

## XSLT 변환을 사용하여 PDF 문서 생성

XSL (eXtensible Stylesheet Language)은 XML 문서를 다른 XML 문서나 HTML로 변환하기 위한 스타일링 언어입니다. 우리의 경우 XML을 HTML로 변환한 다음 HTML 데이터를 기반으로 PDF를 생성할 수 있습니다.

간단한 CD 카탈로그가 있는 XML 파일을 가정합니다 (아래 참조).

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

To convert this file to PDF we should create an XSL with HTML layout. Let's render our data in table. The XSL file that will help us do this might look something like this:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>나의 CD 컬렉션</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">제목</th>
            <th style="text-align:left">아티스트</th>
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

So, we need to transform XML and load into PDF document. 다음 예제는 이 방법을 보여줍니다:

```cpp
void WorkingWithXML::ExampleXSLTtoPDF()
{
 String _dataDir("C:\\Samples\\");

 auto XmlContent = System::IO::File::ReadAllText(u"XMLFile1.xml");
 auto XsltContent = System::IO::File::ReadAllText(u"XSLTFile1.xslt");

 auto options = MakeObject<Aspose::Pdf::HtmlLoadOptions>();
 // 페이지 크기를 A5로 설정
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
## XSL-FO 마크업을 사용하여 PDF 문서 생성

XSL-FO는 XML 데이터를 화면, 종이 또는 기타 매체에 출력하기 위한 서식을 설명하는 XML 기반 마크업 언어입니다. Aspose.PDF는 XSL-FO 마크업을 적용하고 PDF 문서를 얻을 수 있는 특별한 클래스를 제공합니다.

예를 들어 보겠습니다. 다음은 직원의 샘플 데이터가 포함된 XML 파일입니다.

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

직원 데이터를 테이블로 변환하기 위한 또 다른 파일, XSL-FO 마크업 파일을 만들어 보겠습니다.

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

Aspose.PDF에는 XSL-FO 변환을 적용할 수 있는 특별한 [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/) 클래스가 있습니다. 다음 코드는 위에서 설명한 샘플 파일과 함께 이 클래스를 사용하는 방법을 보여줍니다.

```cpp
void WorkingWithXML::Example_XSLFO_to_PDF()
{
 String _dataDir("C:\\Samples\\");
 // XslFoLoadOption 객체 인스턴스화
 auto options = MakeObject<Aspose::Pdf::XslFoLoadOptions>(u"employees.xslt");
 // 문서 객체 생성
 auto pdfDocument = MakeObject<Aspose::Pdf::Document>(u"employees.xml", options);
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

### XSL-FO 마크업 및 XSL 매개변수를 사용하여 PDF 문서 생성

때때로 우리는 [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param)을 사용해야 합니다. `<xsl:param>` 요소는 이름과 선택적으로 해당 매개변수의 기본값으로 매개변수를 설정합니다.

이전 경우와 동일한 예제를 사용하되, 약간의 변경 사항(매개변수 추가)을 적용해 봅시다. 샘플 데이터가 있는 XML 파일은 변경되지 않습니다, ...

```xml
<?xml version="1.0" encoding="utf-8" ?>
<employees>
    <companyname>ABC Inc.</companyname>
    <employee>
        <id>101</id>
        <name>앤드류</name>
        <designation>매니저</designation>
    </employee>

    <employee>
        <id>102</id>
        <name>에두아르드</name>
        <designation>임원</designation>
    </employee>

    <employee>
        <id>103</id>
        <name>피터</name>
        <designation>임원</designation>
    </employee>
</employees>
```

하지만 XSL-FO 마크업 파일에는 매개변수를 추가할 것입니다: `<xsl:param name="isBoldName"></xsl:param>`를 추가하고 `Name` 열에 적용할 것입니다.

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
      회사 이름: <xsl:value-of select="companyname"/>
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
XSL 매개변수를 추가하려면 자체 'XsltArgumentList'를 생성하고 [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/)의 속성으로 설정해야 합니다. 다음 코드는 위에서 설명한 샘플 파일을 사용하여 이 클래스를 사용하는 방법을 보여줍니다.

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

## Aspose.PDF XML Schema 기반으로 PDF 문서 생성하기

XML에서 PDF 문서를 생성하는 또 다른 방법은 Aspose.PDF XML Schema를 사용하는 것입니다. 이 다이어그램을 사용하여 HTML에서 테이블 레이아웃을 사용하는 것처럼 페이지 레이아웃을 설명할 수 있습니다. 이 방법의 작동을 좀 더 자세히 살펴보겠습니다.

### 페이지 정의

기본 매개변수로 페이지를 정의해 봅시다. 우리의 페이지는 A4 페이지 크기를 가지며 단 하나의 텍스트 조각만 포함할 것입니다.

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

PDF 문서를 생성하기 위해 BindXml() 메서드를 사용할 것입니다.

```cpp
void WorkingWithXML::Example_XML_to_PDF()
{
 String _dataDir("C:\\Samples\\");

 auto pdfDocument = MakeObject<Document>();
 pdfDocument->BindXml(_dataDir + u"aspose_pdf_demo.xml");
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

새로운 페이지 크기를 정의하기 위해 `PageInfo` 요소를 추가해야 합니다. 다음 예제에서 우리는 A5 페이지 크기와 여백을 25mm와 10mm로 설정했습니다.

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

### XML 파일에 HtmlFragment 요소 추가

HTML은 XML과 유사한 태그를 포함하고 있기 때문에 XML 태그 내에 HTML을 작성하면 파서가 이를 XML 마크업으로 처리하며 단순히 XML 태그로 인식할 수 없습니다. 문제는 XML에서 "CDATA" 섹션을 사용하여 해결할 수 있습니다. CDATA 섹션은 파서에 의해 구문 분석되지 않는 텍스트를 포함하고 있습니다. 즉, XML 마크업으로 처리되지 않습니다. 다음 샘플 XML 템플릿은 CDATA를 사용하여 XML 마크업 내에 HtmlFragment를 추가하는 방법을 보여줍니다.

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

### XML 파일에 Table 요소 추가

`Table`, `Row`, `Cell` 요소는 테이블을 설명하는 데 사용됩니다. 다음 스니펫은 간단한 테이블을 사용하는 방법을 보여줍니다. 이 예제에서는 일부 셀이 `Alignment` 속성을 가지고 있으며 이 속성은 숫자 값을 가집니다:

1. 왼쪽 정렬
1. 가운데 정렬
1. 오른쪽 정렬
1. 양쪽 정렬. 텍스트는 왼쪽 및 오른쪽 여백에 맞춰 정렬됩니다.
1. Full justify. 'Justify' 정렬과 유사하지만, 'Justify' 모드에서는 마지막 줄만 왼쪽 정렬되고, 'FullJustify' 모드에서는 모든 줄이 왼쪽 및 오른쪽 정렬됩니다.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">GREENTOWN-BLUEBERG 노선의 시간표</h1>
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
            <TextSegment>출발</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>도착</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>요일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>선박</TextSegment>
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
            <TextSegment>월-토</TextSegment>
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
            <TextSegment>매일</TextSegment>
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
            <TextSegment>매일</TextSegment>
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
            <TextSegment>매일</TextSegment>
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
            <TextSegment>매일</TextSegment>
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
            <TextSegment>월-금, 일</TextSegment>
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
문서의 레이아웃을 위해 표가 사용됩니다. 예를 들어, 페이지 헤더를 사용자 정의할 수 있습니다. 이 경우, 표는 헤더를 2개의 열로 나누는 데 사용되었습니다.

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
                        <TextSegment>날짜: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>페이지 $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">그린타운-블루버그 노선의 시간표</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | 그린타운 → 블루버그</TextSegment>
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
            <TextSegment>출발</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>도착</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>평일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>선박</TextSegment>
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
            <TextSegment>월-토</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>스타</TextSegment>
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
            <TextSegment>매일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>메가스타</TextSegment>
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
            <TextSegment>매일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>스타</TextSegment>
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
            <TextSegment>매일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>메가스타</TextSegment>
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
            <TextSegment>매일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>스타</TextSegment>
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
            <TextSegment>월-금, 일</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>메가스타</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```

### 콘텐츠를 동적으로 업데이트하기

BindXML() 메서드는 XML 파일의 내용을 로드하는 기능을 제공하며 Document.save() 메서드는 PDF 형식으로 출력을 저장하는 데 사용할 수 있습니다. 그러나 변환 중에 XML 내부의 개별 요소에 액세스하고 XML을 템플릿으로 사용할 수도 있습니다. 다음 코드 스니펫은 XML 파일에서 TextSegments에 액세스하는 단계를 보여줍니다.

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

 // Document 객체 인스턴스화
 auto doc = MakeObject<Document>();
 // 소스 XML 파일 바인딩
 doc->BindXml(_dataDir + u"log.xml");
 // XML에서 페이지 객체의 참조 가져오기
 auto page = System::DynamicCast<Page>(doc->GetObjectById(u"mainSection"));
 // ID가 boldHtml인 첫 번째 TextSegment의 참조 가져오기
 auto segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"boldHtml"));
 // ID가 strongHtml인 두 번째 TextSegment의 참조 가져오기
 segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"strongHtml"));
 // 결과 PDF 파일 저장
 doc->Save(_dataDir + u"XMLToPDF_out.pdf");
}
```

### 페이지에 그래픽 요소 추가하기

우리는 XML 문서에 추가적인 요소들을 추가할 수 있습니다: 이미지 또는 그래프 객체. 다음 스니펫은 문서에 이러한 요소들을 추가하는 방법을 보여줍니다.

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### XML을 PDF로 변환할 때 이미지 경로 설정하기

다음 XML 템플릿에는 "testImg"라는 ID를 가진 `<Image>` 태그가 포함되어 있습니다. 코드에서 이미지 경로를 설정하고자 하는 경우, 변환 과정에서 XML 템플릿의 Image 요소에 접근하여 원하는 주소로 경로를 설정할 수 있습니다.

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

Code to set image path in XML template is as follows:

```cpp
void WorkingWithXML::UpdatingontentDynamically2() {

 String _dataDir("C:\\Samples\\");
 String inFile = _dataDir + u"aspose-logo.jpg";
 String outFile = _dataDir + u"output_out.pdf";

 // 문서 객체를 인스턴스화합니다.
 auto doc = MakeObject<Document>();
 // 소스 XML 파일을 바인딩합니다.
 doc->BindXml(_dataDir + u"input.xml");

 auto image = System::DynamicCast<Image>(doc->GetObjectById(u"testImg"));

 image->set_File(inFile);
 doc->Save(outFile);
}
```
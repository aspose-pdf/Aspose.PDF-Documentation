---
title: إنشاء PDF من XML
linktitle: إنشاء PDF من XML
type: docs
weight: 10
url: /java/generate-pdf-from-xml
description: توفر Aspose.PDF for Java فرصة لتحويل ملف XML إلى مستند PDF بشرط أن يتبع ملف XML المدخل مخطط Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إنشاء مستند PDF من مستند XML ليس مهمة بسيطة لأن مستند XML يمكن أن يصف محتوى مختلف Aspose.PDF for Java لديها عدة طرق لإنشاء PDF بناءً على مستند XML:

- باستخدام تحويل XSLT
- باستخدام ترميز XSL-FO (كائنات تنسيق XSL)
- باستخدام مخطط Aspose.PDF XML الخاص

## إنشاء مستند PDF باستخدام تحويل XSLT

XSL (لغة الأنماط الممتدة) هي لغة تنسيق لتحويل مستندات XML إلى مستندات XML أخرى أو HTML. في حالتنا يمكننا استخدام تحويل XML إلى HTML ثم إنشاء PDF بناءً على بيانات HTML.

افترض أن لدينا ملف XML يحتوي على كتالوج CD بسيط (انظر أدناه).

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


لتحويل هذا الملف إلى PDF يجب علينا إنشاء XSL بتنسيق HTML. لنقم بعرض بياناتنا في جدول. قد يبدو ملف XSL الذي سيساعدنا في القيام بذلك شيئًا مثل هذا:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>مجموعة الأقراص المدمجة الخاصة بي</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">العنوان</th>
            <th style="text-align:left">الفنان</th>
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

لذلك، نحتاج إلى تحويل XML وتحميله في مستند PDF.
 المثال التالي يوضح هذه الطريقة:

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

## إنشاء مستند PDF باستخدام ترميز XSL-FO

XSL-FO هو لغة ترميز تستند إلى XML تصف تنسيق بيانات XML للإخراج إلى الشاشة أو الورق أو وسائل الإعلام الأخرى. يحتوي Aspose.PDF على فئة خاصة تتيح تطبيق ترميز XSL-FO والحصول على مستند PDF.

لنأخذ مثالاً. هنا ملف XML يحتوي على بيانات نموذجية للموظفين.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<employees>
    <companyname>ABC Inc.</companyname>
    <employee>
        <id>101</id>
        <name>Andrew</name>
        <designation>مدير</designation>
    </employee>

    <employee>
        <id>102</id>
        <name>Eduard</name>
        <designation>تنفيذي</designation>
    </employee>

    <employee>
        <id>103</id>
        <name>Peter</name>
        <designation>تنفيذي</designation>
    </employee>
</employees>
```

لنقم بإنشاء ملف آخر - ملف ترميز XSL-FO لتحويل بيانات الموظفين إلى جدول.

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
                        اسم الشركة: <xsl:value-of select="companyname"/>
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
            <xsl:if test="designation = 'مدير'">
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


Aspose.PDF لديها فئة خاصة [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XslFoLoadOptions) التي تسمح بتطبيق تحويل XSL-FO. يوضح المقتطف التالي كيفية استخدام هذه الفئة مع ملفات العينة الموضحة أعلاه.

```java
public static void Example_XSLFO_to_PDF() {
    // إنشاء كائن XslFoLoadOption
    com.aspose.pdf.XslFoLoadOptions options = new com.aspose.pdf.XslFoLoadOptions(_dataDir+"employees.xslt");
    // إنشاء كائن Document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(_dataDir+"employees.xml", options);
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

## إنشاء مستند PDF استنادًا إلى مخطط Aspose.PDF XML

طريقة أخرى لإنشاء مستند PDF من XML هي استخدام مخطط Aspose.PDF XML. باستخدام هذا الرسم البياني، يمكنك وصف تخطيط الصفحة بنفس الطريقة كما لو كنت تستخدم تخطيط الجداول في HTML. لنلق نظرة على عمل هذه الطريقة بمزيد من التفصيل.

### تحديد الصفحة

لنحدد الصفحة بالمعلمات الافتراضية.
 صفحتنا ستكون بحجم A4 وستحتوي على قطعة واحدة من النص.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <TextFragment>
      <TextSegment>لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسينغ إليت. نولا أوديو لوريم، لوكتوس إن لوريم فيتاي، أكومسان سيمبر لكتوس. كراس أ أوكتور ليو، إت تينسيدنت لاكوس.</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

لإنشاء مستند PDF سنستخدم طريقة [bindXml](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#bindXml--).

```java
public static void Example_XML_to_PDF() {
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    pdfDocument.bindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

لتحديد حجم صفحة جديد يجب علينا إضافة عنصر `PageInfo`. في المثال التالي، قمنا بتعيين حجم الصفحة A5 والهوامش 25 مم و10 مم.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="true" Height="595" Width="420">
      <Margin Top="70.8661" Bottom="70.8661" Left="28.3465" Right="28.3465" />           
    </PageInfo>
    <TextFragment>
      <TextSegment>لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسينغ إليت. نولا أوديو لوريم، لوكتوس إن لوريم فيتاي، أكومسان سيمبر لكتوس. كراس أ أوكتور ليو، إت تينسيدنت لاكوس.</TextSegment>
    </TextFragment>    
  </Page>
</Document>
```

### إضافة عنصر HtmlFragment في ملف XML

نظرًا لأن HTML يحتوي على علامات مشابهة لـ XML، فعندما تكتب HTML داخل أي علامة XML، يعاملها المحلل على أنها علامات XML ولا يمكن التعرف عليها ببساطة كعلامات XML. يمكن التغلب على هذه المشكلة باستخدام قسم "CDATA" في XML. يحتوي قسم CDATA على نص لا يتم تحليله بواسطة المحلل أو بعبارة أخرى، لا يعامل كنصوص XML. يوضح قالب XML النموذجي التالي كيفية إضافة HtmlFragment داخل علامات XML باستخدام CDATA.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">هذا نص HTML.</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### إضافة عنصر Table في ملف XML

تُستخدم العناصر `Table`، `Row`، `Cell` لوصف الجداول. يوضح المقتطف التالي استخدام جدول بسيط. في هذا المثال، تحتوي بعض الخلايا على خاصية `Alignment` وهذه الخاصية لها قيمة رقمية:

1. محاذاة لليسار
1. محاذاة للوسط
1. محاذاة لليمين.
1. محاذاة مبررة. سيتم محاذاة النص على الهامشين الأيسر والأيمن.
1. محاذاة مبررة بالكامل. مشابهة لمحاذاة "مبرر"، باستثناء أن السطر الأخير سيكون محاذى فقط لليسار في وضع "مبرر"، بينما في وضع "مبرر بالكامل" ستكون جميع الأسطر محاذاة لليسار واليمين.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">الجداول الزمنية على خط جرينتاون-بلو بيرج</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | جرينتاون → بلو بيرج</TextSegment>
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
            <TextSegment>المغادرة</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>الوصول</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>يوم الأسبوع</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>السفينة</TextSegment>
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
            <TextSegment>الإثنين-السبت</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>نجم</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>نجم</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>نجم</TextSegment>
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
            <TextSegment>الإثنين-الجمعة، الأحد</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```


Tables تستخدم لتنسيق المستندات. على سبيل المثال، يمكننا تخصيص رأس الصفحة. في هذه الحالة، تم استخدام الجدول لتقسيم الرأس إلى عمودين.

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
                        <TextSegment>التاريخ: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>صفحة $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">الجداول الزمنية على خط جرينتاون-بلوبيرج</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | جرينتاون → بلوبيرج</TextSegment>
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
            <TextSegment>المغادرة</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>الوصول</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>اليوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>السفينة</TextSegment>
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
            <TextSegment>الإثنين-السبت</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
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
            <TextSegment>كل يوم</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ستار</TextSegment>
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
            <TextSegment>الإثنين-الجمعة، الأحد</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>ميجاستار</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```


### تحديث المحتوى ديناميكيًا

يوفر أسلوب BindXML() ميزة تحميل محتويات ملف XML ويمكن استخدام أسلوب Document.save() لحفظ الناتج بتنسيق PDF. ومع ذلك، أثناء التحويل، يمكننا أيضًا الوصول إلى العناصر الفردية داخل XML واستخدام XML كقالب. يظهر مقتطف الشيفرة التالي الخطوات للوصول إلى TextSegments من ملف XML.

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
    // إنشاء كائن مستند
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    // ربط ملف XML المصدر
    pdfDocument.bindXml(_dataDir + "log.xml");
    
    // الحصول على مرجع لأول TextSegment مع المعرف boldHtml
    TextSegment segment = (TextSegment)pdfDocument.getObjectById("boldHtml");
    segment.setText("Demo 1");
    // الحصول على مرجع للـ TextSegment الثاني مع المعرف strongHtml
    segment = (TextSegment)pdfDocument.getObjectById("strongHtml");
    segment.setText("Demo 2");
    // حفظ ملف PDF الناتج
    pdfDocument.save(_dataDir + "XMLToPDF_out.pdf");
}
```


### إضافة عناصر رسومية إلى الصفحة

يمكننا إضافة عناصر إضافية أخرى إلى مستند XML: كائنات صورة أو رسم بياني. يُظهر المقتطف التالي كيفية إضافة هذه العناصر إلى المستند

```xml
<Graph Width="20" Height="20">    
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### تعيين مسار الصورة أثناء تحويل XML إلى PDF

يحتوي قالب XML التالي على علامة `<Image>` مع معرف "testImg". في حالة رغبتك في تعيين مسار الصورة من الكود الخاص بك، يمكنك الوصول إلى عنصر الصورة من قالب XML أثناء عملية التحويل وتعيين المسار إلى العنوان المطلوب للصورة.

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


Code لضبط مسار الصورة في قالب XML هو كما يلي:

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
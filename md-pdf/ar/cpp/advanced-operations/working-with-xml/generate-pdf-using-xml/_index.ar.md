---
title: إنشاء PDF من XML
linktitle: إنشاء PDF من XML
type: docs
weight: 10
url: /cpp/generate-pdf-from-xml
description: يوفر Aspose.PDF for C++ عدة طرق لتحويل ملف XML إلى مستند PDF يتطلب أن يكون ملف XML المدخل.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إنشاء مستند PDF من مستند XML ليس مهمة بسيطة لأن مستند XML يمكن أن يصف محتوى مختلف. يحتوي Aspose.PDF for C++ على عدة طرق لإنشاء PDF بناءً على مستند XML:

- باستخدام تحويل XSLT
- باستخدام XSL-FO (كائنات تنسيق XSL) ترميز
- باستخدام مخطط XML الخاص بـ Aspose.PDF

## إنشاء مستند PDF باستخدام تحويل XSLT

 XSL (لغة الأنماط القابلة للامتداد) هي لغة تنسيق لتحويل مستندات XML إلى مستندات XML أخرى أو HTML. في حالتنا، يمكننا استخدام تحويل XML إلى HTML ثم إنشاء PDF بناءً على بيانات HTML.

 نفترض أن لدينا ملف XML مع كتالوج CD بسيط (انظر أدناه).

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

لتحويل هذا الملف إلى PDF يجب علينا إنشاء XSL بتنسيق HTML. دعنا نقوم بعرض بياناتنا في جدول. ملف XSL الذي سيساعدنا في القيام بذلك قد يبدو كالتالي:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>مجموعتي من الأقراص المضغوطة</h2>
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

لذلك، نحن بحاجة إلى تحويل XML وتحميله في مستند PDF. المثال التالي يوضح هذه الطريقة:

```cpp
void WorkingWithXML::ExampleXSLTtoPDF()
{
 String _dataDir("C:\\Samples\\");

 auto XmlContent = System::IO::File::ReadAllText(u"XMLFile1.xml");
 auto XsltContent = System::IO::File::ReadAllText(u"XSLTFile1.xslt");

 auto options = MakeObject<Aspose::Pdf::HtmlLoadOptions>();
 // ضبط حجم الصفحة إلى A5
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
## توليد مستند PDF باستخدام تعليمات XSL-FO

XSL-FO هي لغة ترميز تعتمد على XML لوصف تنسيق بيانات XML للإخراج على الشاشة أو الورق أو وسائل الإعلام الأخرى. يحتوي Aspose.PDF على فئة خاصة تسمح بتطبيق تعليمات XSL-FO والحصول على مستند PDF.

لنأخذ مثالاً. هنا ملف XML يحتوي على بيانات نموذجية للموظفين.

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

لنقم بإنشاء ملف آخر - ملف تعليمات XSL-FO لتحويل بيانات الموظفين إلى جدول.

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

Aspose.PDF يحتوي على فئة خاصة [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/) التي تسمح بتطبيق تحويل XSL-FO. يُظهر المقتطف التالي كيفية استخدام هذه الفئة مع الملفات النموذجية المذكورة أعلاه.

```cpp
void WorkingWithXML::Example_XSLFO_to_PDF()
{
 String _dataDir("C:\\Samples\\");
 // Instantiate XslFoLoadOption object
 auto options = MakeObject<Aspose::Pdf::XslFoLoadOptions>(u"employees.xslt");
 // Create Document object
 auto pdfDocument = MakeObject<Aspose::Pdf::Document>(u"employees.xml", options);
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

### إنشاء مستند PDF باستخدام ترميز XSL-FO ومعلمات XSL

أحيانًا نحتاج إلى استخدام [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param). يُنشئ عنصر `<xsl:param>` معلمة بالاسم، وبشكل اختياري، قيمة افتراضية لتلك المعلمة.

لنأخذ نفس المثال كما في الحالة السابقة، ولكن مع تغييرات طفيفة (إضافة معلمات). ملف XML مع البيانات النموذجية يبقى كما هو، ...

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

ولكن في ملف ترميز XSL-FO سنضيف المعامل: `<xsl:param name="isBoldName"></xsl:param>` وسنطبقه على عمود `Name`.

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
لإضافة معلمات XSL نحتاج إلى إنشاء 'XsltArgumentList' خاص بنا وتعيينها كخاصية في [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/). يوضح المقتطف التالي كيفية استخدام هذه الفئة مع ملفات العينة الموضحة أعلاه.

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

## إنشاء مستند PDF استنادًا إلى مخطط Aspose.PDF XML

طريقة أخرى لإنشاء مستند PDF من XML هي استخدام مخطط Aspose.PDF XML. باستخدام هذا الرسم البياني، يمكنك وصف تخطيط الصفحة بنفس الطريقة كما لو كنت تستخدم تخطيط الجدول في HTML. دعونا ننظر في عمل هذه الطريقة بمزيد من التفصيل.

### تعريف الصفحة

لنقم بتعريف الصفحة بالمعايير الافتراضية. ستكون صفحتنا بحجم A4 وستحتوي على قطعة نصية واحدة فقط.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <TextFragment>
      <TextSegment>لوريم إيبسوم دولور سيت أميت، كونسيكتيتور أديبيسكينغ إيليت. نولا أوديو لوريم، لوكتوس إن لوريم فيتاي، أكومسان سيمبر ليكتوس. كراس أ أوكتور ليو، إت تينسيدنت لاكوس.</TextSegment>
    </TextFragment>
  </Page>
</Document>
```

لإنشاء مستند PDF سنستخدم طريقة BindXml().

```cpp
void WorkingWithXML::Example_XML_to_PDF()
{
 String _dataDir("C:\\Samples\\");

 auto pdfDocument = MakeObject<Document>();
 pdfDocument->BindXml(_dataDir + u"aspose_pdf_demo.xml");
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

لتعريف حجم صفحة جديد يجب علينا إضافة عنصر `PageInfo`. في المثال التالي، قمنا بتعيين حجم الصفحة A5 والهوامش 25 مم و10 مم.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="true" Height="595" Width="420">
      <Margin Top="70.8661" Bottom="70.8661" Left="28.3465" Right="28.3465" />
    </PageInfo>
    <TextFragment>
      <TextSegment>لوريم إيبسوم دولار سيت أميت، كونسيكتيتور أديبيسشينغ إليت. نولا أوديو لوريم، لوكتوس إن لوريم فيتاي، أكومسان سيمبر ليكتوس. كراس أ أوكتور ليو، إت تينسيدنت لاكوس.</TextSegment>
    </TextFragment>
  </Page>
</Document>
```

### إضافة عنصر HtmlFragment في ملف XML

نظرًا لأن HTML يحتوي على علامات مشابهة لـ XML، فعند كتابة HTML داخل أي علامة XML، يتعامل المحلل معها كعلامات XML ولا يمكن ببساطة التعرف عليها كعلامات XML. يمكن التغلب على المشكلة باستخدام قسم "CDATA" في XML. يحتوي قسم CDATA على نص غير محلل من قبل المحلل أو بعبارة أخرى، لا يُعامل كنصوص XML. يُظهر قالب XML النموذجي التالي كيفية إضافة HtmlFragment داخل نصوص XML باستخدام CDATA.

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

### إضافة عنصر جدول في ملف XML

تُستخدم العناصر `Table`، `Row`، `Cell` لوصف الجداول. يُظهر المقتطف التالي استخدام جدول بسيط. في هذا المثال، تحتوي بعض الخلايا على سمة `Alignment` وهذه السمة لها قيمة رقمية:

1. محاذاة لليسار
1. محاذاة للوسط
1. محاذاة لليمين
1. محاذاة مُبررة. سيتم محاذاة النص على الهوامش اليسرى واليمنى.
1. ضبط كامل. مشابه لمحاذاة 'ضبط'، باستثناء أن السطر الأخير سيتم محاذاته فقط لليسار في وضع 'ضبط'، بينما في وضع 'الضبط الكامل' سيتم محاذاة جميع السطور لليسار واليمين.

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
            <TextSegment>الاثنين-السبت</TextSegment>
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
            <TextSegment>الاثنين-الجمعة، الأحد</TextSegment>
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
الجداول تُستخدم لتنسيق المستندات. على سبيل المثال، يمكننا تخصيص رأس الصفحة. في هذه الحالة، تم استخدام الجدول لتقسيم الرأس إلى عمودين.

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
        <h1 style="font-family:Tahoma; font-size:16pt;">الجداول الزمنية على خط جرين تاون - بلوبرج</h1>
        ]]>
    </HtmlFragment>
    <TextFragment>
      <TextSegment>4.1.-28.3.2021 | جرين تاون → بلوبرج</TextSegment>
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
            <TextSegment>أيام الأسبوع</TextSegment>
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
            <TextSegment>ميجا ستار</TextSegment>
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
            <TextSegment>ميجا ستار</TextSegment>
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
            <TextSegment>ميجا ستار</TextSegment>
          </TextFragment>
        </Cell>
      </Row>
    </Table>
  </Page>
</Document>
```

### تحديث المحتوى ديناميكيًا

توفر طريقة BindXML() ميزة تحميل محتويات ملف XML ويمكن استخدام طريقة Document.save() لحفظ النتيجة بتنسيق PDF. ومع ذلك أثناء التحويل، يمكننا أيضًا الوصول إلى العناصر الفردية داخل XML واستخدام XML كقالب. يوضح مقتطف الشيفرة التالي الخطوات للوصول إلى TextSegments من ملف XML.

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

 // إنشاء كائن Document
 auto doc = MakeObject<Document>();
 // ربط ملف XML المصدر
 doc->BindXml(_dataDir + u"log.xml");
 // الحصول على مرجع كائن الصفحة من XML
 auto page = System::DynamicCast<Page>(doc->GetObjectById(u"mainSection"));
 // الحصول على مرجع TextSegment الأول بالمعرف boldHtml
 auto segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"boldHtml"));
 // الحصول على مرجع TextSegment الثاني بالمعرف strongHtml
 segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"strongHtml"));
 // حفظ ملف PDF الناتج
 doc->Save(_dataDir + u"XMLToPDF_out.pdf");
}
```

### إضافة عناصر رسومية إلى الصفحة

يمكننا إضافة عناصر إضافية أخرى إلى مستند XML: كائنات صورة أو رسم بياني. يُظهر المقتطف التالي كيفية إضافة تلك العناصر إلى المستند

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### تعيين مسار الصورة أثناء تحويل XML إلى PDF

يحتوي قالب XML التالي على علامة `<Image>` تحتوي على معرّف "testImg". في حال كنت ترغب في تعيين مسار الصورة من الكود الخاص بك، يمكنك الوصول إلى عنصر الصورة من قالب XML أثناء عملية التحويل وتعيين المسار إلى العنوان المطلوب للصورة.

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

كود لتعيين مسار الصورة في قالب XML هو كما يلي:

```cpp
void WorkingWithXML::UpdatingontentDynamically2() {

 String _dataDir("C:\\Samples\\");
 String inFile = _dataDir + u"aspose-logo.jpg";
 String outFile = _dataDir + u"output_out.pdf";

 // إنشاء كائن المستند
 auto doc = MakeObject<Document>();
 // ربط ملف XML المصدر
 doc->BindXml(_dataDir + u"input.xml");

 auto image = System::DynamicCast<Image>(doc->GetObjectById(u"testImg"));

 image->set_File(inFile);
 doc->Save(outFile);
}
```
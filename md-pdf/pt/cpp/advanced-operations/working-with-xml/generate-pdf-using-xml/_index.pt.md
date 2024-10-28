---
title: Gerar PDF a partir de XML
linktitle: Gerar PDF a partir de XML
type: docs
weight: 10
url: /cpp/generate-pdf-from-xml
description: Aspose.PDF para C++ fornece várias maneiras de converter um arquivo XML em um documento PDF exigindo que o arquivo XML de entrada.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gerar um documento PDF a partir de um documento XML não é uma tarefa trivial porque o documento XML pode descrever diferentes conteúdos. Aspose.PDF para C++ tem várias maneiras de gerar PDF baseado em documento XML:

- usando transformação XSLT
- usando XSL-FO (XSL Formatting Objects) markup
- usando seu próprio esquema XML Aspose.PDF

## Gerando documento PDF usando transformação XSLT

XSL (eXtensible Stylesheet Language) é uma linguagem de estilo para transformar documentos XML em outros documentos XML ou HTMLs. No nosso caso, podemos usar a transformação XML para HTML e, em seguida, criar PDF baseado em dados HTML.

Assumimos que temos um arquivo XML com um catálogo de CDs simples (veja abaixo).

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

Para converter este arquivo para PDF, devemos criar um XSL com layout HTML. Vamos renderizar nossos dados em uma tabela. O arquivo XSL que nos ajudará a fazer isso pode se parecer com isto:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Minha Coleção de CDs</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">Título</th>
            <th style="text-align:left">Artista</th>
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

Então, precisamos transformar XML e carregar no documento PDF. O exemplo a seguir mostra este caminho:

```cpp
void WorkingWithXML::ExampleXSLTtoPDF()
{
 String _dataDir("C:\\Samples\\");

 auto XmlContent = System::IO::File::ReadAllText(u"XMLFile1.xml");
 auto XsltContent = System::IO::File::ReadAllText(u"XSLTFile1.xslt");

 auto options = MakeObject<Aspose::Pdf::HtmlLoadOptions>();
 // definir o tamanho da página para A5
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
## Gerando documento PDF usando a marcação XSL-FO

XSL-FO é uma linguagem de marcação baseada em XML que descreve a formatação de dados XML para saída em tela, papel ou outros meios. Aspose.PDF possui uma classe especial que permite aplicar a marcação XSL-FO e obter um documento PDF.

Vamos pegar um exemplo. Aqui está um arquivo XML com dados de exemplo de funcionários.

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

Vamos criar ainda outro arquivo - o arquivo de marcação XSL-FO para transformar os dados dos funcionários em uma tabela.

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
                        Nome da Empresa: <xsl:value-of select="companyname"/>
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

Aspose.PDF possui uma classe especial [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/) que permite aplicar transformação XSL-FO. O trecho a seguir mostra como usar esta classe com os arquivos de exemplo descritos acima.

```cpp
void WorkingWithXML::Example_XSLFO_to_PDF()
{
 String _dataDir("C:\\Samples\\");
 // Instanciar objeto XslFoLoadOption
 auto options = MakeObject<Aspose::Pdf::XslFoLoadOptions>(u"employees.xslt");
 // Criar objeto Document
 auto pdfDocument = MakeObject<Aspose::Pdf::Document>(u"employees.xml", options);
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

### Gerando documento PDF usando marcação XSL-FO e parâmetros XSL

Às vezes, precisamos usar [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param). O elemento `<xsl:param>` estabelece um parâmetro pelo nome e, opcionalmente, um valor padrão para esse parâmetro.

Vamos pegar o mesmo exemplo do caso anterior, mas com pequenas alterações (adicionando parâmetros). O arquivo XML com dados de exemplo permanece intocado, ...

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

mas no arquivo de marcação XSL-FO adicionaremos o parâmetro: `<xsl:param name="isBoldName"></xsl:param>` e o aplicaremos à coluna `Name`.

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
Para adicionar parâmetros XSL, precisamos criar nosso próprio 'XsltArgumentList' e defini-lo como propriedade em [XslFoLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xsl_fo_load_options/). O trecho a seguir mostra como usar esta classe com os arquivos de exemplo descritos acima.

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

## Gerando documento PDF baseado no Esquema XML Aspose.PDF

Outra maneira de criar um documento PDF a partir de XML é usando o Esquema XML Aspose.PDF. Usando este diagrama, você pode descrever o layout da página da mesma forma que se estivesse usando um layout de tabela em HTML. Vamos considerar o funcionamento deste método em mais detalhes.

### Definindo página

Vamos definir a página com parâmetros padrão. Nossa página terá um tamanho de página A4 e conterá apenas um pedaço de texto.

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

Para gerar o documento PDF, usaremos o método BindXml().

```cpp
void WorkingWithXML::Example_XML_to_PDF()
{
 String _dataDir("C:\\Samples\\");

 auto pdfDocument = MakeObject<Document>();
 pdfDocument->BindXml(_dataDir + u"aspose_pdf_demo.xml");
 pdfDocument->Save(_dataDir + u"data_xml.pdf");
}
```

Para definir um novo tamanho de página, devemos adicionar um elemento `PageInfo`. No exemplo a seguir, definimos o tamanho da página como A5 e margens de 25mm e 10mm.

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

### Adicionando o elemento HtmlFragment no arquivo XML

Como o HTML contém tags semelhantes ao XML, ao escrever HTML dentro de qualquer tag XML, o analisador o trata como marcações XML e elas simplesmente não podem ser reconhecidas como tags XML. O problema pode ser superado usando a Seção "CDATA" em XML. A Seção CDATA contém texto que não é analisado pelo analisador ou, em outras palavras, não é tratado como marcações XML. O modelo XML de exemplo a seguir mostra como adicionar HtmlFragment dentro das marcações XML usando CDATA.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">Este é um Html String.</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### Adicionando elemento de tabela no arquivo XML

Os elementos `Table`, `Row`, `Cell` são usados para descrever tabelas. O fragmento a seguir mostra o uso de uma tabela simples. Neste exemplo, algumas células têm o atributo `Alignment` e este atributo tem valor numérico:

1. Alinhamento à esquerda
1. Alinhamento central
1. Alinhamento à direita.
1. Alinhamento justificado. O texto será alinhado nas margens esquerda e direita.
1. Justificar completamente. Similar ao alinhamento 'Justificar', exceto que a última linha será apenas alinhada à esquerda no modo 'Justificar', enquanto no modo 'Justificar Completo' todas as linhas serão alinhadas à esquerda e à direita.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">HORÁRIOS NA ROTA GREENTOWN-BLUEBERG</h1>
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
            <TextSegment>Partida</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Chegada</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Dia da semana</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Navio</TextSegment>
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
            <TextSegment>Seg-Sáb</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>Seg-Sex, Dom</TextSegment>
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
Tables são usadas para o layout de documentos. Por exemplo, podemos personalizar um cabeçalho de página. Neste caso, a tabela foi usada para dividir o cabeçalho em 2 colunas.

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
                        <TextSegment>Data: 01/01/2021</TextSegment>
                    </TextFragment>
                </Cell>
                <Cell Alignment="3">
                    <TextFragment>
                        <TextSegment>Página $p / $P</TextSegment>
                    </TextFragment>
                </Cell>
            </Row>
        </Table>
    </Header>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">HORÁRIOS NA ROTA GREENTOWN-BLUEBERG</h1>
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
            <TextSegment>Partida</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Chegada</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Dia da semana</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Nave</TextSegment>
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
            <TextSegment>Seg-Sáb</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
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
            <TextSegment>todos os dias</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Estrela</TextSegment>
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
            <TextSegment>Seg-Sex, Dom</TextSegment>
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

### Atualizando conteúdo dinamicamente

O método BindXML() oferece a funcionalidade de carregar conteúdos de arquivos XML e o método Document.save() pode ser usado para salvar o resultado em formato PDF. No entanto, durante a conversão, também podemos acessar elementos individuais dentro do XML e usar o XML como modelo. O trecho de código a seguir mostra as etapas para acessar TextSegments de um arquivo XML.

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

 // Instanciar objeto Document
 auto doc = MakeObject<Document>();
 // Vincular arquivo XML de origem
 doc->BindXml(_dataDir + u"log.xml");
 // Obter referência do objeto página do XML
 auto page = System::DynamicCast<Page>(doc->GetObjectById(u"mainSection"));
 // Obter referência do primeiro TextSegment com ID boldHtml
 auto segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"boldHtml"));
 // Obter referência do segundo TextSegment com ID strongHtml
 segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(doc->GetObjectById(u"strongHtml"));
 // Salvar arquivo PDF resultante
 doc->Save(_dataDir + u"XMLToPDF_out.pdf");
}
```

### Adicionando elementos gráficos à página

Podemos adicionar outros elementos adicionais ao documento XML: objetos de Imagem ou Gráfico. O trecho a seguir mostra como adicionar esses elementos ao documento

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Definir caminho da imagem ao converter XML para PDF

O seguinte modelo XML contém uma tag `<Image>` com um ID "testImg". Caso você queira definir o caminho da imagem a partir do seu código, você pode acessar o elemento de Imagem do modelo XML durante o processo de conversão e definir o caminho para o endereço desejado para a imagem.

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

Código para definir o caminho da imagem no modelo XML é o seguinte:

```cpp
void WorkingWithXML::UpdatingontentDynamically2() {

 String _dataDir("C:\\Samples\\");
 String inFile = _dataDir + u"aspose-logo.jpg";
 String outFile = _dataDir + u"output_out.pdf";

 // Instanciar objeto Document
 auto doc = MakeObject<Document>();
 // Vincular arquivo XML de origem
 doc->BindXml(_dataDir + u"input.xml");

 auto image = System::DynamicCast<Image>(doc->GetObjectById(u"testImg"));

 image->set_File(inFile);
 doc->Save(outFile);
}
```
---
title: Generar PDF desde XML
linktitle: Generar PDF desde XML
type: docs
weight: 10
url: /java/generate-pdf-from-xml
description: Aspose.PDF para Java ofrece la oportunidad de convertir un archivo XML en un documento PDF requiriendo que el archivo XML de entrada siga el esquema de Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Generar un documento PDF desde un documento XML no es una tarea trivial porque el documento XML puede describir contenido diferente. Aspose.PDF para Java tiene varias formas de generar PDF basándose en documentos XML:

- usando la transformación XSLT
- usando el marcado XSL-FO (Objetos de Formateo XSL)
- usando su propio esquema XML de Aspose.PDF

## Generar documento PDF usando la transformación XSLT

XSL (eXtensible Stylesheet Language) es un lenguaje de estilo para transformar documentos XML en otros documentos XML o HTML. En nuestro caso podemos usar la transformación XML a HTML y luego crear un PDF basado en los datos HTML.

Supongamos que tenemos un archivo XML con un catálogo de CDs simple (ver abajo).

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


Para convertir este archivo a PDF, debemos crear un XSL con diseño HTML. Vamos a renderizar nuestros datos en una tabla. El archivo XSL que nos ayudará a hacer esto podría lucir algo como esto:

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>Mi Colección de CDs</h2>
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

Así que, necesitamos transformar XML y cargarlo en un documento PDF.
 El siguiente ejemplo muestra esta manera:

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

## Generación de documento PDF usando XSL-FO markup

XSL-FO es un lenguaje de marcado basado en XML que describe el formato de datos XML para la salida en pantalla, papel u otros medios. Aspose.PDF tiene una clase especial que permite aplicar el marcado XSL-FO y obtener un documento PDF.

Tomemos un ejemplo. Aquí hay un archivo XML con datos de muestra de empleados.

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

Vamos a crear otro archivo más: el archivo de marcado XSL-FO para transformar los datos de los empleados en una tabla.

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
                        Nombre de la Compañía: <xsl:value-of select="companyname"/>
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


Aspose.PDF tiene una clase especial [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XslFoLoadOptions) que permite aplicar la transformación XSL-FO. El siguiente fragmento muestra cómo usar esta clase con los archivos de muestra descritos anteriormente.

```java
public static void Example_XSLFO_to_PDF() {
    // Instanciar objeto XslFoLoadOption
    com.aspose.pdf.XslFoLoadOptions options = new com.aspose.pdf.XslFoLoadOptions(_dataDir+"employees.xslt");
    // Crear objeto Document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(_dataDir+"employees.xml", options);
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

## Generar un documento PDF basado en el esquema XML de Aspose.PDF

Otra forma de crear un documento PDF desde XML es usando el esquema XML de Aspose.PDF. Usando este diagrama, puedes describir el diseño de la página de la misma manera que si estuvieras usando un diseño de tabla en HTML. Consideremos el trabajo de este método con más detalle.

### Definiendo la página

Vamos a definir la página con parámetros predeterminados.
 Nuestra página tendrá un tamaño de página A4 y contendrá solo un fragmento de texto.

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

Para generar el documento PDF usaremos el método [bindXml](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#bindXml--).

```java
public static void Example_XML_to_PDF() {
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    pdfDocument.bindXml(_dataDir + "aspose_pdf_demo.xml");
    pdfDocument.save(_dataDir + "data_xml.pdf");
}
```

Para definir un nuevo tamaño de página, debemos agregar un elemento `PageInfo`. En el siguiente ejemplo, configuramos el tamaño de página A5 y márgenes de 25mm y 10mm.

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

### Agregar elemento HtmlFragment en archivo XML

Como HTML contiene etiquetas similares a XML, cuando escribes HTML dentro de cualquier etiqueta XML, el analizador lo trata como marcas XML y simplemente no pueden ser reconocidas como etiquetas XML. El problema se puede superar utilizando la sección "CDATA" en XML. La sección CDATA contiene texto que no es analizado por el analizador o, en otras palabras, no se trata como marcas XML. El siguiente ejemplo de plantilla XML muestra cómo agregar HtmlFragment dentro de marcas XML utilizando CDATA.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page id="mainSection">
    <HtmlFragment>
      <![CDATA[
        <font style="font-family:Tahoma; font-size:40px;">Esta es una cadena Html.</font>
        ]]>
    </HtmlFragment>
  </Page>
</Document>
```

### Agregar elemento Table en archivo XML

Los elementos `Table`, `Row`, `Cell` se utilizan para describir tablas. El siguiente fragmento muestra el uso de una tabla simple. En este ejemplo, algunas celdas tienen el atributo `Alignment` y este atributo tiene un valor numérico:

1. Alineación a la izquierda
1. Alineación al centro
1. Alineación a la derecha.
1. Alineación justificada. El texto se alineará en ambos márgenes izquierdo y derecho.
1. Justificación completa. Similar a la alineación 'Justify', excepto que la última línea solo estará alineada a la izquierda en el modo 'Justify', mientras que en el modo 'FullJustify' todas las líneas estarán alineadas a la izquierda y derecha.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">HORARIOS EN LA RUTA GREENTOWN-BLUEBERG</h1>
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
            <TextSegment>Salida</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Llegada</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Día de la semana</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Barco</TextSegment>
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
            <TextSegment>Lun-Sáb</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>Lun-Vie, Dom</TextSegment>
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


Las tablas se utilizan para el diseño de documentos. Por ejemplo, podemos personalizar un encabezado de página. En este caso, se utilizó una tabla para dividir el encabezado en 2 columnas.

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
                        <TextSegment>Fecha: 01/01/2021</TextSegment>
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
        <h1 style="font-family:Tahoma; font-size:16pt;">HORARIOS EN LA RUTA GREENTOWN-BLUEBERG</h1>
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
            <TextSegment>Salida</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Llegada</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Día de la semana</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Barco</TextSegment>
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
            <TextSegment>Lun-Sáb</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>todos los días</TextSegment>
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
            <TextSegment>Lun-Vie, Dom</TextSegment>
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


### Actualización de contenido dinámicamente

El método BindXML() ofrece la funcionalidad de cargar el contenido de un archivo XML y el método Document.save() se puede utilizar para guardar el resultado en formato PDF. Sin embargo, durante la conversión, también podemos acceder a elementos individuales dentro del XML y usar XML como plantilla. El siguiente fragmento de código muestra los pasos para acceder a TextSegments desde un archivo XML.

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
    // Instanciar objeto Document
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
    // Vincular archivo XML fuente
    pdfDocument.bindXml(_dataDir + "log.xml");
    
    // Obtener referencia del primer TextSegment con ID boldHtml
    TextSegment segment = (TextSegment)pdfDocument.getObjectById("boldHtml");
    segment.setText("Demo 1");
    // Obtener referencia del segundo TextSegment con ID strongHtml
    segment = (TextSegment)pdfDocument.getObjectById("strongHtml");
    segment.setText("Demo 2");
    // Guardar archivo PDF resultante
    pdfDocument.save(_dataDir + "XMLToPDF_out.pdf");
}
```


### Añadiendo elementos gráficos a la página

Podemos añadir otros elementos adicionales al documento XML: objetos de Imagen o Gráfico. El siguiente fragmento muestra cómo agregar esos elementos al documento

```xml
<Graph Width="20" Height="20">    
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Establecer la Ruta de la Imagen al Convertir XML a PDF

La siguiente plantilla XML contiene una etiqueta `<Image>` con un ID "testImg". En caso de que desees establecer la ruta de la imagen desde tu código, puedes acceder al elemento de Imagen desde la plantilla XML durante el proceso de conversión y establecer la ruta a tu dirección deseada para la imagen.

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


Código para establecer la ruta de la imagen en la plantilla XML es el siguiente:

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
---
title: Creando PDF desde XML usando XSLT
linktitle: Crear PDF desde XML usando XSLT
type: docs
weight: 10
url: /cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: La biblioteca C++ proporciona la capacidad de convertir un archivo XML en un documento PDF, requiriendo que el archivo XML de entrada siga el esquema Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A veces puedes tener archivos XML existentes que contienen datos de la aplicación y deseas generar un informe PDF usando estos archivos. Puedes usar XSLT para transformar tu documento XML existente a un documento XML compatible con Aspose.Pdf y luego generar un archivo PDF. Hay 3 pasos para generar PDF usando XML y XSLT.

Por favor, sigue estos pasos para convertir un archivo XML en un documento PDF usando XSLT:

* Crea una instancia de la clase PDF que representa un documento PDF
* Si has comprado una licencia, entonces también deberías incrustar el código para usar esa licencia con la ayuda de la clase License en el espacio de nombres Aspose.Pdf

* Vincula los archivos XML y XSLT de entrada a la instancia de la clase PDF llamando a su método BindXML
 * Guardar el XML vinculado con la instancia PDF como un documento PDF

## Archivo de entrada XML

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>¡Hola Mundo!</Content>
</Contents>
```

## Archivo de entrada XSLT

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

```cpp
using namespace System;
using namespace Aspose::Pdf;

static System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString);

void WorkingWithXML::CreatingPDFfromXMLusingXSLT()
{
 String _dataDir("C:\\Samples\\");
 //Create pdf document
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Bind XML and XSLT files to the document
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Save the document
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```
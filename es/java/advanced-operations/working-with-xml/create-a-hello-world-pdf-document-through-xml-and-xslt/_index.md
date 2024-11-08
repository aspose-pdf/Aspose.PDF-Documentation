---
title: Crear un Documento PDF de Hello World a través de XML y XSLT
linktitle: Crear un Documento PDF de Hello World a través de XML y XSLT
type: docs
weight: 10
url: /es/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF para Java ofrece la oportunidad de convertir un archivo XML en un documento PDF requiriendo que el archivo XML de entrada siga el esquema Aspose.PDF XSD Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A veces puedes tener archivos XML existentes que contienen datos de la aplicación y deseas generar un informe PDF usando estos archivos. Puedes usar XSLT para transformar tu documento XML existente a un documento XML compatible con Aspose.Pdf y luego generar un archivo PDF. Hay 3 pasos para generar PDF usando XML y XSLT.

Por favor sigue estos pasos para convertir un archivo XML en un documento PDF usando XSLT:

* Crea una instancia de la clase PDF que representa un documento PDF

* Si has comprado una licencia, entonces también deberías incrustar el código para usar esa licencia con la ayuda de la clase License en el espacio de nombres Aspose.Pdf
* Vincula los archivos XML y XSLT de entrada a la instancia de la clase PDF llamando a su método BindXML
* Guarda el XML vinculado con la instancia PDF como un documento PDF

## Archivo XML de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>¡Hola Mundo!</Content>
</Contents>
```

## Archivo XSLT de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState Font = "Helvetica" FontSize="8" LineSpacing="4"/>
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


## Haciendo Hello World usando XML y Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```
---
title: Créer un document PDF Hello World via XML et XSLT
linktitle: Créer un document PDF Hello World via XML et XSLT
type: docs
weight: 10
url: /java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF pour Java offre la possibilité de convertir un fichier XML en document PDF, à condition que le fichier XML d'entrée suive le schéma XSD Java d'Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Parfois, vous pouvez avoir des fichiers XML existants contenant des données d'application et vous souhaitez générer un rapport PDF en utilisant ces fichiers. Vous pouvez utiliser XSLT pour transformer votre document XML existant en document XML compatible avec Aspose.Pdf, puis générer un fichier PDF. Il y a 3 étapes pour générer un PDF en utilisant XML et XSLT.

Veuillez suivre ces étapes pour convertir un fichier XML en document PDF à l'aide de XSLT :

* Créez une instance de la classe PDF qui représente un document PDF

* Si vous avez acheté une licence, vous devez également intégrer le code pour utiliser cette licence à l'aide de la classe License dans l'espace de noms Aspose.Pdf
* Liez les fichiers XML et XSLT d'entrée à l'instance de la classe PDF en appelant sa méthode BindXML
* Enregistrez le XML lié avec l'instance PDF en tant que document PDF

## Fichier XML d'entrée

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Fichier XSLT d'entrée

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


## Création de Hello World en utilisant XML et Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```
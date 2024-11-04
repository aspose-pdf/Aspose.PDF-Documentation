---
title: Création de PDF à partir de XML en utilisant XSLT
linktitle: Créer un PDF à partir de XML en utilisant XSLT
type: docs
weight: 10
url: /cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: La bibliothèque C++ offre la possibilité de convertir un fichier XML en document pdf à condition que le fichier XML d'entrée suive le schéma Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Parfois, vous pouvez avoir des fichiers XML existants contenant des données d'application et vous souhaitez générer un rapport PDF en utilisant ces fichiers. Vous pouvez utiliser XSLT pour transformer votre document XML existant en un document XML compatible avec Aspose.Pdf, puis générer un fichier PDF. Il y a 3 étapes pour générer un PDF en utilisant XML et XSLT.

Veuillez suivre ces étapes pour convertir un fichier XML en un document PDF en utilisant XSLT :

* Créez une instance de la classe PDF qui représente un document PDF
* Si vous avez acheté une licence, vous devez également intégrer le code pour utiliser cette licence à l'aide de la classe License dans l'espace de noms Aspose.Pdf

* Lie les fichiers XML et XSLT d'entrée à l'instance de la classe PDF en appelant sa méthode BindXML
* Enregistrer le XML lié avec l'instance PDF en tant que document PDF

## Fichier XML d'entrée

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Bonjour le monde!</Content>
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
 //Créer un document pdf
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Lier les fichiers XML et XSLT au document
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Enregistrer le document
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```
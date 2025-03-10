---
title: Générer un PDF à partir de XML
linktitle: Générer un PDF à partir de XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/generate-pdf-from-xml
description: Aspose.PDF for .NET fournit plusieurs façons de convertir un fichier XML en un document PDF nécessitant que le fichier XML d'entrée.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate PDF from XML",
    "alternativeHeadline": "Generate PDF directly from XML data",
    "abstract": "Aspose.PDF for .NET génère désormais des PDF directement à partir des données XML en utilisant plusieurs méthodes : transformations XSLT, balisage XSL-FO et un schéma XML Aspose.PDF personnalisé. Cette nouvelle fonctionnalité offre une création de PDF flexible à partir de diverses structures XML, rationalisant les flux de travail de génération de documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3834",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/generate-pdf-from-xml",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-pdf-from-xml"
    },
    "dateModified": "2024-11-26",
    "description": "Aspose.PDF for .NET fournit plusieurs façons de convertir un fichier XML en un document PDF nécessitant que le fichier XML d'entrée."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Générer un document PDF à partir d'un document XML n'est pas une tâche triviale car le document XML peut décrire différents contenus. Aspose.PDF for .NET a plusieurs façons de générer un PDF basé sur un document XML :

- en utilisant la transformation XSLT
- en utilisant le balisage XSL-FO (XSL Formatting Objects)
- en utilisant son propre schéma XML Aspose.PDF

## Générer un document PDF en utilisant la transformation XSLT

XSL (eXtensible Stylesheet Language) est un langage de style pour transformer des documents XML en d'autres documents XML ou en HTML. Dans notre cas, nous pouvons utiliser la transformation XML en HTML, puis créer un PDF basé sur les données HTML.

Supposons que nous ayons un fichier XML avec un simple catalogue de CD (voir ci-dessous).

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

Pour convertir ce fichier en PDF, nous devrions créer un XSL avec une mise en page HTML. Rendons nos données dans un tableau. Le fichier XSL qui nous aidera à faire cela pourrait ressembler à ceci :

```xml
<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <body>
        <h2>My CD Collection</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">Title</th>
            <th style="text-align:left">Artist</th>
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

Ainsi, nous devons transformer XML et charger dans le document PDF. L'exemple suivant montre cette méthode :

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXsltToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var XmlContent = File.ReadAllText(dataDir + "XMLFile1.xml");
    var XsltContent = File.ReadAllText(dataDir + "XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // set page size to A5
    options.PageInfo.Height = 595;
    options.PageInfo.Width = 420;

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(TransformXmlToHtml(XmlContent, XsltContent), options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLT_out.pdf");
    }
}

public static MemoryStream TransformXmlToHtml(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    using (var reader = XmlReader.Create(new StringReader(xsltString)))
    {
        transform.Load(reader);
    }

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using (var reader = XmlReader.Create(new StringReader(inputXml)))
    {
        transform.Transform(reader, null, results);
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXsltToPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var XmlContent = File.ReadAllText(dataDir + "XMLFile1.xml");
    var XsltContent = File.ReadAllText(dataDir + "XSLTFile1.xslt");
    var options = new Aspose.Pdf.HtmlLoadOptions();

    // set page size to A5
    options.PageInfo.Height = 595;
    options.PageInfo.Width = 420;

    // Open PDF document
    using var document = new Aspose.Pdf.Document(TransformXmlToHtml(XmlContent, XsltContent), options);

    // Save PDF document
    document.Save(dataDir + "XSLT_out.pdf");
}

public static MemoryStream TransformXmlToHtml(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    using var reader1 = XmlReader.Create(new StringReader(xsltString));
    transform.Load(reader1);

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using var reader2 = XmlReader.Create(new StringReader(inputXml));
    transform.Transform(reader2, null, results);

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}
{{< /tabs >}}

## Générer un document PDF en utilisant le balisage XSL-FO

XSL-FO est un langage de balisage basé sur XML décrivant le formatage des données XML pour une sortie à l'écran, sur papier ou d'autres médias. Aspose.PDF a une classe spéciale qui permet d'appliquer le balisage XSL-FO et d'obtenir un document PDF.

Prenons un exemple. Voici un fichier XML avec des données d'exemple d'employés.

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

Créons encore un autre fichier - le fichier de balisage XSL-FO pour transformer les données des employés en tableau.

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

Aspose.PDF a une classe spéciale [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions) qui permet d'appliquer la transformation XSL-FO. Le snippet suivant montre comment utiliser cette classe avec les fichiers d'exemple décrits ci-dessus.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    // Open XML file
    using (var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    // Open XML file
    using var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Générer un document PDF en utilisant le balisage XSL-FO et les paramètres XSL

Parfois, nous devons utiliser [XSL:param](https://developer.mozilla.org/en-US/docs/Web/XSLT/Element/param). L'élément `<xsl:param>` établit un paramètre par nom et, éventuellement, une valeur par défaut pour ce paramètre.

Prenons le même exemple que dans le cas précédent, mais avec des modifications mineures (ajout de paramètres). Le fichier XML avec des données d'exemple reste inchangé, ...

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

mais dans le fichier de balisage XSL-FO, nous ajouterons le paramètre : `<xsl:param name="isBoldName"></xsl:param>` et l'appliquerons à la colonne `Name`.

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

Pour ajouter des paramètres XSL, nous devons créer notre propre [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) et
le définir comme propriété dans [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Le snippet suivant montre comment utiliser cette classe avec les fichiers d'exemple décrits ci-dessus.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_7()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open XML file
    using (var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_7()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Instantiate XslFoLoadOption object
    var options = new Aspose.Pdf.XslFoLoadOptions(dataDir + "employees.xslt");

    options.XsltArgumentList = new XsltArgumentList();
    options.XsltArgumentList.AddParam("isBoldName", "", "yes");

    // Open XML file
    using var document = new Aspose.Pdf.Document(dataDir + "employees.xml", options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Si vous utilisez une version antérieure à 21.7, veuillez utiliser la technique suivante :

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdfParam_21_6()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var xmlContent = File.ReadAllText(dataDir + "employees.xml");
    var xsltContent = File.ReadAllText(dataDir + "employees.xslt");

    var options = new Aspose.Pdf.XslFoLoadOptions();

    // Open XML file
    using (var document = new Aspose.Pdf.Document(TransformXsl(xmlContent, xsltContent), options))
    {
        // Save PDF document
        document.Save(dataDir + "XSLFO_out.pdf");
    }
}

public static MemoryStream TransformXsl(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    // Create own XsltArgumentList
    var argsList = new XsltArgumentList();
    argsList.AddParam("isBoldName", "", "no");

    using (var reader = XmlReader.Create(new StringReader(xsltString)))
    {
        transform.Load(reader);
    }

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using (var reader = XmlReader.Create(new StringReader(inputXml)))
    {
        transform.Transform(reader, argsList, results);
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXslfoToPdf_Param_21_6()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    var xmlContent = File.ReadAllText(dataDir + "employees.xml");
    var xsltContent = File.ReadAllText(dataDir + "employees.xslt");

    var options = new Aspose.Pdf.XslFoLoadOptions();

    // Open XML file
    using var document = new Aspose.Pdf.Document(TransformXsl(xmlContent, xsltContent), options);

    // Save PDF document
    document.Save(dataDir + "XSLFO_out.pdf");
}

public static MemoryStream TransformXsl(string inputXml, string xsltString)
{
    var transform = new XslCompiledTransform();

    // Create own XsltArgumentList
    var argsList = new XsltArgumentList();
    argsList.AddParam("isBoldName", "", "no");

    using var reader1 = XmlReader.Create(new StringReader(xsltString));
    transform.Load(reader1);

    var memoryStream = new MemoryStream();
    var results = new StreamWriter(memoryStream);

    using var reader2 = XmlReader.Create(new StringReader(inputXml));
    transform.Transform(reader2, argsList, results);

    memoryStream.Position = 0;
    return memoryStream;
}
```
{{< /tab >}}
{{< /tabs >}}

## Générer un document PDF basé sur le schéma XML Aspose.PDF

Une autre façon de créer un document PDF à partir de XML est d'utiliser le schéma XML Aspose.PDF. En utilisant ce diagramme, vous pouvez décrire la mise en page de la page de la même manière que si vous utilisiez une mise en page de tableau en HTML. Considérons le fonctionnement de cette méthode plus en détail.

### Définir la page

Définissons la page avec des paramètres par défaut. Notre page aura un format A4 et contiendra uniquement un morceau de texte.

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

Pour générer un document PDF, nous utiliserons la méthode [BindXml](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/bindxml/index).

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXmlToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file to the document
        document.BindXml(dataDir + "aspose_pdf_demo.xml");

        // Save PDF document
        document.Save(dataDir + "XML_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExampleXmlToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    //Bind XML file to the document
    document.BindXml(dataDir + "aspose_pdf_demo.xml");

    // Save PDF document
    document.Save(dataDir + "XML_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Pour définir une nouvelle taille de page, nous devrions ajouter un élément `PageInfo`. Dans l'exemple suivant, nous avons défini une taille de page A5 et des marges de 25 mm et 10 mm.

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

### Ajouter un élément HtmlFragment dans le fichier XML

Comme HTML contient des balises similaires à XML, lorsque vous écrivez du HTML à l'intérieur de n'importe quelle balise XML, le parseur le traite comme des balisages XML et ils ne peuvent tout simplement pas être reconnus comme des balises XML. Le problème peut être contourné en utilisant une section "CDATA" dans XML. La section CDATA contient du texte qui n'est pas analysé par le parseur ou, en d'autres termes, il n'est pas traité comme des balisages XML. Le modèle XML d'exemple suivant montre comment ajouter HtmlFragment à l'intérieur des balisages XML en utilisant CDATA.

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

### Ajouter un élément Table dans le fichier XML

Les éléments `Table`, `Row`, `Cell` sont utilisés pour décrire des tableaux. Le snippet suivant montre l'utilisation d'un tableau simple. Dans cet exemple, certaines cellules ont un attribut `Alignment` et cet attribut a une valeur numérique :

1. Alignement à gauche
1. Alignement centré
1. Alignement à droite.
1. Alignement justifié. Le texte sera aligné sur les marges gauche et droite.
1. Justification complète. Semblable à l'alignement 'Justifié', sauf que la toute dernière ligne sera uniquement alignée à gauche en mode 'Justifié', tandis qu'en mode 'Justification complète', toutes les lignes seront alignées à gauche et à droite.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Document xmlns="Aspose.Pdf">
  <Page>
    <PageInfo IsLandscape="false" Height="595" Width="420">
      <Margin Top="71" Bottom="71" Left="28" Right="28" />
    </PageInfo>
    <HtmlFragment>
      <![CDATA[
        <h1 style="font-family:Tahoma; font-size:16pt;">TIMETABLES ON GREENTOWN-BLUEBERG ROUTE</h1>
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
            <TextSegment>Departure</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Arrival</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Weekday</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Ship</TextSegment>
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
            <TextSegment>Mon-Sat</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>Mon-Fri, Sun</TextSegment>
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

Les tableaux sont utilisés pour la mise en page des documents. Par exemple, nous pouvons personnaliser un en-tête de page. Dans ce cas, un tableau a été utilisé pour diviser l'en-tête en 2 colonnes.

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
        <h1 style="font-family:Tahoma; font-size:16pt;">TIMETABLES ON GREENTOWN-BLUEBERG ROUTE</h1>
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
            <TextSegment>Departure</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Arrival</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Weekday</TextSegment>
          </TextFragment>
        </Cell>
        <Cell>
          <TextFragment>
            <TextSegment>Ship</TextSegment>
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
            <TextSegment>Mon-Sat</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>every day</TextSegment>
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
            <TextSegment>Mon-Fri, Sun</TextSegment>
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

### Mise à jour dynamique du contenu

La méthode BindXML() offre la fonctionnalité de charger le contenu du fichier XML et la méthode Document.save() peut être utilisée pour enregistrer la sortie au format PDF. Cependant, lors de la conversion, nous pouvons également accéder aux éléments individuels à l'intérieur de XML et utiliser XML comme modèle. Le snippet de code suivant montre les étapes pour accéder aux TextSegments à partir du fichier XML.

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

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file
        document.BindXml(dataDir + "log.xml");

        // Get reference of page object from XML
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get reference of first TextSegment with ID boldHtml
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");

        // Get reference of second TextSegment with ID strongHtml
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "XMLToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Bind XML file
    document.BindXml(dataDir + "log.xml");

    // Get reference of page object from XML
    var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

    // Get reference of first TextSegment with ID boldHtml
    var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");

    // Get reference of second TextSegment with ID strongHtml
    segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

    // Save PDF document
    document.Save(dataDir + "XMLToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Ajouter des éléments graphiques à la page

Nous pouvons ajouter d'autres éléments supplémentaires au document XML : des objets Image ou Graph. Le snippet suivant montre comment ajouter ces éléments au document.

```xml
<Graph Width="20" Height="20">
  <Circle PosX="30" PosY="30" Radius="10">
    <GraphInfo Color="Red" FillColor="Blue"></GraphInfo>
  </Circle>
</Graph>

<Image File="logo.png" Id = "testImg"></Image>
```

### Définir le chemin de l'image lors de la conversion de XML en PDF

Le modèle XML suivant contient une balise `<Image>` avec un ID "testImg". Si vous souhaitez définir le chemin de l'image depuis votre code, vous pouvez accéder à l'élément Image à partir du modèle XML pendant le processus de conversion et définir le chemin vers l'adresse souhaitée pour l'image.

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

Le code pour définir le chemin de l'image dans le modèle XML est le suivant :

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Bind XML file
        document.BindXml(dataDir + "input.xml");

        // Get reference of Image with ID testImg
        var image = (Aspose.Pdf.Image)document.GetObjectById("testImg");

        // Set image file
        image.File = dataDir + "aspose-logo.jpg";

        // Save PDF document
        document.Save(dataDir + "output_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Bind XML file
    document.BindXml(dataDir + "input.xml");

    // Get reference of Image with ID testImg
    var image = (Aspose.Pdf.Image)document.GetObjectById("testImg");

    // Set image file
    image.File = dataDir + "aspose-logo.jpg";

    // Save PDF document
    document.Save(dataDir + "output_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
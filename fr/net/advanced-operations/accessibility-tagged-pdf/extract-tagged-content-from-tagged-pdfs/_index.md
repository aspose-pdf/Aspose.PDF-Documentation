---
title: Extraire le contenu tagué à partir d'un PDF
linktitle: Extraire le contenu tagué
type: docs
weight: 20
url: fr/net/extract-tagged-content-from-tagged-pdfs/
description: Cet article explique comment extraire le contenu tagué d'un document PDF en utilisant Aspose.PDF pour .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraire le contenu tagué à partir d'un PDF",
    "alternativeHeadline": "Comment taguer une image dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "tag, pdf, extract",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment extraire le contenu tagué d'un document PDF en utilisant Aspose.PDF pour .NET"
}
</script>

Dans cet article, vous apprendrez comment extraire le contenu tagué d'un document PDF en utilisant C#.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtenir le contenu PDF Tagué

Pour obtenir le contenu d'un document PDF avec du texte tagué, Aspose.PDF offre la propriété [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Le code suivant montre comment obtenir le contenu d'un document PDF avec du texte tagué :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// Travailler avec le contenu Pdf tagué
//

// Définir le titre et la langue pour le document
taggedContent.SetTitle("Simple Tagged Pdf Document");
taggedContent.SetLanguage("en-US");

// Sauvegarder le document PDF tagué
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## Obtention de la structure racine

Pour obtenir la structure racine d'un document PDF balisé, Aspose.PDF propose la propriété [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) de l'interface [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) et [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Le fragment de code suivant montre comment obtenir la structure racine d'un document PDF balisé :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Définir le titre et la langue du document
taggedContent.SetTitle("Document PDF balisé");
taggedContent.SetLanguage("en-US");

// Les propriétés StructTreeRootElement et RootElement sont utilisées pour accéder à
// l'objet StructTreeRoot du document pdf et à l'élément de structure racine (élément de structure du document).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## Accès aux éléments enfants

Pour accéder aux éléments enfants d'un document PDF balisé, Aspose.PDF propose la classe [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist). Le fragment de code suivant montre comment accéder aux éléments enfants d'un document PDF balisé :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document PDF
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Accès à l'élément racine
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Obtenir les propriétés
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// Accès aux éléments enfants du premier élément dans l'élément racine
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Définir les propriétés
        structureElement.Title = "titre";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "texte actuel";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// Sauvegarder le document PDF balisé
document.Save(dataDir + "AccessChildElements.pdf");
```
## Étiquetage des images dans un PDF existant

Pour étiqueter les images dans un document PDF existant, Aspose.PDF propose la méthode [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) de la classe [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Vous pouvez ajouter un texte alternatif pour les figures en utilisant la propriété [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) de la classe [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement).

Le fragment de code suivant montre comment étiqueter les images dans un document PDF existant :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// Ouvrir le document
Document document = new Document(inFile);

// Obtient le contenu étiqueté et l'élément de structure racine
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// Définir le titre pour le document PDF étiqueté
taggedContent.SetTitle("Document avec images");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // Définir le texte alternatif pour la figure
    figureElement.AlternativeText = "Texte alternatif de la figure (technique 2)";


    // Créer et définir l'attribut BBox
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// Déplacer l'élément Span dans le paragraphe (trouver le mauvais span et paragraphe dans le premier TD)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// Déplacer l'élément Span dans le paragraphe
spanElement.ChangeParentElement(paragraph);


// Sauvegarder le document
document.Save(outFile);



// Vérification de la conformité PDF/UA pour le document sortant
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformité PDF/UA : {0}", isPdfUaCompliance));
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
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
```


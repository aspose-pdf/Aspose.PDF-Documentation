---
title: Créer un PDF balisé en utilisant C#
linktitle: Créer un PDF balisé
type: docs
weight: 10
url: /fr/net/create-tagged-pdf/
description: Cet article explique comment créer des éléments de structure pour un document PDF balisé de manière programmatique en utilisant Aspose.PDF pour .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Créer un PDF balisé en utilisant C#",
    "alternativeHeadline": "Comment créer un PDF balisé",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "créer, balisé, pdf",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article explique comment créer des éléments de structure pour un document PDF balisé de manière programmatique en utilisant Aspose.PDF pour .NET."
}
</script>
Créer un PDF balisé signifie ajouter (ou créer) certains éléments au document qui permettront de valider le document conformément aux exigences PDF/UA. Ces éléments sont souvent appelés Éléments de Structure.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Création d'un PDF balisé (Scénario Simple)

Pour créer des éléments de structure dans un document PDF balisé, Aspose.PDF propose des méthodes pour créer un élément de structure en utilisant l'interface [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). Le code suivant montre comment créer un PDF balisé qui contient 2 éléments : en-tête et paragraphe.

```csharp
private static void CreateTaggedPdfDocument01()
{
    // Créer le document PDF
    var document = new Document();

    // Obtenir le contenu pour travailler avec TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Définir le titre et la langue pour le document
    taggedContent.SetTitle("Document PDF balisé");
    taggedContent.SetLanguage("en-US");

    // 
    HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("En-tête principal");

    ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
    "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
    "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
    "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
    "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
    "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
    "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
    "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
    "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // Sauvegarder le document PDF balisé
    document.Save("C:\\Samples\\TaggedPDF\\Sample1.pdf");
}
```
Nous obtiendrons un document suivant après création :

![Document PDF balisé avec 2 éléments - En-tête et Paragraphe](taggedpdf-01.png)

## Création de PDF balisé avec des éléments imbriqués (Création d'une arborescence d'éléments de structure)

Dans certains cas, nous avons besoin de créer une structure plus complexe, par exemple placer des citations dans un paragraphe. 
Pour créer une arborescence d'éléments de structure, nous devrions utiliser la méthode [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild).
Le fragment de code suivant montre comment créer une arborescence d'éléments de structure d'un document PDF balisé :

```csharp
private static void CreateTaggedPdfDocument02()
{
    // Créer un document PDF
    var document = new Document();

    // Obtenir le contenu pour travailler avec TaggedPdf
    ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;
    // Définir le titre et la langue du document
    taggedContent.SetTitle("Document PDF balisé");
    taggedContent.SetLanguage("en-US");

    HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("Niveau d'en-tête 1");

    ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = FontRepository.FindFont("Calibri");
    // Adjust position
    paragraphWithQuotes.AdjustPosition(new Aspose.Pdf.Tagged.PositionSettings
    {
        Margin = new Aspose.Pdf.MarginInfo(10, 5, 10, 5)
    });

    SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
    QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
    SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // Sauvegarder le document PDF balisé
    document.Save("C:\\Samples\\TaggedPDF\\Sample2.pdf");
}
```
Nous obtiendrons le document suivant après sa création :
![Document PDF balisé avec des éléments imbriqués - span et guillemets](taggedpdf-02.png)

## Structurer le style de texte

Pour structurer le style de texte dans un document PDF balisé, Aspose.PDF propose les propriétés [Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font), [FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize), [FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) et [ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) de la classe [StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate). Le fragment de code suivant montre comment styliser la structure de texte dans un document PDF balisé :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Définir le titre et la langue pour le document
taggedContent.SetTitle("Document PDF balisé");
taggedContent.SetLanguage("en-US");

ParagraphElement p = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(p);

// En développement
p.StructureTextState.FontSize = 18F;
p.StructureTextState.ForegroundColor = Color.Red;
p.StructureTextState.FontStyle = FontStyles.Italic;

p.SetText("Texte rouge en italique.");

// Sauvegarder le document PDF balisé
document.Save(dataDir + "StyleTextStructure.pdf");
```
## Illustration des éléments de structure

Afin d'illustrer les éléments de structure dans un document PDF balisé, Aspose.PDF propose la classe [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement). Le fragment de code suivant montre comment illustrer les éléments de structure dans un document PDF balisé :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Définir le titre et la langue pour le document
taggedContent.SetTitle("Document PDF balisé");
taggedContent.SetLanguage("en-US");

// En développement
IllustrationElement figure1 = taggedContent.CreateFigureElement();
taggedContent.RootElement.AppendChild(figure1);
figure1.AlternativeText = "Figure Un";
figure1.Title = "Image 1";
figure1.SetTag("Fig1");
figure1.SetImage("image.png");

// Sauvegarder le document PDF balisé
document.Save(dataDir + "IllustrationStructureElements.pdf");

```
## Valider le PDF Tagué

Aspose.PDF pour .NET offre la capacité de valider un document PDF tagué PDF/UA. La validation de la norme PDF/UA inclut :

- Vérifications des XObjects
- Vérifications des Actions
- Vérifications du Contenu Optionnel
- Vérifications des Fichiers Incorporés
- Vérifications des Champs de l'Acroform (Valider la Langue Naturelle et le Nom Alternatif et les Signatures Numériques)
- Vérifications des Champs de Formulaire XFA
- Vérifications des Paramètres de Sécurité
- Vérifications de la Navigation
- Vérifications des Annotations

Le fragment de code ci-dessous montre comment valider le document PDF tagué. Les problèmes correspondants seront affichés dans le rapport de journalisation XML.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inputFileName = dataDir + "StructureElements.pdf";
string outputLogName = dataDir + "ua-20.xml";

using (var document = new Aspose.Pdf.Document(inputFileName))
{
    bool isValid = document.Validate(outputLogName, Aspose.Pdf.PdfFormat.PDF_UA_1);

}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour .NET Library",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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


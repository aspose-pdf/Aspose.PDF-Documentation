---
title: Utilisation de l'annotation de texte pour PDF
linktitle: Annotation de texte
type: docs
weight: 10
url: /fr/net/text-annotation/
description: Aspose.PDF pour .NET vous permet d'ajouter, de récupérer et de supprimer des annotations de texte de votre document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Utilisation de l'annotation de texte pour PDF",
    "alternativeHeadline": "Comment ajouter une annotation de texte dans un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotation de texte",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter, de récupérer et de supprimer des annotations de texte de votre document PDF."
}
</script>

## Comment ajouter une annotation de texte dans un fichier PDF existant

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Une annotation de texte est une annotation attachée à un emplacement spécifique dans un document PDF. Lorsqu'elle est fermée, l'annotation est affichée sous forme d'icône ; lorsqu'elle est ouverte, elle doit afficher une fenêtre contextuelle contenant le texte de la note dans la police et la taille choisies par le lecteur.

Les annotations sont contenues dans la collection [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) d'une page particulière. Cette collection contient les annotations pour cette page individuelle uniquement ; chaque page a sa propre collection Annotations.

Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page avec la méthode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Commencez par créer une annotation que vous souhaitez ajouter au PDF.
1. Ensuite, ouvrez le PDF d'entrée.
1.
Le code suivant vous montre comment ajouter une annotation dans une page PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Créer une annotation
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Titre de l'annotation exemple";
textAnnotation.Subject = "Sujet exemple";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Contenu exemple pour l'annotation";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Ajouter l'annotation dans la collection d'annotations de la page
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Sauvegarder le fichier de sortie
pdfDocument.Save(dataDir);
```
## Comment ajouter une annotation popup

Une annotation popup affiche du texte dans une fenêtre popup pour la saisie et l'édition. Elle ne doit pas apparaître seule mais est associée à une annotation de marquage, son annotation parente, et doit être utilisée pour éditer le texte du parent.

Elle ne doit avoir aucun flux d'apparence ou actions associées propres et doit être identifiée par l'entrée Popup dans le dictionnaire d'annotation du parent.

Le code suivant vous montre comment ajouter une [Annotation Popup](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) dans une page PDF en utilisant un exemple d'ajout d'une [Annotation de ligne](/pdf/fr/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) parente.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // Le chemin vers le répertoire des documents.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Charger le fichier PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Créer une annotation de ligne
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Ajouter l'annotation à la page
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## Comment ajouter (ou créer) une nouvelle annotation de texte libre

Une annotation de texte libre affiche du texte directement sur la page. La méthode [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) permet de créer ce type d'annotation. Dans l'extrait suivant, nous ajoutons une annotation de texte libre au-dessus de la première occurrence de la chaîne.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Démonstration de texte libre", 1); // le dernier paramètre est un numéro de page
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### Définir la propriété de rappel pour FreeTextAnnotation
### Définir la propriété Callout pour FreeTextAnnotation

Pour une configuration plus flexible de l'annotation dans le document PDF, Aspose.PDF pour .NET fournit la propriété [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) de la classe [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) qui permet de spécifier un tableau de points de la ligne de rappel. Le fragment de code suivant montre comment utiliser cette fonctionnalité :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">Ceci est un exemple</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Définir la propriété de légende pour un fichier XFDF

Si vous utilisez l'importation à partir d'un fichier XFDF, veuillez utiliser le nom callout-line au lieu de juste Callout. Le fragment de code suivant montre comment utiliser cette fonctionnalité :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

La méthode suivante est utilisée pour créer XFDF :

```csharp
/// <summary>
/// Créer XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">Ceci est un exemple</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### Rendre l'annotation de texte libre invisible

Parfois, il est nécessaire de créer un filigrane qui n’est pas visible dans le document lors de sa consultation mais qui doit être visible lors de l'impression du document. Utilisez les drapeaux d'annotation à cet effet. Le code suivant montre comment faire.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Sauvegarder le fichier de sortie
doc.Save(dataDir);
```
### Définir le formatage de FreeTextAnnotation

Cette partie examine comment formater le texte dans une annotation de texte libre.

Les annotations sont contenues dans la collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Lors de l'ajout d'une [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) à un document PDF, vous pouvez spécifier les informations de formatage telles que la police, la taille, la couleur, etc. en utilisant la classe [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). Il est également possible de spécifier les informations de formatage en utilisant la propriété TextStyle. De plus, vous pouvez mettre à jour le formatage de toute FreeTextAnnotation déjà dans le document PDF.

La classe [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) prend en charge le travail avec l'entrée de style par défaut.
La classe [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) prend en charge le travail avec l'entrée de style par défaut.

- La propriété FontName permet d'obtenir ou de définir le nom de la police (chaîne).
- La propriété FontSize permet d'obtenir et de définir la taille de texte par défaut (double).
- La propriété System.Drawing.Color permet d'obtenir et de définir la couleur du texte (couleur).
- La propriété TextAlignment permet d'obtenir et de définir l'alignement du texte de l'annotation (alignement).

Le fragment de code suivant montre comment ajouter une FreeTextAnnotation avec un formatage de texte spécifique.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

Lorsque vous modifiez le contenu ou le style de texte d'une annotation de texte libre, l'apparence de l'annotation est régénérée pour refléter les changements.

{{% /alert %}}

### Barrer des mots en utilisant StrikeOutAnnotation

Aspose.PDF pour .NET vous permet d'ajouter, de supprimer et de mettre à jour des annotations dans des documents PDF.
Aspose.PDF pour .NET vous permet d'ajouter, de supprimer et de mettre à jour des annotations dans des documents PDF.

Pour barrer un certain TextFragment :

1. Recherchez un TextFragment dans le fichier PDF.
1. Obtenez les coordonnées de l'objet TextFragment.
1. Utilisez les coordonnées pour instancier un objet StrikeOutAnnotation.

Le code suivant montre comment rechercher un TextFragment particulier et ajouter un StrikeOutAnnotation à cet objet.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

Cette fonctionnalité est prise en charge par la version 19.6 ou supérieure.

{{% /alert %}}

## Supprimer toutes les annotations d'une page de fichier PDF

La collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contient toutes les annotations de cette page particulière.
La collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contient toutes les annotations pour cette page spécifique.

Le code suivant montre comment supprimer toutes les annotations d'une page particulière.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Supprimer une annotation particulière
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir);
```

## Supprimer une Annotation Particulière du Fichier PDF

{{% alert color="primary" %}}

Vous pouvez vérifier la qualité d'Aspose.PDF et obtenir les résultats en ligne à ce lien :
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF vous permet de supprimer une annotation particulière d'un fichier PDF. Ce sujet explique comment faire.

Pour supprimer une annotation particulière d'un PDF, appelez la méthode Delete de la [collection AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Cette collection appartient à l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). La méthode Delete nécessite l'index de l'annotation que vous souhaitez supprimer. Ensuite, enregistrez le fichier PDF mis à jour. Le fragment de code suivant montre comment supprimer une annotation particulière.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Supprimer une annotation particulière
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Enregistrer le document mis à jour
pdfDocument.Save(dataDir);
```
## Obtenir toutes les annotations d'une page de document PDF

Aspose.PDF vous permet d'obtenir les annotations de tout un document ou d'une page donnée. Pour obtenir toutes les annotations d'une page dans un document PDF, parcourez la collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) des ressources de la page désirée. Le fragment de code suivant vous montre comment obtenir toutes les annotations d'une page.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Parcourir toutes les annotations
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Obtenir les propriétés de l'annotation
    Console.WriteLine("Titre : {0} ", annotation.Title);
    Console.WriteLine("Sujet : {0} ", annotation.Subject);
    Console.WriteLine("Contenus : {0} ", annotation.Contents);
}
```
Veuillez noter que pour obtenir toutes les annotations de l'ensemble du PDF, vous devez parcourir la collection de la classe PageCollection du document avant de naviguer à travers la collection de la classe AnnotationCollection. Vous pouvez obtenir chaque annotation de la collection dans un type de base d'annotation appelé classe MarkupAnnotation, puis afficher ses propriétés.

## Obtenir une Annotation Particulière du Fichier PDF

Les annotations sont associées à des pages individuelles et stockées dans la collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
Les annotations sont associées à des pages individuelles et stockées dans la collection [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Obtenir une annotation particulière
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Obtenir les propriétés de l'annotation
Console.WriteLine("Titre : {0} ", textAnnotation.Title);
Console.WriteLine("Sujet : {0} ", textAnnotation.Subject);
Console.WriteLine("Contenu : {0} ", textAnnotation.Contents);
```

## Obtenir la ressource d'une annotation

Aspose.PDF vous permet d'obtenir une ressource d'annotation d'un document entier ou d'une page donnée.
Aspose.PDF vous permet de récupérer une ressource d'annotation d'un document entier ou d'une page donnée.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// Créer une annotation
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Sauvegarder le document
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Ouvrir le document
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Obtenir l'action de l'annotation
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// Obtenir la représentation de l'action de représentation
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// Clip multimédia
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// Les données du média sont accessibles dans FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
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
Certainly, I'm ready to translate the document provided. However, it seems there's no content from the original document included in your message. Please paste the content you need translated into French, and I will assist you accordingly while preserving the markdown formatting and other specifications you mentioned.

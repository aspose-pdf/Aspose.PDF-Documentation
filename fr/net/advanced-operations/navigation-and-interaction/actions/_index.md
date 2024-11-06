---
title: Travailler avec les actions dans PDF
linktitle: Actions
type: docs
weight: 20
url: fr/net/actions/
description: Cette section explique comment ajouter des actions au document et aux champs de formulaire de manière programmatique avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Travailler avec les actions dans PDF",
    "alternativeHeadline": "Comment ajouter des actions dans PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, actions dans pdf",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section explique comment ajouter des actions au document et aux champs de formulaire de manière programmatique avec C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter un hyperlien dans un fichier PDF

Il est possible d'ajouter des hyperliens aux fichiers PDF, soit pour permettre aux lecteurs de naviguer vers une autre partie du PDF, soit vers un contenu externe.

Pour ajouter des hyperliens web aux documents PDF :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtenez la classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). L'objet rectangle est utilisé pour spécifier l'emplacement sur la page où le lien doit être ajouté.
1. Définissez la propriété Action sur l'objet [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) qui spécifie l'emplacement de l'URI distant.
1.

1. Pour ajouter un texte libre :

- Instanciez un objet [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). Il accepte également des objets Page et Rectangle en argument, il est donc possible de fournir les mêmes valeurs que celles spécifiées pour le constructeur de LinkAnnotation.
- Utilisez la propriété Contents de l'objet [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) pour spécifier la chaîne qui devrait être affichée dans le PDF de sortie.
- Facultativement, réglez la largeur de la bordure des objets [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) et FreeTextAnnotation à 0 afin qu'ils n'apparaissent pas dans le document PDF.
- Une fois que les objets [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) et [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) ont été définis, ajoutez ces liens à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
```
- Une fois les objets [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) et [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) définis, ajoutez ces liens à la collection d'annotations de l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Enfin, enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Le snippet de code suivant vous montre comment ajouter un hyperlien à un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Ouvrir le document
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Créer un lien
Page page = document.Pages[1];
// Créer l'objet annotation de lien
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Créer l'objet bordure pour LinkAnnotation
Border border = new Border(link);
// Définir la valeur de la largeur de la bordure comme 0
border.Width = 0;
// Définir la bordure pour LinkAnnotation
link.Border = border;
// Spécifier le type de lien comme URI distant
link.Action = new GoToURIAction("www.aspose.com");
// Ajouter l'annotation de lien à la collection d'annotations de la première page du fichier PDF
page.Annotations.Add(link);

// Créer une annotation de texte libre
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// Chaîne à ajouter comme texte libre
textAnnotation.Contents = "Lien vers le site web d'Aspose";
// Définir la bordure pour l'annotation de texte libre
textAnnotation.Border = border;
// Ajouter l'annotation de texte libre à la collection d'annotations de la première page du document
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// Enregistrer le document mis à jour
document.Save(dataDir);
```
## Créer un hyperlien vers des pages dans le même PDF

Aspose.PDF pour .NET offre une excellente fonctionnalité pour la création de PDF ainsi que sa manipulation. Il propose également la fonctionnalité d'ajouter des liens vers des pages de PDF et un lien peut diriger vers des pages dans un autre fichier PDF, une URL web, lancer une application ou même lier à des pages dans le même fichier PDF. Pour ajouter des hyperliens locaux (liens vers des pages dans le même fichier PDF), une classe nommée [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) est ajoutée à l'espace de noms Aspose.PDF et cette classe possède une propriété nommée TargetPageNumber, qui est utilisée pour spécifier la page cible/destination pour l'hyperlien.

Pour ajouter l'hyperlien local, nous devons créer un TextFragment afin que le lien puisse être associé au TextFragment. La classe [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) possède une propriété nommée Hyperlink qui est utilisée pour associer une instance de LocalHyperlink. Le fragment de code suivant montre les étapes pour accomplir cette exigence.

```csharp
// Création d'un document PDF
Document pdfDocument = new Document();
// Ajout d'une page au document
Page page = pdfDocument.Pages.Add();

// Création d'un TextFragment
TextFragment textFragment = new TextFragment("Cliquez ici pour aller à la page cible");
textFragment.Position = new Position(100, 600);

// Création d'un LocalHyperlink
LocalHyperlink localHyperlink = new LocalHyperlink();
localHyperlink.TargetPageNumber = 2; // Numéro de la page cible

// Association de l'hyperlien au TextFragment
textFragment.Hyperlink = localHyperlink;

// Ajout du TextFragment à la page
page.Paragraphs.Add(textFragment);

// Sauvegarde du document PDF
pdfDocument.Save("output.pdf");
```
```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Créer une instance de Document
Document doc = new Document();
// Ajouter une page à la collection de pages du fichier PDF
Page page = doc.Pages.Add();
// Créer une instance de Fragment de Texte
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("tester le lien vers le numéro de page 7");
// Créer une instance de lien hypertexte local
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// Définir la page cible pour l'instance de lien
link.TargetPageNumber = 7;
// Définir le lien hypertexte du Fragment de Texte
text.Hyperlink = link;
// Ajouter le texte à la collection de paragraphes de la Page
page.Paragraphs.Add(text);
// Créer une nouvelle instance de Fragment de Texte
text = new TextFragment("tester le lien vers le numéro de page 1");
// Le Fragment de Texte doit être ajouté sur une nouvelle page
text.IsInNewPage = true;
// Créer une autre instance de lien hypertexte local
link = new LocalHyperlink();
// Définir la page cible pour le deuxième lien hypertexte
link.TargetPageNumber = 1;
// Définir le lien pour le deuxième Fragment de Texte
text.Hyperlink = link;
// Ajouter le texte à la collection de paragraphes de l'objet page
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```
## Obtenir la destination d'hyperlien PDF (URL)

Les liens sont représentés comme des annotations dans un fichier PDF et ils peuvent être ajoutés, mis à jour ou supprimés. Aspose.PDF pour .NET prend également en charge l'obtention de la destination (URL) de l'hyperlien dans le fichier PDF.

Pour obtenir l'URL d'un lien :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Obtenez la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) à partir de laquelle vous souhaitez extraire les liens.
3. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) de la page spécifiée.
4. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) à la méthode Accept de l'objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Enfin, extrayez l'Action LinkAnnotation en tant que GoToURIAction.

Le fragment de code suivant montre comment obtenir les destinations des hyperliens (URL) à partir d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Charger le fichier PDF
Document document = new Document(dataDir + "input.pdf");

// Parcourir toutes les pages du PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // Obtenir les annotations de lien de la page particulière
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Créer une liste contenant tous les liens
    IList<Annotation> list = selector.Selected;
    // Itérer sur chaque élément de la liste
    foreach (LinkAnnotation a in list)
    {
        // Afficher l'URL de destination
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## Obtenir le texte du lien hypertexte

Un lien hypertexte comporte deux parties : le texte qui apparaît dans le document et l'URL de destination. Dans certains cas, c'est le texte plutôt que l'URL dont nous avons besoin.

Le texte et les annotations/actions dans un fichier PDF sont représentés par différentes entités. Le texte sur une page est juste un ensemble de mots et de caractères, tandis que les annotations apportent une certaine interactivité, comme celle inhérente à un lien hypertexte.

Pour trouver le contenu de l'URL, vous devez travailler à la fois avec l'annotation et le texte. L'objet [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) n'a pas lui-même le texte mais se situe sous le texte sur la page. Ainsi, pour obtenir le texte, l'Annotation donne les limites de l'URL, tandis que l'objet Texte donne le contenu de l'URL. Veuillez voir le fragment de code suivant.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // Le chemin vers le répertoire des documents.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // Charger le fichier PDF
                Document document = new Document(dataDir + "input.pdf");
                // Itérer à travers chaque page du PDF
                foreach (Page page in document.Pages)
                {
                    // Afficher l'annotation de lien
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // Imprimer l'URL de chaque annotation de lien
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // Imprimer le texte associé au lien hypertexte
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## Supprimer l'action d'ouverture de document d'un fichier PDF

[Comment spécifier la page PDF lors de la visualisation du document](#how-to-specify-pdf-page-when-viewing-document) expliquait comment indiquer à un document de s'ouvrir sur une page différente de la première. Lorsque vous concaténez plusieurs documents, et qu'un ou plusieurs ont une action GoTo définie, vous voudrez probablement les supprimer. Par exemple, si vous combinez deux documents et que le second contient une action GoTo qui vous amène à la seconde page, le document final s'ouvrira sur la seconde page du second document au lieu de la première page du document combiné. Pour éviter ce comportement, supprimez la commande d'action d'ouverture.

Pour supprimer une action d'ouverture :

1. Définissez la propriété [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) à null.
1. Enregistrez le PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant montre comment supprimer une action d'ouverture de document du fichier PDF.
Le code suivant montre comment supprimer une action d'ouverture de document d'un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Ouvrir le document
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Supprimer l'action d'ouverture du document
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// Sauvegarder le document mis à jour
document.Save(dataDir);
```

## Comment spécifier la page PDF lors de la visualisation du document {#how-to-specify-pdf-page-when-viewing-document}

Lors de la visualisation de fichiers PDF dans un lecteur PDF tel qu'Adobe Reader, les fichiers s'ouvrent généralement sur la première page. Cependant, il est possible de configurer le fichier pour qu'il s'ouvre sur une page différente.

La classe [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) vous permet de spécifier une page dans un fichier PDF que vous souhaitez ouvrir.
La classe [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) vous permet de spécifier une page d'un fichier PDF que vous souhaitez ouvrir.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Charger le fichier PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Obtenir l'instance de la deuxième page du document
Page page2 = doc.Pages[2];
// Créer la variable pour définir le facteur de zoom de la page cible
double zoom = 1;
// Créer une instance de GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// Aller à la 2ème page
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Définir l'action d'ouverture du document
doc.OpenAction = action;
// Sauvegarder le document mis à jour
doc.Save(dataDir + "goto2page_out.pdf");
```

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



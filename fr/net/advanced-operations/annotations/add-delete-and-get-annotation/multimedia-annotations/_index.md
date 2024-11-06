---
title: Annotation multimédia PDF en utilisant C#
linktitle: Annotation multimédia
type: docs
weight: 40
url: fr/net/multimedia-annotation/
description: Aspose.PDF pour .NET vous permet d'ajouter, de récupérer et de supprimer l'annotation multimédia de votre document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "headline": "Annotation multimédia PDF en utilisant C#",
    "alternativeHeadline": "Comment ajouter une annotation multimédia dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, annotation multimédia, annotation d'écran, annotation sonore, annotation de widget, annotation 3D",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter, de récupérer et de supprimer l'annotation multimédia de votre document PDF."
}
</script>
Les annotations dans un document PDF sont contenues dans la collection Annotations d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Cette collection contient toutes les annotations pour cette page individuelle uniquement : chaque page possède sa propre collection Annotations. Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page en utilisant la méthode Add.

Utilisez la classe [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) dans l'espace de noms Aspose.PDF.InteractiveFeatures.Annotations pour inclure des fichiers SWF en tant qu'annotations dans un document PDF à la place. Une annotation d'écran spécifie une région d'une page sur laquelle des clips média peuvent être joués.

Lorsque vous avez besoin d'ajouter un lien vidéo externe dans un document PDF, vous pouvez utiliser [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Une annotation de film contient des graphiques animés et du son à présenter sur l'écran de l'ordinateur et via les haut-parleurs.

Une [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) doit être analogue à une annotation de texte sauf qu'au lieu d'une note textuelle, elle contient un son enregistré depuis le microphone de l'ordinateur ou importé depuis un fichier.
Une [Annotation Sonore](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) doit être analogue à une annotation textuelle sauf qu'au lieu d'une note textuelle, elle contient un son enregistré à partir du microphone de l'ordinateur ou importé d'un fichier.

Cependant, lorsqu'il est nécessaire d'incorporer des médias dans un document PDF, vous devez utiliser [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Les méthodes/propriétés suivantes de la classe RichMediaAnnotation peuvent être utilisées.

- Stream CustomPlayer { set; }: Permet de définir le lecteur utilisé pour lire la vidéo.
- string CustomFlashVariables { set; }: Permet de définir les variables qui sont transmises à l'application flash. Cette ligne est un ensemble de paires "clé=valeur" qui sont séparées par '&'.
- void AddCustomData(string name, Stream data): Ajoute des données supplémentaires pour le lecteur. Par exemple source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: L'événement active le lecteur; les valeurs possibles sont Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Définit les données vidéo/audio à lire.
- void SetContent(Stream stream, string name): Définir les données vidéo/audio à lire.
- void Update(): Créer une structure de données pour l'annotation. Cette méthode doit être appelée en dernier.
- void SetPoster(Stream): Définir l'affiche de la vidéo, c'est-à-dire l'image affichée lorsque le lecteur n'est pas actif.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Ajouter une Annotation de l'Écran

Le code suivant montre comment ajouter une Annotation de l'Écran à un fichier PDF :

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // Le chemin vers le répertoire des documents.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Charger le fichier PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Créer une Annotation de l'Écran
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## Ajouter une annotation sonore

Le code suivant montre comment ajouter une annotation sonore à un fichier PDF :

```csharp
        public static void AddSoundAnnotation()
        {
            // Charger le fichier PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Créer une annotation sonore
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "Démonstration d'annotation sonore",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Ajouter une annotation RichMedia

Le code suivant montre comment ajouter une annotation RichMedia à un fichier PDF :
Le code suivant montre comment ajouter une RichMediaAnnotation à un fichier PDF :

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //donner un nom aux données vidéo. Ces données seront intégrées dans le document sous ce nom et référencées à partir des variables flash par ce nom.
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //nous utilisons également un habillage pour le lecteur vidéo
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //ici nous devons spécifier le flux contenant le code du lecteur vidéo
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //composer la ligne de variables flash pour le lecteur. veuillez noter que différents lecteurs peuvent avoir différents formats de la ligne de variables flash. Consultez la documentation de votre lecteur.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //ajouter le code de l'habillage.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //définir une affiche pour la vidéo
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //définir le contenu vidéo
            rma.SetContent(videoName, fs);

            //définir le type de contenu (vidéo)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //activer le lecteur par clic
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //mettre à jour les données de l'annotation. Cette méthode doit être appelée après toutes les affectations/configurations. Cette méthode initialise la structure de données de l'annotation et intègre les données requises.
            rma.Update();

            //ajouter l'annotation à la page.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### Obtenir MultimediaAnnotation

Veuillez essayer d'utiliser le code suivant pour obtenir MultimediaAnnotation d'un document PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Charger le fichier PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Supprimer MultimediaAnnotation

Le code suivant montre comment supprimer MultimediaAnnotation d'un fichier PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Charger le fichier PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```

## Ajouter des Annotations de Widget

Les formulaires interactifs utilisent des [Annotations de Widget](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) pour représenter l'apparence des champs et pour gérer les interactions des utilisateurs. Nous utilisons ces éléments de formulaire qui ajoutent à un PDF pour faciliter la saisie, la soumission d'informations ou effectuer d'autres interactions utilisateur.

Les Annotations de Widget sont une représentation graphique d'un champ de formulaire sur des pages spécifiques, donc nous ne pouvons pas les créer directement en tant qu'annotation.

Chaque Annotation de Widget aura une apparence graphique appropriée (apparence) en fonction de son type. Après la création, certains aspects visuels peuvent être modifiés, tels que le style de bordure et la couleur de fond. D'autres propriétés telles que la couleur du texte et la police peuvent être modifiées via le champ, une fois attaché à celui-ci.

Dans certains cas, vous pouvez vouloir qu'un champ apparaisse sur plusieurs pages, répétant la même valeur.
Dans certains cas, vous pouvez vouloir qu'un champ apparaisse sur plusieurs pages, répétant la même valeur. Quelqu'un remplissant le formulaire peut utiliser n'importe lequel de ces widgets pour mettre à jour la valeur du champ, et cela se reflète dans tous les autres widgets également.

Chaque champ de formulaire pour chaque emplacement dans le document représente une Annotation de Widget. Les données spécifiques à l'emplacement de l'Annotation de Widget sont ajoutées à la page particulière. Chaque champ de formulaire a plusieurs variantes. Un bouton peut être un bouton radio, une case à cocher ou un bouton-poussoir. Un widget de choix peut être une boîte de liste ou une boîte combinée.

Dans cet exemple, nous apprendrons comment ajouter des boutons-poussoirs pour la navigation dans le document.

### Ajouter un bouton au document

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Imprimer le document actuel",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Imprimer le document"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
Ce bouton a une bordure et définit un arrière-plan. Nous définissons également un nom de bouton (Name), une infobulle (AlternateName), une étiquette (NormalCaption) et une couleur du texte de l'étiquette (Color).

### Utilisation des actions de navigation dans les documents

Il existe un exemple plus complexe de l'utilisation des annotations de widget - la navigation dans un document PDF. Cela peut être nécessaire pour préparer une présentation de document PDF.

Cet exemple montre comment créer 4 boutons :

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
var normalCaptions = new[] { "First", "Prev", "Next", "Last" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

Nous devrions créer les boutons sans les attacher à la page.
Nous devrions créer les boutons sans les attacher à la page.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

Nous devrions dupliquer ce tableau de boutons sur chaque page du document.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

Nous appelons la [méthode Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) avec les paramètres suivants : champ, nom, et l'indice des pages sur lesquelles ce champ sera ajouté.
Nous appelons [la méthode Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) avec les paramètres suivants : champ, nom et l'index des pages sur lesquelles ce champ sera ajouté.

Et pour obtenir le résultat complet, nous devons désactiver les boutons « First » et « Prev » sur la première page et les boutons « Next » et « Last » sur la dernière page.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

Pour plus d'informations détaillées et les possibilités de ces fonctionnalités, consultez également [Travailler avec les formulaires](/pdf/net/acroforms/).

Dans les documents PDF, vous pouvez visualiser et gérer des contenus 3D de haute qualité créés avec des logiciels de CAO 3D ou de modélisation 3D et intégrés dans le document PDF. Vous pouvez faire pivoter les éléments 3D dans toutes les directions comme si vous les teniez dans vos mains.

Pourquoi avez-vous besoin d'une affichage 3D des images en premier lieu ?

Au cours des dernières années, la technologie a réalisé d'énormes percées dans tous les domaines grâce à l'impression 3D.
Au cours des dernières années, la technologie a réalisé d'énormes percées dans tous les domaines grâce à l'impression 3D.

La tâche principale de la modélisation 3D est l'idée d'un futur objet car, pour produire un objet, il est nécessaire de comprendre ses caractéristiques de conception en détail pour une régénération successive dans la conception industrielle ou l'architecture.

## Ajouter une annotation 3D

L'annotation 3D est ajoutée à l'aide d'un modèle créé au format U3D.

1. Créer un nouveau [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Charger les données du modèle 3D souhaité (dans notre cas "Ring.u3d") pour créer [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Créer un objet [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) et le lier au document et au 3DContent
1. Configurer l'objet pdf3dArtWork :

    - 3DLightingScheme - (nous réglerons sur `CAD` dans cet exemple)
    - 3DRenderMode - (nous réglerons sur `Solid` dans cet exemple)
    - Remplir `ViewArray`, créer au moins une [Vue 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) et l'ajouter au tableau.

- Remplissez `ViewArray`, créez au moins une [Vue 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) et ajoutez-la au tableau.

1. Définissez 3 paramètres de base dans l'annotation :
    - la `page` sur laquelle l'annotation sera placée,
    - le `rectangle`, à l'intérieur duquel l'annotation,
    - et l'objet `3dArtWork`.
1. Pour une meilleure présentation de l'objet 3D, configurez le cadre de la bordure.
1. Définissez la vue par défaut (par exemple - TOP)
1. Ajoutez quelques paramètres supplémentaires : nom, affiche de prévisualisation, etc.
1. Ajoutez l'annotation à la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Enregistrez le résultat

### Exemple

Veuillez vérifier le fragment de code suivant pour ajouter une annotation 3D.

```csharp
    public static void Add3dAnnotation()
    {
    // Charger le fichier PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Nom = "Ring.u3d";
    //définir l'image de prévisualisation si nécessaire
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
Cet exemple de code nous a montré un tel modèle :

![Démonstration d'annotation 3D](3d_demo.png)

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



---
title: Annotation multimédia PDF utilisant C#
linktitle: Annotation multimédia
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /fr/net/multimedia-annotation/
description: Aspose.PDF for .NET vous permet d'ajouter, d'obtenir et de supprimer l'annotation multimédia de votre document PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Multimedia Annotation using C#",
    "alternativeHeadline": "Enable Multimedia Annotations in PDF with C#",
    "abstract": "Aspose.PDF for .NET introduit des capacités avancées d'annotation multimédia, permettant aux utilisateurs d'ajouter, de récupérer et de supprimer facilement divers types multimédias dans des documents PDF. Cette fonctionnalité prend en charge les annotations d'écran, de son et de médias enrichis, améliorant l'interactivité des documents et permettant l'intégration de contenu vidéo externe, de notes audio et de médias intégrés, rendant les documents PDF plus dynamiques et engageants.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF multimedia annotation, Aspose.PDF, C# PDF features, screen annotation, sound annotation, rich media annotation, widget annotations, 3D annotation, document navigation, multimedia file embedding",
    "wordcount": "2247",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Les annotations dans un document PDF sont contenues dans la collection Annotations d'un objet [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Cette collection contient toutes les annotations pour cette page individuelle uniquement : chaque page a sa propre collection Annotations. Pour ajouter une annotation à une page particulière, ajoutez-la à la collection Annotations de cette page en utilisant la méthode Add.

Utilisez la classe [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) dans l'espace de noms Aspose.PDF.InteractiveFeatures.Annotations pour inclure des fichiers SWF en tant qu'annotations dans un document PDF à la place. Une annotation d'écran spécifie une région d'une page sur laquelle des clips multimédias peuvent être lus.

Lorsque vous devez ajouter un lien vidéo externe dans un document PDF, vous pouvez utiliser [MovieAnnotaiton](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation).
Une annotation de film contient des graphiques animés et du son à présenter sur l'écran de l'ordinateur et à travers les haut-parleurs.

Une [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) est analogue à une annotation de texte, sauf qu'au lieu d'une note textuelle, elle contient un son enregistré à partir du microphone de l'ordinateur ou importé d'un fichier. Lorsque l'annotation est activée, le son est joué. L'annotation se comporte comme une annotation de texte dans la plupart des cas, avec une icône différente (par défaut, un haut-parleur) pour indiquer qu'elle représente un son.

Cependant, lorsqu'il est nécessaire d'intégrer des médias dans un document PDF, vous devez utiliser [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Les méthodes/propriétés suivantes de la classe RichMediaAnnotation peuvent être utilisées.

- Stream CustomPlayer { set; }: Permet de définir le lecteur utilisé pour lire la vidéo.
- string CustomFlashVariables { set; }: Permet de définir les variables qui sont passées à l'application flash. Cette ligne est un ensemble de paires "clé=valeur" séparées par '&'.
- void AddCustomData(strig name, Stream data): Ajouter des données supplémentaires pour le lecteur. Par exemple source=video.mp4&autoPlay=true&scale=100.
- ActivationEvent ActivateOn { get; set}: L'événement active le lecteur ; les valeurs possibles sont Click, PageOpen, PageVisible.
- void SetContent(Stream stream, string name): Définir les données vidéo/audio à lire.
- void Update(): Créer une structure de données de l'annotation. Cette méthode doit être appelée en dernier.
- void SetPoster(Stream): Définir l'affiche de la vidéo c'est-à-dire l'image affichée lorsque le lecteur n'est pas actif.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter une annotation d'écran

Le code suivant montre comment ajouter une annotation d'écran à un fichier PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddScreenAnnotationWithMedia()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (cument = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Path to the media file (SWF)
        var mediaFile = dataDir + "input.swf";

        // Create Screen Annotation
        var screenAnnotation = new Aspose.Pdf.Annotations.ScreenAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(170, 190, 470, 380),
            mediaFile);

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(screenAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddScreenAnnotationWithMedia_out.pdf");
    }
}
```

## Ajouter une annotation sonore

Le code suivant montre comment ajouter une annotation sonore à un fichier PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddSoundAnnotation()
{
    // Open PDF document
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        var mediaFile = dataDir + "file_example_WAV_1MG.wav";

        // Create Sound Annotation
        var soundAnnotation = new Aspose.Pdf.Annotations.SoundAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(20, 700, 60, 740),
            mediaFile)
        {
            Color = Aspose.Pdf.Color.Blue,
            Title = "John Smith",
            Subject = "Sound Annotation demo",
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(20, 700, 60, 740))
        };

        document.Pages[1].Annotations.Add(soundAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddSoundAnnotation_out.pdf");
    }
}
```

## Ajouter RichMediaAnnotation

Le code suivant montre comment ajouter RichMediaAnnotation à un fichier PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRichMediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
        Page page = document.Pages.Add();

        // Define video and poster names
        const string videoName = "file_example_MP4_480_1_5MG.mp4";
        const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
        string skinName = "SkinOverAllNoFullNoCaption.swf";

        // Create RichMediaAnnotation
        var rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600));

        // Specify the stream containing the video player code
        rma.CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp, "Players", "Videoplayer.swf"), FileMode.Open, FileAccess.Read);

        // Compose flash variables line for the player
        rma.CustomFlashVariables = $"source={videoName}&skin={skinName}";

        // Add skin code
        rma.AddCustomData(skinName, new FileStream(Path.Combine(pathToAdobeApp, skinName), FileMode.Open, FileAccess.Read));

        // Set poster for the video
        rma.SetPoster(new FileStream(Path.Combine(dataDir, posterName), FileMode.Open, FileAccess.Read));

        // Set video content
        using (Stream fs = new FileStream(Path.Combine(dataDir, videoName), FileMode.Open, FileAccess.Read))
        {
            rma.SetContent(videoName, fs);
        }

        // Set type of the content (video)
        rma.Type = RichMediaAnnotation.ContentType.Video;

        // Activate player by click
        rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

        // Update annotation data
        rma.Update();

        // Add annotation to the page
        page.Annotations.Add(rma);

        // Save PDF document
        document.Save(dataDir + "RichMediaAnnotation_out.pdf");
    }
}
```

### Obtenir MultimediaAnnotation

Veuillez essayer d'utiliser le code suivant pour obtenir MultimediaAnnotation à partir d'un document PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetMultimediaAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get multimedia annotations (Screen, Sound, RichMedia)
        var mediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Screen
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Sound
                        || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.Annotation>();

        // Iterate through the annotations and print their details
        foreach (var ma in mediaAnnotations)
        {
            Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
        }
    }
}
```

### Supprimer MultimediaAnnotation

Le code suivant montre comment supprimer MultimediaAnnotation d'un fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePolyAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RichMediaAnnotation.pdf"))
    {
        // Get RichMedia annotations
        var richMediaAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.RichMedia)
            .Cast<Aspose.Pdf.Annotations.RichMediaAnnotation>();

        // Delete each RichMedia annotation
        foreach (var rma in richMediaAnnotations)
        {
            document.Pages[1].Annotations.Delete(rma);
        }

        // Save PDF document
        document.Save(dataDir + "DeletePolyAnnotation_out.pdf");
    }
}
```

## Ajouter des annotations de widget

Les formulaires interactifs utilisent des [Widget Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) pour représenter l'apparence des champs et gérer les interactions des utilisateurs.
Nous utilisons ces éléments de formulaire qui s'ajoutent à un PDF pour faciliter la saisie, la soumission d'informations ou effectuer d'autres interactions utilisateur.

Les annotations de widget sont une représentation graphique d'un champ de formulaire sur des pages spécifiques, donc nous ne pouvons pas les créer directement en tant qu'annotation.

Chaque annotation de widget aura des graphiques appropriés (apparence) en fonction de son type. Après création, certains aspects visuels peuvent être modifiés, tels que le style de bordure et la couleur de fond.
D'autres propriétés telles que la couleur du texte et la police peuvent être modifiées via le champ, une fois attaché à l'un d'eux.

Dans certains cas, vous pouvez vouloir qu'un champ apparaisse sur plus d'une page, répétant la même valeur. Dans ce cas, les champs qui ont normalement juste un widget peuvent avoir plusieurs widgets attachés : un TextField, ListBox, ComboBox et CheckBox ont généralement exactement un, tandis que le RadioGroup a plusieurs widgets, un pour chaque bouton radio.
Une personne remplissant le formulaire peut utiliser n'importe lequel de ces widgets pour mettre à jour la valeur du champ, et cela se reflète également dans tous les autres widgets.

Chaque champ de formulaire pour chaque emplacement dans le document représente une annotation de widget. Les données spécifiques à l'emplacement de l'annotation de widget sont ajoutées à la page particulière. Chaque champ de formulaire a plusieurs variations. Un bouton peut être un bouton radio, une case à cocher ou un bouton-poussoir. Un widget de choix peut être une liste déroulante ou une boîte combinée.

Dans cet exemple, nous allons apprendre à ajouter des boutons-poussoirs pour la navigation dans le document.

### Ajouter un bouton au document

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPrintButton()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Define the rectangle for the button
        var rect = new Aspose.Pdf.Rectangle(72, 748, 164, 768);

        // Create a button field
        var printButton = new Aspose.Pdf.Forms.ButtonField(page, rect)
        {
            AlternateName = "Print current document",
            Color = Aspose.Pdf.Color.Black,
            PartialName = "printBtn1",
            NormalCaption = "Print Document"
        };

        // Set the border style for the button
        var border = new Aspose.Pdf.Annotations.Border(printButton)
        {
            Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
            Width = 2
        };
        printButton.Border = border;

        // Set the border and background color characteristics
        printButton.Characteristics.Border = System.Drawing.Color.FromArgb(255, 0, 0, 255);
        printButton.Characteristics.Background = System.Drawing.Color.FromArgb(255, 0, 191, 255);

        // Add the button to the form
        document.Form.Add(printButton);

        // Save PDF document
        document.Save(dataDir + "PrintButton_out.pdf");
    }
}
```

Ce bouton a une bordure et définit un arrière-plan. Nous définissons également un nom de bouton (Name), un tooltip (AlternateName), une étiquette (NormalCaption) et une couleur du texte de l'étiquette (Color).

### Utilisation des actions de navigation dans le document

Il existe un exemple plus complexe de l'utilisation des annotations de widget - la navigation dans le document PDF. Cela peut être nécessaire pour préparer une présentation de document PDF.

Cet exemple montre comment créer 4 boutons :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddNavigationButtons()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "JSON Fundamenals.pdf"))
    {
        // Create an array of button fields
        var buttons = new Aspose.Pdf.Forms.ButtonField[4];

        // Define alternate names and normal captions for the buttons
        var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
        var normalCaptions = new[] { "First", "Prev", "Next", "Last" };

        // Define predefined actions for the buttons
        PredefinedAction[] actions = {
            PredefinedAction.FirstPage,
            PredefinedAction.PrevPage,
            PredefinedAction.NextPage,
            PredefinedAction.LastPage
        };

        // Define border and background colors
        var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
        var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);

        // We should create the buttons without attaching them to the page.
        for (var i = 0; i < 4; i++)
        {
            buttons[i] = new Aspose.Pdf.Forms.ButtonField(document, new Aspose.Pdf.Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
            {
                AlternateName = alternateNames[i],
                Color = Aspose.Pdf.Color.White,
                NormalCaption = normalCaptions[i],
                OnActivated = new Aspose.Pdf.Annotations.NamedAction(actions[i])
            };

            // Set the border style for the button
            buttons[i].Border = new Aspose.Pdf.Annotations.Border(buttons[i])
            {
                Style = Aspose.Pdf.Annotations.BorderStyle.Solid,
                Width = 2
            };

            // Set the border and background color characteristics
            buttons[i].Characteristics.Border = clrBorder;
            buttons[i].Characteristics.Background = clrBackGround;
        }

        // Duplicate the array of buttons on each page in the document
        for (var pageIndex = 1; pageIndex <= document.Pages.Count; pageIndex++)
        {
            for (var i = 0; i < 4; i++)
            {
                document.Form.Add(buttons[i], $"btn{pageIndex}_{i + 1}", pageIndex);
            }
        }

        // Save PDF document
        document.Save(dataDir + "NavigationButtons_out.pdf");

        // We call Form.Add method with the following parameters: field, name, and the index of the pages that this field will be added to.
        // And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

        document.Form["btn1_1"].ReadOnly = true;
        document.Form["btn1_2"].ReadOnly = true;

        document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
        document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
    }
}
```

Pour des informations plus détaillées et des possibilités de ces fonctionnalités, consultez également [Travailler avec des formulaires](/pdf/fr/net/acroforms/).

Dans les documents PDF, vous pouvez visualiser et gérer du contenu 3D de haute qualité créé avec des logiciels de CAO 3D ou de modélisation 3D et intégré dans le document PDF. Vous pouvez faire pivoter les éléments 3D dans toutes les directions comme si vous les teniez dans vos mains.

Pourquoi avez-vous besoin d'un affichage 3D d'images ?

Au cours des dernières années, la technologie a réalisé d'énormes avancées dans tous les domaines grâce à l'impression 3D. Les technologies d'impression 3D peuvent être appliquées pour enseigner des compétences technologiques dans la construction, le génie mécanique, le design comme principal outil. Ces technologies, grâce à l'émergence de dispositifs d'impression personnels, peuvent contribuer à l'introduction de nouvelles formes d'organisation du processus éducatif, augmenter la motivation et former les compétences nécessaires des diplômés et des enseignants.

La tâche principale de la modélisation 3D est l'idée d'un objet futur ou d'un objet car, pour libérer un objet, vous devez comprendre ses caractéristiques de conception dans tous les détails pour une régénération successive en design industriel ou en architecture.

## Ajouter une annotation 3D

L'annotation 3D est ajoutée à l'aide d'un modèle créé au format U3D.

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Chargez les données du modèle 3D souhaité (dans notre cas "Ring.u3d") pour créer [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent).
1. Créez un objet [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) et liez-le au document et au 3DContent.
1. Réglez l'objet pdf3dArtWork :

    - 3DLightingScheme - (nous allons définir `CAD` dans l'exemple)
    - 3DRenderMode - (nous allons définir `Solid` dans l'exemple)
    - Remplissez `ViewArray`, créez au moins une [3D View](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) et ajoutez-la au tableau.

1. Définissez 3 paramètres de base dans l'annotation :
    - la `page` sur laquelle l'annotation sera placée.
    - le `rectangle`, à l'intérieur duquel se trouve l'annotation.
    - et l'objet `3dArtWork`.
1. Pour une meilleure présentation de l'objet 3D, définissez le cadre de bordure.
1. Définissez la vue par défaut (par exemple - TOP).
1. Ajoutez quelques paramètres supplémentaires : nom, affiche de prévisualisation, etc.
1. Ajoutez l'annotation à la [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Enregistrez le résultat.

### Exemple

Veuillez consulter le code suivant pour ajouter une annotation 3D.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Add3dAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Load 3D content
        var pdf3DContent = new Aspose.Pdf.Annotations.PDF3DContent(dataDir + "Ring.u3d");

        // Create 3D artwork
        var pdf3dArtWork = new Aspose.Pdf.Annotations.PDF3DArtwork(document, pdf3DContent)
        {
            LightingScheme = new Aspose.Pdf.Annotations.PDF3DLightingScheme(Aspose.Pdf.Annotations.LightingSchemeType.CAD),
            RenderMode = new Aspose.Pdf.Annotations.PDF3DRenderMode(Aspose.Pdf.Annotations.RenderModeType.Solid),
        };

        // Define matrices for different views
        var topMatrix = new Aspose.Pdf.Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Aspose.Pdf.Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);

        // Add views to the 3D artwork
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.ViewArray.Add(new Aspose.Pdf.Annotations.PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        // Add page
        var page = document.Pages.Add();

        // Create a 3D annotation
        var pdf3dAnnotation = new Aspose.Pdf.Annotations.PDF3DAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.Border = new Aspose.Pdf.Annotations.Border(pdf3dAnnotation);
        pdf3dAnnotation.SetDefaultViewIndex(1);
        pdf3dAnnotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.NoZoom;
        pdf3dAnnotation.Name = "Ring.u3d";

        // Set preview image if needed
        // pdf3dAnnotation.SetImagePreview(dataDir + "sample_3d.png");

        // Add the 3D annotation to the page
        document.Pages[1].Annotations.Add(pdf3dAnnotation);

        // Save PDF document
        document.Save(dataDir + "Add3dAnnotation_out.pdf");
    }
}
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
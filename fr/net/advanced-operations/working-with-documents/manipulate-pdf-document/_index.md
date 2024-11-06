---
title: Manipuler un document PDF en C#
linktitle: Manipuler un document PDF
type: docs
weight: 20
url: fr/net/manipulate-pdf-document/
description: Cet article contient des informations sur comment valider un document PDF pour la norme PDF A, comment travailler avec la table des matières, comment définir la date d'expiration d'un PDF, etc.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipuler un document PDF",
    "alternativeHeadline": "Comment manipuler un fichier PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, dotnet, manipuler un fichier PDF",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article contient des informations sur comment valider un document PDF pour la norme PDF A, comment travailler avec la table des matières, comment définir la date d'expiration d'un PDF, etc."
}
</script>
## **Manipuler un document PDF en C#**

## Valider un document PDF selon la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A-1a ou PDF/A-1b, utilisez la méthode Validate de la classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être sauvegardé et le type de validation requis dans l'énumération [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) : PDF_A_1A ou PDF_A_1B.

{{% alert color="primary" %}}

Le format XML de sortie est un format personnalisé Aspose. Le XML contient une collection de balises avec le nom Problème; chaque balise contient les détails d'un problème particulier. L'attribut ObjectID de la balise Problème représente l'ID de l'objet particulier auquel ce problème est lié. L'attribut Clause représente une règle correspondante dans la spécification PDF.

{{% /alert %}}

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le fragment de code suivant vous montre comment valider un document PDF pour PDF/A-1A.
Le code suivant vous montre comment valider un document PDF pour PDF/A-1A.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Valider le PDF pour PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

Le code suivant vous montre comment valider un document PDF pour PDF/A-1B.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Valider le PDF pour PDF/A-1B
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF pour .NET peut être utilisé pour déterminer si le document chargé est un PDF valide et également [s'il est crypté ou non](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Pour étendre davantage les capacités de la classe Document, une propriété *IsPdfaCompliant* est ajoutée pour déterminer si le fichier d'entrée est conforme PDF/A et une propriété nommée *PdfaFormat* pour identifier le format PDF/A sont introduites.

{{% /alert %}}

## Travailler avec la TOC

### Ajouter une TOC à un PDF existant

L'API Aspose.PDF vous permet d'ajouter une table des matières soit lors de la création d'un PDF, soit à un fichier existant. La classe ListSection dans l'espace de noms Aspose.Pdf.Generator vous permet de créer une table des matières lors de la création d'un PDF à partir de zéro. Pour ajouter des titres, qui sont des éléments de la TOC, utilisez la classe Aspose.Pdf.Generator.Heading.

Pour ajouter une TOC à un fichier PDF existant, utilisez la classe Heading dans l'espace de noms Aspose.Pdf.
Pour ajouter une table des matières à un fichier PDF existant, utilisez la classe Heading dans l'espace de noms Aspose.Pdf.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Charger un fichier PDF existant
Document doc = new Document(dataDir + "AddTOC.pdf");

// Accéder à la première page du fichier PDF
Page tocPage = doc.Pages.Insert(1);

// Créer un objet pour représenter les informations de la table des matières
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table des matières");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Définir le titre pour la table des matières
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Créer des objets de chaîne qui seront utilisés comme éléments de la table des matières
string[] titles = new string[4];
titles[0] = "Première page";
titles[1] = "Deuxième page";
titles[2] = "Troisième page";
titles[3] = "Quatrième page";
for (int i = 0; i < 2; i++)
{
    // Créer un objet Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Spécifier la page de destination pour l'objet Heading
    heading2.DestinationPage = doc.Pages[i + 2];

    // Page de destination
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // Coordonnée de destination
    segment2.Text = titles[i];

    // Ajouter le titre à la page contenant la table des matières
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```
### Définir différents types de TabLeader pour différents niveaux de TOC

Aspose.PDF permet également de définir différents types de TabLeader pour différents niveaux de TOC. Vous devez définir la propriété LineDash de FormatArray avec la valeur appropriée de l'énumération TabLeaderType comme suit.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//définir LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Table des matières");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//Ajouter la section liste à la collection de sections du document PDF
tocPage.TocInfo = tocInfo;
//Définir le format des quatre niveaux de liste en définissant les marges gauche
//et
//les paramètres de format de texte de chaque niveau

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//Créer une section dans le document PDF
Page page = doc.Pages.Add();

//Ajouter quatre titres dans la section
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Titre exemple" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //Ajouter le titre à la table des matières.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// sauvegarder le PDF

doc.Save(outFile);
```
### Masquer les numéros de page dans la TOC

Dans le cas où vous ne souhaitez pas afficher les numéros de page, ainsi que les titres dans la TOC, vous pouvez utiliser la propriété [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) de la classe [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) sur false. Veuillez consulter l'extrait de code suivant pour masquer les numéros de page dans la table des matières :

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table des matières");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Ajoutez la section de liste à la collection de sections du document PDF
tocPage.TocInfo = tocInfo;
//Définir le format des quatre niveaux de liste en réglant les marges gauche et
//les paramètres de format de texte de chaque niveau

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//Ajoutez quatre titres dans la section
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "ceci est un titre de niveau " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### Personnaliser les numéros de page lors de l'ajout d'une table des matières

Il est courant de personnaliser la numérotation des pages dans la table des matières lors de l'ajout d'une table des matières dans un document PDF. Par exemple, nous pourrions avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans un tel cas, Aspose.PDF pour .NET fournit la propriété PageNumbersPrefix de la classe TocInfo qui peut être utilisée pour personnaliser les numéros de page comme le montre l'exemple de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// Charger un fichier PDF existant
Document doc = new Document(inFile);
// Accéder à la première page du fichier PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// Créer un objet pour représenter les informations de la table des matières
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Table des matières");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Définir le titre pour la table des matières
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Créer un objet Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Spécifier la page de destination pour l'objet titre
    heading2.DestinationPage = doc.Pages[i + 1];
    // Page de destination
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // Coordonnée de destination
    segment2.Text = "Page " + i.ToString();
    // Ajouter le titre à la page contenant la table des matières
    tocPage.Paragraphs.Add(heading2);
}

// Sauvegarder le document mis à jour
doc.Save(outFile);
```
## Comment définir la date d'expiration du PDF

Nous appliquons des privilèges d'accès sur les fichiers PDF afin qu'un certain groupe d'utilisateurs puisse accéder à des fonctionnalités/objets particuliers des documents PDF. Afin de restreindre l'accès au fichier PDF, nous appliquons généralement un chiffrement et nous pouvons avoir besoin de définir une date d'expiration du fichier PDF, de sorte que l'utilisateur accédant/consultant le document reçoive une invite valide concernant l'expiration du fichier PDF.

Pour accomplir l'exigence mentionnée ci-dessus, nous pouvons utiliser l'objet *JavascriptAction*. Veuillez regarder le fragment de code suivant.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instancier l'objet Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// Ajouter une page à la collection de pages du fichier PDF
doc.Pages.Add();
// Ajouter un fragment de texte à la collection de paragraphes de l'objet page
doc.Pages[1].Paragraphs.Add(new TextFragment("Bonjour le monde..."));
// Créer un objet JavaScript pour définir la date d'expiration du PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');");
// Définir le JavaScript comme action d'ouverture du PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// Sauvegarder le document PDF
doc.Save(dataDir);
```
## Déterminer la progression de la génération de fichiers PDF

Un client nous a demandé d'ajouter une fonctionnalité permettant aux développeurs de déterminer la progression de la génération de fichiers PDF. Voici la réponse à cette demande.

Le champ [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) de la classe [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) vous permet de déterminer comment se déroule la génération du PDF. Le gestionnaire a les types suivants :

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

Les extraits de code ci-dessous montrent comment utiliser CustomerProgressHandler.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Avancement de la conversion : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - Page source {1} sur {2} analysée.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Mise en page du résultat {1} sur {2} créée.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Page de résultat {1} sur {2} exportée.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## Aplatir un PDF remplissable en C#

Les documents PDF incluent souvent des formulaires avec des widgets interactifs remplissables tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour le rendre non modifiable pour diverses applications, nous devons aplatir le fichier PDF.
Aspose.PDF fournit la fonction pour aplatir votre PDF en C# avec juste quelques lignes de code :

```csharp

// Charger le formulaire PDF source
Document doc = new Document(dataDir + "input.pdf");

// Aplatir le PDF remplissable
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```


---
title: Create AcroForm - Create Fillable PDF in C#
linktitle: Create AcroForm
type: docs
weight: 10
url: /net/create-form/
description: Avec Aspose.PDF pour .NET, vous pouvez créer un formulaire à partir de zéro dans votre fichier PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm",
    "alternativeHeadline": "Comment créer AcroForm dans PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, créer acroform",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Avec Aspose.PDF pour .NET, vous pouvez créer un formulaire à partir de zéro dans votre fichier PDF"
}
</script>
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Créer un formulaire à partir de zéro

### Ajouter un champ de formulaire dans un document PDF

La classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) fournit une collection nommée [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) qui vous aide à gérer les champs de formulaire dans un document PDF.

Pour ajouter un champ de formulaire :

1. Créez le champ de formulaire que vous souhaitez ajouter.
1. Appelez la méthode Add de la collection [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### Ajout de TextBoxField

L'exemple ci-dessous montre comment ajouter un [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Créer un champ
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Ajouter le champ au document
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Sauvegarder le PDF modifié
pdfDocument.Save(dataDir);
```
### Ajout de RadioButtonField

Le code suivant montre comment ajouter [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) dans un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Instancier l'objet Document
Document pdfDocument = new Document();
// Ajouter une page au fichier PDF
pdfDocument.Pages.Add();
// Instancier l'objet RadioButtonField avec le numéro de page comme argument
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Ajouter la première option de bouton radio et spécifier également son origine à l'aide de l'objet Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Ajouter la deuxième option de bouton radio
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Ajouter le bouton radio à l'objet formulaire de l'objet Document
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Sauvegarder le fichier PDF
pdfDocument.Save(dataDir);
```
Le fragment de code suivant montre les étapes pour ajouter un RadioButtonField avec trois options et les placer dans des cellules de tableau.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// Enregistrer le fichier PDF
doc.Save(dataDir);
```

### Ajout de légende à RadioButtonField

Le fragment de code suivant montre comment ajouter une légende qui sera associée à RadioButtonField:

```csharp
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire PDF source
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Oui";
        fieldoption.PartialName = "NomOui";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // Créer un objet TextParagraph
        TextParagraph par = new TextParagraph();

        // Définir la position du paragraphe
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Spécifier le mode d'enveloppement des mots
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Ajouter un nouveau TextFragment au paragraphe
        par.AppendLine(updatedFragment);

        // Ajouter le TextParagraph en utilisant TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### Ajout d'un champ ComboBox

Le code suivant montre comment ajouter un champ ComboBox dans un document PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Créer un objet Document
Document doc = new Document();

// Ajouter une page à l'objet document
doc.Pages.Add();

// Instancier l'objet ComboBox Field
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Ajouter des options à ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// Ajouter l'objet combo box à la collection de champs de formulaire de l'objet document
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Sauvegarder le document PDF
doc.Save(dataDir);
```

### Ajouter une infobulle à un champ de formulaire

La classe Document fournit une collection nommée Form qui gère les champs de formulaire dans un document PDF.
La classe Document fournit une collection nommée Form qui gère les champs de formulaire dans un document PDF.

Les extraits de code qui suivent montrent comment ajouter une infobulle à un champ de formulaire, d'abord en utilisant C# puis Visual Basic.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Charger le formulaire PDF source
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Définir l'infobulle pour le champ de texte
(doc.Form["textbox1"] as Field).AlternateName = "Infobulle de la zone de texte";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Sauvegarder le document mis à jour
doc.Save(dataDir);
```


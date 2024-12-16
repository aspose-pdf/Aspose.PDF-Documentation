---
title: Extraire du texte depuis un PDF en C#
linktitle: Extraire du texte depuis un PDF
type: docs
weight: 10
url: /fr/net/extract-text-from-all-pdf/
description: Cet article décrit diverses manières d'extraire du texte des documents PDF en utilisant Aspose.PDF en C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du texte de toutes les pages d'un document PDF

Extraire du texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour .NET permet d'extraire du texte de toutes les pages d'un document PDF. Vous devez créer un objet de la classe **TextAbsorber**. Ensuite, ouvrez le PDF en utilisant la classe **Document** et appelez la méthode **Accept** de la collection **Pages**. La classe **TextAbsorber** absorbe le texte du document et le retourne dans la propriété **Text**. Le fragment de code suivant vous montre comment extraire du texte de toutes les pages d'un document PDF.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Créer un objet TextAbsorber pour extraire le texte
TextAbsorber textAbsorber = new TextAbsorber();
// Accepter l'absorbeur pour toutes les pages
pdfDocument.Pages.Accept(textAbsorber);
// Obtenir le texte extrait
string extractedText = textAbsorber.Text;
// Créer un écrivain et ouvrir le fichier
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Écrire une ligne de texte dans le fichier
tw.WriteLine(extractedText);
// Fermer le flux
tw.Close();
```
Appelez la méthode **Accept** sur une page particulière de l'objet Document. L'Index est le numéro de page particulier à partir duquel le texte doit être extrait.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// Créer un objet TextAbsorber pour extraire le texte
TextAbsorber textAbsorber = new TextAbsorber();
 
// Accepter l'absorbeur pour une page particulière
pdfDocument.Pages[1].Accept(textAbsorber);

// Obtenir le texte extrait
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// Créer un écrivain et ouvrir le fichier
TextWriter tw = new StreamWriter(dataDir);

// Écrire une ligne de texte dans le fichier
tw.WriteLine(extractedText);

// Fermer le flux
tw.Close();
```
## Extraire du texte des pages en utilisant Text Device

Vous pouvez utiliser la classe **TextDevice** pour extraire du texte d'un fichier PDF. TextDevice utilise TextAbsorber dans son implémentation, ainsi, en fait, ils font la même chose mais TextDevice est juste implémenté pour unifier l'approche "Device" pour extraire n'importe quoi de la page ImageDevice, PageDevice, etc. TextAbsorber peut extraire du texte de Page, du PDF entier ou de XForm, ce TextAbsorber est plus universel

### Extraire le texte de toutes les pages

Les étapes suivantes et l'extrait de code vous montrent comment extraire du texte d'un PDF en utilisant le dispositif de texte.

1. Créer un objet de la classe Document avec le fichier PDF d'entrée spécifié
1. Créer un objet de la classe TextDevice
1. Utiliser un objet de la classe TextExtractOptions pour spécifier les options d'extraction
1. Utiliser la méthode Process de la classe TextDevice pour convertir le contenu en texte
1. Sauvegarder le texte dans le fichier de sortie

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document( dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// Chaîne pour contenir le texte extrait
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // Créer un dispositif de texte
        TextDevice textDevice = new TextDevice();

        // Définir les options d'extraction du texte - définir le mode d'extraction du texte (Raw ou Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // Convertir une page particulière et sauvegarder le texte dans le flux
        textDevice.Process(pdfPage, textStream);
        // Convertir une page particulière et sauvegarder le texte dans le flux
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // Fermer le flux mémoire
        textStream.Close();

        // Obtenir le texte à partir du flux mémoire
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// Sauvegarder le texte extrait dans un fichier texte
File.WriteAllText(dataDir, builder.ToString());
```
## Extraire du texte d'une région spécifique de la page

La classe **TextAbsorber** offre la capacité d'extraire du texte d'une page particulière ou de toutes les pages d'un document PDF. Cette classe renvoie le texte extrait dans la propriété **Text**. Cependant, si nous avons besoin d'extraire du texte d'une région spécifique de la page, nous pouvons utiliser la propriété **Rectangle** de **TextSearchOptions**. La propriété Rectangle prend un objet Rectangle comme valeur et en utilisant cette propriété, nous pouvons spécifier la région de la page d'où nous devons extraire le texte.

La méthode **Accept** d'une page est appelée pour extraire le texte. Créez des objets des classes **Document** et **TextAbsorber**. Appelez la méthode **Accept** sur la page individuelle, comme l'index **Page**, de l'objet **Document**. L'**Index** est le numéro de page particulier d'où le texte doit être extrait. Vous pouvez obtenir le texte à partir de la propriété **Text** de la classe **TextAbsorber**. Le code suivant montre comment extraire du texte d'une page individuelle.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// Créer un objet TextAbsorber pour extraire le texte
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// Accepter l'absorbeur pour la première page
pdfDocument.Pages[1].Accept(absorber);

// Obtenir le texte extrait
string extractedText = absorber.Text;
// Créer un écrivain et ouvrir le fichier
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// Écrire une ligne de texte dans le fichier
tw.WriteLine(extractedText);
// Fermer le flux
tw.Close();
```

## Extraire le texte basé sur des colonnes

Un fichier PDF peut comprendre des éléments Texte, Image, Annotations, Pièces jointes, Graphiques, etc. et Aspose.PDF pour .NET offre la fonctionnalité d'ajouter ainsi que de manipuler tous ces éléments.
Un fichier PDF peut contenir du Texte, des Images, des Annotations, des Pièces jointes, des Graphiques, etc., et Aspose.PDF pour .NET offre la possibilité d'ajouter ainsi que de manipuler tous ces éléments.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // Besoin de réduire la taille de la police d'au moins 70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```

### Deuxième approche - Utilisation du ScaleFactor

Dans cette nouvelle version, nous avons également introduit plusieurs améliorations dans TextAbsorber et dans le mécanisme de formatage de texte interne. Ainsi, maintenant lors de l'extraction de texte en utilisant le mode ‘Pure’, vous pouvez spécifier l'option ScaleFactor et cela peut être une autre approche pour extraire le texte d'un document PDF multi-colonnes en plus de l'approche mentionnée ci-dessus. Ce facteur d'échelle peut être réglé pour ajuster la grille qui est utilisée pour le mécanisme de formatage de texte interne lors de l'extraction de texte. Spécifier les valeurs de ScaleFactor entre 1 et 0.1 (y compris 0.1) a le même effet que la réduction de la taille de la police.

Spécifier les valeurs de ScaleFactor entre 0.1 et -0.1 est traité comme une valeur nulle, mais cela amène l'algorithme à calculer le facteur d'échelle nécessaire pendant l'extraction automatique du texte.
Spécifier des valeurs de ScaleFactor entre 0,1 et -0,1 est considéré comme une valeur nulle, mais cela permet à l'algorithme de calculer le facteur d'échelle nécessaire lors de l'extraction automatique du texte.

Nous proposons l'utilisation de l'auto-échelonnement (ScaleFactor = 0) lors du traitement d'un grand nombre de fichiers PDF pour l'extraction de contenu textuel. Ou réglez manuellement la réduction redondante de la largeur de la grille (environ ScaleFactor = 0,5). Cependant, vous ne devez pas déterminer si un dimensionnement est nécessaire pour des documents concrets ou non. Si vous définissez une réduction redondante de la largeur de la grille pour le document (qui n'en a pas besoin), le contenu textuel extrait restera pleinement adéquat. Veuillez regarder l'extrait de code suivant.

L'extrait de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Ouvrir le document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// Définir un facteur d'échelle de 0,5 est suffisant pour diviser les colonnes dans la majorité des documents
// La définition de zéro permet à l'algorithme de choisir le facteur d'échelle automatiquement
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

Veuillez noter qu'il n'y a pas de correspondance directe entre le nouveau ScaleFactor et l'ancien coefficient de réduction manuelle de la taille de la police. Cependant, par défaut, l'algorithme prend en compte la valeur de la taille de police qui a déjà été réduite pour certaines raisons internes. Par exemple, réduire la taille de la police de 10 à 7 a le même effet que de régler un facteur d'échelle à 5/8 (= 0.625).

{{% /alert %}}

## Extraire le Texte Surligné d'un Document PDF

Dans divers scénarios d'extraction de texte à partir d'un document PDF, vous pouvez avoir besoin d'extraire uniquement le texte surligné du document PDF. Afin de mettre en œuvre cette fonctionnalité, nous avons ajouté les méthodes TextMarkupAnnotation.GetMarkedText() et TextMarkupAnnotation.GetMarkedTextFragments() dans l'API. Vous pouvez extraire le texte surligné d'un document PDF en filtrant TextMarkupAnnotation et en utilisant les méthodes mentionnées. Le fragment de code suivant montre comment vous pouvez extraire le texte surligné d'un document PDF.

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// Parcourir toutes les annotations
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // Filtrer TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // Récupérer les fragments de texte mis en évidence
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // Afficher le texte mis en évidence
            Console.WriteLine(tf.Text);
        }
    }
}
```

## Accéder aux éléments Fragment de Texte et Segment depuis XML

Parfois, nous avons besoin d'accéder aux éléments TextFragement ou TextSegment lors du traitement de documents PDF générés à partir de XML.
Parfois, nous avons besoin d'accéder aux éléments TextFragement ou TextSegment lors du traitement de documents PDF générés à partir de XML.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```


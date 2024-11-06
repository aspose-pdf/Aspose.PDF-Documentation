---
title: Ajouter du texte au fichier PDF 
linktitle: Ajouter du texte au fichier PDF
type: docs
weight: 10
url: fr/java/ajouter-du-texte-au-fichier-pdf/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Découvrez comment ajouter du texte au PDF, ajouter des fragments HTML ou utiliser des polices OTF personnalisées.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrez le PDF d'entrée à l'aide de l'objet Document.
2. Obtenez la page particulière à laquelle vous souhaitez ajouter le texte.
3. Créez un objet TextFragment avec le texte d'entrée ainsi que d'autres propriétés de texte. L'objet TextBuilder créé à partir de cette page particulière – à laquelle vous souhaitez ajouter le texte – vous permet d'ajouter l'objet TextFragment à la page en utilisant la méthode AppendText.
4. Appelez la méthode Save de l'objet Document et enregistrez le fichier PDF de sortie.

## Ajout de texte

Le code suivant vous montre comment ajouter du texte dans un fichier PDF existant.

```java
public static void AddingText() {
    // Charger le fichier PDF
    Document document = new Document(_dataDir + "sample.pdf");

    // obtenir la page particulière
    Page pdfPage = document.getPages().get_Item(1);
    // créer un fragment de texte
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // définir les propriétés du texte
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // créer un objet TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // ajouter le fragment de texte à la page PDF
    textBuilder.appendText(textFragment);

    // Enregistrer le document PDF résultant.
    document.save(_dataDir + "AddText_out.pdf");
}
```


## Chargement de la police depuis un flux

Le code suivant montre comment charger une police depuis un objet Stream lors de l'ajout de texte à un document PDF.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // Charger le fichier PDF d'entrée
    Document doc = new Document(_dataDir + "input.pdf");
    // Créer un objet TextBuilder pour la première page du document
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // Créer un fragment de texte avec une chaîne d'exemple
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // Charger la police TrueType dans l'objet Stream
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // Définir le nom de la police pour la chaîne de texte
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // Spécifier la position pour le fragment de texte
        textFragment.setPosition(new Position(10, 10));
        // Ajouter le texte au TextBuilder afin qu'il puisse être placé sur le fichier PDF
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // Enregistrer le document PDF résultant.
        doc.save(_dataDir); 
    }       
}
```


## Ajouter du texte en utilisant TextParagraph

Le code suivant montre comment ajouter du texte dans un document PDF en utilisant la classe [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph).

```java
public static void AddTextUsingTextParagraph() {
    // Ouvrir le document
    Document doc = new Document();
    // Ajouter une page à la collection de pages de l'objet Document
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // Créer un paragraphe de texte
    TextParagraph paragraph = new TextParagraph();
    // Définir l'indentation des lignes suivantes
    paragraph.setSubsequentLinesIndent (20);
    // Spécifier l'emplacement pour ajouter TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // Spécifier le mode de retour à la ligne
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // Créer un fragment de texte
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // Ajouter le fragment au paragraphe
    paragraph.appendLine(fragment1);
    // Ajouter le paragraphe
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // Enregistrer le document PDF résultant.
    doc.save(_dataDir);        
}
```


## Ajouter un Hyperlien à TextSegment

Une page PDF peut comprendre un ou plusieurs objets TextFragment, où chaque objet TextFragment peut avoir une ou plusieurs instances de TextSegment. Afin de définir un hyperlien pour TextSegment, la propriété Hyperlink de la classe TextSegment peut être utilisée tout en fournissant l'objet de l'instance Aspose.Pdf.WebHyperlink. Veuillez essayer d'utiliser l'extrait de code suivant pour répondre à cette exigence.

```java
public static void AddHyperlinkToTextSegment() {
    // Créer une instance de document
    Document doc = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page1 = doc.getPages().add();

    // Créer une instance de TextFragment
    TextFragment tf = new TextFragment("Fragment de texte d'exemple");
    // Définir l'alignement horizontal pour TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // Créer un textsegment avec un texte d'exemple
    TextSegment segment = new TextSegment(" ... Segment de texte 1...");
    // Ajouter le segment à la collection de segments de TextFragment
    tf.getSegments().add(segment);

    // Créer un nouveau TextSegment
    segment = new TextSegment("Lien vers Google");
    // Ajouter le segment à la collection de segments de TextFragment

    tf.getSegments().add(segment);

    // Définir l'hyperlien pour TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // Définir la couleur de premier plan pour le segment de texte
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // Définir la mise en forme du texte en italique
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // Créer un autre objet TextSegment
    segment = new TextSegment("TextSegment sans hyperlien");

    // Ajouter le segment à la collection de segments de TextFragment
    tf.getSegments().add(segment);

    // Ajouter TextFragment à la collection de paragraphes de l'objet page
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // Enregistrer le document PDF résultant.
    doc.save(_dataDir);

}
```


## Utiliser une police OTF

Aspose.PDF pour Java offre la possibilité d'utiliser des polices personnalisées/TrueType lors de la création/manipulation du contenu des fichiers PDF, de sorte que le contenu du fichier soit affiché en utilisant des polices autres que les polices système par défaut. À partir de la version 10.4.0 d'Aspose.PDF pour Java, nous avons fourni la prise en charge des polices Open Type.

```java
public static void UseOTFFont() {
    // Créer une nouvelle instance de document
    Document pdfDocument = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page = pdfDocument.getPages().add();
    // Créer une instance de TextFragment avec un texte d'exemple
    TextFragment fragment = new TextFragment("Exemple de texte en police OTF");
    // Ou vous pouvez même spécifier le chemin de la police OTF dans le répertoire système
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // Spécifier d'incorporer la police dans le fichier PDF, afin qu'elle soit affichée correctement,
    // Même si la police spécifique n'est pas installée/présente sur la machine cible
    fragment.getTextState().getFont().setEmbedded(true);
    // Ajouter TextFragment à la collection de paragraphes de l'instance Page
    page.getParagraphs().add(fragment);
    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## Ajouter une chaîne HTML en utilisant le DOM

La classe Aspose.Pdf.Generator.Text contient une propriété appelée IsHtmlTagSupported qui permet d'ajouter des balises/contenus HTML dans les fichiers PDF. Le contenu ajouté est rendu dans des balises HTML natives au lieu d'apparaître comme une simple chaîne de texte. Pour prendre en charge une fonctionnalité similaire dans le nouveau modèle d'objet de document (DOM) de l'espace de noms Aspose.Pdf, la classe HtmlFragment a été introduite.

L'instance [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) peut être utilisée pour spécifier les contenus HTML qui doivent être placés à l'intérieur du fichier PDF. Similaire à TextFragment, HtmlFragment est un objet au niveau du paragraphe et peut être ajouté à la collection de paragraphes de l'objet Page. Les extraits de code suivants montrent les étapes pour placer des contenus HTML à l'intérieur d'un fichier PDF en utilisant l'approche DOM.

```java
public static void AddingHtmlString() {
    // Instancier l'objet Document
    Document doc = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page = doc.getPages().add();
    // Instancier HtmlFragment avec des contenus HTML
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>Démo de chaîne HTML</strong></h1>");
    // définir MarginInfo pour les détails de la marge
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // Définir les informations de marge
    title.setMargin(Margin);
    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page.getParagraphs().add(title);
    // Enregistrer le fichier PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


Le fragment de code suivant démontre les étapes pour ajouter des listes ordonnées HTML dans le document :

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Instancier un objet Document
    Document doc = new Document();
    // Instancier un objet HtmlFragment avec le fragment HTML correspondant
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>Premier</li><li>Deuxième</li><li>Troisième</li><li>Quatrième</li><li>Cinquième</li></ul><p>Texte après la liste.</p><p>Ligne suivante<br/>Dernière ligne</p></div>");
    // Ajouter une page dans la collection de pages
    Page page = doc.getPages().add();
    // Ajouter HtmlFragment à l'intérieur de la page
    page.getParagraphs().add(t);
    // Sauvegarder le fichier PDF résultant
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

Vous pouvez également définir le formatage de chaîne HTML en utilisant l'objet TextState comme suit :

```java
public static void AddHTMLStringFormatting() {
    // Instancier un objet Document
    Document doc = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page = doc.getPages().add();
    // Instancier HtmlFragment avec le contenu HTML
    HtmlFragment title = new HtmlFragment("<h1><strong>Démo de chaîne HTML</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page.getParagraphs().add(title);
    // Sauvegarder le fichier PDF
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


Dans le cas où vous définissez certaines valeurs d'attributs de texte via le balisage HTML et que vous fournissez ensuite les mêmes valeurs dans les propriétés TextState, elles écraseront les paramètres HTML par les propriétés du formulaire d'instance TextState. Les extraits de code suivants montrent le comportement décrit.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Instancier un objet Document
    Document doc = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page = doc.getPages().add();
    // Instancier HtmlFragment avec des contenus HTML
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>La table contient du texte</i></b></p>");
    // La famille de polices de 'Verdana' sera réinitialisée à 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // Définir les informations de marge inférieure
    title.getMargin().setBottom(10);
    // Définir les informations de marge supérieure
    title.getMargin().setTop(400);
    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page.getParagraphs().add(title);
    // Enregistrer le fichier PDF
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## FootNotes et EndNotes (DOM)

Les FootNotes indiquent des notes dans le texte de votre document en utilisant des numéros en exposant consécutifs. La note réelle est indentée et peut apparaître en tant que note de bas de page en bas de la page.

### Ajout d'une FootNote

Dans un système de référence par note de bas de page, indiquez une référence en :

- plaçant un petit numéro au-dessus de la ligne de texte directement après le matériel source. Ce numéro est appelé un identifiant de note. Il se trouve légèrement au-dessus de la ligne de texte.
- plaçant le même numéro, suivi d'une citation de votre source, au bas de la page. Les notes de bas de page doivent être numériques et chronologiques : la première référence est 1, la seconde est 2, et ainsi de suite.

L'avantage des notes de bas de page est que le lecteur peut simplement baisser les yeux sur la page pour découvrir la source d'une référence qui l'intéresse.

Veuillez suivre les étapes spécifiées ci-dessous pour créer une FootNote :

- Créer une instance de Document
- Créer un objet Page
- Créer un objet TextFragment

- Créer une instance de Note et passer sa valeur à la propriété TextFragment.FootNote
- Ajouter TextFragment à la collection de paragraphes d'une instance de page

### Style de ligne personnalisé pour la note de bas de page

L'exemple suivant démontre comment ajouter des notes de bas de page au bas de la page PDF et définir un style de ligne personnalisé.

```java
public static void AddFootNote() {
    // créer une instance de Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Démo");
    t.setFootNote(note);

    // créer une instance de TextFragment
    TextFragment text = new TextFragment("Bonjour le monde");
    // définir la valeur de FootNote pour TextFragment
    text.setFootNote(new Note("note de bas de page pour le texte de test 1"));
    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page.getParagraphs().add(text);
    // créer le deuxième TextFragment
    text = new TextFragment("Aspose.Pdf pour Java");
    // définir FootNote pour le deuxième fragment de texte
    text.setFootNote(new Note("note de bas de page pour le texte de test 2"));
    // ajouter le deuxième fragment de texte à la collection de paragraphes du fichier PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


Nous pouvons définir le format de l'étiquette de note de bas de page (identifiant de note) en utilisant l'objet TextState comme suit :

```java
public static void AddCustomFootNoteLabel() {
    // créer une instance de Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Format de Document Portable");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Démo");
    t.setFootNote(note);

    // créer une instance de TextFragment
    TextFragment text = new TextFragment("Bonjour le monde");
    // définir la valeur de FootNote pour TextFragment
    text.setFootNote(new Note("note de bas de page pour le texte de test 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page.getParagraphs().add(text);
    // créer le deuxième TextFragment
    text = new TextFragment("Aspose.Pdf pour Java");
    // définir FootNote pour le deuxième fragment de texte
    text.setFootNote(new Note("note de bas de page pour le texte de test 2"));
    // ajouter le deuxième fragment de texte à la collection de paragraphes du fichier PDF
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### Personnaliser l'étiquette de note de bas de page

Par défaut, le numéro de la note de bas de page est incrémental à partir de 1. Cependant, nous pouvons avoir besoin de définir une étiquette de note de bas de page personnalisée. Pour répondre à cette exigence, veuillez essayer d'utiliser l'extrait de code suivant

```java
public static void CustomFootNote_Label() {
    // Créer une instance de Document
    Document document = new Document();
    // Ajouter une page à la collection de pages du PDF
    Page page = document.getPages().add();
    // Créer un objet GraphInfo
    GraphInfo graph = new GraphInfo();
    // Définir la largeur de ligne à 2
    graph.setLineWidth(2);
    // Définir la couleur pour l'objet graphique
    graph.setColor(Color.getRed());
    // Définir la valeur du tableau de tirets à 3
    graph.setDashArray(new int[] { 3 });
    // Définir la valeur de la phase de tirets à 1
    graph.setDashPhase(1);
    // Définir le style de ligne de note de bas de page pour la page comme graph
    page.setNoteLineStyle(graph);

    // Créer une instance de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // Définir la valeur de la note de bas de page pour TextFragment
    text.setFootNote(new Note("note de bas de page pour le texte de test 1"));
    // Spécifier une étiquette personnalisée pour la note de bas de page
    text.getFootNote().setText(" Aspose(2021)");
    // Ajouter TextFragment à la collection de paragraphes de la première page du document
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## Ajout d'une image et d'un tableau à la note de bas de page

Dans les versions précédentes, la prise en charge des notes de bas de page était fournie mais elle n'était applicable qu'à l'objet TextFragment. Cependant, à partir de la version Aspose.PDF for Java 10.7.0, vous pouvez également ajouter des notes de bas de page à d'autres objets dans le document PDF tels que Table, Cells, etc. Le snippet de code suivant montre les étapes pour ajouter une note de bas de page à l'objet TextFragment et ensuite ajouter un objet Image et Table à la collection de paragraphes de la section de la note de bas de page.

```java
public static void AddingImageAndTableToFootnote() {
    // Créer une instance de Document
    Document document = new Document();
    // Ajouter une page à la collection de pages du PDF
    Page page = document.getPages().add();
    // Créer une instance de TextFragment
    TextFragment text = new TextFragment("Bonjour le monde");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("texte de la note de bas de page");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Ligne 1 Cellule 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## Comment créer des notes de fin

Une note de fin est une citation de source qui renvoie les lecteurs à un endroit spécifique à la fin du document où ils peuvent trouver la source des informations ou des mots cités ou mentionnés dans le document. Lors de l'utilisation de notes de fin, votre phrase citée, paraphrasée ou résumée est suivie d'un numéro en exposant.

L'exemple suivant montre comment ajouter une note de fin dans la page PDF.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // ajouter une page à la collection de pages du PDF
    Page page = doc.getPages().add();
    // créer une instance de TextFragment
    TextFragment text = new TextFragment("Hello World");
    // définir la valeur de la note de fin pour TextFragment
    text.setEndNote(new Note("exemple de note de fin"));
    // spécifier une étiquette personnalisée pour la note de fin
    text.getEndNote().setText(" Aspose(2021)");
    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page.getParagraphs().add(text);
    // enregistrer le fichier PDF
    doc.save(_dataDir + "EndNote.pdf");
}
```


## Texte et Image en Paragraphe Inline

La mise en page par défaut du fichier PDF est une mise en page fluide (de haut-gauche à bas-droite). Par conséquent, chaque nouvel élément ajouté au fichier PDF est ajouté dans le flux en bas à droite. Cependant, nous pouvons avoir besoin d'afficher divers éléments de page, c'est-à-dire une image et du texte au même niveau (l'un après l'autre). Une approche peut être de créer une instance de Table et d'ajouter les deux éléments à des objets de cellule individuels. Cependant, une autre approche peut être le paragraphe inline. En définissant la propriété IsInLineParagraph de l'image et du texte sur vrai, ces paragraphes apparaîtront en ligne avec les autres éléments de la page.

Le fragment de code suivant vous montre comment ajouter du texte et une image comme paragraphes inline dans un fichier PDF.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Instancier l'instance Document
    Document doc = new Document();
    // Ajouter une page à la collection de pages de l'instance Document
    Page page = doc.getPages().add();
    // Créer un TextFragment
    TextFragment text = new TextFragment("Bonjour le monde.. ");
    // Ajouter le fragment de texte à la collection de paragraphes de l'objet Page
    page.getParagraphs().add(text);
    // Créer une instance d'image
    Image image = new Image();
    // Définir l'image comme paragraphe inline pour qu'elle apparaisse juste après
    // L'objet précédent du paragraphe (TextFragment)
    image.setInLineParagraph (true);
    // Spécifier le chemin du fichier image
    image.setFile(_dataDir + "aspose-logo.jpg");
    // Définir la hauteur de l'image (facultatif)
    image.setFixHeight(30);
    // Définir la largeur de l'image (facultatif)
    image.setFixWidth(100);
    // Ajouter l'image à la collection de paragraphes de l'objet page
    page.getParagraphs().add(image);
    // Réinitialiser l'objet TextFragment avec un contenu différent
    text = new TextFragment(" Bonjour encore..");
    // Définir TextFragment comme paragraphe inline
    text.setInLineParagraph (true);
    // Ajouter le nouvellement créé TextFragment à la collection de paragraphes de la page
    page.getParagraphs().add(text);

    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## Spécifier l'espacement des caractères lors de l'ajout de texte

Un texte peut être ajouté à l'intérieur de la collection de paragraphes des fichiers PDF en utilisant une instance de TextFragment ou en utilisant un objet TextParagraph et vous pouvez même tamponner le texte à l'intérieur du PDF en utilisant la classe TextStamp. Lors de l'ajout du texte, nous pouvons avoir besoin de spécifier l'espacement des caractères pour les objets texte. Afin de répondre à cette exigence, une nouvelle propriété nommée propriété CharacterSpacing a été introduite. Veuillez consulter les approches suivantes pour satisfaire cette exigence.

Les approches suivantes montrent les étapes pour spécifier l'espacement des caractères lors de l'ajout de texte à l'intérieur d'un document PDF.

## Utilisation de TextBuilder et TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // Créer une instance de Document
    Document pdfDocument = new Document();
    // Ajouter une page à la collection de pages du Document
    Page page = pdfDocument.getPages().add();
    // Créer une instance de TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Créer une instance de fragment de texte avec des contenus d'exemple
    TextFragment wideFragment = new TextFragment("Texte avec espacement des caractères augmenté");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // Spécifier l'espacement des caractères pour TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // Spécifier la position du TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // Ajouter le TextFragment à l'instance de TextBuilder
    builder.appendText(wideFragment);        
    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## Utilisation de TextBuilder et TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // Créer une instance de Document
    Document pdfDocument = new Document();
    // Ajouter une page à la collection de pages du Document
    Page page = pdfDocument.getPages().add();
    // Créer une instance de TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Instancier une instance de TextParagraph
    TextParagraph paragraph = new TextParagraph();
    // Créer une instance de TextState pour spécifier le nom et la taille de la police
    TextState state = new TextState("Arial", 12);
    // Spécifier l'espacement des caractères
    state.setCharacterSpacing(1.5f);
    // Ajouter du texte à l'objet TextParagraph
    paragraph.appendLine("Ceci est un paragraphe avec espacement des caractères", state);
    // Spécifier la position pour TextParagraph
    paragraph.setPosition(new Position(100, 550));
    // Ajouter TextParagraph à l'instance de TextBuilder
    builder.appendParagraph(paragraph);
    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## Utilisation de TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // Créer une instance de Document
    Document pdfDocument = new Document();
    // Ajouter une page à la collection de pages du document
    Page page = pdfDocument.getPages().add();
    // Instancier une instance de TextStamp avec un texte d'exemple
    TextStamp stamp = new TextStamp("Ceci est un tampon de texte avec espacement des caractères");
    // Spécifier le nom de la police pour l'objet Stamp
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // Spécifier la taille de la police pour TextStamp
    stamp.getTextState().setFontSize(12);
    // Spécifier l'espacement des caractères à 1f
    stamp.getTextState().setCharacterSpacing(1f);
    // Définir le XIndent pour Stamp
    stamp.setXIndent(100);
    // Définir le YIndent pour Stamp
    stamp.setYIndent(500);
    // Ajouter un tampon textuel à l'instance de la page
    stamp.put(page);        
    // Enregistrer le document PDF résultant.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## Créer un document PDF multi-colonnes

Dans les magazines et les journaux, nous voyons principalement que les nouvelles sont affichées en plusieurs colonnes sur les pages uniques, contrairement aux livres où les paragraphes de texte sont principalement imprimés sur des pages entières de la gauche vers la droite.
 De nombreuses applications de traitement de documents comme Microsoft Word et Adobe Acrobat Writer permettent aux utilisateurs de créer plusieurs colonnes sur une seule page et ensuite d'y ajouter des données.

Aspose.PDF pour Java offre également la fonctionnalité de créer plusieurs colonnes à l'intérieur des pages des documents PDF. Afin de créer un fichier PDF à colonnes multiples, nous pouvons utiliser la classe Aspose.Pdf.FloatingBox car elle fournit la propriété ColumnInfo.ColumnCount pour spécifier le nombre de colonnes à l'intérieur de FloatingBox et nous pouvons également spécifier l'espacement entre les colonnes et les largeurs des colonnes en utilisant les propriétés ColumnInfo.ColumnSpacing et ColumnInfo.ColumnWidths en conséquence. Veuillez noter que FloatingBox est un élément à l'intérieur du modèle d'objet de document et qu'il peut avoir un positionnement obsolète par rapport au positionnement relatif (c'est-à-dire Texte, Graphique, Image, etc.).
Column spacing signifie l'espace entre les colonnes et l'espacement par défaut entre les colonnes est de 1,25 cm. Si la largeur de la colonne n'est pas spécifiée, Aspose.PDF pour Java calcule automatiquement la largeur de chaque colonne en fonction de la taille de la page et de l'espacement des colonnes.

Un exemple est donné ci-dessous pour démontrer la création de deux colonnes avec des objets Graphs (Ligne) et ils sont ajoutés à la collection de paragraphes de FloatingBox, qui est ensuite ajoutée à la collection de paragraphes de l'instance de Page.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // Spécifiez l'information de la marge gauche pour le fichier PDF
    doc.getPageInfo().getMargin().setLeft(40);
    
    // Spécifiez l'information de la marge droite pour le fichier PDF
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // Ajoutez la ligne à la collection de paragraphes de l'objet section
    page.getParagraphs().add(graph1);

    // Spécifiez les coordonnées pour la ligne
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // Créez des variables de chaîne avec du texte contenant des balises html
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> Comment éviter les arnaques financières</<strong> </span>";
    
    // Créez des paragraphes de texte contenant du texte HTML

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // Ajoutez quatre colonnes dans la section
    box.getColumnInfo().setColumnCount(2);
    // Définissez l'espacement entre les colonnes
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("Par Un Googlien (Le Blog Officiel de Google)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // Créez un objet de graphiques pour dessiner une ligne
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // Spécifiez les coordonnées pour la ligne
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // Ajoutez la ligne à la collection de paragraphes de l'objet section
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // Enregistrez le fichier PDF
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## Travailler avec des tabulations personnalisées

Une tabulation est un point d'arrêt pour le tabulateur. Dans le traitement de texte, chaque ligne contient un certain nombre de tabulations placées à intervalles réguliers (par exemple, tous les demi-pouces). Cependant, elles peuvent être modifiées, car la plupart des traitements de texte vous permettent de définir des tabulations où vous voulez. Lorsque vous appuyez sur la touche Tab, le curseur ou le point d'insertion saute à la tabulation suivante, qui elle-même est invisible. Bien que les tabulations n'existent pas dans le fichier texte, le traitement de texte les suit afin de pouvoir réagir correctement à la touche Tab.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) permet aux développeurs d'utiliser des tabulations personnalisées dans les documents PDF. La classe Aspose.Pdf.Text.TabStop est utilisée pour définir des tabulations personnalisées dans la classe [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment).

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) offre également certains types de leader de tabulation prédéfinis sous la forme d'une énumération nommée TabLeaderType dont les valeurs prédéfinies et leurs descriptions sont données ci-dessous :

|**Tab Leader Type**|**Description**|
| :- | :- |
|None|Pas de guide-tabulation|
|Solid|Guide-tabulation solide|
|Dash|Guide-tabulation en tirets|
|Dot|Guide-tabulation en points|

Voici un exemple de comment définir des tabulations personnalisées.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("Ceci est un exemple de formation de tableau avec des tabulations", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## Comment ajouter du texte transparent dans un PDF

Un fichier PDF contient des objets Image, Texte, Graphiques, pièces jointes, Annotations et lors de la création d'un TextFragment, vous pouvez définir des informations de couleur de premier plan, d'arrière-plan ainsi que le formatage du texte. Aspose.PDF pour Java prend en charge la fonctionnalité d'ajouter du texte avec un canal de couleur Alpha. Le code suivant montre comment ajouter du texte avec une couleur transparente.

```java
  public static void AddTransparentText() {
    // Créer une instance de Document
    Document pdfdocument = new Document();
    // Ajouter une page à la collection de pages du fichier PDF
    Page page = pdfdocument.getPages().add();

    // Créer un objet Graph
    Graph canvas = new Graph(100, 400);
    // Créer une instance de rectangle avec certaines dimensions
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // Créer un objet couleur à partir du canal de couleur Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Ajouter le rectangle à la collection de formes de l'objet Graph
    canvas.getShapes().add(rect);
    // Ajouter l'objet graph à la collection de paragraphes de l'objet page
    page.getParagraphs().add(canvas);
    // Définir la valeur pour ne pas changer la position de l'objet graph
    canvas.setChangePosition(false);

    // Créer une instance de TextFragment avec une valeur d'exemple
    TextFragment text = new TextFragment(
            "texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent ");
    // Créer un objet couleur à partir du canal Alpha
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // Définir les informations de couleur pour l'instance de texte
    text.getTextState().setForegroundColor (alphaColor);
    // Ajouter le texte à la collection de paragraphes de l'instance de page
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## Spécifier l'espacement des lignes pour les polices

Chaque police a un carré abstrait, dont la hauteur est la distance prévue entre les lignes de texte de la même taille de police. Ce carré est appelé le `carré em` et c'est la grille de conception sur laquelle les contours des glyphes sont définis. De nombreuses lettres de la police d'entrée ont des points qui sont placés en dehors des limites du `carré em` de la police, donc pour afficher correctement la police, l'utilisation d'un réglage spécial est nécessaire. L'objet TextFragment a un ensemble d'options de formatage de texte qui sont accessibles via la méthode [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
Cette méthode retourne la classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions).
 Cette classe a une énumération [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode) qui est conçue pour des polices spécifiques, par exemple la police d'entrée "HPSimplified.ttf". De plus, la classe [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) a une méthode [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) du type LineSpacingMode. Il vous suffit de définir LineSpacing en LineSpacingMode.FullSize. Le code pour afficher correctement une police serait comme suit :

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // Charger le fichier PDF d'entrée
    Document doc = new Document();
    // Créer TextFormattingOptions avec LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // Créer un objet text builder pour la première page du document
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // Créer un fragment de texte avec une chaîne exemple
    TextFragment textFragment = new TextFragment("Hello world");

    // Charger la police TrueType dans l'objet stream
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // Définir le nom de la police pour la chaîne de texte
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // Spécifier la position pour le fragment de texte
    textFragment.setPosition(new Position(100, 600));
    // Définir TextFormattingOptions du fragment courant à prédéfini (qui pointe vers
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // Ajouter le texte à TextBuilder afin qu'il puisse être placé sur le fichier PDF
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // Sauvegarder le document PDF résultant
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## Obtenir la largeur du texte dynamiquement

Parfois, il est nécessaire d'obtenir la largeur du texte dynamiquement. Aspose.PDF pour Java inclut deux méthodes pour la mesure de la largeur des chaînes. Vous pouvez invoquer la méthode [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) des classes com.aspose.pdf.Font ou com.aspose.pdf.TextState (ou les deux). L'extrait de code ci-dessous montre comment utiliser cette fonctionnalité.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("Mesure de la chaîne de caractères de police inattendue!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("Mesure de la chaîne de caractères de police inattendue!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("La mesure de la chaîne de caractères de la police et de l'état ne correspond pas!");
        }
}
```
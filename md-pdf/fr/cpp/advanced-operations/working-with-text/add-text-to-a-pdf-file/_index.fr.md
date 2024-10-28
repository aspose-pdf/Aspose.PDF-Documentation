---
title: Ajouter du Texte au PDF en utilisant C++
linktitle: Ajouter du Texte au PDF
type: docs
weight: 10
url: /cpp/add-text-to-pdf-file/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez à ajouter du texte au PDF, ajouter des fragments HTML ou utiliser des polices OTF personnalisées.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajout de Texte

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrez le PDF d'entrée à l'aide de l'objet Document.
2. Obtenez la page particulière à laquelle vous souhaitez ajouter le texte.
3. Créez un objet TextFragment avec le texte d'entrée ainsi que d'autres propriétés de texte. L'objet TextBuilder créé à partir de cette page particulière – à laquelle vous souhaitez ajouter le texte – vous permet d'ajouter l'objet TextFragment à la page en utilisant la méthode AppendText.
4. Appelez la méthode Save de l'objet Document et enregistrez le fichier PDF de sortie.

Le code ci-dessous vous montre comment ajouter du texte dans un fichier PDF existant.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Chargement de la police depuis un flux

Le code suivant montre comment charger une police à partir d'un objet Stream lors de l'ajout de texte à un document PDF.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Charger le fichier PDF d'entrée
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Créer un objet text builder pour la première page du document
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Créer un fragment de texte avec une chaîne d'exemple
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Charger la police TrueType dans l'objet stream
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Définir le nom de la police pour la chaîne de texte
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Spécifier la position pour le fragment de texte
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Ajouter le texte au TextBuilder afin qu'il puisse être placé sur le fichier PDF
        textBuilder->AppendText(textFragment);

        // Enregistrer le document PDF résultant.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Ajouter du texte en utilisant TextParagraph

Le snippet de code suivant montre comment ajouter du texte dans un document PDF en utilisant la classe [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Ouvrir le document
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Ajouter une page à la collection de pages de l'objet Document
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Créer un paragraphe de texte
    auto paragraph = MakeObject<TextParagraph>();

    // Définir l'indentation des lignes suivantes
    paragraph->set_SubsequentLinesIndent(20);

    // Spécifier l'emplacement pour ajouter TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Spécifier le mode de retour à la ligne
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Créer un fragment de texte
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Ajouter le fragment au paragraphe
    paragraph->AppendLine(fragment1);
    // Ajouter le paragraphe
    builder->AppendParagraph(paragraph);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}

```

## Ajouter un Hyperlien à TextSegment

Une page PDF peut être composée d'un ou plusieurs objets TextFragment, où chaque objet TextFragment peut avoir une ou plusieurs instances TextSegment. Afin de définir un hyperlien pour TextSegment, la propriété Hyperlink de la classe [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment) peut être utilisée tout en fournissant l'objet de l'instance Aspose.Pdf.WebHyperlink. Veuillez essayer d'utiliser l'extrait de code suivant pour accomplir cette exigence.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Créer une instance de document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page1 = document->get_Pages()->Add();

    // Créer une instance de TextFragment
    auto tf = MakeObject<TextFragment>("Fragment de texte d'exemple");
    // Définir l'alignement horizontal pour TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Créer un textsegment avec un texte d'exemple
    auto segment = MakeObject<TextSegment>(" ... Segment de texte 1...");
    // Ajouter le segment à la collection de segments de TextFragment
    tf->get_Segments()->Add(segment);

    // Créer un nouveau TextSegment
    segment = MakeObject<TextSegment>("Lien vers Google");
    // Ajouter le segment à la collection de segments de TextFragment

    tf->get_Segments()->Add(segment);

    // Définir un hyperlien pour TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Définir la couleur de premier plan pour le segment de texte
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Définir la mise en forme du texte en italique
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Créer un autre objet TextSegment
    segment = MakeObject<TextSegment>(u"TextSegment sans hyperlien");

    // Ajouter le segment à la collection de segments de TextFragment
    tf->get_Segments()->Add(segment);

    // Ajouter TextFragment à la collection de paragraphes de l'objet page
    page1->get_Paragraphs()->Add(tf);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);

}
```

## Utiliser la police OTF

Aspose.PDF pour С++ offre la possibilité d'utiliser des polices Custom/TrueType lors de la création/manipulation des contenus de fichiers PDF afin que les contenus des fichiers soient affichés en utilisant des polices autres que celles du système par défaut.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Créer une nouvelle instance de document    
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer une instance de TextFragment avec un texte d'exemple
    auto fragment = MakeObject<TextFragment>("Texte d'exemple en police OTF");

    // Ou vous pouvez même spécifier le chemin de la police OTF dans le répertoire système
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Spécifier d'incorporer la police dans le fichier PDF, pour qu'elle soit affichée correctement,
    // Même si la police spécifique n'est pas installée/présente sur la machine cible
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Ajouter le TextFragment à la collection de paragraphes de l'instance Page
    page->get_Paragraphs()->Add(fragment);
    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

## Ajouter une chaîne HTML en utilisant DOM

La classe Aspose.Pdf.Generator.Text contient une propriété appelée IsHtmlTagSupported qui permet d'ajouter des balises/contenus HTML dans les fichiers PDF. Le contenu ajouté est rendu dans des balises HTML natives au lieu d'apparaître comme une simple chaîne de texte. Pour prendre en charge une fonctionnalité similaire dans le nouveau Modèle Objet Document (DOM) de l'espace de noms Aspose.Pdf, la classe HtmlFragment a été introduite.

L'instance [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) peut être utilisée pour spécifier le contenu HTML qui doit être placé dans le fichier PDF. Similaire à TextFragment, HtmlFragment est un objet de niveau paragraphe et peut être ajouté à la collection de paragraphes de l'objet Page. Les extraits de code suivants montrent les étapes pour placer le contenu HTML dans un fichier PDF en utilisant l'approche DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String pour le nom du fichier d'entrée
    String inputFileName("sample.pdf");

    // String pour le nom du fichier de sortie
    String outputFileName("sample_html_out.pdf");

    // créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Instancier HtmlFragment avec du contenu HTML
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // définir MarginInfo pour les détails de marge
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Définir les informations de marge
    title->set_Margin(margin);

    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(title);
    // Enregistrer le fichier PDF
    document->Save(_dataDir + outputFileName);
}
```

Le fragment de code suivant démontre les étapes pour ajouter des listes ordonnées HTML dans le document :

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Instancier l'objet Document   
    auto document = MakeObject<Document>();

    // Instancier l'objet HtmlFragment avec le fragment HTML correspondant
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Ajouter une page dans la collection de pages
    auto page = document->get_Pages()->Add();

    // Ajouter HtmlFragment à l'intérieur de la page
    page->get_Paragraphs()->Add(htmlFragment);

    // Enregistrer le fichier PDF résultant
    document->Save(_dataDir + outputFileName);
}
```

Vous pouvez également définir la mise en forme de la chaîne HTML en utilisant l'objet TextState comme suit :

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("sample_html_out.pdf");

    // Instancier l'objet Document    
    auto document = MakeObject<Document>();

    // Ajouter une page dans la collection de pages
    auto page = document->get_Pages()->Add();

    // Instancier HtmlFragment avec le contenu HTML
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(title);
    // Enregistrer le fichier PDF
    document->Save(_dataDir + outputFileName);
}

```

Dans le cas où vous définissez certaines valeurs d'attributs de texte via le balisage HTML et que vous fournissez ensuite les mêmes valeurs dans les propriétés de TextState, elles remplaceront les paramètres HTML par les propriétés de l'instance TextState. Les extraits de code suivants montrent le comportement décrit.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier de sortie
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Instancier un objet Document    
    auto document = MakeObject<Document>();

    // Ajouter une page dans la collection de pages
    auto page = document->get_Pages()->Add();

    // Instancier HtmlFragment avec du contenu HTML
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Tableau contient du texte</i></b></p>");

    // La police de caractères de 'Verdana' sera réinitialisée à 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Définir les informations de marge inférieure
    title->get_Margin()->set_Bottom(10);
    // Définir les informations de marge supérieure
    title->get_Margin()->set_Top(400);
    // Ajouter le fragment HTML à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(title);
    // Enregistrer le fichier PDF
    document->Save(_dataDir + outputFileName);
}
```

## FootNotes et EndNotes (DOM)

Les FootNotes indiquent des notes dans le texte de votre document en utilisant des numéros en exposant consécutifs. La note proprement dite est en retrait et peut apparaître comme une note de bas de page au bas de la page.

### Ajouter une FootNote

Dans un système de référence de note de bas de page, indiquez une référence en :

- plaçant un petit numéro au-dessus de la ligne de texte directement après le matériel source. Ce numéro est appelé un identifiant de note. Il se situe légèrement au-dessus de la ligne de texte.
- plaçant le même numéro, suivi d'une citation de votre source, au bas de la page. La notation en bas de page doit être numérique et chronologique : la première référence est 1, la deuxième est 2, et ainsi de suite.

L'avantage de la notation en bas de page est que le lecteur peut simplement jeter un coup d'œil en bas de la page pour découvrir la source d'une référence qui l'intéresse.

Suivez les étapes suivantes :

- Créez une instance de [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- Créez un objet [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- Créez un objet [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
- Créer une instance de Note et passer sa valeur à la propriété TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- Ajouter TextFragment à la collection de paragraphes d'une instance de page

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Instancier l'objet Document    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Ajouter une page dans la collection de pages
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Demo");
    t->set_FootNote(note);

    // créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // définir la valeur de FootNote pour TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page->get_Paragraphs()->Add(text);
    // créer le deuxième TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // définir FootNote pour le deuxième fragment de texte
    text->set_FootNote(MakeObject<Note>("foot note for test text 2"));
    // ajouter le deuxième fragment de texte à la collection de paragraphes du fichier PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Style de ligne personnalisé pour FootNote

L'exemple suivant démontre comment ajouter des notes de bas de page au bas de la page PDF et définir un style de ligne personnalisé.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie
    String outputFileName("customFootNote_Line.pdf");

    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // ajouter une page à la collection de pages du PDF
    auto page = document->get_Pages()->Add();
    
    // créer un objet GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // définir la largeur de la ligne à 2
    graph->set_LineWidth(2);
    // définir la couleur pour l'objet graph
    graph->set_Color(Color::get_Red());
    // définir la valeur du tableau de tirets à 3
    graph->set_DashArray(MakeArray<int>(3));
    // définir la valeur de phase de tirets à 1
    graph->set_DashPhase(1);
    // définir le style de ligne de note de bas de page pour la page comme graph
    page->set_NoteLineStyle(graph);

    // créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // définir la valeur de FootNote pour TextFragment
    text->set_FootNote(MakeObject<Note>("note de bas de page pour le texte de test 1"));
    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page->get_Paragraphs()->Add(text);
    // créer le second TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // définir FootNote pour le second fragment de texte
    text->set_FootNote(MakeObject<Note>("note de bas de page pour le texte de test 2"));
    // ajouter le second fragment de texte à la collection de paragraphes du fichier PDF
    page->get_Paragraphs()->Add(text);
    // sauvegarder le fichier PDF
    document->Save(_dataDir + outputFileName);
}
```

Nous pouvons définir le formatage de l'Étiquette de Renvoi (identifiant de note) en utilisant l'objet TextState comme suit :

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier d'entrée   
    String inputFileName("sample.pdf");

    // Chaîne pour le nom du fichier de sortie   
    String outputFileName("sample_footnote.pdf");

    // Créer une instance de Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // définir la valeur de FootNote pour TextFragment
    text->set_FootNote(MakeObject<Note>("note de bas de page pour le texte de test 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page->get_Paragraphs()->Add(text);
    // créer le deuxième TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // définir FootNote pour le deuxième fragment de texte
    text->set_FootNote(MakeObject<Note>("note de bas de page pour le texte de test 2"));
    // ajouter le deuxième fragment de texte à la collection de paragraphes du fichier PDF
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Personnaliser l'étiquette de note de bas de page

Par défaut, le numéro de la note de bas de page est incrémental à partir de 1. Cependant, nous pouvons avoir besoin de définir une étiquette de note de bas de page personnalisée. Pour accomplir cette exigence, veuillez essayer d'utiliser l'extrait de code suivant

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier de sortie    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet GraphInfo
    auto graph = MakeObject<GraphInfo>();

    // Définir la largeur de ligne à 2
    graph->set_LineWidth(2);

    // Définir la couleur de l'objet graphique
    graph->set_Color(Color::get_Red());

    // Définir la valeur du tableau de tirets à 3
    graph->set_DashArray(MakeArray<int>(3));

    // Définir la valeur de phase de tiret à 1
    graph->set_DashPhase(1);

    // Définir le style de ligne de note de bas de page pour la page comme graphique
    page->set_NoteLineStyle(graph);

    // Créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // Définir la valeur de la note de bas de page pour TextFragment
    text->set_FootNote(MakeObject<Note>("note de bas de page pour le texte de test 1"));
    // Spécifier une étiquette personnalisée pour la note de bas de page
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Ajouter TextFragment à la collection de paragraphes de la première page du document
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Ajout d'Image et de Tableau à la Note de Bas de Page

Le code suivant montre les étapes pour ajouter une [Footnote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) à un objet [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment) puis ajouter un objet Image et Tableau à la collection de paragraphes de la section de la note de bas de page.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom de fichier de sortie    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Créer une instance de Document
    auto document = new Document();
    // Ajouter une page à la collection de pages du PDF
    auto page = document->get_Pages()->Add();

    // Créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("texte de la note de bas de page");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Ligne 1 Cellule 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Comment créer des notes de fin

Une note de fin est une citation de source qui renvoie les lecteurs à un endroit spécifique à la fin du document où ils peuvent trouver la source de l'information ou des mots cités ou mentionnés dans le document. Lors de l'utilisation des notes de fin, votre phrase citée ou paraphrasée ou votre matériel résumé est suivi d'un numéro en exposant.

L'exemple suivant démontre comment ajouter une note de fin dans la page Pdf.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String pour le nom du fichier de sortie    
    String outputFileName("endNote_out.pdf");

    // Créer une instance de Document
    auto document = new Document();
    // Ajouter une page à la collection de pages du PDF
    auto page = document->get_Pages()->Add();

    // créer une instance de TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    // définir la valeur de FootNote pour TextFragment
    text->set_EndNote(MakeObject<Note>("exemple de note de fin"));

    // spécifier une étiquette personnalisée pour FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // ajouter TextFragment à la collection de paragraphes de la première page du document
    page->get_Paragraphs()->Add(text);
    // enregistrer le fichier PDF
    document->Save(_dataDir + outputFileName);
}
```

## Texte et Image en Paragraphe En Ligne

La disposition par défaut du fichier PDF est une disposition en flux (de haut en bas, de gauche à droite). Par conséquent, chaque nouvel élément ajouté au fichier PDF est ajouté dans le flux en bas à droite. Cependant, nous pouvons avoir besoin d'afficher divers éléments de page, c'est-à-dire Image et Texte, au même niveau (l'un après l'autre). Une approche peut être de créer une instance de Table et d'ajouter les deux éléments à des objets cellule individuels. Cependant, une autre approche peut être le paragraphe en ligne. En définissant la propriété IsInLineParagraph de l'Image et du Texte comme vrai, ces paragraphes apparaîtront en ligne avec d'autres éléments de page.

Le code suivant vous montre comment ajouter du texte et une image en tant que paragraphes en ligne dans le fichier PDF.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Instancier l'instance Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages de l'instance Document
    auto page = document->get_Pages()->Add();

    // Créer TextFragment
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Ajouter le fragment de texte à la collection de paragraphes de l'objet Page
    page->get_Paragraphs()->Add(text);

    // Créer une instance d'image
    auto image = MakeObject<Image>();

    // Définir l'image comme paragraphe en ligne afin qu'elle apparaisse juste après
    // Le précédent objet paragraphe (TextFragment)
    image->set_IsInLineParagraph(true);

    // Spécifier le chemin du fichier image
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Définir la hauteur de l'image (optionnel)
    image->set_FixHeight(30);
    // Définir la largeur de l'image (optionnel)
    image->set_FixWidth(100);
    // Ajouter l'image à la collection de paragraphes de l'objet page
    page->get_Paragraphs()->Add(image);
    // Réinitialiser l'objet TextFragment avec différents contenus
    text = MakeObject<TextFragment>(" Hello Again..");
    // Définir TextFragment comme paragraphe en ligne
    text->set_IsInLineParagraph(true);
    // Ajouter le nouveau TextFragment créé à la collection de paragraphes de la page
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Spécifier l'espacement des caractères lors de l'ajout de texte

Le texte peut être ajouté à une collection de paragraphes d'un PDF en utilisant une instance de TextFragment ou un objet TextParagraph, et vous pouvez même tamponner du texte à l'intérieur d'un PDF en utilisant la classe TextStamp. Lors de l'ajout de texte, il peut être nécessaire de spécifier l'espacement entre les caractères pour les objets texte. Pour répondre à cette exigence, une nouvelle propriété a été introduite, nommée CharacterSpacing.

Veuillez considérer les approches suivantes pour répondre à cette exigence.

Les approches suivantes montrent les étapes pour spécifier l'espacement des caractères lors de l'ajout de texte à l'intérieur d'un document PDF.

### Utilisation de TextBuilder et TextFragment

```cpp
// Spécifier l'espacement des caractères lors de l'ajout de texte en utilisant TextBuilder et TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Créer une instance de Document
    auto document = MakeObject<Document>();
    // Ajouter une page à la collection de pages du Document
    auto page = document->get_Pages()->Add();

    // Créer une instance de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Créer une instance de fragment de texte avec du contenu d'exemple
    auto wideFragment = MakeObject<TextFragment>("Texte avec espacement des caractères augmenté");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Spécifier l'espacement des caractères pour TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Spécifier la position de TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Ajouter TextFragment à l'instance TextBuilder
    builder->AppendText(wideFragment);

    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

### Utilisation de TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier de sortie    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du document
    auto page = document->get_Pages()->Add();

    // Créer une instance de TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Instancier une instance de TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // Créer une instance de TextState pour spécifier le nom et la taille de la police
    auto state = MakeObject<TextState>("Arial", 12);

    // Spécifier l'espacement des caractères
    state->set_CharacterSpacing(1.5f);

    // Ajouter du texte à l'objet TextParagraph
    paragraph->AppendLine(u"Ceci est un paragraphe avec un espacement des caractères", state);

    // Spécifier la position pour TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Ajouter TextParagraph à l'instance de TextBuilder
    builder->AppendParagraph(paragraph);

    // Sauvegarder le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

### Utilisation de TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Créer une instance de Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du Document    
    auto page = document->get_Pages()->Add();

    // Instancier une instance de TextStamp avec du texte d'exemple
    auto stamp = MakeObject<TextStamp>("Ceci est un timbre texte avec espacement des caractères");

    // Spécifier le nom de la police pour l'objet Stamp
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Spécifier la taille de la police pour TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Spécifier l'espacement des caractères comme 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Définir l'XIndent pour Stamp
    stamp->set_XIndent(100);
    // Définir l'YIndent pour Stamp
    stamp->set_YIndent(500);
    // Ajouter un timbre textuel à l'instance de la page
    stamp->Put(page);
    // Enregistrer le document PDF résultant.
    document->Save(_dataDir + outputFileName);
}
```

## Créer un document PDF à colonnes multiples

Ce sujet montre comment vous pouvez créer un PDF à colonnes multiples en utilisant Aspose.Pdf pour C++.

Aujourd'hui, nous voyons le plus souvent des nouvelles affichées en plusieurs colonnes sur des pages séparées, plutôt que dans des livres, où les paragraphes de texte sont principalement imprimés sur toutes les pages de gauche à droite. De nombreuses applications de traitement de documents, telles que Microsoft Word et Adobe Acrobat Writer, permettent aux utilisateurs de créer plusieurs colonnes sur une seule page, puis d'y ajouter des données.

Aspose.Pdf pour C++ offre également la possibilité de créer plusieurs colonnes dans les pages de documents PDF. Pour créer un PDF avec plusieurs colonnes, nous pouvons utiliser la classe [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box) car elle fournit une propriété ColumnInfo.ColumnCount pour spécifier le nombre de colonnes à l'intérieur du FloatingBox, et nous pouvons également spécifier l'espacement des colonnes et les largeurs des colonnes en utilisant respectivement ColumnInfo .ColumnSpacing et ColumnInfo .ColumnWidths.

Un exemple est donné ci-dessous pour démontrer la création de deux colonnes avec des objets Graphs (Line) et ils sont ajoutés à la collection de paragraphes de FloatingBox, qui est ensuite ajoutée à la collection de paragraphes de l'instance Page.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Créer une nouvelle instance de document
    auto document = MakeObject<Document>();

    // Spécifiez les informations sur la marge gauche pour le fichier PDF
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Spécifiez les informations sur la marge droite pour le fichier PDF
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Ajouter une page à la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Ajouter la ligne à la collection de paragraphes de l'objet section
    page->get_Paragraphs()->Add(graph1);

    // Spécifiez les coordonnées de la ligne
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Créer des variables de chaîne avec du texte contenant des balises html
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> Comment éviter les arnaques financières</<strong> </span>");

    // Créer des paragraphes de texte contenant du texte HTML

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Ajouter quatre colonnes dans la section
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Définir l'espacement entre les colonnes
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("Par A Googler (Le Blog Officiel de Google)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Créer un objet graphique pour dessiner une ligne
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Spécifiez les coordonnées de la ligne
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Ajouter la ligne à la collection de paragraphes de l'objet section
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Enregistrer le fichier PDF
    document->Save(_dataDir + outputFileName);
}
```

## Travailler avec des tabulations personnalisées

Un tabulateur est un point d'arrêt pour la tabulation. Dans le traitement de texte, chaque ligne contient un certain nombre de tabulations placées à intervalles réguliers (par exemple, tous les demi-pouces). Ils peuvent être modifiés, cependant, car la plupart des traitements de texte vous permettent de définir des tabulations où vous le souhaitez. Lorsque vous appuyez sur la touche Tab, le curseur ou le point d'insertion saute à la tabulation suivante, qui est elle-même invisible. Bien que les tabulations n'existent pas dans le fichier texte, le traitement de texte les garde en mémoire afin de pouvoir réagir correctement à la touche Tab.

Voici un exemple de comment définir des tabulations personnalisées.

```cpp
void CustomTabStops() {
    String _dataDir("C:\\Samples\\");
    String outputFileName("CustomTabStops_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto ts = MakeObject<TabStops>();
    auto ts1 = ts->Add(100);

    ts1->set_AlignmentType(TabAlignmentType::Right);
    ts1->set_LeaderType(TabLeaderType::Solid);

    auto ts2 = ts->Add(200);
    ts2->set_AlignmentType(TabAlignmentType::Center);
    ts2->set_LeaderType(TabLeaderType::Dash);

    auto ts3 = ts->Add(300);
    ts3->set_AlignmentType(TabAlignmentType::Left);
    ts3->set_LeaderType(TabLeaderType::Dot);

    auto header = MakeObject<TextFragment>("This is a example of forming table with TAB stops", ts);
    auto text0 =  MakeObject<TextFragment>("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    auto text1 = MakeObject<TextFragment>("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    auto text2 = MakeObject<TextFragment>("#$TABdata21 ", ts);
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data22 "));
    text2->get_Segments()->Add(MakeObject<TextSegment>("#$TAB"));
    text2->get_Segments()->Add(MakeObject<TextSegment>("data23"));
              
    page->get_Paragraphs()->Add(header);
    page->get_Paragraphs()->Add(text0);
    page->get_Paragraphs()->Add(text1);
    page->get_Paragraphs()->Add(text2);

    document->Save(_dataDir + outputFileName);
}
```

## Comment ajouter du texte transparent dans un PDF

PDF 1.4 (un format de fichier pris en charge par Acrobat 5) a été la première version de PDF à prendre en charge la transparence. Ce PDF est arrivé sur le marché à peu près en même temps qu'Adobe Illustrator 9.

Un fichier PDF contient des objets Image, Texte, Graphique, pièce jointe, Annotations et lors de la création d'un TextFragment, vous pouvez définir des informations de couleur de premier plan, d'arrière-plan ainsi que le formatage du texte. Aspose.PDF pour C++ prend en charge la fonctionnalité d'ajout de texte avec un canal de couleur Alpha. L'extrait de code suivant montre comment ajouter du texte avec une couleur transparente.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Créer une instance Document
    auto document = MakeObject<Document>();    
    // Créer une page pour la collection de pages du fichier PDF
    auto page = document->get_Pages()->Add();

    // Créer un objet Graph
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Créer une instance de rectangle avec des dimensions spécifiques
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Créer un objet couleur à partir du canal de couleur Alpha
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Ajouter le rectangle à la collection de formes de l'objet Graph
    canvas->get_Shapes()->Add(rect);

    // Ajouter l'objet graphique à la collection de paragraphes de l'objet page
    page->get_Paragraphs()->Add(canvas);

    // Définir la valeur pour ne pas changer la position de l'objet graphique
    canvas->set_IsChangePosition(false);

    // Créer une instance de TextFragment avec une valeur d'exemple
    auto text = MakeObject<TextFragment>(
        "texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent texte transparent ");
    // Créer un objet couleur à partir du canal Alpha
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Définir les informations de couleur pour l'instance de texte
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Ajouter le texte à la collection de paragraphes de l'instance de page
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Spécifier l'espacement des lignes pour les polices

La classe [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) a une énumération [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91) qui est conçue pour des polices spécifiques, par exemple, la police d'entrée "HPSimplified.ttf". De plus, la classe [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) a une propriété [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) de type LineSpacingMode. Vous devez simplement définir LineSpacing sur LineSpacingMode.FullSize. L'extrait de code pour afficher correctement une police serait le suivant :

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Charger le fichier PDF d'entrée
    auto document = MakeObject<Document>();
    
    // Créer TextFormattingOptions avec LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Créer un fragment de texte avec une chaîne d'exemple
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Charger la police TrueType dans l'objet de flux
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Définir le nom de la police pour la chaîne de texte
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Spécifier la position du fragment de texte
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Définir TextFormattingOptions du fragment actuel sur prédéfini (qui pointe vers
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Ajouter le texte à TextBuilder afin qu'il puisse être placé sur le fichier PDF    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Enregistrer le document PDF résultant
    document->Save(_dataDir + outputFileName);
}
```

## Obtenir la largeur du texte dynamiquement

La classe [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) montre comment obtenir la largeur du texte dynamiquement dans un document PDF.

Parfois, il est nécessaire d'obtenir la largeur du texte dynamiquement. Aspose.PDF pour C++ inclut deux méthodes pour la mesure de la largeur de chaîne. Vous pouvez invoquer la méthode [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) des classes Aspose.Pdf.Text.Font ou Aspose.Pdf.Text.TextState (ou les deux). Le code ci-dessous montre comment utiliser cette fonctionnalité.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Mesure de chaîne de police inattendue!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Mesure de chaîne de police inattendue!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"La mesure de chaîne de police et d'état ne correspond pas!");
    }
}
```
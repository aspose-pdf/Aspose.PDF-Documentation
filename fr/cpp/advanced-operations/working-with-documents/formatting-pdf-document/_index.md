---
title: Formatage du document PDF en C++
linktitle: Formatage du document PDF
type: docs
weight: 20
url: fr/cpp/formatting-pdf-document/
description: Créez et formatez le document PDF avec Aspose.PDF pour C++. Utilisez l'extrait de code suivant pour résoudre vos tâches.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Formatage du document PDF

### Obtenir les propriétés de la fenêtre du document et de l'affichage des pages

Ce sujet vous aide à comprendre comment obtenir les propriétés de la fenêtre du document, de l'application de visualisation et comment les pages sont affichées. Pour définir ces propriétés, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Vous pouvez maintenant définir les propriétés de l'objet Document, telles que :

- CenterWindow – Centrer la fenêtre du document sur l'écran. Par défaut : faux.
- Direction – Ordre de lecture. Cela détermine comment les pages sont disposées lorsqu'elles sont affichées côte à côte. Par défaut : de gauche à droite.
- DisplayDocTitle – Afficher le titre du document dans la barre de titre de la fenêtre du document.  Default: false (le titre est affiché).
- HideMenuBar – Masquer ou afficher la barre de menu de la fenêtre du document. Par défaut : false (la barre de menu est affichée).
- HideToolBar – Masquer ou afficher la barre d'outils de la fenêtre du document. Par défaut : false (la barre d'outils est affichée).
- HideWindowUI – Masquer ou afficher les éléments de la fenêtre du document comme les barres de défilement. Par défaut : false (les éléments de l'interface utilisateur sont affichés).
- NonFullScreenPageMode – Comment le document est affiché lorsqu'il n'est pas en mode plein écran.
- PageLayout – La disposition des pages.
- PageMode – Comment le document est affiché lors de la première ouverture. Les options sont afficher les vignettes, plein écran, afficher le panneau des pièces jointes.

Le fragment de code suivant vous montre comment obtenir les propriétés à l'aide de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Obtenez différentes propriétés du document
    // Position de la fenêtre du document - Par défaut : false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Ordre de lecture prédominant; détermine la position de la page
    // Lorsqu'affiché côte à côte - Par défaut : L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // La barre de titre de la fenêtre doit-elle afficher le titre du document
    // Si false, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Redimensionner la fenêtre du document pour s'adapter à la taille de
    // La première page affichée - Par défaut : false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Masquer la barre de menu de l'application de visualisation - Par défaut : false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Masquer la barre d'outils de l'application de visualisation - Par défaut : false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Masquer les éléments de l'interface utilisateur comme les barres de défilement
    // Et ne laisser affiché que le contenu de la page - Par défaut : false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Mode de page du document. Comment afficher le document en quittant le mode plein écran.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // La disposition des pages c'est-à-dire page unique, une colonne
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // Comment le document doit être affiché à l'ouverture
    // C'est-à-dire afficher les vignettes, plein écran, afficher le panneau des pièces jointes
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### Définir les propriétés de la fenêtre du document et de l'affichage de la page

Ce sujet explique comment définir les propriétés de la fenêtre du document, de l'application de visualisation et de l'affichage de la page. Pour définir ces différentes propriétés :

1. Ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Définissez différentes propriétés du document :

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [Enregistrez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) le fichier PDF mis à jour en utilisant la méthode Save.

Les propriétés disponibles sont :

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Chacune est utilisée et décrite dans le code ci-dessous. Le code suivant - extrait de code vous montre comment définir les propriétés en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Définir différentes propriétés du document
    // Spécifier pour positionner la fenêtre du document - Par défaut : false
    document->set_CenterWindow(true);

    // Ordre de lecture prédominant ; détermine la position de la page
    // Lorsqu'elle est affichée côte à côte - Par défaut : L2R
    document->set_Direction(Direction::R2L);

    // Spécifier si la barre de titre de la fenêtre doit afficher le titre du document
    // Si faux, la barre de titre affiche le nom du fichier PDF - Par défaut : false
    document->set_DisplayDocTitle(true);

    // Spécifier si redimensionner la fenêtre du document pour s'adapter à la taille de
    // La première page affichée - Par défaut : false
    document->set_FitWindow(true);

    // Spécifier si cacher la barre de menu de l'application de visualisation - Par défaut : false
    document->set_HideMenubar(true);

    // Spécifier si cacher la barre d'outils de l'application de visualisation - Par défaut : false
    document->set_HideToolBar(true);

    // Spécifier si cacher les éléments d'interface utilisateur comme les barres de défilement
    // Et laisser uniquement le contenu de la page affiché - Par défaut : false
    document->set_HideWindowUI(true);

    // Mode de page du document. spécifier comment afficher le document en quittant le mode plein écran.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Spécifier la mise en page de la page, c'est-à-dire une seule page, une colonne
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Spécifier comment le document doit être affiché lorsqu'il est ouvert
    // C'est-à-dire afficher les vignettes, plein écran, afficher le panneau des pièces jointes
    document->set_PageMode(PageMode::UseThumbs);

    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + outputFileName);
}
```
### Incorporation de polices dans un fichier PDF existant

Les lecteurs PDF prennent en charge [un ensemble de 14 polices](https://en.wikipedia.org/wiki/PDF#Text) afin que les documents puissent être affichés de la même manière quel que soit le système sur lequel le document est affiché. Lorsqu'un PDF contient une police qui ne fait pas partie des 14 polices de base, intégrez la police dans le fichier PDF pour éviter la substitution de police.

Aspose.PDF pour C++ prend en charge l'incorporation de polices dans les fichiers PDF existants. Vous pouvez intégrer une police complète ou un sous-ensemble de la police. Pour intégrer la police, ouvrez le fichier PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Ensuite, utilisez la classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) pour intégrer la police dans le fichier PDF. Pour intégrer la police complète, utilisez la propriété IsEmbeded de la classe Font ; pour utiliser un sous-ensemble de la police, utilisez la propriété IsSubset.

{{% alert color="primary" %}}

Un sous-ensemble de police intègre uniquement les caractères utilisés et est utile lorsque les polices sont utilisées pour des phrases courtes ou des slogans, par exemple lorsque qu'une police d'entreprise est utilisée pour un logo, mais pas pour le texte principal.  Utiliser un sous-ensemble réduit la taille du fichier du PDF de sortie. Cependant, si une police personnalisée est utilisée pour le texte du corps, intégrez-la dans son intégralité.

{{% /alert %}}

Le fragment de code suivant montre comment intégrer une police dans un fichier PDF.

### Intégration des polices standard de type 1

Il existe des documents PDF qui utilisent des polices d'un ensemble spécial appelées "Polices standard de type 1". Cet ensemble comprend 14 polices et l'intégration de ce type de police nécessite l'utilisation de drapeaux spéciaux c'est-à-dire [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

Voici le fragment de code qui peut être utilisé pour obtenir un document avec toutes les polices intégrées, y compris les polices standard de type 1 :

```cpp
void EmbeddingStandardType1Fonts()
{

    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Définir la propriété EmbedStandardFonts du document
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Vérifier si la police est déjà intégrée
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### Intégration des polices lors de la création de PDF

Si vous avez besoin d'utiliser une police autre que les 14 polices de base prises en charge par Adobe Reader, vous devez intégrer la description de la police lors de la génération du fichier Pdf. Si les informations sur la police ne sont pas intégrées, Adobe Reader les récupérera à partir du système d'exploitation si elles sont installées sur le système, ou il construira une police de substitution selon le descripteur de police dans le Pdf.

>Veuillez noter que la police intégrée doit être installée sur la machine hôte, c'est-à-dire que dans le cas du code suivant, la police 'Univers Condensed' est installée sur le système.

Nous utilisons la propriété IsEmbedded de la classe Font pour intégrer les informations de police dans le fichier Pdf. Définir la valeur de cette propriété à 'True' intégrera le fichier de police complet dans le Pdf, sachant que cela augmentera la taille du fichier Pdf. Voici l'extrait de code qui peut être utilisé pour intégrer les informations de police dans le Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom de fichier.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Crée une section dans l'objet Pdf
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"Voici un texte exemple utilisant une police personnalisée.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Enregistrer le document PDF
    document->Save(_dataDir);
}
```

### Définir le nom de police par défaut lors de l'enregistrement en PDF

Lorsqu'un document PDF contient des polices qui ne sont pas disponibles dans le document lui-même et sur l'appareil, l'API remplace ces polices par la police par défaut. Lorsque la police est disponible (installée sur l'appareil ou intégrée au document), le PDF de sortie doit avoir la même police (ne doit pas être remplacée par la police par défaut). La valeur de la police par défaut doit contenir le nom de la police (et non le chemin vers les fichiers de police). Apose.PDF pour C++ a implémenté une fonctionnalité pour définir le nom de la police par défaut lors de l'enregistrement d'un document en tant que PDF. Le code suivant peut être utilisé pour définir la police par défaut :

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // Chaîne pour le chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom de fichier.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Spécifier le nom de la police par défaut
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Obtenir Toutes les Polices d'un Document PDF

Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() fournie dans la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Veuillez consulter l'extrait de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```cpp
void GetAllFontsFromPDFdocument()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Obtenir des Avertissements pour la Substitution de Police

Aspose.PDF pour C++ fournit des méthodes pour obtenir des notifications concernant la substitution de police pour gérer les cas de substitution de police. Les extraits de code ci-dessous montrent comment utiliser la fonctionnalité correspondante.

```cpp
void GetWarningsForFontSubstitution()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

La méthode [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) est listée ci-dessous.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Warning: Font " << font.get_FontName() 
            << " was substituted with another font -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Améliorer l'Intégration des Polices en utilisant FontSubsetStrategy

La fonctionnalité pour intégrer les polices comme un sous-ensemble peut être réalisée en utilisant la propriété IsSubset, mais parfois vous souhaitez réduire un ensemble de polices entièrement intégré à seulement des sous-ensembles qui sont utilisés dans le document. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) possède la propriété [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) qui inclut la méthode SubsetFonts(FontSubsetStrategy subsetStrategy). Dans la méthode SubsetFonts(), le paramètre subsetStrategy aide à ajuster la stratégie de sous-ensemble. FontSubsetStrategy prend en charge deux variantes de sous-ensemble de polices suivantes.

- SubsetAllFonts - Cela sous-ensemble toutes les polices utilisées dans un document.
- SubsetEmbeddedFontsOnly - Cela sous-ensemble uniquement les polices qui sont entièrement intégrées dans le document.

L'extrait de code suivant montre comment définir FontSubsetStrategy :

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    // Chaîne pour le nom du fichier.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // Toutes les polices seront intégrées en tant que sous-ensemble dans le document en cas de SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // Le sous-ensemble de polices sera intégré pour les polices entièrement intégrées mais les polices qui ne sont pas intégrées dans le document ne seront pas affectées.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### Définir-Obtenir le Facteur de Zoom d'un Fichier PDF

Parfois, vous souhaitez définir le facteur de zoom d'un document PDF. Avec Aspose.PDF pour C++, vous pouvez définir la valeur du facteur de zoom avec la méthode [set_OpenAction(…)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) de la classe Document.

La propriété Destination de la classe [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) vous permet d'obtenir la valeur du zoom associée à un fichier PDF. De même, elle peut être utilisée pour définir le facteur de zoom d'un fichier.

#### Définir le facteur de zoom

L'extrait de code suivant montre comment définir le facteur de zoom d'un fichier PDF.

```cpp
void SetZoomFactor() {
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");
    // Chaîne pour le nom du fichier.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Enregistrer le document
    document->Save(_dataDir + outputFileName);
}
```

#### Obtenez le Facteur de Zoom

Obtenez le facteur de zoom dans votre fichier PDF en utilisant Aspose.PDF pour C++.

L'extrait de code suivant montre comment obtenir le facteur de zoom d'un fichier PDF :

```cpp
void GetZoomFactor() 
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Créer un objet GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Obtenez le facteur de zoom du fichier PDF
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Valeur de zoom du document;
}
```

### Définir les Propriétés Prédéfinies de la Boîte de Dialogue d'Impression

Aspose.PDF pour C++ permet de définir les propriétés prédéfinies de la boîte de dialogue d'impression d'un document PDF. Il vous permet de modifier la propriété DuplexMode pour un document PDF qui est réglé sur simplex par défaut. Cela peut être réalisé en utilisant deux méthodologies différentes comme indiqué ci-dessous.

```cpp
void SettingPrintDialogPresetProperties()
{
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom de fichier.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Réglage des propriétés prédéfinies de la boîte de dialogue d'impression à l'aide de l'éditeur de contenu PDF

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom de fichier.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "Le fichier a un retournement en duplex sur le bord court" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```
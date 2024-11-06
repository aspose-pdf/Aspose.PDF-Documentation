---
title: Remplacer le texte dans un PDF en utilisant C++
linktitle: Remplacer le texte dans un PDF
type: docs
weight: 40
url: fr/cpp/replace-text-in-pdf/
description: En savoir plus sur les différentes façons de remplacer et de supprimer du texte dans un PDF. Aspose.PDF permet de remplacer du texte dans une région particulière ou avec une expression régulière.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Parfois, une tâche apparaît pour corriger ou remplacer du texte dans un document PDF. Essayer de le faire manuellement sera une tâche ardue, donc voici la solution à ce problème.

Honnêtement, éditer un fichier PDF n'est pas une tâche facile. Ainsi, une situation où vous devez trouver et remplacer un mot par un autre tout en éditant un fichier PDF sera très difficile car cela vous prendra beaucoup de temps. De plus, vous pouvez rencontrer de nombreux problèmes avec votre sortie, tels que le formatage ou des polices cassées. Si vous souhaitez facilement trouver et remplacer du texte dans des fichiers PDF, nous vous recommandons d'utiliser le logiciel Aspose.Pdf car il fera le travail en quelques minutes.

Dans cet article, nous vous montrerons comment trouver et remplacer avec succès du texte dans vos fichiers PDF en utilisant Aspose.PDF pour C++.

## Remplacer le texte dans toutes les pages d'un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de remplacer le texte dans le document en utilisant Aspose.PDF et obtenir les résultats en ligne à ce [lien](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Pour remplacer le texte dans toutes les pages d'un document PDF, vous devez d'abord utiliser TextFragmentAbsorber pour trouver la phrase particulière que vous souhaitez remplacer. Après cela, vous devez parcourir tous les TextFragments pour remplacer le texte et modifier d'autres attributs. Une fois cela fait, vous n'avez besoin que d'enregistrer le PDF de sortie en utilisant la méthode Save de l'objet Document. Le code ci-dessous vous montre comment remplacer le texte dans toutes les pages d'un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Créer un objet TextAbsorber pour trouver toutes les instances de la phrase de recherche entrée
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Accepter l'absorbeur pour la première page du document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtenir les fragments de texte extraits dans la collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Boucle à travers les fragments
    for (auto textFragment : textFragmentCollection) {
        // Mettre à jour le texte et d'autres propriétés
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Remplacer le texte dans une région particulière de la page

Afin de remplacer le texte dans une région particulière de la page, nous devons d'abord instancier un objet TextFragmentAbsorber, spécifier la région de la page en utilisant la propriété TextSearchOptions.Rectangle, puis parcourir tous les TextFragments pour remplacer le texte. Une fois ces opérations terminées, nous avons seulement besoin d'enregistrer le PDF de sortie en utilisant la méthode Save de l'objet Document. Le code suivant vous montre comment remplacer le texte dans toutes les pages d'un document PDF.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // charger le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // instancier l'objet TextFragment Absorber
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // rechercher du texte dans les limites de la page
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // spécifier la région de la page pour les options de recherche de texte
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // rechercher du texte à partir de la première page du fichier PDF
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // parcourir chaque TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // remplacer le texte par "---"
        tf->set_Text(u"---");
    }

    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Remplacer le texte basé sur une expression régulière

Si vous souhaitez remplacer certaines phrases basées sur une expression régulière, vous devez d'abord trouver toutes les phrases correspondant à cette expression régulière particulière en utilisant TextFragmentAbsorber. Vous devrez passer l'expression régulière en tant que paramètre au constructeur de TextFragmentAbsorber. Vous devez également créer un objet TextSearchOptions qui spécifie si l'expression régulière est utilisée ou non. Une fois que vous avez les phrases correspondantes dans TextFragments, vous devez les parcourir et les mettre à jour selon les besoins. Enfin, vous devez enregistrer le PDF mis à jour en utilisant la méthode Save de l'objet Document. Le fragment de code suivant vous montre comment remplacer le texte basé sur une expression régulière.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Create TextAbsorber object to find all instances of the input search phrase
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // like 1999-2000

    // Set text search option to specify regular expression usage
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Accept the absorber for first page of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Loop through the fragments
    for (auto textFragment : textFragmentCollection) {
        // Update text and other properties
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Remplacer les polices dans un fichier PDF existant

Aspose.PDF pour C++ prend en charge la capacité de remplacer le texte dans un document PDF. Cependant, parfois, vous avez besoin de ne remplacer que la police utilisée dans le document PDF. Au lieu de remplacer le texte, seule la police utilisée est remplacée. L'une des surcharges du constructeur TextFragmentAbsorber accepte un objet TextEditOptions comme argument et nous pouvons utiliser la valeur RemoveUnusedFonts de l'énumération TextEditOptions.FontReplace pour répondre à nos besoins. L'extrait de code suivant montre comment remplacer la police à l'intérieur du document PDF.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Instancier l'objet Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Rechercher les fragments de texte et définir l'option d'édition pour supprimer les polices inutilisées
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // Accepter l'absorbeur pour toutes les pages du document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // parcourir tous les TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // si le nom de la police est ArialMT, remplacer le nom de la police par Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // Enregistrer le fichier PDF mis à jour
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

Dans le prochain extrait de code, vous verrez comment utiliser une police non anglaise lors du remplacement de texte :

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Instancier un objet Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Changeons chaque mot "PDF" en un texte japonais avec une police spécifique
    // MSGothic qui pourrait être installée dans le système d'exploitation
    // De plus, cela peut être une autre police qui supporte les hiéroglyphes
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Créer une instance des options de recherche de texte
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Accepter l'absorbeur pour toutes les pages du document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtenir les fragments de texte extraits dans la collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Boucle à travers les fragments
    for (auto textFragment : textFragmentCollection) {
        // Mettre à jour le texte et d'autres propriétés
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Enregistrer le document mis à jour
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## Le remplacement de texte devrait réorganiser automatiquement le contenu de la page

Aspose.PDF pour C++ prend en charge la recherche et le remplacement de texte dans un fichier PDF. Récemment, cependant, certains clients ont rencontré des problèmes lors du remplacement de texte, où un TextFragment particulier est remplacé par un contenu plus petit et un espace blanc supplémentaire est affiché dans le PDF résultant, ou si le TextFragment est remplacé par une chaîne plus longue, alors les mots se chevauchent avec le contenu de la page existante. Ainsi, il a été nécessaire d'introduire un mécanisme qui, après avoir remplacé le texte dans le document PDF, réorganise son contenu.

Pour répondre aux scénarios susmentionnés, Aspose.PDF pour C++ a été amélioré afin que de tels problèmes ne se produisent pas lors du remplacement de texte dans un fichier PDF. Le fragment de code suivant démontre comment remplacer le texte dans un fichier PDF et le contenu de la page doit être réorganisé automatiquement.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Instantiate Document object
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Create TextFragment Absorber object with regular expression
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // You also can specify the ReplaceAdjustment.WholeWordsHyphenation option to
    // wrap text on the next or current line if the current line becomes too long or
    // short after replacement:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Accept the absorber for all pages of document
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Get the extracted text fragments into collection
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Replace each TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Set font of text fragment being replaced
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Set font size
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Replace the text with larger string than placeholder
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Save resultant PDF
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Rendu des symboles remplaçables lors de la création de PDF

Les symboles remplaçables sont des symboles spéciaux dans une chaîne de texte qui peuvent être remplacés par le contenu correspondant au moment de l'exécution. Les symboles remplaçables actuellement pris en charge par le nouveau modèle d'objet de document du namespace Aspose.PDF sont `$P`, `$p,` `\n`, `\r`. Les symboles `$p` et `$P` sont utilisés pour gérer la numérotation des pages au moment de l'exécution. `$p` est remplacé par le numéro de la page où se trouve la classe Paragraph actuelle. `$P` est remplacé par le nombre total de pages dans le document. Lors de l'ajout d'un `TextFragment` à la collection de paragraphes des documents PDF, il ne prend pas en charge le saut de ligne à l'intérieur du texte. Cependant, afin d'ajouter du texte avec un saut de ligne, veuillez utiliser `TextFragment` avec `TextParagraph` :

- utilisez "\r\n" ou Environment.NewLine dans TextFragment au lieu d'un seul "\n" ;
- créez un objet TextParagraph. Il ajoutera du texte avec une séparation de ligne ;
- ajoutez le TextFragment avec TextParagraph.AppendLine ;
- ajoutez le TextParagraph avec TextBuilder.AppendParagraph.

```cpp
void RenderingReplaceableSymbols() {

    String _dataDir("C:\\Samples\\");

    // chargez le fichier PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->Add();

    // Initialiser un nouveau TextFragment avec du texte contenant les marqueurs de nouvelle ligne requis
    auto textFragment = MakeObject<TextFragment>("Nom du demandeur : \r\n Joe Smoe");

    // Définir les propriétés du fragment de texte si nécessaire
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Créer un objet TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Ajouter un nouveau TextFragment au paragraphe
    par->AppendLine(textFragment);

    // Définir la position du paragraphe
    par->set_Position(MakeObject<Position>(100, 600));

    // Créer un objet TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);

    // Ajouter le TextParagraph en utilisant TextBuilder
    textBuilder->AppendParagraph(par);

    document->Save(_dataDir + u"RenderingReplaceableSymbols_out.pdf");
}
```

## Symboles remplaçables dans la zone En-tête/Pied de page

Le symbole remplaçable peut également être placé à l'intérieur de la section en-tête/pied de page du fichier PDF. Consultez l'extrait de code suivant pour voir comment ajouter un symbole remplaçable à une section de pied de page.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Assigner l'instance marginInfo à la propriété Margin de PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instancier un paragraphe de texte qui stockera le contenu à afficher comme en-tête
    auto t1 = MakeObject<TextFragment>("titre du rapport");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Nom_Rapport");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Créer un objet HeaderFooter pour la section
    auto hfFoot = MakeObject<HeaderFooter>();

    // Définir l'objet HeaderFooter pour le pied de page impair et pair
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Ajouter un paragraphe de texte contenant le numéro de page actuel sur le nombre total de pages
    auto t3 = MakeObject<TextFragment>("Généré à la date de test");
    auto t4 = MakeObject<TextFragment>("nom du rapport ");
    auto t5 = MakeObject<TextFragment>("Page $p de $P");

    // Instancier un objet table
    auto tab2 = MakeObject<Table>();

    // Ajouter le tableau dans la collection de paragraphes de la section souhaitée
    hfFoot->get_Paragraphs()->Add(tab2);

    // Définir les largeurs des colonnes du tableau
    tab2->set_ColumnWidths(u"165 172 165");

    // Créer des lignes dans le tableau puis des cellules dans les lignes
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Définir l'alignement vertical du texte comme centré
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Ajouter le tableau dans la collection de paragraphes de la section souhaitée
    page.getParagraphs().add(table);

    // Définir la bordure de cellule par défaut à l'aide de l'objet BorderInfo
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Définir la bordure du tableau à l'aide d'un autre objet BorderInfo personnalisé
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Créer des lignes dans le tableau puis des cellules dans les lignes
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total pour C++ est une compilation de chaque composant Java proposé par Aspose. Il est compilé sur une"
                    + CRLF
                    + u"base quotidienne pour s'assurer qu'il contient les versions les plus récentes de chacun de nos composants Java. "
                    + CRLF
                    + u"base quotidienne pour s'assurer qu'il contient les versions les plus récentes de chacun de nos composants Java. "
                    + CRLF
                    + u"En utilisant Aspose.Total pour C++, les développeurs peuvent créer une large gamme d'applications.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Supprimer tout le texte d'un document PDF

### Supprimer tout le texte en utilisant des opérateurs

Dans certaines opérations sur le texte, vous devez supprimer tout le texte du document PDF, et pour cela, vous devez généralement définir le texte trouvé comme une valeur de chaîne vide. Le fait est que changer le texte pour un ensemble de fragments de texte entraîne un certain nombre d'opérations pour vérifier et ajuster la position du texte. Elles sont nécessaires dans les scripts d'édition de texte. La difficulté réside dans le fait que vous ne pouvez pas déterminer combien de morceaux de texte seront supprimés dans le script où ils sont traités dans la boucle.

Par conséquent, nous recommandons d'utiliser une approche différente pour le scénario de suppression de tout le texte des pages PDF.

Le code suivant montre comment résoudre cette tâche rapidement.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Loop through all pages of PDF Document
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Select all text on the page
        page->get_Contents()->Accept(operatorSelector);
        // Delete all text
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Save the document
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```
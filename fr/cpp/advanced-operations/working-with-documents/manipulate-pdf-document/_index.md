---
title: Manipuler un Document PDF
linktitle: Manipuler un Document PDF
type: docs
weight: 30
url: fr/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: Cette section explique la validation d'un Document PDF pour la norme PDF A, comment travailler avec la table des matières, comment définir la date d'expiration du PDF, et comment déterminer la progression de la génération du fichier PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Valider un Document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A-1a ou PDF/A-1b, utilisez la méthode [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis de l'énumération [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) : PDF_A_1A ou PDF_A_1B.

{{% alert color="primary" %}}

Le format XML de sortie est un format Aspose personnalisé. Le XML contient une collection de balises avec le nom Problem ; chaque balise contient les détails d'un problème particulier. L'attribut ObjectID de la balise Problem représente l'ID de l'objet particulier auquel ce problème est lié. L'attribut Clause représente une règle correspondante dans la spécification PDF.

{{% /alert %}}

Le code suivant vous montre comment valider un document PDF pour PDF/A-1A.

```cpp
void ExampleValidate01() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Valider le PDF pour PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

Le code suivant vous montre comment valider un document PDF pour PDF/A-1B.

```cpp
void ExampleValidate02() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Valider le PDF pour PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Travailler avec TOC

### Ajouter une TOC à un PDF existant

L'API Aspose.PDF vous permet d'ajouter une table des matières soit lors de la création d'un PDF, soit à un fichier existant.

Pour ajouter un TOC à un fichier PDF existant, utilisez la classe [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) dans l'espace de noms Aspose.Pdf. L'espace de noms Aspose.Pdf vous permet de créer de nouveaux fichiers PDF et de manipuler des fichiers PDF existants. Pour ajouter un TOC à un PDF existant, utilisez l'espace de noms Aspose.Pdf.

L'extrait de code suivant montre comment créer une table des matières dans un fichier PDF existant.

```cpp
void ExampleToc01() {
    // Chaîne pour les noms de chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour les noms de fichiers
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Accéder à la première page du fichier PDF
    auto tocPage = document->get_Pages()->Insert(1);

    // Créer un objet pour représenter les informations de TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Des Matières");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Définir le titre pour le TOC
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Créer des objets chaîne qui seront utilisés comme éléments de TOC
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"Première page", 0);
    titles->SetValue(u"Deuxième page", 1);
    titles->SetValue(u"Troisième page", 2);
    titles->SetValue(u"Quatrième page", 3);

    for (int i = 0; i < 2; i++)
    {
        // Créer un objet Heading
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Spécifier la page de destination pour l'objet heading

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Page de destination
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Coordonnée de destination
        segment2->set_Text(titles[i]);

        // Ajouter un heading à la page contenant la TOC
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```

### Définir différents TabLeaderType pour différents niveaux de TOC

Aspose.PDF pour C++ permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir la propriété LineDash de FormatArray avec la valeur appropriée de TabLeaderType. Ensuite, vous pouvez ajouter la section de liste à la collection de la section du document Pdf. Après, créez une section dans le document Pdf et enregistrez le fichier PDF.

```cpp
void ExampleToc02() {
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //définir LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Créer un objet pour représenter les informations TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Des Matières");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Définir le titre pour TOC
    tocInfo->set_Title(title);

    //Ajouter la section de liste à la collection des sections du document Pdf
    tocPage->set_TocInfo(tocInfo);

    //Définir le format de la liste des quatre niveaux en définissant les marges de gauche
    //et
    //paramètres de format du texte de chaque niveau

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Créer une section dans le document Pdf
    auto page = document->get_Pages()->Add();

    //Ajouter quatre titres dans la section
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Exemple de Titre" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Ajouter le titre dans la Table Des Matières.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // enregistrer le Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Masquer les numéros de page dans la table des matières

Si vous souhaitez masquer les numéros de page avec les titres dans une table des matières, vous pouvez utiliser la propriété [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) de la classe [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) comme faux.

Veuillez vérifier l'extrait de code suivant pour masquer les numéros de page dans la table des matières :

```cpp
void ExampleToc03() {
    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Créer un objet pour représenter les informations de la table des matières
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Des Matières");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Définir le titre pour la table des matières
    tocInfo->set_Title(title);

    // Ajouter la section de liste à la collection de sections du document Pdf
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // Définir le format de la liste à quatre niveaux en définissant les marges de gauche et
    // paramètres de format de texte de chaque niveau

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // Ajouter quatre titres dans la section
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"ceci est le titre de niveau " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // enregistrer le Pdf
    document->Save(_dataDir + outputFileName);
}
```

## Comment définir une date d'expiration pour un PDF

Nous appliquons des privilèges d'accès aux fichiers PDF afin qu'un certain groupe d'utilisateurs puisse accéder à des fonctionnalités/objets particuliers des documents PDF. Afin de restreindre l'accès au fichier PDF, nous appliquons généralement un cryptage et nous pouvons avoir besoin de définir l'expiration du fichier PDF, de sorte que l'utilisateur accédant/visionnant le document reçoive une notification valide concernant l'expiration du fichier PDF.

Pour accomplir l'exigence énoncée ci-dessus, nous pouvons utiliser l'objet [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). Veuillez consulter l'extrait de code suivant.

```cpp
void SetPDFexpiryDate() {

    // Chaîne pour le nom du chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String outputFileName("SetExpiryDate_out.pdf");

    // Instancier l'objet Document
    auto document = MakeObject<Document>();

    // Ajouter une page à la collection de pages du fichier PDF
    document->get_Pages()->Add();

    // Ajouter un fragment de texte à la collection de paragraphes de l'objet page
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Créer un objet JavaScript pour définir la date d'expiration du PDF
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Définir JavaScript comme action d'ouverture du PDF
    document->set_OpenAction(javaScript);

    // Enregistrer le document PDF
    document->Save(_dataDir + outputFileName);
}
```

## Déterminer la Progression de la Génération de Fichier PDF

Un client nous a demandé d'ajouter une fonctionnalité permettant aux développeurs de déterminer la progression de la génération de fichiers PDF. Voici la réponse à cette demande.

Le champ [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) de la classe [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) vous permet de déterminer comment se déroule la génération du PDF.

Les extraits de code ci-dessous montrent comment utiliser [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Ouvrir le document
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Aplatir un PDF remplissable en C++

Les documents PDF incluent souvent des formulaires avec des widgets remplissables interactifs tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour le rendre non éditable pour divers objectifs d'application, nous devons aplatir le fichier PDF.
Aspose.PDF pour C++ fournit la fonction pour aplatir votre PDF en C++ avec juste quelques lignes de code :

```cpp
void FlattenFillablePDF() {
    // Chaîne pour le nom de chemin.
    String _dataDir("C:\\Samples\\");
    // Chaîne pour le nom du fichier.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Aplatir le PDF remplissable
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outputFileName);
}
```
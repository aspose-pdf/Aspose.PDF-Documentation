```
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /fr/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir d'autres formats de fichiers en document PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB en PDF

**Aspose.PDF for C++** vous permet de convertir simplement des fichiers EPUB au format PDF.

<abbr title="electronic publication">EPUB</abbr> (abréviation de publication électronique) est une norme gratuite et ouverte pour les livres électroniques du Forum International de l'Édition Numérique (IDPF). Les fichiers ont l'extension .epub. EPUB est conçu pour le contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier.

EPUB prend également en charge le contenu à mise en page fixe.
``` Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook. La version EPUB 3 est également approuvée par le Book Industry Study Group (BISG), une association commerciale de premier plan pour les meilleures pratiques standardisées, la recherche, l'information et les événements, pour l'emballage de contenu.

Étapes de conversion :

1. Créez une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Créez une instance de classe [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec mention du nom de fichier source et des options.
1. Chargez et [Enregistrez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier d'entrée.

Le code suivant montre comment convertir des fichiers EPUB au format PDF avec C++.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir EPUB en PDF en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion EPUB en PDF avec application gratuite](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir du texte en PDF

**Aspose.PDF pour C++** prend en charge la fonctionnalité de conversion de texte brut et de fichier texte pré-formaté au format PDF.

Convertir du texte en PDF signifie ajouter des fragments de texte à la page PDF. En ce qui concerne les fichiers texte, nous traitons 2 types de texte : le pré-formatage (par exemple, 25 lignes avec 80 caractères par ligne) et le texte non formaté (texte brut). Selon nos besoins, nous pouvons contrôler cette addition nous-mêmes ou la confier aux algorithmes de la bibliothèque.

### Convertir un fichier texte brut en PDF

Dans le cas d'un fichier texte brut, nous pouvons utiliser la technique suivante :

1. Créer une [Classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom du chemin et le nom du fichier.
1. Lire le fichier texte source en utilisant [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)
1. Instancier un objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Ajouter une [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) à la collection de pages du document.
1. Créer un nouvel objet TextFragment et passer l'objet TextReader à son constructeur.
1. Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment.
1. Charger et [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier d'entrée.

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Lire le fichier texte source
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instancier un objet Document en appelant son constructeur vide
    auto document = MakeObject<Document>();

    // Ajouter une nouvelle page dans la collection de Pages du Document
    auto page = document->get_Pages()->Add();

    // Créer une instance de TextFragmet et passer le texte de l'objet lecteur à son constructeur en tant qu'argument
    auto text = MakeObject<TextFragment>(content);

    // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Enregistrer le fichier PDF résultant
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```
### Convertir un fichier texte pré-formaté en PDF

La conversion de texte pré-formaté est semblable au texte brut, mais vous devez effectuer des actions supplémentaires telles que la définition des marges, du type et de la taille de police. Évidemment, cette police doit être à chasse fixe (par exemple, Courier New).

Suivez ces étapes pour convertir un texte pré-formaté en PDF avec C++ :

1. Instancier un objet Document en appelant son constructeur vide.
1. Définir les marges gauche et droite pour une meilleure présentation.
1. Instancier l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et ajouter une nouvelle page dans la collection Pages.
1. Charger et [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier image d'entrée.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Texte pré-formaté en PDF : Début" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // Lire le fichier texte comme un tableau de chaînes
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // Instancier un objet Document en appelant son constructeur vide
    auto document = MakeObject<Document>();

    // Ajouter une nouvelle page dans la collection Pages du Document
    auto page = document->get_Pages()->Add();

    // Définir les marges gauche et droite pour une meilleure présentation
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // vérifier si la ligne contient le caractère "saut de page"
        // voir https://fr.wikipedia.org/wiki/Saut_de_page
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // Définir les marges gauche et droite pour une meilleure présentation
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // Créer une instance de TextFragment et
        // passer la ligne à son constructeur en tant qu'argument
        auto text = MakeObject<TextFragment>(line);

        // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
        page->get_Paragraphs()->Add(text);
        }
    }

    // Enregistrer le fichier PDF résultant
    document->Save(_dataDir + outfilename);
    std::clog << "Texte pré-formaté en PDF : Fin" << std::endl;
}
```

{{% alert color="success" %}}
**Essayez de convertir du TEXTE en PDF en ligne**

Aspose.PDF pour C++ vous présente l'application gratuite en ligne ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF TEXTE en PDF avec application gratuite](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## Convertir XPS en PDF

**Aspose.PDF pour C++** prend en charge la fonctionnalité de conversion des fichiers <abbr title="XML Paper Specification">XPS</abbr> au format PDF. Consultez cet article pour résoudre vos tâches.

Le type de fichier XPS est principalement associé à la spécification XML Paper Specification par Microsoft Corporation. La spécification XML Paper Specification (XPS), anciennement nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans son système d'exploitation Windows.

{{% alert color="primary" %}}

Le format de fichier est fondamentalement un fichier XML compressé qui est principalement utilisé pour la distribution et le stockage. Il est très difficile de modifier et principalement implémenté par Microsoft.

{{% /alert %}}

Afin de convertir XPS en PDF avec Aspose.PDF pour C++, nous avons introduit une classe nommée [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) qui est utilisée pour initialiser un objet [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options). Plus tard, cet objet est passé comme argument lors de l'initialisation de l'objet Document et il aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le fragment de code suivant montre le processus de conversion d'un fichier XPS au format PDF avec C++.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS à PDF convertir : Début" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS à PDF convertir : Terminé" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir le format XPS en PDF en ligne**

Aspose.PDF pour C++ vous propose une application en ligne gratuite ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF XPS en PDF avec application gratuite](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir XML en PDF

Le format XML est utilisé pour stocker des données structurées. Il existe plusieurs façons de convertir <abbr title="Extensible Markup Language">XML</abbr> en PDF dans Aspose.PDF.

## Convertir XSL-FO en PDF

1. Créez une [classe String](https://reference.aspose.com/pdf/cpp/class/system.string) pour le nom de chemin et le nom de fichier.
1. Instancier un [objet XslFoLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options).
1. Définir la stratégie de gestion des erreurs.
1. Instancier un [objet Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. [Enregistrer](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier image d'entrée.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // Instantiate XslFoLoadOption object
    auto options = new XslFoLoadOptions(infilenameXSL);
    // Set error handling strategy
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Create Document object
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**Essayez de convertir XML en PDF en ligne**

Aspose.PDF pour C++ vous présente l'application en ligne gratuite ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion XML to PDF avec application gratuite](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}
```
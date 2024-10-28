---
title: Extraire le texte de toutes les pages PDF en utilisant C++
linktitle: Extraire le texte du PDF
type: docs
weight: 10
url: /cpp/extract-text-from-all-pdf/
description: Cet article décrit diverses façons d'extraire du texte de documents PDF en utilisant Aspose.PDF en C++. De pages entières, d'une partie spécifique, basé sur des colonnes, etc.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Extraire du texte d'un document PDF est une exigence courante. Dans cet exemple, vous verrez comment Aspose.PDF pour C++ permet d'extraire du texte de toutes les pages d'un document PDF. Vous devez créer un objet de la classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Après cela, ouvrez le PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) et appelez la méthode 'Accept' de la collection [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). La classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) absorbe le texte du document et le renvoie dans la propriété 'Text'. Le fragment de code suivant vous montre comment extraire le texte de toutes les pages d'un document PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom de fichier
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Créer un objet TextAbsorber pour extraire le texte
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accepter l'absorbeur pour toutes les pages
    document->get_Pages()->Accept(textAbsorber);
    // Obtenir le texte extrait
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Appelez la méthode **Accept** sur une page particulière de l'objet Document. L'Index est le numéro de page particulier d'où le texte doit être extrait.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Créer un objet TextAbsorber pour extraire le texte
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Acceptez l'absorbeur pour toutes les pages
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obtenez le texte extrait
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraire du texte des pages en utilisant Text Device

Vous pouvez utiliser la classe [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) pour extraire du texte d'un fichier PDF. TextDevice utilise TextAbsorber dans son implémentation, ainsi, en fait, ils font la même chose mais TextDevice est simplement implémenté pour unifier l'approche "Device" pour extraire quoi que ce soit de la page ImageDevice, PageDevice, etc. TextAbsorber peut extraire du texte d'une Page, d'un PDF entier ou d'un XForm, ce TextAbsorber est plus universel

### Extraire du texte de toutes les pages

Les étapes suivantes et l'extrait de code vous montrent comment extraire du texte d'un PDF en utilisant le dispositif de texte.

1. Créez un objet de la classe Document avec le fichier PDF d'entrée spécifié
1. Créez un objet de la classe TextDevice
1. Utilisez l'objet de la classe TextExtractOptions pour spécifier les options d'extraction
1. Utilisez la méthode Process de la classe TextDevice pour convertir le contenu en texte
1. Enregistrez le texte dans le fichier de sortie

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // Chaîne pour contenir le texte extrait
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // Créer un dispositif de texte
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // Définir les options d'extraction de texte - définir le mode d'extraction de texte (Brut ou Pur)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // Convertir une page particulière et sauvegarder le texte dans le flux
        textDevice->Process(page, textStream);

        // Fermer le flux de mémoire
        textStream->Close();

        // Obtenir le texte du flux de mémoire
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // Sauvegarder le texte extrait dans un fichier texte
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extraire du texte d'une région spécifique de la page

La classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) fournit la capacité d'extraire du texte d'une page ou de toutes les pages d'un document PDF. Cette classe renvoie le texte extrait dans la propriété 'Text'. Cependant, si nous avons besoin d'extraire du texte d'une région spécifique de la page, nous pouvons utiliser la propriété **Rectangle** de [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). La propriété Rectangle prend un objet Rectangle comme valeur et en utilisant cette propriété, nous pouvons spécifier la région de la page à partir de laquelle nous devons extraire le texte.

La méthode **Accept** d'une page est appelée pour extraire le texte. Créez des objets des classes [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) et [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Appelez la méthode 'Accept' sur la page individuelle, comme **Page** Index, de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). L'**Index** est le numéro de page particulier à partir duquel le texte doit être extrait. Vous pouvez obtenir le texte à partir de la propriété 'Text' de la classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Le code suivant vous montre comment extraire du texte d'une page individuelle.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom de fichier
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Créer un objet TextAbsorber pour extraire le texte
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Accepter l'absorbeur pour toutes les pages
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Obtenez le texte extrait
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## Extraire le texte basé sur les colonnes

PDF est un format très populaire, et pour une bonne raison : avec PDF, vous pouvez être pratiquement sûr que votre document s'affichera et s'imprimera de la même manière sur différents ordinateurs.

Cependant, les documents PDF souffrent de l'inconvénient qu'ils manquent généralement d'informations sur le contenu des paragraphes, des tableaux, des figures, des informations d'en-tête/pied de page, etc.

Aspose.PDf pour C++ - c'est un utilitaire facile à utiliser, qui vous permet d'extraire du texte basé sur les colonnes.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Créer un objet TextAbsorber pour extraire le texte
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Accepter l'absorbeur pour toutes les pages
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Besoin de réduire la taille de la police d'au moins 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Deuxième approche - Utilisation de ScaleFactor

Dans cette nouvelle version, nous avons également introduit plusieurs améliorations dans TextAbsorber et dans le mécanisme de formatage de texte interne. Ainsi, maintenant lors de l'extraction de texte en utilisant le mode 'Pure', vous pouvez spécifier l'option [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) et cela peut être une autre approche pour extraire le texte d'un document PDF à colonnes multiples en plus de l'approche mentionnée ci-dessus. Ce facteur d'échelle peut être défini pour ajuster la grille utilisée pour le mécanisme de formatage de texte interne lors de l'extraction de texte. Spécifier les valeurs de ScaleFactor entre 1 et 0.1 (y compris 0.1) a le même effet que la réduction de police.

Spécifier les valeurs de ScaleFactor entre 0.1 et -0.1 est traité comme une valeur zéro, mais cela fait que l'algorithme calcule automatiquement le facteur d'échelle nécessaire lors de l'extraction de texte. Le calcul est basé sur la largeur moyenne des glyphes de la police la plus populaire sur la page, mais nous ne pouvons pas garantir que dans le texte extrait, aucune chaîne de colonne n'atteint le début de la colonne suivante. Veuillez noter que si la valeur de ScaleFactor n'est pas spécifiée, la valeur par défaut de 1.0 sera utilisée. Cela signifie qu'aucun redimensionnement ne sera effectué. Si la valeur de ScaleFactor spécifiée est supérieure à 10 ou inférieure à -0.1, la valeur par défaut de 1.0 sera utilisée.

Nous proposons l'utilisation du redimensionnement automatique (ScaleFactor = 0) lors du traitement d'un grand nombre de fichiers PDF pour l'extraction de contenu textuel. Ou définissez manuellement la réduction redondante de la largeur de la grille (environ ScaleFactor = 0.5). Cependant, vous ne devez pas déterminer si le redimensionnement est nécessaire pour des documents concrets ou non. Si vous définissez une réduction redondante de la largeur de la grille pour le document (qui n'en a pas besoin), le contenu textuel extrait restera entièrement adéquat. Veuillez consulter l'exemple de code suivant.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Extraire le texte surligné du document PDF

Dans divers scénarios d'extraction de texte d'un document PDF, vous pouvez avoir besoin d'extraire uniquement le texte surligné du document PDF. Afin de mettre en œuvre cette fonctionnalité, nous avons ajouté les méthodes TextMarkupAnnotation.GetMarkedText() et TextMarkupAnnotation.GetMarkedTextFragments() dans l'API. Vous pouvez extraire le texte surligné d'un document PDF en filtrant TextMarkupAnnotation et en utilisant les méthodes mentionnées. Le code suivant montre comment vous pouvez extraire le texte surligné d'un document PDF.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom de fichier
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Boucle à travers toutes les annotations
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // Filtrer TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // Récupérer les fragments de texte surlignés
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // Afficher le texte surligné
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## Accéder aux Éléments de Fragment et Segment de Texte depuis XML

Parfois, nous avons besoin d'accéder aux éléments TextFragment ou TextSegment lors du traitement des documents PDF générés à partir de XML. Aspose.PDF pour C++ permet d'accéder à ces éléments par nom. L'extrait de code ci-dessous montre comment utiliser cette fonctionnalité.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // Effectuer certaines opérations avec la page
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // Effectuer certaines opérations avec le segment
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```
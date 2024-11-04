---
title: Convertir un fichier PDF en d'autres formats 
linktitle: Convertir PDF en d'autres formats 
type: docs
weight: 90
url: /cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en d'autres formats de fichier.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (abréviation de Electronic Publication) est une norme de livre numérique libre et ouverte de l'International Digital Publishing Forum (IDPF). Les fichiers ont l'extension .epub.
EPUB est conçu pour un contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est conçu comme un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour C++ prend également en charge la fonctionnalité de conversion de documents PDF en format EPUB. Aspose.PDF pour C++ a une classe nommée EpubSaveOptions qui peut être utilisée comme second argument à la méthode [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa), pour générer un fichier EPUB.
Veuillez essayer d'utiliser l'extrait de code suivant pour accomplir cette exigence avec C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for output file name
    String outfilename("PDFToEPUB_out.epub");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Save PDF file into EPUB format
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour C++** prend en charge la conversion de PDF en LaTeX/TeX. Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

Pour convertir des fichiers PDF en TeX, Aspose.PDF a la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) qui fournit la propriété OutDirectoryPath pour enregistrer des images temporaires pendant le processus de conversion.

L'extrait de code suivant montre le processus de conversion des fichiers PDF au format TEX avec C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToTeX_out.tex");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'option de sauvegarde LaTex
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // Définir le chemin du répertoire de sortie pour l'objet option de sauvegarde
    saveOptions->set_OutDirectoryPath(_dataDir);

    // Enregistrer le fichier PDF au format LaTex
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF pour C++ vous présente l'application en ligne gratuite ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF en Texte

**Aspose.PDF pour C++** supporte la conversion de l'ensemble du document PDF et de la page unique en un fichier Texte.

### Convertir l'ensemble du document PDF en fichier Texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

Le code suivant explique comment extraire les textes de toutes les pages.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("input_Text_Extracted_out.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Enregistrer le texte extrait dans un fichier texte
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF pour C++. Vous devez utiliser la classe [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) pour résoudre cette tâche.

Le code ci-dessous explique comment extraire les textes des pages particulières.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Début" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample-4pages.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("sample-4pages_out.txt");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // Enregistrer le texte extrait dans un fichier texte
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Fin" << std::endl;
}
```

{{% alert color="success" %}}
**Essayez de convertir Convertir PDF en texte en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en texte avec application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en XPS

**Aspose.PDF pour C++** offre la possibilité de convertir des fichiers PDF au format <abbr title="XML Paper Specification">XPS</abbr>. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF au format XPS avec C++.

Le type de fichier XPS est principalement associé à la XML Paper Specification par Microsoft Corporation. La XML Paper Specification (XPS), anciennement nommée Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) qui est utilisée comme second argument de la méthode [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) pour générer le fichier XPS.

Le code suivant montre le processus de conversion d'un fichier PDF en format XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToXPS_out.xps");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'option de sauvegarde LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // Enregistrer le fichier PDF en format XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Essayez de convertir un PDF en SVG en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.
{{% /alert %}}


[![Aspose.PDF Conversion PDF to SVG with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
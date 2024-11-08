---
title: Convertir un fichier PDF au format HTML
linktitle: Convertir un fichier PDF au format HTML
type: docs
weight: 50
url: /fr/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF au format HTML avec la bibliothèque C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** fournit de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en <abbr title="HyperText Markup Language">HTML</abbr>. Aspose.PDF for C++ offre la possibilité de convertir des fichiers HTML en format PDF en utilisant l'approche InLineHtml. Nous avons reçu de nombreuses demandes pour une fonctionnalité qui convertit un fichier PDF en format HTML et avons fourni cette fonctionnalité. Veuillez noter que cette fonctionnalité prend également en charge XHTML 1.0.

**Aspose.PDF for C++** prend en charge les fonctionnalités pour convertir un fichier PDF en HTML. Les principales tâches que vous pouvez accomplir avec la bibliothèque Aspose.PDF sont listées :

- convertir PDF en HTML ;
- diviser la sortie en HTML multi-pages ;
- spécifier le dossier pour stocker les fichiers SVG ;
- compresser les images SVG pendant la conversion ;
- spécifier le dossier des images ;
- créer des fichiers subséquents avec uniquement le contenu du corps ;
- rendu de texte transparent ;
- rendu des couches du document PDF.

Aspose.PDF pour C++ fournit un code en deux lignes pour transformer un fichier PDF source en HTML. L'énumération `SaveFormat` contient la valeur Html qui vous permet d'enregistrer le fichier source en HTML. Le snippet de code suivant montre le processus de conversion d'un fichier PDF en HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Save the output in HTML format
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir PDF en HTML en ligne**

Aspose.PDF for C++ vous présente l'application en ligne gratuite ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'évaluer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en HTML avec l'application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Fractionnement de la sortie en HTML multi-pages

Lors de la conversion d'un fichier PDF volumineux avec plusieurs pages au format HTML, la sortie apparaît sous forme d'une seule page HTML. Cela peut finir par être très long. Pour contrôler la taille de la page, il est possible de diviser la sortie en plusieurs pages lors de la conversion de PDF en HTML. Veuillez essayer d'utiliser le code suivant.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Début" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Spécifier de diviser la sortie en plusieurs pages
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Fin" << std::endl;
}
```

## Spécifier le Dossier pour Stocker les Fichiers SVG

Lors de la conversion de PDF en HTML, il est possible de spécifier le dossier dans lequel les images SVG doivent être enregistrées. Utilisez la [`classe HtmlSaveOption`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`propriété SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) pour spécifier un répertoire d'images SVG spécial. Cette propriété obtient ou définit le chemin vers le répertoire dans lequel les images SVG doivent être enregistrées lorsqu'elles sont rencontrées lors de la conversion. Si le paramètre est vide ou nul, alors tous les fichiers SVG sont enregistrés avec les autres fichiers image.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Spécifier le dossier où les images SVG sont enregistrées lors de la conversion PDF en HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Compression des images SVG lors de la conversion

Pour compresser les images SVG lors de la conversion PDF en HTML, veuillez essayer d'utiliser le code suivant :

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Spécifiez le dossier où les images SVG sont enregistrées lors de la conversion PDF en HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Enregistrez la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Spécification du dossier d'images

Nous pouvons également spécifier le dossier où les images seront enregistrées lors de la conversion PDF en HTML :

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Démarrer" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Spécifier le dossier où toutes les images sont enregistrées lors de la conversion de PDF en HTML
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Terminer" << std::endl;
}
```

## Créer des fichiers suivants avec uniquement le contenu du corps

Récemment, on nous a demandé d'introduire une fonctionnalité où les fichiers PDF sont convertis en HTML et l'utilisateur peut obtenir uniquement le contenu de la balise `<body>` pour chaque page. Cela produirait un fichier avec les détails CSS, `<html>`, `<head>` et toutes les pages dans d'autres fichiers juste avec les contenus `<body>`.

Pour répondre à cette exigence, une nouvelle propriété, HtmlMarkupGenerationMode, a été introduite dans la classe [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

Avec l'exemple de code simple suivant, vous pouvez diviser le HTML de sortie en pages. Dans les pages de sortie, tous les objets HTML doivent aller exactement là où ils vont maintenant (traitement et sortie des polices, création et sortie de CSS, création et sortie d'images), sauf que le HTML de sortie contiendra les contenus actuellement placés à l'intérieur des balises (maintenant, les balises “body” seront omises). Cependant, en utilisant cette approche, le lien vers le CSS est la responsabilité de votre code, car des éléments comme seront supprimés. À cette fin, vous pouvez lire le CSS via File.ReadAllText() et l'envoyer via AJAX à une page web où il sera appliqué par jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Rendu de texte transparent

Dans le cas où le fichier PDF source/entrée contient des textes transparents ombragés par des images de premier plan, il pourrait y avoir des problèmes de rendu de texte. Donc, afin de répondre à ces scénarios, les propriétés [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) et SaveTransparentTexts peuvent être utilisées.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Rendu des couches de document PDF

Nous pouvons rendre les couches de document PDF dans un élément de type couche séparée lors de la conversion de PDF en HTML :

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Début" << std::endl;
    // Chaîne pour le chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier un objet d'option de sauvegarde HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Spécifier de rendre les couches du document PDF séparément dans le HTML de sortie
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Enregistrer la sortie au format HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Fin" << std::endl;
}
```
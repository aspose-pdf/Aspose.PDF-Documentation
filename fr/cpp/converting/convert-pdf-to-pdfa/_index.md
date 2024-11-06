---
title: Convertir des PDF aux formats PDF/A 
linktitle: Convertir des PDF aux formats PDF/A
type: docs
weight: 100
url: fr/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme à PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour C++** vous permet de convertir un fichier PDF en un fichier PDF conforme à <abbr title="Portable Document Format / A">PDF/A</abbr>. Avant de le faire, le fichier doit être validé. Ce sujet explique comment.

{{% alert color="primary" %}}

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre « représentation » de la conformité PDF/A. Veuillez consulter cet article sur les outils de validation PDF/A à titre de référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF car Adobe est au centre de tout ce qui est lié au PDF.

{{% /alert %}}

Convertissez le fichier à l'aide de la méthode Convert de la classe Document. Avant de convertir le PDF en un fichier conforme à PDF/A, validez le PDF en utilisant la méthode Validate. Le résultat de la validation est stocké dans un fichier XML et ce résultat est ensuite passé à la méthode Convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération ConvertErrorAction.

## Convertir un fichier PDF en PDF/A-1b

Le snippet de code suivant montre comment convertir des fichiers PDF en PDF conformes à PDF/A-1b.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier journal
    String logfilename("log.xml");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToPDFA_out.pdf");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Convertir en document conforme à PDF/A
    // Pendant le processus de conversion, la validation est également effectuée
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de log
    String logfilename("log.xml");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Convertir en document conforme PDF/A
    // Pendant le processus de conversion, la validation est également effectuée
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir un fichier PDF en PDF/A-3b

Aspose.PDF pour C++ prend également en charge la fonctionnalité de conversion d'un fichier PDF au format PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de log
    String logfilename("log.xml");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToPDFA3b_out.pdf");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Convertir en document conforme PDF/A
    // Pendant le processus de conversion, la validation est également effectuée
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir un fichier PDF en PDF/A-2u

Aspose.PDF pour C++ prend également en charge la fonctionnalité de conversion d'un fichier PDF au format PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier journal
    String logfilename("log.xml");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToPDFA3b_out.pdf");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Convertir en document conforme PDF/A
    // Pendant le processus de conversion, la validation est également effectuée
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir un fichier PDF en PDF/A-3u

Aspose.PDF pour C++ prend également en charge la fonctionnalité de conversion d'un fichier PDF au format PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Début" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier journal
    String logfilename("log.xml");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToPDFA3b_out.pdf");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Convertir en document conforme PDF/A
    // Lors du processus de conversion, la validation est également effectuée
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Fin" << std::endl;
}
```

## Ajouter une pièce jointe au fichier PDF/A

Dans le cas où vous auriez besoin de joindre des fichiers au format de conformité PDF/A, nous recommandons d'utiliser la valeur PDF_A_3A de l'énumération Aspose.PDF.PdfFormat.

PDF/A_3a est le format qui offre la possibilité de joindre n'importe quel format de fichier en tant que pièce jointe à un fichier conforme PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": Début" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier d'entrée
    String infilename("sample.pdf");
    // Chaîne pour le nom du fichier de log
    String logfilename("log.xml");
    // Chaîne pour le nom du fichier de sortie
    String outfilename("PDFToPDFA3b_out.pdf");

    // Ouvrir le document
    auto document = new Document(_dataDir + infilename);

    // Configurer un nouveau fichier à ajouter en tant que pièce jointe
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("Fichier image de grande taille"));
    // Ajouter la pièce jointe à la collection de pièces jointes du document
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // Convertir en document conforme à PDF/A
    // Pendant le processus de conversion, la validation est également effectuée
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // Enregistrer le document de sortie
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Fin" << std::endl;
}
```

## Remplacer les polices manquantes par des polices alternatives

Conformément aux normes PDFA, les polices doivent être intégrées dans le document PDFA. Cependant, si les polices ne sont pas intégrées dans le document source ou n'existent pas sur la machine, alors le PDFA échoue à la validation. Dans ce cas, nous avons besoin de remplacer les polices manquantes par des polices alternatives de la machine. Nous pouvons substituer les polices manquantes en utilisant la méthode SimpleFontSubstitution comme suit lors de la conversion de PDF en PDFA.

{{% alert color="primary" %}}
**Essayez de convertir PDF en PDF/A en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF vers PDF/A avec Application Gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}
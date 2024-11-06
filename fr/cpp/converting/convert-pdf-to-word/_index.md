---
title: Convertir des documents PDF en Microsoft Word en C++
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: fr/cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: La bibliothèque Aspose.PDF pour C++ vous permet de convertir des PDF en format Word en utilisant C++ avec facilité et contrôle total. Ces formats incluent DOC et DOCX. Apprenez-en plus sur la manière d'optimiser la conversion de documents PDF en Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Vue d'ensemble

Cet article explique comment convertir des documents PDF en Microsoft Word en utilisant C++. Il couvre les sujets suivants.

_Format_: **DOC**
- [PDF à DOC en C++](#cpp-pdf-to-doc)
- [Convertir PDF en DOC en C++](#cpp-pdf-to-doc)
- [Comment convertir un fichier PDF en DOC en C++](#cpp-pdf-to-doc)

_Format_: **DOCX**
- [PDF à DOCX en C++](#cpp-pdf-to-docx)
- [Convertir PDF en DOCX en C++](#cpp-pdf-to-docx)
- [Comment convertir un fichier PDF en DOCX en C++](#cpp-pdf-to-docx)

_Format_: **Format Microsoft Word DOC**
- [PDF à Word en C++](#cpp-pdf-to-word-doc)
- [Convertir PDF en Word en C++](#cpp-pdf-to-word-doc)

- [Comment convertir un fichier PDF en Word en C++](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX format**
- [C++ PDF vers Word](#cpp-pdf-to-word-docx)
- [C++ Convertir PDF en Word](#cpp-pdf-to-word-docx)
- [C++ Comment convertir un fichier PDF en Word](#cpp-pdf-to-word-docx)

Autres sujets couverts par cet article
- [Voir aussi](#see-also)

## Conversions de PDF en Word en C++

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC Microsoft Word, ce qui facilite la manipulation du contenu. Aspose.PDF pour C++ vous permet de convertir des fichiers PDF en DOC.

## Convertir un fichier PDF en DOC (Word 97-2003)

Convertissez un fichier PDF au format DOC avec facilité et contrôle total. Aspose.PDF pour C++ est flexible et prend en charge une grande variété de conversions. La conversion de pages de documents PDF en images, par exemple, est une fonctionnalité très populaire.

Une conversion que beaucoup de nos clients ont demandée est la conversion de PDF en DOC : convertir un fichier PDF en document Microsoft Word. Les clients veulent cela parce que les fichiers PDF ne peuvent pas être facilement modifiés, alors que les documents Word le peuvent. Certaines entreprises souhaitent que leurs utilisateurs puissent manipuler le texte, les tableaux et les images dans des fichiers qui ont commencé comme des PDF.

En gardant vivante la tradition de rendre les choses simples et compréhensibles, Aspose.PDF pour C++ vous permet de transformer un fichier PDF source en un fichier DOC avec deux lignes de code. Pour accomplir cette fonctionnalité, nous avons introduit une énumération nommée SaveFormat et sa valeur .Doc vous permet d'enregistrer le fichier source au format Microsoft Word.

Le code C++ suivant montre le processus de conversion d'un fichier PDF en format DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Étapes : Convertir un PDF en DOC en C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Étapes : Convertir un PDF en format Microsoft Word DOC en C++</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le document PDF source.
2. Sauvegardez-le au format **SaveFormat::Doc** en appelant la méthode **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Enregistrer le fichier au format document MS
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

Le code suivant montre le processus de conversion d'un fichier PDF en version DOC Avancée :

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Définir le mode de reconnaissance comme Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Définir la proximité horizontale à 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Activer la valeur pour reconnaître les puces pendant le processus de conversion
    saveOptions->set_RecognizeBullets(true);

    try {
        // Enregistrer le fichier au format document MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Essayez de convertir un PDF en DOC en ligne**

Aspose.PDF pour C++ vous propose une application en ligne gratuite ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Convertir PDF en DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF pour C++ API vous permet de lire et de convertir des documents PDF en DOCX en utilisant le langage C++. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été changée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui prennent en charge les extensions de fichiers DOC.

Le code C++ suivant montre le processus de conversion d'un fichier PDF en format DOCX.


<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Étapes : Convertir PDF en DOCX en C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Étapes : Convertir PDF en format Microsoft Word DOCX en C++</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat::DocX** en appelant la méthode **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Enregistrer le fichier au format document MS
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

La classe [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) a une propriété nommée Format qui offre la possibilité de spécifier le format du document résultant, c'est-à-dire, DOC ou DOCX. Afin de convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l'énumération DocSaveOptions.DocFormat.

Veuillez consulter l'extrait de code suivant qui offre la possibilité de convertir un fichier PDF au format DOCX avec C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le chemin d'accès
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Définir d'autres paramètres DocSaveOptions
    // ...

    // Enregistrer le fichier au format MS document

    try {
        // Enregistrer le fichier au format MS document
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application gratuite](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_: **Format Microsoft Word DOC**
- [C++ PDF vers Code Word](#cpp-pdf-to-word-doc)
- [C++ PDF vers API Word](#cpp-pdf-to-word-doc)
- [C++ PDF vers Word Programmatiquement](#cpp-pdf-to-word-doc)
- [C++ PDF vers Bibliothèque Word](#cpp-pdf-to-word-doc)
- [C++ Enregistrer PDF en tant que Word](#cpp-pdf-to-word-doc)
- [C++ Générer Word à partir de PDF](#cpp-pdf-to-word-doc)
- [C++ Créer Word à partir de PDF](#cpp-pdf-to-word-doc)
- [C++ Convertisseur PDF en Word](#cpp-pdf-to-word-doc)

_Format_: **Format Microsoft Word DOCX**

- [C++ PDF vers Code Word](#cpp-pdf-to-word-docx)
- [C++ PDF vers Word API](#cpp-pdf-to-word-docx)
- [C++ PDF vers Word Programmatiquement](#cpp-pdf-to-word-docx)
- [C++ PDF vers Word Bibliothèque](#cpp-pdf-to-word-docx)
- [C++ Enregistrer PDF en tant que Word](#cpp-pdf-to-word-docx)
- [C++ Générer Word à partir de PDF](#cpp-pdf-to-word-docx)
- [C++ Créer Word à partir de PDF](#cpp-pdf-to-word-docx)
- [C++ Convertisseur PDF en Word](#cpp-pdf-to-word-docx)

_Format_: **DOC**
- [C++ PDF vers DOC Code](#cpp-pdf-to-doc)
- [C++ PDF vers DOC API](#cpp-pdf-to-doc)
- [C++ PDF vers DOC Programmatiquement](#cpp-pdf-to-doc)
- [C++ PDF vers DOC Bibliothèque](#cpp-pdf-to-doc)
- [C++ Enregistrer PDF en tant que DOC](#cpp-pdf-to-doc)
- [C++ Générer DOC à partir de PDF](#cpp-pdf-to-doc)
- [C++ Créer DOC à partir de PDF](#cpp-pdf-to-doc)
- [C++ Convertisseur PDF en DOC](#cpp-pdf-to-doc)

_Format_: **DOC**
- [C++ PDF vers DOCX Code](#cpp-pdf-to-docx)
- [C++ PDF vers DOCX API](#cpp-pdf-to-docx)
- [C++ PDF vers DOCX Programmatiquement](#cpp-pdf-to-docx)
- [C++ PDF vers DOCX Bibliothèque](#cpp-pdf-to-docx)
- [C++ Enregistrer PDF en tant que DOCX](#cpp-pdf-to-docx)

- [C++ Générer DOCX à partir de PDF](#cpp-pdf-to-docx)
- [C++ Créer DOCX à partir de PDF](#cpp-pdf-to-docx)
- [C++ Convertisseur PDF en DOCX](#cpp-pdf-to-docx)
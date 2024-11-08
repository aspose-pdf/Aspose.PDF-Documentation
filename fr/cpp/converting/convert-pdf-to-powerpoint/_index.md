---
title: Convertir un PDF en Microsoft PowerPoint en C++
linktitle: Convertir un PDF en PowerPoint
type: docs
weight: 30
url: /fr/cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF vous permet de convertir un PDF au format PowerPoint en utilisant C++. Il est possible de convertir un PDF en PPTX avec des diapositives sous forme d'images.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Aperçu

Cet article explique comment **convertir des PDF en formats PowerPoint en utilisant C++**. Il couvre les sujets suivants.

_Format_: **PPTX**
- [C++ PDF en PPTX](#cpp-pdf-to-pptx)
- [C++ Convertir un PDF en PPTX](#cpp-pdf-to-pptx)
- [C++ Comment convertir un fichier PDF en PPTX](#cpp-pdf-to-pptx)

_Format_: **Format Microsoft PowerPoint PPTX**
- [C++ PDF en PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Convertir un PDF en PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Comment convertir un fichier PDF en PowerPoint](#cpp-pdf-to-powerpoint-pptx)

Autres sujets couverts par cet article.
- [Voir aussi](#see-also)

## Conversions de PDF en PowerPoint en C++

**Aspose.PDF pour C++** vous permet de suivre la progression de la conversion de PDF en PPTX.

Pendant la conversion de PDF à <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, le texte est rendu comme Texte où vous pouvez le sélectionner/mettre à jour. Veuillez noter que pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Un objet de la classe PptxSaveOptions est passé comme second argument à la méthode [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa). L'extrait de code suivant montre le processus pour convertir des fichiers PDF en format PPTX.

## Conversion simple de PDF en PPTX avec Aspose.PDF pour C++

Afin de convertir PDF en PPTX, Aspose.PDF pour C++ conseille d'utiliser les étapes de code suivantes.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>Étapes : Convertir PDF en PPTX en C++</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>Étapes : Convertir PDF en format PowerPoint PPTX en C++</strong></a>

1. Créez une instance de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
2. Créez une instance de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options).
3. Utilisez la méthode **Save** de l'objet **Document** pour _enregistrer le PDF en tant que PPTX_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Enregistrer la sortie au format PPTX
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir le PDF en PPTX avec des diapositives comme images

Dans le cas où vous avez besoin de convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF offre cette fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options). Pour y parvenir, définissez la propriété [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) sur 'true' comme indiqué dans l'exemple de code suivant.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // Enregistrer la sortie au format PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Détail de la progression de la conversion PPTX

Aspose.PDF pour C++ vous permet de suivre la progression de la conversion de PDF en PPTX. Le [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) classe fournit la propriété [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) qui peut être spécifiée à une méthode personnalisée pour suivre la progression de la conversion comme indiqué dans l'exemple de code suivant.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //Spécifier le gestionnaire de progression personnalisé
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // Enregistrer la sortie au format PPTX
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Suivi est la méthode personnalisée pour afficher la conversion de progression.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Progression de la conversion : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Page de résultat " << eventInfo->Value << " de " << eventInfo->MaxValue << " mise en page créée." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Page de résultat " << eventInfo->Value << " de " << eventInfo->MaxValue << " exportée." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - Page source " << eventInfo->Value << " de " << eventInfo->MaxValue << " analysée." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour C++ vous présente une application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Voir Aussi

Cet article couvre également ces sujets. Les codes sont identiques à ceux ci-dessus.

_Format_: **PowerPoint**
- [C++ PDF vers PowerPoint Code](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF vers PowerPoint API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF vers PowerPoint Programmatiquement](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF vers PowerPoint Bibliothèque](#cpp-pdf-to-powerpoint-pptx)
- [C++ Enregistrer PDF comme PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ Générer PowerPoint à partir de PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Créer PowerPoint à partir de PDF](#cpp-pdf-to-powerpoint-pptx)

- [C++ Convertisseur PDF vers PowerPoint](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF to PowerPoint PPTX Code](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX Programmatically](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF to PowerPoint PPTX Library](#cpp-pdf-to-powerpoint-pptx)
- [C++ Enregistrer le PDF comme PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ Générer PowerPoint PPTX à partir de PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Créer PowerPoint PPTX à partir de PDF](#cpp-pdf-to-powerpoint-pptx)
- [C++ Convertisseur PDF en PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF to PPTX Code](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX Programmatically](#cpp-pdf-to-pptx)
- [C++ PDF to PPTX Library](#cpp-pdf-to-pptx)
- [C++ Enregistrer le PDF comme PPTX](#cpp-pdf-to-pptx)
- [C++ Générer PPTX à partir de PDF](#cpp-pdf-to-pptx)
- [C++ Créer PPTX à partir de PDF](#cpp-pdf-to-pptx)
- [C++ Convertisseur PDF en PPTX](#cpp-pdf-to-pptx)
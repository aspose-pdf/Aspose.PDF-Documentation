---
title: Enregistrer un document PDF en utilisant C++
linktitle: Enregistrer
type: docs
weight: 30
url: fr/cpp/save-pdf-document/
description: Apprenez à enregistrer un fichier PDF avec la bibliothèque Aspose.PDF pour C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Enregistrer un document PDF dans le système de fichiers

Vous pouvez enregistrer le document PDF créé ou modifié dans le système de fichiers en utilisant la méthode Save de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // faire des manipulations, par exemple ajouter une nouvelle page vide
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## Enregistrer un document PDF dans un flux

Vous pouvez également enregistrer le document PDF créé ou modifié dans un flux en utilisant les surcharges des méthodes Save.

```cpp
void SaveDocumentStream()
{
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // faire des manipulations, par exemple ajouter une nouvelle page vide
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## Enregistrer au format PDF/A ou PDF/X

PDF/A est une version du format de document portable (PDF) normalisée par l'ISO pour être utilisée dans l'archivage et la préservation à long terme des documents électroniques. PDF/A diffère du PDF en ce qu'il interdit des fonctionnalités non adaptées à l'archivage à long terme, telles que le lien de police (par opposition à l'incorporation de police) et le cryptage. Les exigences ISO pour les visionneuses PDF/A incluent des directives de gestion des couleurs, la prise en charge des polices incorporées et une interface utilisateur pour lire les annotations incorporées.

PDF/X est un sous-ensemble de la norme ISO PDF. Le but de PDF/X est de faciliter l'échange graphique, et il comprend donc une série d'exigences liées à l'impression qui ne s'appliquent pas aux fichiers PDF standard.

Dans les deux cas, la méthode Save est utilisée pour stocker les documents, tandis que les documents doivent être préparés en utilisant les [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\");

    // Chaîne pour le nom du fichier
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```
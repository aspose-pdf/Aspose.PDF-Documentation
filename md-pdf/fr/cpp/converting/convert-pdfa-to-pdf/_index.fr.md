---
title: Convertir le format PDF/A en PDF
linktitle: Convertir le format PDF/A en PDF
type: docs
weight: 110
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF avec la bibliothèque C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir un document PDF/A en PDF

Convertir un document PDF/A en PDF signifie supprimer la restriction <abbr title="Portable Document Format Archive">PDF/A</abbr> du document original. La classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) possède la méthode 'RemovePdfaCompliance' pour supprimer l'information de conformité PDF du fichier d'entrée/source. Après [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) le fichier d'entrée.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Supprimer les informations de conformité PDF/A
    document->RemovePdfaCompliance();

    // Enregistrer le document mis à jour
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

Cette information est également supprimée si vous apportez des modifications au document (par exemple, ajouter des pages). Dans l'exemple suivant, le document de sortie perd la conformité PDF/A après l'ajout de la page.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Adding a new (empty) page removes PDF/A compliance information.

    document->get_Pages()->Add();
    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```
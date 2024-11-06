---
title: Quoi de neuf dans C++
linktitle: Quoi de neuf
type: docs
weight: 10
url: fr/cpp/whatsnew/
description: Cette page présente les nouvelles fonctionnalités les plus populaires dans Aspose.PDF pour C++ qui ont été introduites dans les versions récentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Quoi de neuf dans Aspose.PDF 24.8

Possibilité d'ajouter des images SVG à une page.

## Quoi de neuf dans Aspose.PDF 24.4

Correction d'un problème de chargement des images SVG.

## Quoi de neuf dans Aspose.PDF 24.3

Correction des fuites de mémoire lors de la conversion de documents PDF en d'autres formats.

## Quoi de neuf dans Aspose.PDF 24.2

Depuis la version 24.2, ont été implémentés :

- La performance du JPXDecoder a été améliorée.

- Correction de la lecture des documents avec une structure cassée.

## Quoi de neuf dans Aspose.PDF 23.7

- La sauvegarde des documents PDF au format EPUB a été introduite :

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

- Le chargement des fichiers au format PCL a été implémenté :

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Erreur : {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Erreur : " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Quoi de neuf dans Aspose.PDF 23.1

À partir de 23.1, la prise en charge des images au format Dicom a été ajoutée :

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Quoi de neuf dans Aspose.PDF 22.11

À partir de 22.11, la première version publique de **Aspose.PDF pour C++ macOS** a été annoncée.

Nous sommes heureux d'annoncer la première version publique d'Aspose.PDF pour C++ macOS. Aspose.PDF pour C++ macOS est une bibliothèque C++ propriétaire qui permet aux développeurs de créer et de manipuler des documents PDF sans utiliser Adobe Acrobat.
Aspose.PDF pour C++ macOS permet aux développeurs de créer des formulaires, d'ajouter/modifier du texte, de manipuler des pages PDF, d'ajouter des annotations, de traiter des polices personnalisées, et plus encore.

## Quoi de neuf dans Aspose.PDF 22.5

La prise en charge des formulaires XFA dans les documents PDF a été mise en œuvre.

## Quoi de neuf dans Aspose.PDF 22.4

La nouvelle version d'Aspose.PDF pour C++ a une base de code d'Aspose.PDF pour .Net 22.4 et Aspose.Imaging 22.4.

- la méthode System::Drawing::GetThumbnailImage() a été mise en œuvre ;
- le constructeur RegionDataNodeRect a été optimisé ;
- le chargement d'image noir et blanc de 1 bit par pixel a été corrigé.

## Quoi de neuf dans Aspose.PDF 22.3

Les surcharges de méthode ont été ajoutées à de nombreuses classes. Ces paramètres de support de type ArrayView où seul ArrayPtr était pris en charge auparavant.

## Quoi de neuf dans Aspose.PDF 22.1

La nouvelle version d'Aspose.PDF pour C++ a une base de code d'Aspose.PDF pour .Net 22.1 :

- la nouvelle implémentation pour System::Xml a été fournie. Auparavant, nous avions une implémentation personnalisée basée sur les bibliothèques libxml2 et libxslt. La nouvelle version est basée sur le code CoreFX porté

- la bibliothèque double-conversion a été mise à niveau vers la version 3.1.7

- Les fichiers Dll sont signés avec le certificat Aspose

## Quoi de neuf dans Aspose.PDF 21.10

### Aspose.PDF pour C++ prend en charge la conversion de SVG en format PDF

Le code suivant montre le processus de conversion d'un fichier SVG en format PDF avec Aspose.PDF pour C++.

```cpp

    void ConvertSVGtoPDF()
    {
        std::clog << "Conversion SVG en PDF : Début" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("sample.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }
        std::clog << "Conversion SVG en PDF : Fin" << std::endl;
    }
```
Сonsidérer un exemple avec des fonctionnalités avancées :

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "Conversion SVG en PDF : Début" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        options->set_AdjustPageSize(true);
        options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }

        std::clog << "Conversion SVG en PDF : Fin" << std::endl;
    }
```

## Quoi de neuf dans Aspose.PDF 21.4

### Enregistrement des documents PDF au format HTML a été mis en œuvre

Aspose.PDF pour C++ prend en charge les fonctionnalités pour convertir un fichier PDF en HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```
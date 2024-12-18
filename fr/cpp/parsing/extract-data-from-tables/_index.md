---
title: Extraire des données d'un tableau dans un PDF 
linktitle: Extraire des données d'un tableau
type: docs
weight: 40
url: /fr/cpp/extract-data-from-table-in-pdf/
description: Apprenez à extraire des données tabulaires d'un PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des tableaux d'un PDF par programmation

Étant donné que le PDF est le format le plus courant pour l'échange de documents, considérons un document avec plusieurs ensembles de données nécessitant une analyse. Dans cet article, nous décrirons l'extraction de tableaux d'un PDF.

**Aspose.PDF pour C++** fournit aux développeurs les outils nécessaires pour extraire des données de tableaux dans des documents PDF.

Cet exemple démontre l'utilisation de la classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) pour récupérer des données tabulaires à partir de tableaux dans un fichier PDF.

L'exemple suivant montre l'extraction de tableau de toutes les pages :

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Scanner les pages
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Itérer à travers la liste des lignes
        for (auto row : table->get_RowList()) {
            // Itérer à travers la liste des cellules
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraire un tableau dans une zone spécifique de la page PDF

Chaque tableau absorbé a une propriété [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) qui décrit la position du tableau sur la page.

Donc, si vous avez besoin d'extraire des tableaux situés dans une région spécifique, vous devez travailler avec des coordonnées spécifiques.

L'exemple suivant montre comment extraire un tableau marqué avec une annotation carrée :

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Tableaux marqués non trouvés.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // Itérer à travers la liste des cellules
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraire les données de tableau à partir de PDF et les stocker dans un fichier CSV

L'exemple suivant montre comment extraire un tableau et le stocker sous forme de fichier CSV. Pour voir comment convertir un PDF en feuille de calcul Excel, veuillez vous référer à l'article [Convertir PDF en Excel](/pdf/fr/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom de fichier
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet d'option de sauvegarde Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Enregistrer la sortie au format XLS
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
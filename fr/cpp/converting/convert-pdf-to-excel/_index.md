---
title: Convert PDF to Excel en C++
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF pour C++ vous permet de convertir des PDF en format Excel en utilisant C++. Pendant ce processus, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Aperçu

Cet article explique comment **convertir des formats PDF en Excel en utilisant C++**. Il couvre les sujets suivants.

_Format_: **XLS**
- [C++ PDF à XLS](#cpp-pdf-to-xls)
- [C++ Convertir PDF en XLS](#cpp-pdf-to-xls)
- [C++ Comment convertir un fichier PDF en XLS](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [C++ PDF à XLSX](#cpp-pdf-to-xlsx)
- [C++ Convertir PDF en XLSX](#cpp-pdf-to-xlsx)
- [C++ Comment convertir un fichier PDF en XLSX](#cpp-pdf-to-xlsx)

_Format_: **Format Microsoft Excel XLS**
- [C++ PDF à Excel](#cpp-pdf-to-excel-xls)
- [C++ Convertir PDF en Excel](#cpp-pdf-to-excel-xls)
- [C++ Comment convertir un fichier PDF en Excel](#cpp-pdf-to-excel-xls)

_Format_: **Format Microsoft Excel XLSX**
- [C++ PDF vers Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Convertir PDF en Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Comment convertir un fichier PDF en Excel](#cpp-pdf-to-excel-xlsx)

Autres sujets couverts par cet article
- [Voir aussi](#see-also)

## Conversions PDF vers Excel en C++

**Aspose.PDF pour C++** prend en charge la fonctionnalité de conversion de fichiers PDF en formats Excel.

Aspose.PDF pour C++ est un composant de manipulation de PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLS). Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

Afin de convertir des fichiers PDF au format <abbr title="Microsoft Excel Spreadsheet">XLS</abbr>, Aspose.PDF a une classe appelée ExcelSaveOptions. Un objet de la classe ExcelSaveOptions est passé en tant que deuxième argument au constructeur Document.Save(..).

Le code suivant montre le processus de conversion d'un fichier PDF au format XLS avec Aspose.PDF pour C++.


<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Étapes : Convertir PDF en XLS en C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Étapes : Convertir PDF en format Excel XLS en C++</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le document PDF source.
2. Enregistrez-le au format _XLS_ en appelant la méthode **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String pour le chemin du répertoire
    String _dataDir("C:\\Samples\\Conversion\\");

    // String pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Enregistrer la sortie au format XLS
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir PDF en XLS avec colonne de contrôle

Lors de la conversion d'un PDF en format XLS, une colonne vide est ajoutée au fichier de sortie comme première colonne. La classe ExcelSaveOptions utilise l'option InsertBlankColumnAtFirst pour contrôler cette colonne. Sa valeur par défaut est true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom du fichier
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // La classe ExcelSaveOptions utilise l'option InsertBlankColumnAtFirst pour contrôler cette colonne. Sa valeur par défaut est true.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Enregistrer la sortie au format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir un PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec beaucoup de pages vers XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour garantir que toutes les pages sont exportées sur une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Enregistrer la sortie au format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convertir au format XLSX

Par défaut, Aspose.PDF utilise XML Spreadsheet 2003 pour stocker les données. Afin de convertir des fichiers PDF au format XLSX, Aspose.PDF dispose d'une classe appelée [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) avec 'Format'. Un objet de la classe [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) est passé en tant que deuxième argument à la méthode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

L'extrait de code suivant montre le processus de conversion d'un fichier PDF en format XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Étapes : Convertir PDF en XLSX en C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Étapes : Convertir PDF en format Excel XLSX en C++</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le document PDF source.
2. Créer une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Définir le format comme _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Enregistrez-le au format _XLSX_ en appelant la méthode **Document->Save()** et en lui passant l'instance de _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom de chemin
    String _dataDir("C:\\Samples\\Conversion\\");

    // Chaîne pour le nom de fichier
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instancier l'objet ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // Enregistrez la sortie au format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**Essayez de convertir PDF en Excel en ligne**
Aspose.PDF pour C++ vous présente une application gratuite en ligne ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Excel avec Application Gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Voir Aussi

Cet article couvre également ces sujets. Les codes sont identiques à ceux ci-dessus.

_Format_: **Format Microsoft Excel XLS**
- [Code C++ PDF en Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ PDF en Excel XLS Programmatiquement](#cpp-pdf-to-excel-xls)
- [Bibliothèque C++ PDF en Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Enregistrer PDF en Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Générer Excel XLS à partir de PDF](#cpp-pdf-to-excel-xls)
- [C++ Créer Excel XLS à partir de PDF](#cpp-pdf-to-excel-xls)
- [Convertisseur C++ PDF en Excel XLS](#cpp-pdf-to-excel-xls)

_Format_: **Format Microsoft Excel XLSX**
- [Code C++ PDF en Excel XLSX](#cpp-pdf-to-excel-xlsx)

- [C++ PDF en Excel XLSX Programmatiquement](#cpp-pdf-to-excel-xlsx)
- [Bibliothèque C++ PDF vers Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Enregistrer PDF en tant qu'Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Générer Excel XLSX à partir de PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Créer Excel XLSX à partir de PDF](#cpp-pdf-to-excel-xlsx)
- [Convertisseur C++ PDF vers Excel XLSX](#cpp-pdf-to-excel-xlsx)

_Format_: **XLS**
- [Code C++ PDF vers XLS](#cpp-pdf-to-xls)
- [C++ PDF vers XLS Programmatiquement](#cpp-pdf-to-xls)
- [Bibliothèque C++ PDF vers XLS](#cpp-pdf-to-xls)
- [C++ Enregistrer PDF en tant que XLS](#cpp-pdf-to-xls)
- [C++ Générer XLS à partir de PDF](#cpp-pdf-to-xls)
- [C++ Créer XLS à partir de PDF](#cpp-pdf-to-xls)
- [Convertisseur C++ PDF vers XLS](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [Code C++ PDF vers XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF vers XLSX Programmatiquement](#cpp-pdf-to-xlsx)
- [Bibliothèque C++ PDF vers XLSX](#cpp-pdf-to-xlsx)
- [C++ Enregistrer PDF en tant que XLSX](#cpp-pdf-to-xlsx)
- [C++ Générer XLSX à partir de PDF](#cpp-pdf-to-xlsx)
- [C++ Créer XLSX à partir de PDF](#cpp-pdf-to-xlsx)
- [Convertisseur C++ PDF vers XLSX](#cpp-pdf-to-xlsx)
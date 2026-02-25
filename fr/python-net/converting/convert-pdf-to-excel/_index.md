---
title: Convertir PDF en Excel avec Python
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Convertissez des PDF en feuilles de calcul Excel facilement avec Aspose.PDF pour Python via .NET. Suivez ce guide pour des conversions précises de PDF en XLSX.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en Excel avec Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en différents formats Excel à l'aide de Python, spécifiquement avec la bibliothèque Aspose.PDF pour Python via .NET. Il détaille les processus de conversion pour les formats XLS, XLSX, CSV et ODS. Le document explique les étapes nécessaires pour convertir un PDF en XLS et XLSX, en soulignant la création d'instances Document et ExcelSaveOptions, ainsi que l'utilisation de la méthode Document.Save() pour spécifier les formats de sortie. L'article aborde également des fonctionnalités telles que le contrôle de l'insertion de colonnes vides et la réduction du nombre de feuilles de calcul lors de la conversion. De plus, il fournit des exemples de conversion de PDF en feuilles de calcul Excel uniques et d'autres formats comme CSV et ODS, en soulignant la flexibilité et les capacités d'Aspose.PDF. Un outil en ligne pour la conversion PDF en XLSX est également mentionné, permettant aux utilisateurs d'examiner la qualité de la conversion. L'article se conclut par une liste de sujets connexes et des extraits de code pour aider davantage à comprendre et mettre en œuvre ces conversions de manière programmatique.
---

## Conversion PDF en Excel via Python

**Aspose.PDF pour Python via .NET** prend en charge la fonctionnalité de conversion de fichiers PDF en Excel et en formats CSV.

Aspose.PDF pour Python via .NET est un composant de manipulation PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLSX). Lors de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

{{% alert color="success" %}}
**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF vous propose une application en ligne gratuite ["PDF en XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité du service.

[![Conversion Aspose.PDF PDF en Excel avec Application Gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF pour Python via .NET.

Étapes : Convertir un fichier PDF en format Excel (XML Spreadsheet 2003)

1. Charger le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Enregistrer le fichier converti.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Étapes : Convertir un fichier PDF en format XLSX (Excel 2007+)

1. Charger le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Enregistrer le fichier converti.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en XLS avec contrôle de colonne

Lors de la conversion d'un PDF au format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne. Dans la classe 'ExcelSaveOptions', l'option 'insert_blank_column_at_first' est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir PDF en feuille de calcul Excel unique

Aspose.PDF pour Python via .NET montre comment convertir un PDF en fichier Excel (.xlsx), avec l'option 'minimize_the_number_of_worksheets' activée.

Étapes : Convertir PDF en XLS ou XLSX feuille unique dans Python

1. Charger le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. L'option 'minimize_the_number_of_worksheets' réduit le nombre de feuilles Excel en combinant les pages du PDF en moins de feuilles de calcul (par exemple, une seule feuille pour l'ensemble du document si possible).
1. Enregistrer le fichier converti.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir un fichier PDF en fichier Excel au format XLSM

Cet exemple Python montre comment convertir un fichier PDF en fichier Excel au format XLSM (Classeur Excel avec macros).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Convertir vers d'autres formats de feuille de calcul

### Convertir en CSV

La fonction 'convert_pdf_to_excel_2007_csv' effectue la même opération qu'auparavant, mais cette fois le format cible est CSV (valeurs séparées par des virgules) au lieu de XLSM.

Étapes : Convertir PDF en CSV avec Python

1. Créer une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
1. Créer une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **ExcelSaveOptions.ExcelFormat.CSV**
1. Enregistrez-le au format **CSV** en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir en ODS

Étapes : Convertir PDF en ODS avec Python

1. Créez une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le document PDF source.
1. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **ExcelSaveOptions.ExcelFormat.ODS**
1. Enregistrez-le au format **ODS** en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversion au format ODS s'effectue de la même manière que tous les autres formats.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


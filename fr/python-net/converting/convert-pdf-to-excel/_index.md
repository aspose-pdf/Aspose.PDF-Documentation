---
title: Convertir le PDF en Excel avec Python
linktitle: Convertir le PDF en Excel
type: docs
weight: 20
url: /fr/python-net/convert-pdf-to-excel/
lastmod: "2026-05-22"
description: Apprenez à convertir des fichiers PDF en Excel en Python avec Aspose.PDF for Python via .NET, y compris XLS, XLSX, CSV, ODS et une sortie à feuille unique.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en Excel en Python
Abstract: Cet article fournit un guide complet sur la conversion de fichiers PDF en divers formats Excel à l'aide de Python, en particulier avec la bibliothèque Aspose.PDF for Python via .NET. Il détaille les processus de conversion pour les formats XLS, XLSX, CSV et ODS. Le document explique les étapes nécessaires pour convertir un PDF en XLS et XLSX, en soulignant la création d'instances Document et ExcelSaveOptions, ainsi que l'utilisation de la méthode Document.Save() pour spécifier les formats de sortie. L'article aborde également des fonctionnalités telles que le contrôle de l'insertion de colonnes vides et la réduction du nombre de feuilles de calcul lors de la conversion. De plus, il fournit des exemples de conversion de PDFs en feuilles Excel uniques et d'autres formats comme CSV et ODS, en mettant en avant la flexibilité et les fonctionnalités d'Aspose.PDF. Un outil en ligne pour la conversion PDF en XLSX est également mentionné, permettant aux utilisateurs d'évaluer la qualité de la conversion. L'article se conclut par une liste de sujets associés et des extraits de code pour aider davantage à comprendre et à mettre en œuvre ces conversions de manière programmatique.
---

## Convertir le PDF en Excel (Spreadsheet 2003 XML)

**Aspose.PDF for Python via .NET** prend en charge la fonctionnalité de conversion des fichiers PDF aux formats Excel et CSV.

Aspose.PDF for Python via .NET est un composant de manipulation de PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLSX). Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

Utilisez cette page lorsque vous devez extraire du contenu PDF orienté tableau ou de type rapport en formats de feuille de calcul pour le trier, le filtrer ou l'analyser en aval.

{{% alert color="success" %}}
**Essayez de convertir le PDF en Excel en ligne**

Aspose.PDF vous présente une application en ligne ["PDF vers XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner le fonctionnement et la qualité.

[![Aspose.PDF Conversion PDF en Excel avec App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Le fragment de code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF for Python via .NET.

Étapes : Convertir un fichier PDF en format Excel (XML Spreadsheet 2003)

1. Chargez le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Enregistrez le fichier converti.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en Excel 2007+ (XLSX)

Étapes : Convertir un fichier PDF au format XLSX (Excel 2007+)

1. Chargez le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Enregistrez le fichier converti.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en XLS avec la colonne de contrôle

Lors de la conversion d'un PDF au format XLS, une colonne vierge est ajoutée au fichier de sortie en tant que première colonne. Dans la classe ‘ExcelSaveOptions’, l'option ‘insert_blank_column_at_first’ est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en une feuille Excel unique

Aspose.PDF for Python via .NET montre comment convertir un PDF en fichier Excel (.xlsx), avec l'option 'minimize_the_number_of_worksheets' activée.

Étapes : Convertir le PDF en XLS ou XLSX avec une seule feuille de calcul en Python

1. Chargez le document PDF.
1. Configurer les options d'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. L'option 'minimize_the_number_of_worksheets' réduit le nombre de feuilles Excel en combinant les pages PDF en moins de feuilles de calcul (par exemple, une feuille de calcul pour l'ensemble du document si possible).
1. Enregistrez le fichier converti.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir le PDF en Excel 2007 avec macros activées (XLSM)

Cet exemple Python montre comment convertir un fichier PDF en un fichier Excel au format XLSM (Classeur Excel avec macros).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Convertir vers d'autres formats de feuilles de calcul

### Convertir le PDF en CSV

La fonction 'convert_pdf_to_excel_2007_csv' effectue la même opération qu'auparavant, mais cette fois le format cible est CSV (Comma-Separated Values) au lieu de XLSM.

Étapes : Convertir le PDF en CSV en Python

1. Créer une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le document PDF source.
1. Créer une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **ExcelSaveOptions.ExcelFormat.CSV**
1. Enregistrez‑le au format **CSV** en appelant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* méthode et le passer [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Convertir PDF en ODS

Étapes : Convertir le PDF en ODS en Python

1. Créer une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le document PDF source.
1. Créer une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **ExcelSaveOptions.ExcelFormat.ODS**
1. Enregistrez-le au format **ODS** en appelant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode et la passer [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversion au format ODS s'effectue de la même manière que tous les autres formats.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Conversions associées

- [Convertir le PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) si votre priorité est le flux de texte modifiable plutôt que la structure de feuille de calcul.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) lorsque vous avez besoin d'une sortie compatible avec le navigateur.
- [Convertir le PDF en d'autres formats](/pdf/fr/python-net/convert-pdf-to-other-files/) pour EPUB, Markdown, texte, XPS et les flux de travail d'exportation associés.
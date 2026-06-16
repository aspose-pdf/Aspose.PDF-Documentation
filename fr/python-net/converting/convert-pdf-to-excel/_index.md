---
title: Convertir le PDF en Excel en Python
linktitle: Convertir le PDF en Excel
type: docs
weight: 20
url: /fr/python-net/convert-pdf-to-excel/
lastmod: "2026-04-14"
description: Apprenez à convertir PDF en Excel en Python, y compris XLS, XLSX, CSV, ODS, sortie d'une seule feuille de calcul et gestion des colonnes avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertissez le PDF en Excel, XLSX, CSV et ODS en Python
Abstract: Cet article montre comment convertir des fichiers PDF en formats de feuille de calcul avec Aspose.PDF for Python via .NET. Il couvre les sorties XLS, XLSX, XLSM, CSV et ODS, ainsi que les options pour contrôler les colonnes vides et réduire le nombre de feuilles de calcul générées.
---

## Convertir le PDF en Excel en Python

**Aspose.PDF for Python via .NET** prend en charge la conversion des fichiers PDF en Excel et autres formats de feuille de calcul depuis le code Python.

Utilisez cette page lorsque vous devez convertir un PDF en XLS, XLSX, CSV ou ODS pour l'extraction de tableaux, la réutilisation de rapports, le tri, le filtrage ou l'analyse en aval. Lors de la conversion PDF vers Excel, les pages PDF individuelles peuvent être rendues en feuilles de calcul Excel.

Le premier exemple convertit un fichier PDF au format Spreadsheet 2003 XML. Les sections suivantes montrent les formats XLSX, XLSM, CSV, ODS et la sortie d'une seule feuille de calcul.

{{% alert color="success" %}}
**Essayez de convertir un PDF en Excel en ligne**

Aspose.PDF vous présente une application en ligne ["PDF vers XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec laquelle il fonctionne.

[![Aspose.PDF Conversion PDF vers Excel avec l'application](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

L'extrait de code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF for Python via .NET.

Étapes : Convertir un fichier PDF au format Excel (XML Spreadsheet 2003)

1. Chargez le document PDF.
1. Configurer les options d\'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## Convertir le PDF en XLSX en Python

Étapes : Convertir un fichier PDF au format XLSX (Excel 2007+)

1. Chargez le document PDF.
1. Configurer les options d\'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
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

## Convertir le PDF en XLSX avec contrôle des colonnes

Lors de la conversion d'un PDF en format Excel, une colonne vide peut être ajoutée comme première colonne dans le fichier de sortie. Utilisez le `insert_blank_column_at_first` option du `ExcelSaveOptions` classe pour contrôler ce comportement. Sa valeur par défaut est `true`.

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

## Convertir le PDF en une seule feuille de calcul Excel

Aspose.PDF for Python via .NET montre comment convertir un PDF en fichier Excel (.xlsx), avec l'option 'minimize_the_number_of_worksheets' activée.

Étapes : Convertir le PDF en XLS ou XLSX avec une seule feuille de calcul en Python

1. Chargez le document PDF.
1. Configurer les options d\'enregistrement Excel en utilisant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. L'option 'minimize_the_number_of_worksheets' réduit le nombre de feuilles Excel en combinant les pages PDF en moins de feuilles (par ex., une feuille pour l'ensemble du document si possible).
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

## Convertir le PDF en Excel 2007 macro‑activé (XLSM)

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

La fonction 'convert_pdf_to_excel_2007_csv' effectue la même opération qu'auparavant, mais cette fois le format cible est CSV (valeurs séparées par des virgules) au lieu de XLSM.

Étapes : Convertir le PDF en CSV avec Python

1. Créer une instance de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet avec le document PDF source.
1. Créer une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **ExcelSaveOptions.ExcelFormat.CSV**
1. Enregistrez-le au format **CSV** en appelant [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* méthode et le passer [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

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

### Convertir le PDF en ODS

Étapes : Convertir le PDF en ODS en Python

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

- [Convertir PDF en Word](/pdf/fr/python-net/convert-pdf-to-word/) si votre priorité est le flux de texte éditable plutôt que la structure de la feuille de calcul.
- [Convertir le PDF en HTML](/pdf/fr/python-net/convert-pdf-to-html/) lorsque vous avez besoin d’une sortie adaptée aux navigateurs.
- [Convertir le PDF en d'autres formats](/pdf/fr/python-net/convert-pdf-to-other-files/) pour EPUB, Markdown, texte, XPS et les flux de travail d'exportation associés.

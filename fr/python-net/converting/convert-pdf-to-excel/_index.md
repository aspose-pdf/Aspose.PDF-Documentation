---
title: Convertir PDF en Excel en Python
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
description: La bibliothèque Aspose.PDF pour Python vous permet de convertir des PDF en format Excel en utilisant Python. Ces formats incluent XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Aperçu

Cet article explique comment **convertir des PDF en formats Excel en utilisant Python**. Il couvre les sujets suivants.

_Format_: **XLS**

- [Python PDF en XLS](#python-pdf-to-xls)
- [Python Convertir PDF en XLS](#python-pdf-to-xls)
- [Python Comment convertir un fichier PDF en XLS](#python-pdf-to-xls)

_Format_: **XLSX**

- [Python PDF en XLSX](#python-pdf-to-xlsx)
- [Python Convertir PDF en XLSX](#python-pdf-to-xlsx)
- [Python Comment convertir un fichier PDF en XLSX](#python-pdf-to-xlsx)

_Format_: **Excel**

- [Python PDF à Excel](#python-pdf-to-xlsx)
- [Python PDF à Excel XLS](#python-pdf-to-xls)
- [Python PDF à Excel XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**

- [Python PDF à CSV](#python-pdf-to-csv)
- [Python Convertir PDF en CSV](#python-pdf-to-csv)
- [Python Comment convertir un fichier PDF en CSV](#python-pdf-to-csv)

_Format_: **ODS**

- [Python PDF à ODS](#python-pdf-to-ods)
- [Python Convertir PDF en ODS](#python-pdf-to-ods)
- [Python Comment convertir un fichier PDF en ODS](#python-pdf-to-ods)

## Conversion de PDF en EXCEL via Python

**Aspose.PDF pour Python via .NET** prend en charge la fonctionnalité de conversion de fichiers PDF en formats Excel et CSV.

Aspose.PDF pour Python via .NET est un composant de manipulation de PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLSX). Lors de cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

{{% alert color="success" %}}
**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF vous présente l'application en ligne gratuite ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Le code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF pour Python via .NET.

<a name="python-pdf-to-xls"><strong>Étapes: Convertir PDF en XLS en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Enregistrez-le au format **XLS** en spécifiant l'**extension .xls** en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Enregistrer le fichier au format MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Étapes : Convertir un PDF en XLSX en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Enregistrez-le au format **XLSX** en spécifiant l'**extension .xlsx** en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Enregistrer le fichier au format MS Excel
    document.save(output_pdf, save_option)
```

## Convertir un PDF en XLS avec contrôle de la colonne

Lors de la conversion d'un PDF au format XLS, une colonne vide est ajoutée au fichier de sortie en tant que première colonne.
 La fonction InsertBlankColumnAtFirst dans la classe 'ExcelSaveOptions' est utilisée pour contrôler cette colonne. Sa valeur par défaut est vraie.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Enregistrer le fichier au format MS Excel
    document.save(output_pdf, save_option)
```

## Convertir un PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec beaucoup de pages vers XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour garantir que toutes les pages sont exportées vers une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

<a name="python-pdf-to-excel-single"><strong>Étapes : Convertir un PDF en une seule feuille de calcul XLS ou XLSX en Python</strong></a>
1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **MinimizeTheNumberOfWorksheets = true**.
3. Enregistrez-le au format **XLS** ou **XLSX** avec une seule feuille de calcul en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Enregistrez le fichier au format MS Excel
    document.save(output_pdf, save_option)

```


## Convertir en d'autres formats de tableur

### Convertir en CSV

La conversion au format CSV se réalise de la même manière que ci-dessus. Tout ce dont vous avez besoin - c'est de définir le format approprié.

<a name="python-pdf-to-csv"><strong>Étapes : Convertir PDF en CSV en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Enregistrez-le au format **CSV** en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Enregistrer le fichier
    document.save(output_pdf, save_option)
```


### Convertir en ODS

<a name="python-pdf-to-ods"><strong>Étapes : Convertir un PDF en ODS en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) avec **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Enregistrez-le au format **ODS** en appelant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

La conversion au format ODS est effectuée de la même manière que pour tous les autres formats.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Ouvrir le document PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Enregistrer le fichier
    document.save(output_pdf, save_option)
```


## Voir Aussi

Cet article couvre également ces sujets. Les codes sont les mêmes qu'au-dessus.

_Format_: **Excel**
- [Python PDF to Excel Code](#python-pdf-to-xlsx)
- [Python PDF to Excel API](#python-pdf-to-xlsx)
- [Python PDF to Excel Programmatically](#python-pdf-to-xlsx)
- [Python PDF to Excel Library](#python-pdf-to-xlsx)
- [Python Save PDF as Excel](#python-pdf-to-xlsx)
- [Python Generate Excel from PDF](#python-pdf-to-xlsx)
- [Python Create Excel from PDF](#python-pdf-to-xlsx)
- [Python PDF to Excel Converter](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Python PDF to XLS Code](#python-pdf-to-xls)
- [Python PDF to XLS API](#python-pdf-to-xls)
- [Python PDF to XLS Programmatically](#python-pdf-to-xls)
- [Python PDF to XLS Library](#python-pdf-to-xls)
- [Python Save PDF as XLS](#python-pdf-to-xls)
- [Python Generate XLS from PDF](#python-pdf-to-xls)
- [Python Create XLS from PDF](#python-pdf-to-xls)
- [Python PDF to XLS Converter](#python-pdf-to-xls)

_Format_: **XLSX**

- [Python PDF to XLSX Code](#python-pdf-to-xlsx)
- [API Python PDF to XLSX](#python-pdf-to-xlsx)
- [Programme Python PDF to XLSX](#python-pdf-to-xlsx)
- [Bibliothèque Python PDF to XLSX](#python-pdf-to-xlsx)
- [Enregistrer PDF en tant que XLSX avec Python](#python-pdf-to-xlsx)
- [Générer XLSX à partir de PDF avec Python](#python-pdf-to-xlsx)
- [Créer XLSX à partir de PDF avec Python](#python-pdf-to-xlsx)
- [Convertisseur Python PDF to XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Code Python PDF to CSV](#python-pdf-to-csv)
- [API Python PDF to CSV](#python-pdf-to-csv)
- [Programme Python PDF to CSV](#python-pdf-to-csv)
- [Bibliothèque Python PDF to CSV](#python-pdf-to-csv)
- [Enregistrer PDF en tant que CSV avec Python](#python-pdf-to-csv)
- [Générer CSV à partir de PDF avec Python](#python-pdf-to-csv)
- [Créer CSV à partir de PDF avec Python](#python-pdf-to-csv)
- [Convertisseur Python PDF to CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Code Python PDF to ODS](#python-pdf-to-ods)
- [API Python PDF to ODS](#python-pdf-to-ods)
- [Programme Python PDF to ODS](#python-pdf-to-ods)
- [Bibliothèque Python PDF to ODS](#python-pdf-to-ods)

- [Enregistrer PDF en tant que ODS avec Python](#python-pdf-to-ods)
- [Python Générer ODS à partir de PDF](#python-pdf-to-ods)
- [Python Créer ODS à partir de PDF](#python-pdf-to-ods)
- [Convertisseur PDF en ODS Python](#python-pdf-to-ods)
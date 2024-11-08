---
title: Convertir PDF en Excel en Python  
linktitle: Convertir PDF en Excel  
type: docs  
weight: 20  
url: /fr/python-java/convert-pdf-to-excel/  
lastmod: "2022-12-23"  
keywords: convertir PDF en Excel en utilisant python, convertir PDF en XLS en utilisant python, convertir PDF en XLSX en utilisant python, exporter un tableau de PDF vers Excel en python.  
description: La bibliothèque Aspose.PDF pour Python vous permet de convertir un PDF en format Excel en utilisant Python. Ces formats incluent XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---
## Aperçu

Cet article explique comment **convertir un PDF en formats Excel en utilisant Python**. Il couvre les sujets suivants.

_Format_: **XLS**  
- [Python PDF en XLS](#python-pdf-to-xls)  
- [Python Convertir PDF en XLS](#python-pdf-to-xls)  
- [Python Comment convertir un fichier PDF en XLS](#python-pdf-to-xls)  

_Format_: **XLSX**  
- [Python PDF en XLSX](#python-pdf-to-xlsx)  
- [Python Convertir PDF en XLSX](#python-pdf-to-xlsx)  
- [Python Comment convertir un fichier PDF en XLSX](#python-pdf-to-xlsx)  

_Format_: **Excel**  
- [Python PDF to Excel](#python-pdf-to-xlsx)
- [Python PDF vers Excel XLS](#python-pdf-to-xls)
- [Python PDF vers Excel XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Python PDF vers CSV](#python-pdf-to-csv)
- [Python Convertir PDF en CSV](#python-pdf-to-csv)
- [Python Comment convertir un fichier PDF en CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Python PDF vers ODS](#python-pdf-to-ods)
- [Python Convertir PDF en ODS](#python-pdf-to-ods)
- [Python Comment convertir un fichier PDF en ODS](#python-pdf-to-ods)

## Conversion PDF en EXCEL via Python

**Aspose.PDF pour Python via .NET** prend en charge la fonctionnalité de conversion des fichiers PDF aux formats Excel et CSV.

Aspose.PDF pour Python via Java est un composant de manipulation de PDF, nous avons introduit une fonctionnalité qui rend le fichier PDF en classeur Excel (fichiers XLSX). Pendant cette conversion, les pages individuelles du fichier PDF sont converties en feuilles de calcul Excel.

{{% alert color="success" %}}
**Essayez de convertir PDF en Excel en ligne**

Aspose.PDF vous présente une application en ligne gratuite ["PDF vers XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Le code suivant montre le processus de conversion d'un fichier PDF en format XLS ou XLSX avec Aspose.PDF pour Python via Java.

<a name="python-pdf-to-xls"><strong>Étapes : Convertir PDF en XLS en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Enregistrez-le au format **XLS** en spécifiant l'extension **.xls** en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python



from asposepdf import Api


# initialiser la licence
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# conversion à partir d'un tableau d'octets
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversion à partir d'un fichier
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)


# conversion à partir d'un tableau d'octets
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# conversion à partir d'un fichier
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Étapes : Convertir PDF en XLSX en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Enregistrez-le au format **XLSX** en spécifiant l'**extension .xlsx** en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Convertir PDF en XLS avec contrôle de colonne

Lors de la conversion d'un PDF en format XLS, une colonne vide est ajoutée au fichier de sortie comme première colonne.
 Le 'option InsertBlankColumnAtFirst' dans la classe 'ExcelSaveOptions' est utilisée pour contrôler cette colonne. Sa valeur par défaut est true.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## Convertir un PDF en une seule feuille de calcul Excel

Lors de l'exportation d'un fichier PDF avec beaucoup de pages en XLS, chaque page est exportée vers une feuille différente dans le fichier Excel. Cela est dû au fait que la propriété MinimizeTheNumberOfWorksheets est définie sur false par défaut. Pour s'assurer que toutes les pages sont exportées vers une seule feuille dans le fichier Excel de sortie, définissez la propriété MinimizeTheNumberOfWorksheets sur true.

<a name="python-pdf-to-excel-single"><strong>Étapes : Convertir un PDF en une seule feuille de calcul XLS ou XLSX en Python</strong></a>
1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) avec **MinimizeTheNumberOfWorksheets = True**.
3. Enregistrez-le au format **XLS** ou **XLSX** ayant une seule feuille de calcul en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Enregistrez le fichier au format MS Excel
doc.save(documentOutName, save_option)

```

## Convertir vers d'autres formats de feuille de calcul


### Convertir en CSV

La conversion au format CSV s'effectue de la même manière que ci-dessus. Tout ce dont vous avez besoin - définir le format approprié.

<a name="python-pdf-to-csv"><strong>Étapes : Convertir un PDF en CSV en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) avec **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Enregistrez-le au format **CSV** en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et en lui passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### Convertir en ODS

<a name="python-pdf-to-ods"><strong>Étapes : Convertir PDF en ODS en Python</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) avec le document PDF source.
2. Créez une instance de [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) avec **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Enregistrez-le au format **ODS** en appelant la méthode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) et en passant [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

La conversion au format ODS s'effectue de la même manière que tous les autres formats.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## Voir Aussi

Cet article couvre également ces sujets. Les codes sont identiques à ceux ci-dessus.

_Format_: **Excel**
- [Python PDF en code Excel](#python-pdf-to-xlsx)
- [Python PDF vers API Excel](#python-pdf-to-xlsx)
- [Python PDF vers Excel Programmatiquement](#python-pdf-to-xlsx)
- [Python PDF vers Bibliothèque Excel](#python-pdf-to-xlsx)
- [Python Enregistrer PDF comme Excel](#python-pdf-to-xlsx)
- [Python Générer Excel à partir de PDF](#python-pdf-to-xlsx)
- [Python Créer Excel à partir de PDF](#python-pdf-to-xlsx)
- [Python Convertisseur PDF en Excel](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Python PDF en code XLS](#python-pdf-to-xls)
- [Python PDF vers API XLS](#python-pdf-to-xls)
- [Python PDF vers XLS Programmatiquement](#python-pdf-to-xls)
- [Python PDF vers Bibliothèque XLS](#python-pdf-to-xls)
- [Python Enregistrer PDF comme XLS](#python-pdf-to-xls)
- [Python Générer XLS à partir de PDF](#python-pdf-to-xls)
- [Python Créer XLS à partir de PDF](#python-pdf-to-xls)
- [Python Convertisseur PDF en XLS](#python-pdf-to-xls)

_Format_: **XLSX**

- [Python PDF en code XLSX](#python-pdf-to-xlsx)
- [API de Python PDF à XLSX](#python-pdf-to-xlsx)
- [Programmer en Python PDF à XLSX](#python-pdf-to-xlsx)
- [Bibliothèque Python PDF à XLSX](#python-pdf-to-xlsx)
- [Enregistrer PDF en XLSX avec Python](#python-pdf-to-xlsx)
- [Générer XLSX à partir de PDF avec Python](#python-pdf-to-xlsx)
- [Créer XLSX à partir de PDF avec Python](#python-pdf-to-xlsx)
- [Convertisseur Python PDF en XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Code Python PDF à CSV](#python-pdf-to-csv)
- [API de Python PDF à CSV](#python-pdf-to-csv)
- [Programmer en Python PDF à CSV](#python-pdf-to-csv)
- [Bibliothèque Python PDF à CSV](#python-pdf-to-csv)
- [Enregistrer PDF en CSV avec Python](#python-pdf-to-csv)
- [Générer CSV à partir de PDF avec Python](#python-pdf-to-csv)
- [Créer CSV à partir de PDF avec Python](#python-pdf-to-csv)
- [Convertisseur Python PDF en CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Code Python PDF à ODS](#python-pdf-to-ods)
- [API de Python PDF à ODS](#python-pdf-to-ods)
- [Programmer en Python PDF à ODS](#python-pdf-to-ods)
- [Bibliothèque Python PDF à ODS](#python-pdf-to-ods)

- [Enregistrer PDF en ODS avec Python](#python-pdf-to-ods)
- [Python Générer ODS à partir de PDF](#python-pdf-to-ods)
- [Python Créer ODS à partir de PDF](#python-pdf-to-ods)
- [Convertisseur Python PDF en ODS](#python-pdf-to-ods)
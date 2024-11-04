---
title: Importer et Exporter les Champs de Formulaire
type: docs
weight: 60
url: /net/import-export-form-field/
description: Remplir les champs du formulaire en utilisant DataTable avec la classe FormEditor par Aspose.PDF pour .NET
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF pour .NET offre de grandes capacités pour créer/manipuler des champs de formulaire à l'intérieur d'un document PDF. En utilisant cette API, vous pouvez remplir les champs de formulaire à l'intérieur d'un fichier PDF de manière programmatique, remplir les champs de formulaire en [important des données de FDF dans un fichier PDF](/pdf/net/import-and-export-data/), [important des données de XFDF dans un fichier PDF](/pdf/net/import-and-export-data/), [important des données de XML dans un fichier PDF](/pdf/net/import-and-export-data/) ou même vous pouvez importer des données depuis un objet [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

```csharp
 public static void ImportData()
    {
    var editor = new Form();
    editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
    editor.ImportFdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.fdf"));
    editor.ImportXml(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xml"));

    //TODO: Bug! Create issue
    editor.ImportXfdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xfdf"));
    editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
    }

```

## Exporter les données de FDF dans un fichier PDF

```csharp
    public static void ExportData()
        {
            var editor = new Form();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.ExportFdf(System.IO.File.OpenWrite(_dataDir + "Sample-Form-01-mod.fdf"));
            editor.ExportXml(System.IO.File.OpenWrite(_dataDir + "Sample-Form-01-mod.xml"));
            editor.ExportXfdf(System.IO.File.OpenWrite(_dataDir + "Sample-Form-01-mod.xfdf"));
        }

```
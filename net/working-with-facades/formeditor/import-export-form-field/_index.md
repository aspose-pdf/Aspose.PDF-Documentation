---
title: Import and Export Form Field
type: docs
weight: 60
url: /net/import-export-form-field/
description: Fill Form fields using DataTable using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF for .NET provides great capabilities for create/manipulating form fields inside PDF document. Using this API, you can programmatically fill form fields inside PDF file, fill form fields by [Import Data from FDF into a PDF File](/pdf/net/import-and-export-data/), [Import Data from XFDF into a PDF File](/pdf/net/import-and-export-data/), [Import Data from XML into a PDF File](/pdf/net/import-and-export-data/) or even you can import data from [System.Data.DataTable](https://apireference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) object.


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

## Export Data from FDF into a PDF File

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

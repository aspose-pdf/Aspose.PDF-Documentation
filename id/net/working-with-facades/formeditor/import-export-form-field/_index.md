---
title: Import dan Ekspor Form Field
type: docs
weight: 60
url: id/net/import-export-form-field/
description: Mengisi bidang Form menggunakan DataTable dengan Kelas FormEditor oleh Aspose.PDF untuk .NET
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF untuk .NET menyediakan kemampuan luar biasa untuk membuat/memanipulasi bidang formulir di dalam dokumen PDF. Menggunakan API ini, Anda dapat secara programatis mengisi bidang formulir di dalam file PDF, mengisi bidang formulir dengan [Mengimpor Data dari FDF ke dalam File PDF](/pdf/net/import-and-export-data/), [Mengimpor Data dari XFDF ke dalam File PDF](/pdf/net/import-and-export-data/), [Mengimpor Data dari XML ke dalam File PDF](/pdf/net/import-and-export-data/) atau bahkan Anda dapat mengimpor data dari objek [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

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

## Ekspor Data dari FDF ke dalam File PDF

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
---
title: フォームフィールドのインポートとエクスポート
type: docs
weight: 60
url: /ja/net/import-export-form-field/
description: Aspose.PDF for .NETのFormEditorクラスを使用してDataTableを使用してフォームフィールドを入力します
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF for .NETは、PDFドキュメント内のフォームフィールドの作成/操作のための優れた機能を提供します。このAPIを使用すると、プログラムによってPDFファイル内のフォームフィールドを入力したり、[FDFからPDFファイルへのデータのインポート](/pdf/ja/net/import-and-export-data/)、[XFDFからPDFファイルへのデータのインポート](/pdf/ja/net/import-and-export-data/)、[XMLからPDFファイルへのデータのインポート](/pdf/ja/net/import-and-export-data/)を行ったり、[System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1)オブジェクトからデータをインポートすることもできます。

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

## FDFからPDFファイルにデータをエクスポートする

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
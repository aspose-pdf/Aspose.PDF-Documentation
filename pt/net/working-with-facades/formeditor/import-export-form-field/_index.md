---
title: Importar e Exportar Campo de Formulário
type: docs
weight: 60
url: /pt/net/import-export-form-field/
description: Preencher campos de formulário usando DataTable com a Classe FormEditor por Aspose.PDF para .NET
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF para .NET fornece grandes capacidades para criar/manipular campos de formulário dentro de um documento PDF. Usando esta API, você pode programaticamente preencher campos de formulário dentro de um arquivo PDF, preencher campos de formulário por [Importar Dados de FDF para um Arquivo PDF](/pdf/pt/net/import-and-export-data/), [Importar Dados de XFDF para um Arquivo PDF](/pdf/pt/net/import-and-export-data/), [Importar Dados de XML para um Arquivo PDF](/pdf/pt/net/import-and-export-data/) ou até mesmo importar dados de um objeto [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

```csharp
 public static void ImportData()
    {
    var editor = new Form();
    editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
    editor.ImportFdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.fdf"));
    editor.ImportXml(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xml"));

    //TODO: Bug! Criar problema
    editor.ImportXfdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xfdf"));
    editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
    }
```

## Exportar Dados de FDF para um Arquivo PDF

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
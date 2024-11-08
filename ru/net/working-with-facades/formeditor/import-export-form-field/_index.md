---
title: Импорт и Экспорт Поля Формы
type: docs
weight: 60
url: /ru/net/import-export-form-field/
description: Заполнение полей формы с использованием DataTable с классом FormEditor от Aspose.PDF для .NET
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF для .NET предоставляет отличные возможности для создания/манипулирования полями формы внутри PDF документа. Используя этот API, вы можете программно заполнять поля формы внутри PDF файла, заполнять поля формы с помощью [Импорт данных из FDF в PDF файл](/pdf/ru/net/import-and-export-data/), [Импорт данных из XFDF в PDF файл](/pdf/ru/net/import-and-export-data/), [Импорт данных из XML в PDF файл](/pdf/ru/net/import-and-export-data/) или даже импортировать данные из объекта [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

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

## Экспорт данных из FDF в PDF файл

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
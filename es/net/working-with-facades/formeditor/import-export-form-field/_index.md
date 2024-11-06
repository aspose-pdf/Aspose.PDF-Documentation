---
title: Importar y Exportar Campo de Formulario
type: docs
weight: 60
url: es/net/import-export-form-field/
description: Rellenar campos de formulario usando DataTable con la Clase FormEditor de Aspose.PDF para .NET
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF para .NET proporciona grandes capacidades para crear/manipular campos de formulario dentro de documentos PDF. Usando esta API, puedes programar el llenado de campos de formulario dentro de un archivo PDF, llenar campos de formulario por [Importar datos de FDF en un archivo PDF](/pdf/net/import-and-export-data/), [Importar datos de XFDF en un archivo PDF](/pdf/net/import-and-export-data/), [Importar datos de XML en un archivo PDF](/pdf/net/import-and-export-data/) o incluso puedes importar datos desde el objeto [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

```csharp
 public static void ImportData()
    {
    var editor = new Form();
    editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
    editor.ImportFdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.fdf"));
    editor.ImportXml(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xml"));

    //TODO: ¡Error! Crear problema
    editor.ImportXfdf(System.IO.File.OpenRead(_dataDir + "Sample-Form-01-upd.xfdf"));
    editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
    }

```

## Exportar Datos de FDF a un Archivo PDF

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
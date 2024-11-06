---
title: 导入和导出表单字段
type: docs
weight: 60
url: zh/net/import-export-form-field/
description: 使用 Aspose.PDF for .NET 的 FormEditor 类通过 DataTable 填写表单字段
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF for .NET 提供了在 PDF 文档中创建/操作表单字段的强大功能。使用此 API，您可以通过编程方式填写 PDF 文件中的表单字段，通过[从 FDF 导入数据到 PDF 文件](/pdf/net/import-and-export-data/)、[从 XFDF 导入数据到 PDF 文件](/pdf/net/import-and-export-data/)、[从 XML 导入数据到 PDF 文件](/pdf/net/import-and-export-data/)或甚至可以从 [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 对象导入数据。

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

## 从FDF导出数据到PDF文件

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
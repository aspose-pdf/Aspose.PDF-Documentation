---
title: استيراد وتصدير حقل النموذج
type: docs
weight: 60
url: /ar/net/import-export-form-field/
description: تعبئة حقول النموذج باستخدام DataTable مع فئة FormEditor بواسطة Aspose.PDF ل .NET
lastmod: "2021-06-05"
draft: false
---

يوفر Aspose.PDF ل .NET قدرات رائعة لإنشاء ومعالجة حقول النماذج داخل مستند PDF. باستخدام هذه الواجهة البرمجية، يمكنك تعبئة حقول النماذج برمجيًا داخل ملف PDF، تعبئة حقول النماذج بواسطة [استيراد البيانات من FDF إلى ملف PDF](/pdf/ar/net/import-and-export-data/)، [استيراد البيانات من XFDF إلى ملف PDF](/pdf/ar/net/import-and-export-data/)، [استيراد البيانات من XML إلى ملف PDF](/pdf/ar/net/import-and-export-data/) أو حتى يمكنك استيراد البيانات من كائن [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

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

## تصدير البيانات من FDF إلى ملف PDF

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
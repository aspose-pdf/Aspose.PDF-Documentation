---
title: Import and Export Form Field
type: docs
weight: 60
url: /ko/net/import-export-form-field/
description: Aspose.PDF for .NET의 FormEditor 클래스를 사용하여 DataTable로 양식 필드 채우기
lastmod: "2021-06-05"
draft: false
---

Aspose.PDF for .NET은 PDF 문서 내의 양식 필드를 생성/조작하는 데 뛰어난 기능을 제공합니다. 이 API를 사용하면 프로그래밍 방식으로 PDF 파일 내의 양식 필드를 채우거나, [FDF에서 PDF 파일로 데이터 가져오기](/pdf/ko/net/import-and-export-data/), [XFDF에서 PDF 파일로 데이터 가져오기](/pdf/ko/net/import-and-export-data/), [XML에서 PDF 파일로 데이터 가져오기](/pdf/ko/net/import-and-export-data/) 또는 [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) 객체에서 데이터를 가져올 수도 있습니다.

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

## FDF에서 PDF 파일로 데이터 내보내기

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
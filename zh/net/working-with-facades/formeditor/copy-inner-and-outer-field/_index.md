---
title: 复制内外字段
type: docs
weight: 40
url: /zh/net/copy-inner-and-outer-field/
description: 本节解释如何使用 FormEditor 类通过 Aspose.PDF Facades 复制内外字段。
lastmod: "2021-06-05"
draft: false
---

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) 方法允许您在同一文件中、相同坐标、指定页面上复制字段。此方法需要您要复制的字段名称、新字段名称以及字段需要复制的页码。[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供了此方法。以下代码片段向您展示如何在同一文件的相同位置复制字段。

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 复制现有 PDF 文件中的外部字段

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) 方法允许您从外部 PDF 文件中复制一个表单字段，然后将其添加到输入 PDF 文件的相同位置和指定的页码。此方法需要提供要复制字段的 PDF 文件、字段名称以及需要复制字段的页码。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段向您展示如何从外部 PDF 文件中复制一个字段。

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```
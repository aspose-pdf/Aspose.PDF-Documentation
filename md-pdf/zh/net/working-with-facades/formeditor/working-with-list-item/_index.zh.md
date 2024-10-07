---
title: 处理列表项
type: docs
weight: 30
url: /net/working-with-list-item/
description: 本节介绍如何使用 FormEditor 类通过 Aspose.PDF Facades 处理列表项。
lastmod: "2021-06-05"
draft: false
---

## 在现有 PDF 文件中添加列表项

[AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) 方法允许您在 [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) 字段中添加项目。第一个参数是字段名称，第二个参数是字段项。您可以传递单个字段项，也可以传递包含项目列表的字符串数组。此方法由 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类提供。以下代码片段展示了如何在 PDF 文件中添加列表项。

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 从现有 PDF 文件中删除列表项

[DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) 方法允许您从 [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) 中删除特定项。第一个参数是字段名称，而第二个参数是您想从列表中删除的项。此方法由 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类提供。以下代码片段演示了如何从 PDF 文件中删除列表项。

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```
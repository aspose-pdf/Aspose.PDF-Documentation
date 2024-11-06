---
title: 使用列表项
type: docs
weight: 30
url: zh/java/working-with-list-item/
description: 本节介绍如何使用 FormEditor 类通过 com.aspose.pdf.facades 处理列表项。
lastmod: "2021-06-05"
draft: false
---

## 在现有 PDF 文件中添加列表项

[addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) 方法允许您在 ListBox 字段中添加一个项。第一个参数是字段名称，第二个参数是字段项。您可以传递单个字段项，也可以传递包含项列表的字符串数组。此方法由 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类提供。以下代码片段向您展示如何在 PDF 文件中添加列表项。

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## 从现有 PDF 文件中删除列表项

[delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) 方法允许您从列表框中删除特定项。第一个参数是字段名称，而第二个参数是您想从列表中删除的项。该方法由 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类提供。以下代码片段向您展示了如何从 PDF 文件中删除列表项。

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```
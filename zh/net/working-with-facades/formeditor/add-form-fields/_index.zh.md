---
title: 添加PDF表单字段
type: docs
weight: 10
url: /net/add-form-fields/
description: 本主题解释了如何使用Aspose.PDF Facades和FormEditor类处理表单字段。
lastmod: "2021-06-05"
draft: false
---

## 在现有PDF文件中添加表单字段

为了在现有PDF文件中添加表单字段，您需要使用[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)类的[AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index)方法。 该方法要求您指定要添加的字段类型以及字段的名称和位置。您需要创建一个 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类的对象，使用 [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 方法在 PDF 中添加一个新字段。此外，您可以使用 [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) 方法指定字段中的字符数限制，最后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 方法保存更新的 PDF 文件。下面的代码片段向您展示了如何在现有的 PDF 文件中添加表单字段。

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## 在现有 PDF 文件中添加提交按钮 URL

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 方法允许您在 PDF 文件中设置提交按钮的 URL。这是当提交按钮被点击时数据被发布的 URL。在我们的示例代码中，我们指定了 URL、字段名称、要添加的页码以及按钮放置的坐标。[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 方法需要提交按钮字段的名称和 URL。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段向您展示了如何设置提交按钮的 URL。

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## 添加 JavaScript 到按钮

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) 方法允许您在 PDF 文件中的按钮上添加 JavaScript。此方法需要按钮的名称和 JavaScript 。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段演示了如何为按钮设置 JavaScript。

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
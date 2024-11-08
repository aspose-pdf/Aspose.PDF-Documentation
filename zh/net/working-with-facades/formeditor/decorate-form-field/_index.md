---
title: 在 PDF 中装饰表单字段
type: docs
weight: 20
url: /zh/net/decorate-form-field/
description: 本节解释如何使用 FormEditor 类在 PDF 中装饰表单字段。
lastmod: "2021-06-05"
draft: false
---

## 在现有 PDF 文件中装饰特定表单字段

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) 方法存在于 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类中，允许您在 PDF 文件中装饰特定表单字段。 如果你想装饰一个特定的字段，那么你需要将字段名称传递给这个方法。 然而，在调用此方法之前，您需要创建 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 和 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类的对象。 你还需要将 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 对象分配给 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 对象的 [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) 属性。之后，你可以设置 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 对象提供的任何属性。一旦设置了属性，就可以调用 [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) 方法，最后使用 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 方法保存更新后的 PDF。
下面的代码片段展示了如何装饰特定的表单字段。

```csharp
public static void DecorateField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var cityDecoration = new FormFieldFacade
            {
                Font = FontStyle.Courier,
                FontSize = 12,
                BorderColor = System.Drawing.Color.Black,
                BorderWidth = 2
            };

            editor.Facade = cityDecoration;
            editor.DecorateField("City");
            editor.Save(_dataDir + "Sample-Form-02.pdf");
        }
```
## 装饰现有 PDF 文件中特定类型的所有字段

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) 方法允许您一次性装饰 PDF 文件中特定类型的所有表单字段。 如果您想装饰特定类型的所有字段，则需要将字段类型传递给此方法。 不过，在调用此方法之前，您需要创建 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 和 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类的对象。 你还需要将 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 对象分配给 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 对象的 [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) 属性。之后，你可以设置 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 对象提供的任何属性。一旦设置了属性，你可以调用 [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) 方法，最后使用 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 方法保存更新后的 PDF。以下代码片段向你展示了如何装饰特定类型的所有字段。

```csharp
        public static void DecorateField2()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");

            var textFieldDecoration = new FormFieldFacade
            {
                Alignment = FormFieldFacade.AlignCenter,
            };

            editor.Facade = textFieldDecoration;
            editor.DecorateField(FieldType.Text);
            editor.Save(_dataDir + "Sample-Form-01-align-text.pdf");
        }
```
---

title: 在 PDF 中装饰表单字段
type: docs
weight: 20
url: /zh/java/decorate-form-field/
description: 本节介绍如何使用 FormEditor 类在 PDF 中装饰表单字段。
lastmod: "2021-06-05"
draft: false

---

## 在现有 PDF 文件中装饰特定表单字段

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 方法存在于 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类中，允许您在 PDF 文件中装饰特定的表单字段。
 如果您想装饰特定字段，则需要将字段名称传递给此方法。但是，在调用此方法之前，您需要创建 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 和 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 类的对象。之后，您可以设置 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 对象提供的任何属性。一旦设置了属性，您可以调用 [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 方法，最后使用 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类的 Save 方法保存更新后的 PDF。 以下代码片段展示了如何装饰特定的表单字段。

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## 装饰现有 PDF 文件中特定类型的所有字段

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 方法允许您一次装饰 PDF 文件中特定类型的所有表单字段。
 如果你想装饰特定类型的所有字段，那么你需要将字段类型传递给此方法。但是，在调用此方法之前，你需要创建 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 和 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 类的对象。之后，你可以设置由 [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) 对象提供的任何属性。一旦设置了属性，你可以调用 [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) 方法，最后使用 [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) 类的 Save 方法保存更新后的 PDF。以下代码片段向你展示了如何装饰特定类型的所有字段。

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        // 绑定 PDF 文件
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        // 设置文本字段的对齐方式为居中
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        // 装饰文本字段
        editor.decorateField(FieldType.Text);
        // 保存更新后的 PDF
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```
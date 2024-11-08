---
title: PDFでフォームフィールドを装飾する
type: docs
weight: 20
url: /ja/net/decorate-form-field/
description: このセクションでは、FormEditorクラスを使用してPDFのフォームフィールドを装飾する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイルで特定のフォームフィールドを装飾する

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスに存在する[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield)メソッドは、PDFファイル内の特定のフォームフィールドを装飾することを可能にします。 If you want to decorate a particular field then you need to pass the field name to this method.  
特定のフィールドを装飾したい場合は、このメソッドにフィールド名を渡す必要があります。 However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes.

ただし、このメソッドを呼び出す前に、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスと [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) クラスのオブジェクトを作成する必要があります。 以下のドキュメントを翻訳する必要があります。

あなたはまた、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)オブジェクトを[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor)オブジェクトの[Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index)プロパティに割り当てる必要があります。その後、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)オブジェクトが提供する任意の属性を設定できます。属性を設定したら、[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield)メソッドを呼び出し、最後に[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスの[Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index)メソッドを使用して更新されたPDFを保存します。
次のコードスニペットは、特定のフォームフィールドを装飾する方法を示しています。

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
## 特定のタイプのすべてのフィールドを既存のPDFファイルで装飾する

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) メソッドを使用すると、PDFファイル内の特定のタイプのすべてのフォームフィールドを一度に装飾することができます。 If you want to decorate all fields of a particular type then you need to pass the field type to this method.  
特定のタイプのすべてのフィールドを装飾したい場合は、このメソッドにフィールドタイプを渡す必要があります。 However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes.  
しかし、このメソッドを呼び出す前に、[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスおよび [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) クラスのオブジェクトを作成する必要があります。 あなたはまた、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) オブジェクトを [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) オブジェクトの [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) プロパティに割り当てる必要があります。その後、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) オブジェクトによって提供される任意の属性を設定することができます。属性を設定したら、[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) メソッドを呼び出し、最後に [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) クラスの [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) メソッドを使用して更新されたPDFを保存します。次のコードスニペットは、特定のタイプのすべてのフィールドを装飾する方法を示しています。

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
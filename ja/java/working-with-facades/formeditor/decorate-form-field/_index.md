---
title: PDFでフォームフィールドを装飾する
type: docs
weight: 20
url: /ja/java/decorate-form-field/
description: このセクションでは、FormEditorクラスを使用してPDFのフォームフィールドを装飾する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## 既存のPDFファイル内の特定のフォームフィールドを装飾する

[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor)クラスに存在する[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--)メソッドを使用すると、PDFファイル内の特定のフォームフィールドを装飾することができます。
 If you want to decorate a particular field then you need to pass the field name to this method. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) and [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) classes. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) object. Once you have set the attributes, you can call the [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) method and finally save the updated PDF using Save method of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class.  
以下のコードスニペットは、特定のフォームフィールドを装飾する方法を示しています。

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

## 既存のPDFファイル内の特定のタイプのすべてのフィールドを装飾する

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) メソッドを使用すると、PDFファイル内の特定のタイプのすべてのフォームフィールドを一度に装飾することができます。
 もし特定のタイプのすべてのフィールドを装飾したい場合は、このメソッドにフィールドタイプを渡す必要があります。ただし、このメソッドを呼び出す前に、[FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) と [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) クラスのオブジェクトを作成する必要があります。その後、[FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) オブジェクトによって提供される任意の属性を設定できます。属性を設定したら、[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) メソッドを呼び出し、最終的に [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) クラスの Save メソッドを使用して更新された PDF を保存できます。以下のコードスニペットは、特定のタイプのすべてのフィールドを装飾する方法を示しています。

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```
---
title: AcroFormsの変更
linktitle: AcroFormsの変更
type: docs
weight: 40
url: /ja/java/modifing-form/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFドキュメント内のフォームを変更する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## カスタムフォームフィールドフォントの設定

Adobe PDFファイルのフォームフィールドは、特定のデフォルトフォントを使用するように設定できます。Aspose.PDFを使用すると、14のコアフォントのいずれかやカスタムフォントをフィールドのデフォルトフォントとして適用できます。
フォームフィールドで使用されるデフォルトフォントを設定および更新するには、Aspose.PDFにはDefaultAppearance (Font font, double size, Color color) クラスがあります。このクラスはcom.aspose.pdf.DefaultAppearanceを使用してアクセスできます。このオブジェクトを使用するには、FieldクラスのsetDefaultAppearance(..)メソッドを使用します。

次のコードスニペットは、PDFフォームフィールドのデフォルトフォントを設定する方法を示しています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // ドキュメントから特定のフォームフィールドを取得する
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // フォントオブジェクトを作成する
        Font font = FontRepository.findFont("ComicSansMS");

        // フォームフィールドのフォント情報を設定する
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // 更新されたドキュメントを保存する
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## フィールド制限の取得/設定

FormEditorクラスのSetFieldLimitメソッドは、フィールドに入力できる最大文字数を設定することを可能にします。

```java
    public static void GettingMaximumFieldLimit()
    {
        // DOMを使用して最大フィールド制限を取得
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limit: " +field.getMaxLen());
    }
```

同じ値をAspose.PDF.Facades名前空間を使用して次のコードスニペットで取得することもできます。

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Facadesを使用して最大フィールド制限を取得
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limit: " + form.getFieldLimit("textbox1"));
    }
```

同様に、Aspose.PDFにはDOMアプローチを使用してフィールド制限を取得するメソッドがあります。
 以下のコードスニペットは手順を示しています。

```java
    public static void SettingMaximumFieldLimit()
    {
        // DOMを使用して最大フィールド制限を取得
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## PDFドキュメントから特定のフォームフィールドを削除する

すべてのフォームフィールドは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトのFormコレクションに含まれています。このコレクションは、削除メソッドを含む、フォームフィールドを管理するさまざまなメソッドを提供します。特定のフィールドを削除したい場合は、フィールド名を削除メソッドのパラメータとして渡し、更新されたPDFドキュメントを保存します。

以下のコードスニペットは、PDFドキュメントから名前付きフィールドを削除する方法を示しています。

```java
    public static void DeleteParticularFormField()
    {    
        // ドキュメントを開く
        Document pdfDocument = new Document("input.pdf");

        // 名前で指定されたフィールドを削除
        pdfDocument.getForm().delete("textbox1");

        // 修正されたPDFを保存
        pdfDocument.save("output.pdf");
    }
```

## PDFドキュメントのフォームフィールドを変更する

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトのフォームコレクションを使用して、PDFドキュメント内のフォームフィールドを管理できます。

フォームフィールドを変更するには、フォームコレクションからフィールドを取得し、そのプロパティを設定します。その後、更新されたPDFドキュメントを保存します。

次のコードスニペットは、PDFドキュメント内の既存のフォームフィールドを変更する方法を示しています。

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // フィールドを取得
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // フィールドの値を変更
        textBoxField.setValue("Updated Value");

        // フィールドを読み取り専用に設定
        textBoxField.setReadOnly(true);

        // 更新されたドキュメントを保存
        pdfDocument.save("output.pdf");
    }
```

### PDFファイル内の新しい場所にフォームフィールドを移動する

フォームフィールドをPDFページの新しい場所に移動したい場合、まずフィールドオブジェクトを取得し、そのsetRectメソッドに新しい値を指定します。
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトに新しい座標が設定され、setRect(..) メソッドに割り当てられます。その後、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの save メソッドを使用して更新された PDF を保存します。

次のコードスニペットは、フォームフィールドを新しい場所に移動する方法を示しています。

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // フィールドを取得する
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // フィールドの位置を変更する
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // 変更されたドキュメントを保存する
        pdfDocument.save("output.pdf");
    }
}
```
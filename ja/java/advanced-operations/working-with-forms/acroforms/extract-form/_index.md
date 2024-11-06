---
title: データの抽出 AcroForms
linktitle: データの抽出 AcroForms
type: docs
weight: 30
url: ja/java/extract-form/
description: このセクションでは、Aspose.PDF for Java を使用して PDF ドキュメントからフォームを抽出する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントの個々のフィールドから値を取得する

フォームフィールドの[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用すると、特定のフィールドの値を取得できます。

値を取得するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのフォームコレクションからフォームフィールドを取得します。

この例では、[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)を選択し、[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用してその値を取得します。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // フィールドを取得
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // フィールド名を取得
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // フィールド値を取得
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## PDFドキュメントのすべてのフィールドから値を取得する

PDFドキュメントのすべてのフィールドから値を取得するには、すべてのフォームフィールドをナビゲートし、[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用して値を取得する必要があります。[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトの[getForm() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)を使用してFormコレクションから各フィールドを取得し、getFields()を使用してフォームフィールドのリストをField配列に取得し、配列をトラバースしてフィールドの値を取得します。

次のコードスニペットは、PDFドキュメント内のすべてのフィールドの値を取得する方法を示しています。

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // ドキュメントを開く
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("フォームフィールド: " + fields[i].getFullName());
            System.out.println("フォームフィールド: " + fields[i].getValue());
        }

    }
}
```


## PDFファイルの特定の領域からフォームフィールドを取得する

場合によっては、フォーム全体からではなく、例えば印刷されたシートの左上の4分の1からのみデータを取得する必要があります。  
Aspose.PDF for Javaを使用すれば、これは問題ありません。PDFファイルの指定された領域外のフィールドをフィルタリングするための領域を指定できます。PDFファイルの特定の領域からフォームフィールドを取得するには、以下の手順を実行します。

1. Documentオブジェクトを使用してPDFファイルを開きます。
2. ドキュメントのFormsコレクションからフォームを取得します。
3. 長方形の領域を指定し、それをFormオブジェクトの[getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-)メソッドに渡します。[Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field)コレクションが返されます。
4. これを使用してフィールドを操作します。

以下のコードスニペットは、PDFファイルの特定の長方形領域でフォームフィールドを取得する方法を示しています。

```java
public static void GetValuesFromSpecificRegion() {
    // PDFファイルを開く
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // その領域のフィールドを取得するための長方形オブジェクトを作成
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // PDFフォームを取得
    com.aspose.pdf.Form form = doc.getForm();

    // 長方形領域内のフィールドを取得
    Field[] fields = form.getFieldsInRect(rectangle);

    // フィールド名と値を表示
    for (Field field : fields)
    {
        // すべての配置の画像配置プロパティを表示
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```
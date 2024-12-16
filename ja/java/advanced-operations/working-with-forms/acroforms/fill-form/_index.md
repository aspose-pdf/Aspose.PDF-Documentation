---
title: AcroFormsを埋める
linktitle: AcroFormsを埋める
type: docs
weight: 20
url: /ja/java/fill-form/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFドキュメントのフォームフィールドを埋める方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントは素晴らしく、フォームを作成するための好ましいファイルタイプです。

Aspose.PDF for Javaを使用すると、フォームフィールドを埋めることができ、DocumentオブジェクトのFormコレクションからフィールドを取得できます。

次の例を見て、このタスクを解決する方法を見てみましょう：

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // フィールドを作成する
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // フィールドをドキュメントに追加する
        pdfDocument.getForm().add(textBoxField, 1);

        // 変更されたPDFを保存する
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```
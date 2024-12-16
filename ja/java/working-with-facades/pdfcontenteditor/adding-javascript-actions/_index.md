---
title: 既存のPDFファイルにJavascriptアクションを追加
type: docs
weight: 10
url: /ja/java/adding-javascript-actions/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFファイルにJavascriptアクションを追加する方法を説明します。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

com.aspose.pdf.facadesパッケージにある[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)クラスは、PDFファイルにJavascriptアクションを追加する柔軟性を提供します。PDFビューアでメニューアイテムを実行するための連続アクションでリンクを作成することができます。このクラスは、ドキュメントイベントのための追加アクションを作成する機能も提供します。

まず最初に、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)内にオブジェクトが描画されます。私たちの例では、[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)です。
 そして、アクション[createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-)をRectangleに設定します。その後、ドキュメントを保存できます。

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // Javascriptリンクを作成する
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Asposeへようこそ！');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // 出力ファイルを保存する
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```
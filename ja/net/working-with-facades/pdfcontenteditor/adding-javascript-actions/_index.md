---
title: Javascriptアクションを追加するPDF
type: docs
weight: 10
url: /ja/net/adding-javascript-actions/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFファイルにJavascriptアクションを追加する方法を説明します。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) クラスは、Aspose.Pdf.Facadesパッケージの下にあり、PDFファイルにJavascriptアクションを追加する柔軟性を提供します。PDFビューアでメニュー項目を実行するのに対応する連続アクションのリンクを作成できます。このクラスは、ドキュメントイベントのための追加アクションを作成する機能も提供します。

まず最初に、[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) の中にオブジェクトが描画されます。私たちの例では、[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) です。 そして、アクション [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) を Rectangle に設定します。その後、ドキュメントを保存できます。

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // Javascriptリンクを作成
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Welcome to Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // 出力ファイルを保存
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```
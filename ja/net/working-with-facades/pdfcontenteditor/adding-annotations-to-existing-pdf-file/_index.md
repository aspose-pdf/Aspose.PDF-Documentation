---
title: 既存のPDFファイルに注釈を追加する
type: docs
weight: 80
url: /ja/net/adding-annotations-to-existing-pdf-file/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFファイルに注釈を追加する方法を説明します。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFファイルにフリーテキスト注釈を追加する (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) を使用すると、既存のPDFファイルにさまざまなタイプの注釈を追加できます。特定の注釈を追加するには、対応するメソッドを使用します。たとえば、次のコードスニペットでは、[CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) メソッドを使用して [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) タイプの注釈を追加しています。

どのタイプの注釈も同じ方法でPDFファイルに追加することができます。 まず最初に、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 型のオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。次に、注釈の領域を指定するためにRectangleオブジェクトを作成する必要があります。

その後、[CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) メソッドを呼び出して [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 注釈を追加し、[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して更新されたPDFファイルを保存できます。

次のコードスニペットは、PDFファイルにフリーテキスト注釈を追加する方法を示しています。

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // 最後のパラメータはページ番号です
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## 既存のPDFファイルにテキスト注釈を追加する (facades)

この例でも、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 型のオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用して入力PDFファイルをバインドする必要があります。次に、注釈の領域を指定するためにRectangleオブジェクトを作成する必要があります。その後、[CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) メソッドを呼び出してフリーテキスト注釈を追加し、注釈のタイトルと注釈が配置されているページ番号を作成することができます。

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## 既存のPDFファイルにライン注釈を追加する（ファサード）

また、長方形、ラインの始点と終点の座標、ページ番号、注釈フレームの太さ、スタイル、色、ラインダッシュの種類、ラインの始点と終点の種類を指定します。

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // ライン注釈を作成
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```
---
title: 既存のPDFファイルに注釈を追加する
type: docs
weight: 80
url: /ja/java/adding-annotations-to-existing-pdf-file/
description: このセクションでは、Aspose.PDF Facadesを使用して既存のPDFファイルに注釈を追加する方法を説明します。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 既存のPDFファイルにフリーテキスト注釈を追加する (ファサード)

フリーテキスト注釈は、ページ上に直接テキストを表示します。[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)を使用すると、既存のPDFファイルにさまざまなタイプの注釈を追加できます。特定の注釈を追加するには、それぞれのメソッドを使用します。例えば、次のコードスニペットでは、[createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-)メソッドを使用してFreeTextタイプの注釈を追加しています。

どのタイプの注釈も、同じ方法でPDFファイルに追加できます。
 まず最初に、[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 型のオブジェクトを作成し、bindPdf メソッドを使用して入力 PDF ファイルをバインドする必要があります。次に、アノテーションの領域を指定するために Rectangle オブジェクトを作成する必要があります。その後、[createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) メソッドを呼び出してフリーテキストアノテーションを追加し、アノテーションが配置されるページ番号を指定し、save メソッドを使用して更新された PDF ファイルを保存します。

以下のコードスニペットは、PDFファイルにフリーテキストアノテーションを追加する方法を示しています。

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // 最後のパラメータはページ番号です
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## 既存のPDFファイルにテキスト注釈を追加する (facades)

この例でも、[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 型のオブジェクトを作成し、[bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) メソッドを使用して入力PDFファイルをバインドする必要があります。次に、注釈の領域を指定するために Rectangle オブジェクトを作成します。その後、[createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) メソッドを呼び出して FreeText 注釈を追加し、注釈のタイトルと注釈が配置されているページ番号を作成できます。

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDFは現代文書に最適な形式です", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## 既存のPDFファイルにライン注釈を追加する (ファサード)

また、ラインの開始と終了の座標、ページ番号、注釈枠の厚さ、スタイル、色、ラインダッシュの種類、ラインの開始と終了の種類を指定します。

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // ライン注釈を作成
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "テスト",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```
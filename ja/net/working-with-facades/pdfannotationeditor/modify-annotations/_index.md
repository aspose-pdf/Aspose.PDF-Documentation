---
title: PDFの注釈を修正する
type: docs
weight: 50
url: ja/net/modify-annotations/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFに注釈を修正する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations)メソッドを使用すると、注釈の基本属性、すなわち件名、修正日、作成者、注釈の色、およびオープンフラグを変更できます。また、ModifyAnnotationsメソッドを使用して作成者を直接設定することもできます。このクラスは、注釈を削除するための2つのオーバーロードされたメソッドも提供します。最初のメソッドであるDeleteAnnotationsは、PDFファイルからすべての注釈を削除します。

例えば、次のコードでは、[ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor)を使用して注釈の作成者を変更します。

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

以下の2番目の方法では、指定されたタイプのすべての注釈を削除することができます。

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // 注釈属性を変更するための新しいAnnotationタイプのオブジェクトを作成
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // 新しい注釈属性を設定
                Title = "Aspose.PDF デモユーザー",
                Subject = "技術記事"
            };
            // PDFファイルの注釈を変更
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## See also

注釈を比較して、自分に合った方法を見つけてみてください。[PDF注釈](/pdf/net/annotations/)セクションを学びましょう。
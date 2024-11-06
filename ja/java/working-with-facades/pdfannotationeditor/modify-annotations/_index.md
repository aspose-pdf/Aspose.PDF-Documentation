---
title: PDFファイル内の注釈を修正する (ファサード)
type: docs
weight: 50
url: ja/java/modify-annotations/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFに注釈を修正する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) メソッドは、注釈の基本属性、すなわち件名、修正日、作成者、注釈の色、および開くフラグを変更することを可能にします。また、ModifyAnnotationsメソッドを使用して作成者を直接設定することもできます。このクラスは、注釈を削除するための2つのオーバーロードされたメソッドも提供します。最初のメソッドであるDeleteAnnotationsは、PDFファイルからすべての注釈を削除します。

例えば、次のコードでは、[modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-) を使用して注釈の作成者を変更することを考慮します。

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

2番目のメソッドでは、指定したタイプのすべての注釈を削除することができます。

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 注釈属性を変更するためのAnnotationタイプの新しいオブジェクトを作成します
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF デモユーザー");
        annotation.setSubject("技術記事");

        // PDFファイルの注釈を修正します
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## 参照

注釈を使用するための方法を比較し、自分に合った方法を見つけてみてください。[PDF 注釈](/pdf/java/annotations/)セクションを学びましょう。
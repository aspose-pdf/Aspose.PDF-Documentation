---
title: PDFファイルからXFDFへのアノテーションのフラット化 (facades)
type: docs
weight: 40
url: /java/flatten-annotation/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFにアノテーションをエクスポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

フラット化プロセスとは、アノテーションがドキュメントから削除されるとき、その視覚的表現がそのまま保持されることを意味します。フラット化されたアノテーションは依然として表示されますが、ユーザーやアプリケーションによって編集することはできません。これを使用して、たとえば、ドキュメントにアノテーションを永久に適用したり、アノテーションを表示できないビューアにアノテーションを表示させたりすることができます。特に指定しない限り、エクスポートではすべてのアノテーションがそのまま保持されます。

このオプションが選択されると、エクスポートされたPDFにPDF標準のアノテーションとしてアノテーションが含まれます。

次のコードスニペットで使用されている[flatteningAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#flatteningAnnotations--)メソッドを確認してください。

```java
public static void Flattening() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        FlattenSettings flattenSettings = new FlattenSettings();
        flattenSettings.setApplyRedactions(true); // 編集を適用する
        flattenSettings.setCallEvents(false); // イベントを呼び出さない
        flattenSettings.setHideButtons(true); // ボタンを隠す
        flattenSettings.setUpdateAppearances(true); // 外観を更新する
        annotationEditor.flatteningAnnotations(flattenSettings);
        annotationEditor.save(_dataDir + "FlattenAnnotation.pdf");
    }
```
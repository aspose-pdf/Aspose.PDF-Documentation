---
title: PDFからXFDFへの注釈のフラット化
type: docs
weight: 40
url: /net/flatten-annotation/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFに注釈をエクスポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

フラット化プロセスとは、ドキュメントから注釈を削除したときに、その視覚的な表現が維持されることを意味します。フラット化された注釈は依然として表示されますが、ユーザーやアプリによって編集することはできません。これを使用すると、例えば、注釈をドキュメントに永久的に適用したり、注釈を表示できないビューアに注釈を表示させたりすることができます。指定がない場合、エクスポートではすべての注釈がそのまま保持されます。

このオプションを選択すると、エクスポートされたPDFにPDF標準の注釈として注釈が含まれます。

次のコードスニペットで使用されている[flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations)メソッドを確認してください。

```csharp
public static void Flattening()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            FlattenSettings flattenSettings = new FlattenSettings
            {
                ApplyRedactions = true,
                CallEvents = false,
                HideButtons = true,
                UpdateAppearances = true
            };
            annotationEditor.FlatteningAnnotations(flattenSettings);
            annotationEditor.Save(_dataDir + "FlattenAnnotation.pdf");
        }
```
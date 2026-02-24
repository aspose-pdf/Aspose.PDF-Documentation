---
title: Python を使用した PDF スティッキー注釈
linktitle: スティッキー注釈
type: docs
weight: 50
url: /ja/python-net/sticky-annotations/
description: Aspose.PDF for Python を使用して、コメントやフィードバック用に PDF ドキュメントにスティッキー注釈を追加する方法を学びます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF のスティッキー注釈を操作する方法ガイド
Abstract: 本記事では、Aspose.PDF for Python ライブラリを使用して PDF ドキュメントの透かし注釈を管理するための詳細なガイドを提供します。透かし注釈の追加、取得、削除のプロセスを説明し、文書の真正性とブランディングを確保します。透かし注釈は、ロゴなどのグラフィックをページ上の固定サイズと位置に埋め込むために使用できます。ガイドには、特定の位置に透かし注釈を追加し、透明度を調整するコードスニペットや、既存の透かし注釈を取得および削除する方法が含まれています。コード例は、Aspose.PDF ライブラリを使用して PDF ドキュメントをプログラム的に操作する方法を示し、開発者が透かし機能をアプリケーションに統合するための実用的なアプローチを提供します。
---

## 透かし注釈の追加

最も目立ち、視覚化と伝達が容易なのは透かし注釈です。これは、PDF ドキュメントにロゴやその他のオリジナリティを確認できるサインを配置する最適な方法です。

透かし注釈は、印刷ページのサイズに関係なく、ページ上に固定サイズと位置で印刷されるべきグラフィックを表すために使用されます。

特定の PDF ページ位置に [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) を使用して透かしテキストを追加できます。透かしの不透明度は、[opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties) プロパティを使用して制御することもできます。

以下のコードスニペットを確認して、WatermarkAnnotation を追加してください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## 透かし注釈の取得

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## 透かし注釈の削除

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```



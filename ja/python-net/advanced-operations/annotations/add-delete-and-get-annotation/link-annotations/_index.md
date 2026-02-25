---
title: PDFでリンク注釈を使用する
linktitle: リンク注釈
type: docs
weight: 70
url: /ja/python-net/link-annotations/
description: Aspose.PDF for Python via .NET は、PDFドキュメントからリンク注釈を追加、取得、削除することを可能にします。
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## 既存のPDFファイルにリンク注釈を追加する

[リンク](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) は、クリックすると URL を開くか、同じドキュメントまたは外部ドキュメント内の特定の位置へ移動する注釈です。

リンク注釈は、ページ上の任意の場所に配置できる長方形の領域です。各リンクには対応する PDF アクションが関連付けられており、ユーザーがこのリンク領域をクリックするとそのアクションが実行されます。

次のコードスニペットは、電話番号の例を使用して PDF ファイルにリンク注釈を追加する方法を示しています。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### リンク注釈を取得する

次のコードスニペットを使用して、PDF ドキュメントから [リンク注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) を取得してみてください。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### リンク注釈を削除する

次のコードスニペットは、PDF ファイルからリンク注釈を削除する方法を示しています。これを行うには、1 ページ目のすべてのリンク注釈を検索して削除する必要があります。その後、注釈が削除された状態でドキュメントを保存します。

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```

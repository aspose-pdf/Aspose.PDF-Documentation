---
title: Pythonを使用したPDFのリンク更新
linktitle: リンクを更新
type: docs
weight: 20
url: /ja/python-net/update-links/
description: PDFのリンクをプログラムで更新します。このガイドはPythonでPDFのリンクを更新する方法について説明しています。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDFのリンクを更新する方法
Abstract: Aspose.PDF for Python via .NET のリンク更新ガイドは、開発者がPythonを使用してPDFドキュメント内のハイパーリンクの動作を変更するプロセスを案内します。リンク先を特定のページ、外部ウェブサイト、あるいは別のPDFファイルに設定する方法を説明します。また、テキストカラーを含むリンクアノテーションの外観調整方法も取り上げ、各シナリオに対する実用的なコード例を提供します。古くなったURLの修正やナビゲーションの向上を目的とする場合でも、このリソースはリンクをプログラムで管理するための明確で効率的なアプローチを提供します。
---

## リンクアノテーション テキストカラーの更新

この例では、Aspose.PDF for Python を使用して PDF の最初のページにあるすべてのリンクアノテーションを検出し、各リンクの近くのテキストのフォントカラーを赤に変更してハイライトする方法を示します。各リンク矩形の周囲を少し拡張した領域で TextFragmentAbsorber を使用し、近くのテキストを検索・変更します。

以下の用途に使用できます:

- ドキュメント内のリンクを視覚的にマークする
- リンクされたコンテンツを強調してアクセシビリティを向上させる
- レビューやエクスポート前に PDF ファイルを前処理する

これらのリンクアノテーションそれぞれについて、スクリプトは矩形の境界を取得し、近くのテキストを含むように領域を少し拡張します。拡張した領域に対して TextFragmentAbsorber を適用し、その中にあるテキストフラグメントを抽出します。抽出されたフラグメントはフォントカラーを赤に変更され、周囲のテキストが強調表示されます。すべての更新を適用した後、変更されたドキュメントは出力パスに保存され、ハイライトされたアノテーションと関連テキストが保持されます。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## 境界線の更新

スクリプトはドキュメントの最初のページに注目し、すべてのアノテーションをフィルタリングして LINK タイプのものだけを選択します。これらは通常、ハイパーリンクやナビゲーショントリガーなどのインタラクティブ要素を表します。各リンクアノテーションについて、コードはそれらを LinkAnnotation 型にキャストし、カラー属性を赤に更新して視覚的に目立たせます。すべてのリンクアノテーションが変更された後、更新されたドキュメントは指定された出力場所に保存され、新しいスタイルが保持されます。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## Web 先の更新

パスが設定されたら、Aspose.PDF ライブラリを使用して元のドキュメントを読み込み、内容を変更可能にします。スクリプトは続いてドキュメントの最初のページに注目し、すべてのアノテーションをフィルタリングしてリンクタイプのものだけを選択します。これらは通常、クリック可能領域やハイパーリンクを表します。型エラーを回避し安全に処理するため、各アノテーションは is_assignable でチェックされ、適切な LinkAnnotation 型にキャストされます。リンクが GoToURIAction と関連付けられている場合（ウェブアドレスを指す）、スクリプトはその URI を "https://www.google.com" に更新してユーザーをリダイレクトします。最後に、すべての変更が適用された後、変更されたドキュメントは指定された出力パスに保存されます。

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```

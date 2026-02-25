---
title: Python を使用して PDF ファイルからリンクを抽出する
linktitle: リンクを抽出
type: docs
weight: 30
url: /ja/python-net/extract-links/
description: Python と Aspose.PDF を使用して PDF ドキュメントからハイパーリンクを抽出し、コンテンツ管理やリンク分析に活用する方法を紹介します。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF からリンクを抽出する方法
Abstract: Aspose.PDF for Python via .NET のリンク抽出に関するガイドでは、Python を使用して PDF ドキュメントからハイパーリンク注釈をプログラムで取得する方法を説明しています。ドキュメントには実用的なコード例が含まれ、リンク監査、ナビゲーション分析、インタラクティブなドキュメント機能の構築などのタスクにこの機能をどのように活用できるかが強調されています。単一ページの PDF を扱う場合でも、大量のバッチを処理する場合でも、本ガイドはハイパーリンク抽出の明快で効率的なアプローチを提供します。
---

## PDF ファイルからリンクを抽出する

この例では、Aspose.PDF for Python を使用して PDF の最初のページのすべてのリンク注釈を反復処理する方法を示します。注釈をフィルタリングして LinkAnnotation 型のものを特定し、安全にキャストした後、ページインデックスとページ上の矩形位置を出力します。

これは、PDF の既存のリンク注釈のデバッグ、分析、または自動更新に使用できます。

1. PDF ドキュメントを読み込みます。ap.Document(path_infile) を使用してファイルを開きます。
1. 最初のページから注釈にアクセスします。document.pages[1].annotations を使用してすべての注釈を取得します。
1. LinkAnnotation 型のみをフィルタリングします。各注釈の annotation_type を確認します。
1. LinkAnnotation をキャストして処理します。is_assignable() と cast() を使用して、LinkAnnotation のプロパティへの安全なアクセスを確保します。
1. 注釈の詳細を出力します。各リンクのページインデックスと矩形（位置）を表示します。

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## PDF ファイルからハイパーリンクを抽出する

このコードは、Aspose.PDF for Python を使用して PDF ドキュメントの最初のページからすべての LinkAnnotation オブジェクトを抽出し、GoToURIAction を含むものを特定する方法を示します。該当する各リンクについて、ページインデックスと対象 URI を出力します。

これは次のようなタスクに役立ちます：

- PDF 内の外部リンクの監査
- ドキュメントやサポート URL の抽出
- 破損または古くなったハイパーリンクの検出

1. PDF ドキュメントを読み込みます。ap.Document を使用してファイルを開きます。
1. 最初のページからすべてのリンク注釈を取得します。annotation のタイプが AnnotationType.LINK のものだけをフィルタリングします。
1. 型チェックを行い、LinkAnnotation にキャストします。各注釈が実際に LinkAnnotation であることを確認してからプロパティにアクセスします。
1. リンクのアクションタイプを確認します。GoToURIAction（ウェブ URL へのリンク）を使用しているリンクのみをフィルタリングします。
1. URI とページインデックスを抽出して出力します。.uri を使用して外部リンクを取得し、.page_index でコンテキストを取得します。

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```

---
title: PythonでPDFからフォームを削除
linktitle: フォームを削除
type: docs
weight: 70
url: /ja/python-net/remove-form/
description: Aspose.PDF for Python via .NET ライブラリを使用して、サブタイプ/フォームに基づくテキストを削除します。PDFからすべてのフォームを削除します。
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python via .NET を使用して PDF からフォームを削除
Abstract: 本ドキュメントでは、Aspose.PDF for Python via .NET を使用して PDF ファイルからフォーム要素を削除するための、Python ベースの 2 つのアプローチを紹介します。最初の方法は、ページのリソース辞書にアクセスし、forms コレクションの clear() メソッドを呼び出すことで、特定のページからすべてのフォームオブジェクトをクリアする手順を示しています。2 番目の方法は、フォーム注釈を反復処理し、タイプライタ形式のフォームを識別し、属性に基づいて選択的に削除する、よりターゲットを絞った解決策を提供します。両方の手法は、更新された PDF を指定された出力パスに保存することで完了し、自動化ワークフローにおけるフォームのクリーンアップと文書の洗練のための柔軟なオプションを提供します。
---

## PDF からすべてのフォームを削除

このコードは、PDF ドキュメントの最初のページからすべてのフォーム要素を削除し、変更されたドキュメントを指定された出力パスに保存します。

1. PDF ドキュメントを読み込む。
1. ページリソースにアクセスする。
1. フォームオブジェクトをクリアする。
1. 更新されたドキュメントを保存する。

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## 指定されたフォームを削除

次の例では、指定された PDF ページ上のフォームオブジェクトを反復処理し、タイプライタ形式のフォーム注釈を識別して削除し、Aspose.PDF for Python via .NET を使用して更新された PDF を保存します。

1. PDF ドキュメントを読み込む。
1. ページのフォームにアクセスする。
1. フォームを反復処理する。
1. タイプライタ形式のフォームをチェックする。
1. 一致したフォームを削除する。
1. 更新されたドキュメントを保存する。

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```

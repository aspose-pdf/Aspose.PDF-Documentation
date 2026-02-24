---
title: Fill AcroForm - Fill PDF Form using Python
linktitle: Fill AcroForm
type: docs
weight: 20
url: /ja/python-net/fill-form/
description: Aspose.PDF for Python ライブラリを使用して、PDF ドキュメントのフォームに入力できます。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF のフォームフィールドに入力する方法
Abstract: この記事では、Aspose.PDF ライブラリ for Python を使用して PDF ドキュメントのフォームフィールドに入力する方法を案内します。ドキュメントのフォーム コレクションからフォームフィールドにアクセスし、フィールドの value プロパティを介してその値を設定する手順を説明しています。サンプルコードは、PDF ドキュメントを開き、フォームフィールドを反復処理して特定のフィールド（この例では "Field 1"）を部分名で検索し、TextBoxField の値を "777" に変更する方法を示しています。最後に、更新されたドキュメントを出力ファイルに保存します。さらに参考になるよう、関連する Aspose のドキュメントへのリンクも提供しています。
---

## PDF ドキュメントのフォームフィールドに入力する

次の例では、Aspose.PDF for Python を .NET 経由で使用して PDF フォームフィールドに新しい値を入力し、更新されたドキュメントを保存します。フィールド名と値の辞書を指定することで、複数のフィールドの更新をサポートします。

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```




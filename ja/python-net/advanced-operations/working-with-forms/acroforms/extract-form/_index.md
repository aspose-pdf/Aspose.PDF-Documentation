---
title: AcroFormの抽出 - PythonでPDFのフォームデータを抽出
linktitle: AcroFormの抽出
type: docs
weight: 30
url: /ja/python-net/extract-form/
description: Aspose.PDF for Python ライブラリを使用して PDF ドキュメントからフォームを抽出します。PDF ファイルの個々のフィールドから値を取得します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFからフォームデータを取得する方法
Abstract: この記事では、Python を使用して PDF ドキュメント内のフォーム フィールドからデータを抽出する方法を案内します。Aspose.PDF ライブラリを使用してすべてのフィールドをナビゲートする方法を説明し、特に `Form` コレクションにアクセスし、`Field` タイプとその `value` プロパティを利用する方法を示します。サンプルの Python コードスニペットが含まれており、PDF ドキュメントを開き、フォームフィールドを反復処理し、各フィールドの名前と値を出力する方法をデモンストレーションしています。この手法は、PDF ファイルからプログラムでフォームデータを取得する際に便利です。
---

## フォームからデータを抽出

### PDF ドキュメントのすべてのフィールドから値を取得

PDF ドキュメントのすべてのフィールドから値を取得するには、すべてのフォームフィールドをナビゲートし、Value プロパティを使用して値を取得する必要があります。Form コレクションから各フィールドを取得します。基本フィールドタイプは [フィールド](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) と呼ばれ、[値](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) プロパティにアクセスします。

以下の Python コードスニペットは、PDF ドキュメントからすべてのフィールドの値を取得する方法を示します。

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```


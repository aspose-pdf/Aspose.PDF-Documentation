---
title: AcroForm の変更
linktitle: AcroForm の変更
type: docs
weight: 45
url: /ja/python-net/modifying-form/
description: Aspose.PDF for Python via .NET ライブラリを使用して PDF ファイルのフォームを変更します。既存のフォームにフィールドを追加または削除したり、フィールドの制限を取得・設定したりできます。
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF フォームフィールドの管理とカスタマイズ
Abstract: この例集は、Aspose.PDF for Python via .NET を使用した PDF フォームフィールドの管理およびカスタマイズに関するさまざまな手法を示しています。TextFragmentAbsorber を使用してタイプライタ形式のフォームフィールドからテキストをクリアする方法、FormEditor で文字数制限を設定および取得する方法、テキストボックスフィールドにカスタムフォントとスタイルを適用する方法、名前で特定のフォームフィールドを削除する方法が含まれます。これらの操作により、開発者は PDF フォームをサニタイズ、フォーマット、カスタマイズして、再配布、ブランディング、データ検証などの目的に合わせることができ、自動化された文書ワークフローにおける美的・機能的な洗練をサポートします。
---

## フォーム内のテキストをクリア

この例では、Aspose.PDF for Python via .NET を使用して PDF のタイプライタ形式フォームフィールドからテキストをクリアする方法を示します。PDF の最初のページをスキャンし、タイプライタフォームを特定してその内容を削除し、更新されたドキュメントを保存します。この手法は、PDF を再配布する前にフォームフィールドをリセットまたはサニタイズするのに有用です。

1. 入力 PDF ドキュメントを読み込む。
1. 最初のページのフォームにアクセスする。
1. 各フォームを反復処理し、それが `Typewriter` フォームかどうかを確認する。
1. TextFragmentAbsorber を使用してフォーム内のテキストフラグメントを検索する。
1. 各フラグメントのテキストをクリアする。
1. 変更された PDF を出力ファイルに保存する。

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## フィールド制限の取得または設定

FormEditor クラスの set_field_limit(field, limit) メソッドを使用すると、フィールドに入力できる最大文字数であるフィールド制限を設定できます。

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

同様に、Aspose.PDF にはフィールド制限を取得するメソッドがあります。

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## フォームフィールドにカスタムフォントを設定

Adobe PDF ファイルのフォームフィールドは、特定のデフォルトフォントを使用するよう設定できます。Aspose.PDF の初期バージョンでは、14 のデフォルトフォントのみがサポートされていました。その後のリリースでは、開発者が任意のフォントを適用できるようになりました。

このコードは、カスタムフォント、サイズ、カラーを設定して PDF フォームのテキストボックスフィールドの外観を更新し、Aspose.PDF for Python via .NET を使用して変更されたドキュメントを保存します。

以下のコードスニペットは、PDF フォームフィールドのデフォルトフォントを設定する方法を示しています。

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## 既存フォームのフィールドを削除

このコードは、PDF ドキュメントから特定のフォームフィールド（名前で指定）を削除し、Aspose.PDF for Python via .NET を使用して更新されたファイルを保存します。

1. PDF ドキュメントを読み込む。
1. 名前でフォームフィールドを削除する。
1. 更新された PDF を保存する。

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```


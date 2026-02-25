---
title: AcroForm を作成 - Python で入力可能な PDF を作成
linktitle: AcroForm を作成
type: docs
weight: 10
url: /ja/python-net/create-form/
description: Aspose.PDF for Python を使用すると、PDF ファイル内に最初からフォームを作成できます
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF で AcroForm を作成する方法
Abstract: この記事では、Aspose.PDF for Python ライブラリを使用して PDF ドキュメントにフォームフィールドを作成する方法について解説します。`Document` クラスを紹介し、フォームフィールドの管理に使用できる `Form` コレクションが含まれています。フォームフィールドを追加する手順は、目的のフィールドを作成し、`Form` コレクションの `add` メソッドを使用することです。具体例として、`TextBoxField` を PDF ドキュメントに追加する方法を示します。例では、`TextBoxField` の作成、位置、名前、値、枠線、色などのプロパティ設定、そしてドキュメントへの追加を詳細なコードで示しています。変更された PDF は、新しく追加されたフォームフィールドとともに保存されます。
---

## 最初からフォームを作成

### PDF ドキュメントにフォームフィールドを追加

この [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスは、PDF ドキュメントのフォームフィールドを管理するのに役立つ [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) というコレクションを提供します。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
1. Form コレクションの [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) メソッドを呼び出します。

### TextBoxField の追加

以下の例は、[TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) を追加する方法を示しています。

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```



---
title: 创建 AcroForm - 使用 Python 创建可填写的 PDF
linktitle: 创建 AcroForm
type: docs
weight: 10
url: /zh/python-net/create-form/
description: 使用 Aspose.PDF for Python，您可以在 PDF 文件中从头创建表单
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中创建 AcroForm
Abstract: 本文提供了使用 Aspose.PDF for Python 库在 PDF 文档中创建表单字段的指南。它介绍了 `Document` 类，其中包含用于管理表单字段的 `Form` 集合。添加表单字段的过程包括创建所需字段并利用 `Form` 集合的 `add` 方法。文中提供了一个具体示例，演示如何向 PDF 文档添加 `TextBoxField`。示例包含详细代码，展示了创建 `TextBoxField`、设置其位置、名称、值、边框和颜色等属性，并随后将其添加到文档中。修改后的 PDF 随后保存，包含新添加的表单字段。
---

## 从头创建表单

### 在 PDF 文档中添加表单字段

[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类提供一个名为 [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) 的集合，帮助您管理 PDF 文档中的表单字段。

要添加表单字段：

1. 创建您想要添加的表单字段。
1. 调用 Form 集合的 [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) 方法。

### 添加 TextBoxField

下面的示例展示了如何添加 [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/)。

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



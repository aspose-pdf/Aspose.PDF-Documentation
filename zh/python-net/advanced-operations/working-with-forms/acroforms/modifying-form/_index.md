---
title: 修改 AcroForm
linktitle: 修改 AcroForm
type: docs
weight: 45
url: /zh/python-net/modifying-form/
description: 使用 Aspose.PDF for Python via .NET 库修改 PDF 文件中的表单。您可以在现有表单中添加或删除字段，获取和设置字段限制等。
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 管理和自定义 PDF 表单字段
Abstract: 本示例集展示了使用 Aspose.PDF for Python via .NET 管理和自定义 PDF 表单字段的各种技术。它包括使用 TextFragmentAbsorber 清除打字机样式表单字段文本、使用 FormEditor 设置和获取字符限制、为文本框字段应用自定义字体和样式以及按名称删除特定表单字段的方法。这些操作使开发人员能够对 PDF 表单进行清理、格式化和定制，以便重新分发、品牌化或数据验证，并在自动化文档工作流中支持外观和功能的优化。
---

## 清除表单中的文本

本示例演示了如何使用 Aspose.PDF for Python via .NET 清除 PDF 中打字机表单字段的文本。它扫描 PDF 的第一页，识别打字机表单，删除其内容，并保存更新后的文档。此方法在重新分发 PDF 前重置或清理表单字段时非常有用。

1. 加载输入 PDF 文档。
1. 访问第一页上的表单。
1. 遍历每个表单并检查它是否为 `Typewriter` 表单。
1. 使用 TextFragmentAbsorber 在表单中查找文本片段。
1. 清除每个片段的文本。
1. 将修改后的 PDF 保存到输出文件。

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

## 获取或设置字段限制

FormEditor 类的 set_field_limit(field, limit) 方法允许您设置字段限制，即字段中可输入的最大字符数。

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

类似地，Aspose.PDF 也提供了获取字段限制的方法。

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

## 为表单字段设置自定义字体

Adobe PDF 文件中的表单字段可以配置为使用特定的默认字体。在早期版本的 Aspose.PDF 中，仅支持 14 种默认字体。后续版本允许开发人员使用任意字体。

此代码通过设置自定义字体、大小和颜色来更新 PDF 表单中文本框字段的外观，然后使用 Aspose.PDF for Python via .NET 保存修改后的文档。

下面的代码片段展示了如何为 PDF 表单字段设置默认字体。

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

## 删除现有表单中的字段

此代码根据名称从 PDF 文档中删除特定表单字段，并使用 Aspose.PDF for Python via .NET 保存更新后的文件。

1. 加载 PDF 文档。
1. 按名称删除表单字段。
1. 保存更新后的 PDF。

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


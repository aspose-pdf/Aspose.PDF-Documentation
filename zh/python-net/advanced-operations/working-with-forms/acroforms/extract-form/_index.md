---
title: 提取 AcroForm - 使用 Python 提取 PDF 表单数据
linktitle: 提取 AcroForm
type: docs
weight: 30
url: /zh/python-net/extract-form/
description: 使用 Aspose.PDF for Python 库从 PDF 文档中提取表单。获取 PDF 文件中单个字段的值。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 获取 PDF 表单数据
Abstract: 本文提供了使用 Python 从 PDF 文档中的表单字段提取数据的指南。它描述了如何使用 Aspose.PDF 库遍历所有字段，具体通过访问 `Form` 集合并利用 `Field` 类型及其 `value` 属性。文中还包含一个示例 Python 代码片段，演示如何打开 PDF 文档、遍历其表单字段并打印每个字段的名称和值。此方法可用于以编程方式从 PDF 文件中检索表单数据。
---

## 提取表单数据

### 获取 PDF 文档中所有字段的值

要获取 PDF 文档中所有字段的值，您需要遍历所有表单字段，然后使用 Value 属性获取值。从 Form 集合中获取每个字段，该基字段类型称为 [字段](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/)，并访问其 [值](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties) 属性。

以下 Python 代码片段演示了如何获取 PDF 文档中所有字段的值。

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


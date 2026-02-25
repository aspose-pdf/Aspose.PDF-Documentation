---
title: 填充 AcroForm - 使用 Python 填写 PDF 表单
linktitle: 填充 AcroForm
type: docs
weight: 20
url: /zh/python-net/fill-form/
description: 您可以使用 Aspose.PDF for Python 库在 PDF 文档中填写表单。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中填写表单字段
Abstract: 本文提供了使用 Aspose.PDF for Python 库在 PDF 文档中填写表单字段的指南。它解释了如何从文档的表单集合中访问表单字段并通过字段的 value 属性设置其值。示例代码演示了如何打开 PDF 文档，遍历其表单字段以通过部分名称（此处为“Field 1”）找到特定字段，并将 TextBoxField 的值修改为“777”。最后，将更新后的文档保存到输出文件。文中提供了相关 Aspose 文档的链接，以供进一步参考。
---

## 在 PDF 文档中填写表单字段

下面的示例使用 Aspose.PDF for Python via .NET 填充 PDF 表单字段的新值并保存更新后的文档。通过指定字段名称和值的字典，支持一次更新多个字段。

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




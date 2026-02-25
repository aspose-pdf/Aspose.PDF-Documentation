---
title: 使用 XFA 表单
linktitle: XFA 表单
type: docs
weight: 20
url: /zh/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API 使您能够在 PDF 文档中处理 XFA 和 XFA Acroform 字段。
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 将 XFA 转换为 Acroform

{{% alert color="primary" %}}

在线尝试
您可以通过以下链接在线检查 Aspose.PDF 转换的质量并查看结果: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

下面的代码片段演示如何将动态 XFA（XML 表单结构）表单转换为标准 AcroForm。

**关键步骤包括：**

1. 加载输入 PDF 文档。
1. 将表单类型更改为 STANDARD。
1. 将转换后的 PDF 保存为新文件。

此转换可实现更好的兼容性，并在不同的 PDF 阅读器和应用程序之间保持表单处理的一致性。

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## 使用 IgnoreNeedsRendering

本示例演示如何使用 Aspose.PDF for Python 将动态 XFA 表单转换为标准 AcroForm。代码检查输入的 PDF 是否包含 XFA 表单，并在必要时覆盖渲染。随后将表单类型设置为 STANDARD 并保存更新后的 PDF。

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```


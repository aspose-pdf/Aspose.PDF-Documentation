---
title: 在 Python 中删除 PDF 表单
linktitle: 删除表单
type: docs
weight: 70
url: /zh/python-net/remove-form/
description: 使用 Aspose.PDF for Python via .NET 库根据子类型/表单删除文本。删除 PDF 中的所有表单。
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python via .NET 从 PDF 中删除表单
Abstract: 本文档介绍了使用 Aspose.PDF for Python via .NET 删除 PDF 文件中表单元素的两种基于 Python 的方法。第一种方法演示了通过访问页面的资源字典并对表单集合调用 clear() 方法，清除特定页面的所有表单对象。第二种方法通过遍历表单注释，识别打字机样式的表单，并根据其属性有选择地删除它们，提供了更有针对性的解决方案。两种技术均通过将更新后的 PDF 保存到指定的输出路径结束，为自动化工作流中的表单清理和文档优化提供了灵活的选项。
---

## 删除 PDF 中的所有表单

此代码从 PDF 文档的第一页中删除所有表单元素，然后将修改后的文档保存到指定的输出路径。

1. 加载 PDF 文档。
1. 访问页面资源。
1. 清除表单对象。
1. 保存更新后的文档。

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

## 删除指定表单

下一个示例遍历给定 PDF 页面上的表单对象，识别打字机表单注释，删除它们，然后使用 Aspose.PDF for Python via .NET 保存更新后的 PDF。

1. 加载 PDF 文档。
1. 访问页面表单。
1. 迭代遍历表单。
1. 检查打字机表单。
1. 删除匹配的表单。
1. 保存更新后的文档。

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

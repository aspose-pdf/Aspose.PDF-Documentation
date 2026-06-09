---
title: 在 Python 中删除 PDF 表单
linktitle: 删除表单
type: docs
weight: 70
url: /zh/python-net/remove-form/
description: 使用 Aspose.PDF for Python via .NET 从 PDF 页面中移除表单对象，包括完整清理和有针对性的删除。
lastmod: "2026-06-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Python via .NET 从 PDF 中移除表单
Abstract: 本文介绍了两种使用 Aspose.PDF for Python via .NET 从 PDF 文档中移除表单元素的方法。第一种方法清除选定页面上的所有表单对象，而第二种方法仅移除匹配的 Typewriter 表单资源。这些示例有助于表单清理、模板准备以及文档标准化工作流程。
---

## 从页面中移除所有表单

此代码会从指定的页面中删除所有表单对象 `page_num` 并保存更新后的文档。

1. 加载 PDF 文档。
1. 访问页面资源。
1. 清除表单对象。
1. 保存更新后的文档。

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## 移除特定的表单类型

下面的示例遍历给定 PDF 页面上的表单对象，识别打字机表单注释，删除它们，然后使用 Aspose.PDF for Python via .NET 保存更新后的 PDF。

1. 加载 PDF 文档。
1. 访问页面表单。
1. 遍历表单。
1. 检查是否有打字机表单。
1. 删除匹配的表单。
1. 保存更新后的文档。

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## 相关主题

- [创建 AcroForm](/pdf/zh/python-net/create-form/)
- [填写 AcroForm](/pdf/zh/python-net/fill-form/)
- [修改 AcroForm](/pdf/zh/python-net/modifying-form/)
- [发布表单](/pdf/zh/python-net/posting-form/)

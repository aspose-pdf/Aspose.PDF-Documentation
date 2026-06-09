---
title: 通过 Python 在 PDF 中发布表单
linktitle: 发布表单
type: docs
weight: 75
url: /zh/python-net/posting-form/
description: 使用 Aspose.PDF for Python via .NET 向 PDF AcroForms 添加提交按钮和提交操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加提交按钮和表单提交操作
Abstract: 本文展示了两种通过 Aspose.PDF for Python via .NET 为 PDF 表单添加提交功能的方法。您可以通过 FormEditor 添加现成的提交按钮，或使用 SubmitFormAction 创建自定义按钮字段以实现高级控制。这些模式有助于将 PDF 表单与服务器端表单处理端点集成。
---

## 使用 FormEditor 添加提交按钮

以下代码片段演示了如何使用 Aspose.PDF for Python via .NET 中的 FormEditor 类向 PDF 表单添加提交按钮。该按钮被配置为在点击时将表单数据提交到指定的 URL。

1. 创建一个 `FormEditor` 对象。
1. 向目标页面添加提交按钮。
1. 设置提交 URL 和按钮坐标。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## 添加自定义提交操作

以下代码片段说明了如何使用 Aspose.PDF for Python via .NET 在 PDF 表单中创建自定义提交按钮。该按钮被配置为在点击时将表单数据发送到指定的 URL。

1. 使用 ap.Document() 打开 PDF。
1. 创建提交操作。
1. 设置目标 URL 和提交标志。
1. 创建按钮字段并绑定其点击操作。
1. 将按钮添加到表单中。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## 相关主题

- [创建 AcroForm](/pdf/zh/python-net/create-form/)
- [填写 AcroForm](/pdf/zh/python-net/fill-form/)
- [修改 AcroForm](/pdf/zh/python-net/modifying-form/)
- [导入和导出表单数据](/pdf/zh/python-net/import-export-form-data/)
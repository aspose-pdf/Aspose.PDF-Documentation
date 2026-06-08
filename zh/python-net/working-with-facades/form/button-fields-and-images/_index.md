---
title: 按钮字段和图像
type: docs
weight: 40
url: /zh/python-net/button-fields-and-images/
description: 本示例演示如何使用 Aspose.PDF Facades API 在 PDF 表单中管理按钮字段。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 向按钮字段添加图像外观并读取提交标志
Abstract: PDF 表单通常包含交互式按钮，这些按钮要么触发 JavaScript 动作，要么提交表单数据。您可以通过添加图像作为外观来在视觉上增强按钮字段，并通过编程方式检查其提交行为。
---

## 向按钮字段添加图像外观

此代码片段说明了如何在 PDF 表单中的现有按钮字段上添加图像外观。此操作通过将默认外观替换为自定义图像来提升 PDF 按钮的视觉呈现效果。

1. 创建一个 Form 对象。
1. 将 PDF 文件绑定到 Form 对象。
1. 向 Button Field 添加 Image。

    - 确定与 PDF 关联的图像文件的路径
    - 以二进制模式打开图像，作为 image_stream。
    - 使用完整限定的 button field 名称调用 fill_image_field()。

1. 保存已更新的 PDF。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## 获取提交标志

Python 库帮助您使用 Aspose.PDF Facades API 检索 PDF 表单中提交按钮的提交标志。提交标志定义了提交按钮的行为，例如它是发送整个表单、包含注释，还是以 FDF、XFDF、PDF 或 HTML 格式提交。

1. 创建一个 Form 对象。
1. 在表单对象上调用 get_submit_flags()，并使用完全限定的提交按钮名称。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```

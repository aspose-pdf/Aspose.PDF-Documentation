---
title: 获取富文本值
type: docs
weight: 40
url: /zh/python-net/get-rich-text-values/
description: 本节介绍如何使用 Aspose.PDF Facades API 检索 PDF 文档中表单字段的富文本内容。与普通文本字段不同，富文本字段可以包含诸如粗体文字、不同字体、颜色以及段落样式等格式化内容。
lastmod: "2026-06-08"
---

PDF 表单可能包含支持富文本格式的文本字段。这些字段除了普通文本值外，还可以存储具有样式属性的内容。

1. 创建 Form 对象。
1. 绑定 PDF 文档。
1. 检索富文本值。

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")
```

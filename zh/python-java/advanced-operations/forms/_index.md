---
title: 使用 Python 处理表单
linktitle: PDF 文档中的表单
type: docs
weight: 60
url: /zh/python-java/forms/
lastmod: "2023-05-19"
description: 本节包含有关使用 Python API 处理 PDF 文档中的表单的文章。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

表单是包含用户选择或填写信息区域的文件，目的是收集和存储信息。

AcroForms 是包含表单字段的 PDF 文件。最终用户或表单的作者可以（手动或通过自动化过程）在这些字段中输入数据。在内部，AcroForms 是应用于 PDF 文档的注释或字段。

本节描述了一种通过 Aspose.PDF 以编程方式完成 PDF 文档的快速简单的方法。本节还讨论了如何使用 Aspose.PDF for Java 来发现和映射现有 PDF 中 AcroForms 的可用字段。

**我们的 Aspose.PDF for Python via Java** 库允许您成功、快速且轻松地处理 PDF 文档中的表单。

- **AcroForms** - 创建表单、填写表单字段、从表单中提取数据、使用 Java 库修改 PDF 中的字段。
- **XFA Forms** - 填写 XFA 字段、转换 XFA、获取 XFA 字段属性。

## 以下功能可用：

- 导出/导入 fdf
- 导出/导入 xfdf
- 导出/导入 xml
- 导出/设置 XfaData
- 填写字段
- 扁平化字段
- 确定有效的单选按钮值
- 获取字段名称、标志、类型、值
- 重命名字段

```python

from asposepdf import Api, Forms


# 初始化许可证
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# 填写字段示例

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```
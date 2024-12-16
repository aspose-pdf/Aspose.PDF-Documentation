---
title: 创建 PDF 文档
linktitle: 创建 PDF
type: docs
weight: 10
url: /zh/python-cpp/create-document/
description: 本页面描述如何使用 Aspose.PDF for Python 通过 C++ 库从头创建 PDF 文档。
---

对于开发人员来说，存在许多需要以编程方式生成 PDF 文件的场景。在您的软件中，您可能需要以编程方式生成 PDF 报告和其他 PDF 文件。从头编写自己的代码和函数相当冗长且效率低下。使用 Python 创建 PDF 文件，有一个更好的解决方案 - **Aspose.PDF for Python via C++**。

## 使用 Python 创建 PDF 文件

要使用 Python 创建 PDF 文件，可以使用以下步骤。

* 从 Aspose.PDF for Python via C++ 库导入所有类和方法。
* 使用 [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/) 创建一个代表空 PDF 文档的新 Document 对象。

* 获取包含文档中所有页面的 [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) 对象。
* 向页面集合的末尾添加一个新页面 [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) 并返回表示已添加页面的 Page 对象。
* 将文档保存到当前工作目录中指定名称的文件。
* 关闭文档的句柄并释放与其关联的任何资源。

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## 基于 DOM 创建 PDF 文件

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```
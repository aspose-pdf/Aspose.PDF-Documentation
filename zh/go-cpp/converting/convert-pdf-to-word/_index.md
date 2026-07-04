---
title: 在 Go 中将 PDF 转换为 Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: 了解如何编写 Go 代码将 PDF 转换为 DOC（DOCX）。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Go 将 PDF 转换为 Word 的工具
Abstract: 通过 C++ 的 Aspose.PDF for Go 实现 PDF 文档到 DOC 格式的无缝转换，同时保留原始文本、图像、表格以及整体文档结构。此功能使开发人员能够将静态 PDF 转换为可编辑的 Word 文件，以便进一步修改和处理。该库提供多种自定义选项来控制转换输出，确保高保真度和准确性。文档中包含详细的说明和示例代码，帮助开发者在其应用程序中高效实现 PDF-to-DOC 转换。
SoftwareApplication: go-cpp
---

在 Microsoft Word 或其他支持 DOC 和 DOCX 格式的文字处理软件中编辑 PDF 文件的内容。PDF 文件是可编辑的，但 DOC 和 DOCX 文件更灵活且可自定义。

## 将 PDF 转换为 DOC

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 DOC：

1. 打开 PDF 文档。
1. 使用 将 PDF 文件转换为 DOC [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Go 为您呈现在线免费应用 ["PDF 转 DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，在此您可以尝试调查其功能和质量的工作方式。

[![将 PDF 转换为 DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Go API 让您能够读取并将 PDF 文档转换为 DOCX。DOCX 是一种广为人知的 Microsoft Word 文档格式，其结构已从纯二进制更改为 XML 与二进制文件的组合。Docx 文件可以在 Word 2007 及其后续版本中打开，但不能在早期支持 DOC 文件扩展名的 MS Word 版本中打开。

提供的 Go 代码片段演示了如何使用 Aspose.PDF 库将 PDF 文档转换为 DOCX：

1. 打开 PDF 文档。
1. 使用以下方法将 PDF 文件转换为 DOCX [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) 函数。
1. 关闭 PDF 文档并释放任何已分配的资源。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Go 为您呈现在线免费应用 ["PDF 转 Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，在此您可以尝试调查其功能和质量的工作方式。

[![Aspose.PDF 转换 PDF 为 Word 免费应用](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
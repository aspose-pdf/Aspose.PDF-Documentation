---
title: Aspose PDF 许可证
linktitle: 许可与限制
type: docs
weight: 90
url: /zh/go-cpp/licensing/
description: Aspose.PDF for Go 邀请其客户获取 Classic License，同时使用受限许可证以更好地探索产品。
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 C++ 使用 Aspose.PDF for Go 的许可
Abstract: 通过 C++ 使用 Aspose.PDF for Go 的许可页面说明了该产品可用的许可选项。客户可以在 Classic License、Metered License 或用于评估目的的受限许可证之间进行选择。该页面还强调了获取正式许可证的好处，例如解锁全部功能并消除评估限制。
SoftwareApplication: go-cpp
---


## 评估版本的限制

我们希望客户在购买前对我们的组件进行彻底测试，因此评估版允许您像平常一样使用它。

- **带有评估水印的文档。** Aspose.PDF for Go 的评估版提供完整的产品功能，但生成文件的所有页面顶部都带有文字 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." 的水印。

- **限制可处理的页数。**
在评估版中，您只能处理文档的前四页。

>如果您希望在不受评估版限制的情况下测试 Aspose.PDF for Go，您也可以请求 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

使用许可证文件 (Aspose.PDF.GoViaCPP.lic) 为 Aspose.PDF 库启用完整功能的许可。

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```

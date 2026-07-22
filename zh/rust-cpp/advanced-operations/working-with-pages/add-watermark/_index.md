---
title: 使用 Rust 向 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 80
url: /zh/rust-cpp/add-watermarks/
description: 此示例演示了如何使用 Aspose.PDF for Rust via C++ 向 PDF 文档添加可自定义的文本水印。
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 添加文本水印
Abstract: Aspose.PDF for Rust via C++ 提供了一种灵活的方式来向 PDF 文档添加文本水印。此示例演示了如何通过指定文本内容、字体、大小、颜色、位置、旋转角度、层叠行为和透明度来插入可自定义的水印。水印通常用于品牌标识、机密标签、草稿标记或文档保护。
SoftwareApplication: rust-cpp
---

该 [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) 此方法允许开发者以编程方式将文字水印应用于现有的 PDF 文档。水印可完全自定义，包括：

- 水印文本
- 字体系列
- 字体大小
- 文本颜色（十六进制格式）
- X 和 Y 位置坐标
- 旋转角度
- 前景或背景放置
- 不透明度（透明级别）

在本例中，应用程序打开一个已有的 PDF 文件，应用半透明的旋转水印，并以新文件名保存修改后的文档。

此功能特别适用于将文档标记为草稿、机密、样本，或在分发前添加品牌元素。

1. 打开现有的 PDF 文档。
1. 调用 add_watermark 方法并配置水印属性。
1. 保存更新后的文档。

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```
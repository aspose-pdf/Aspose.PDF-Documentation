---
title: 从 PDF 中提取图像 
linktitle: 从 PDF 中提取图像
type: docs
weight: 20
url: /zh/cpp/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for C++ 从 PDF 中提取图像的一部分。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

在处理 PDF 文档时，提取 PDF 文件中的图像也是一项需求。例如，你收到了一封包含大量精美图像的 PDF 邮件，你希望将这些图像提取为单独的文件。

Aspose.PDF 库允许你使用以下代码片段从 PDF 中提取图像：

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extract a particular image
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Save output image
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```
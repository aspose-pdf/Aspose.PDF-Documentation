---
title: 将PDF/A转换为PDF格式 
linktitle: 将PDF/A转换为PDF格式
type: docs
weight: 110
url: /zh/cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF的C++库将PDF/A文件转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF/A文档转换为PDF

将PDF/A文档转换为PDF意味着从原始文档中移除<abbr title="Portable Document Format Archive">PDF/A</abbr>限制。[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类具有方法'RemovePdfaCompliance'，用于从输入/源文件中移除PDF合规信息。之后[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入文件。

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Remove PDF/A compliance information
    document->RemovePdfaCompliance();

    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

该信息还会在您对文档进行任何更改时删除（例如，添加页面）。在以下示例中，添加页面后输出文档失去了PDF/A合规性。

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Adding a new (empty) page removes PDF/A compliance information.

    document->get_Pages()->Add();
    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```
---
title: 在 PDF 中添加 PDF 页面印章
linktitle: PDF 文件中的页面印章
type: docs
weight: 30
url: /zh/cpp/page-stamps-in-the-pdf-file/
description: 使用 PdfPageStamp 类通过 C++ 向 PDF 文件添加页面印章。
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用 C++ 添加页面印章

当您需要应用包含图形、文本、表格的复合印章时，可以使用 [PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp)。以下示例展示了如何使用印章创建类似于使用 Adobe InDesign、Illustrator、Microsoft Word 的信头。假设我们有一些输入文档，并且我们想要应用两种颜色为蓝色和李子的边框。

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```
---
title: 使用C++旋转PDF页面
linktitle: 旋转PDF页面
type: docs
weight: 50
url: /zh/cpp/rotate-pages/
description: 本主题描述了如何使用C++以编程方式旋转现有PDF文件中的页面方向。
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

本主题描述了如何使用C++以编程方式更新或更改现有PDF文件中页面的方向。

## 更改页面方向

Aspose.PDF for C++允许您在横向和纵向之间更改页面方向。要更改页面方向，请使用以下代码片段设置页面的MediaBox。您还可以通过使用Rotate()方法设置旋转角度来更改页面方向。

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // 我们必须将页面向上移动以补偿页面大小的变化
        // （页面的下边缘是0,0，信息通常从页面的顶部放置。
        // 这就是为什么我们将下边缘向上移动旧高度和新高度之间的差异。

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // 有时我们还需要设置CropBox（如果它在原始文件中已设置）
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // 设置页面的旋转角度
        page->set_Rotate(Rotation::on90);
    }

    // 保存输出文件
    document->Save(_dataDir + outputFileName);
}
```

## 将页面内容调整为新的页面方向

请注意，使用上述代码片段时，文档的一些内容可能会被切掉，因为页面高度减少。为避免这种情况，请按比例增加宽度，并保持高度不变。计算示例如下：

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // 新高度相同
        double newHeight = r->get_Height();
        // 新宽度按比例扩展以使方向为横向
        // （我们假设先前的方向是纵向）
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

除了上述方法，还可以考虑使用 PdfPageEditor 外观界面，它可以对页面内容进行缩放。

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // 获取PDF第一页的矩形区域
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // 实例化PdfPageEditor实例
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // 绑定源PDF
    ppe->BindPdf(_dataDir + inputFileName);
    // 设置缩放系数
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // 更新页面大小
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // 保存输出文件
    document->Save(_dataDir + outputFileName);
}
```
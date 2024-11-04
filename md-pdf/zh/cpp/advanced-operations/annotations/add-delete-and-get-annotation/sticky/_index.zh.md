---
title: PDF 粘性注释使用 C++
linktitle: 粘性注释
type: docs
weight: 50
url: /cpp/sticky-annotations/
description: 本主题关于粘性注释，作为示例，我们展示了文本中的水印注释。它用于在页面上表示图形。检查代码片段以解决此任务。
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 添加水印注释

水印注释应用于表示图形，无论打印页面的尺寸如何，其均应以固定大小和位置打印在页面上。

您可以在 PDF 页面上的特定位置使用 [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) 添加水印文本。水印的不透明度也可以通过使用不透明属性进行控制。

请检查以下代码片段以添加 WatermarkAnnotation。

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 创建注释
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    // 将注释添加到页面的注释集合中
    page->get_Annotations()->Add(wa);

    // 创建用于字体设置的 TextState
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    // 设置注释文本的不透明度级别
    wa->set_Opacity(0.5);

    // 向注释添加文本
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    // 保存文档
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## 获取水印注释

请尝试使用以下代码片段从 PDF 文档中获取水印注释。

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 使用 AnnotationSelector 筛选注释
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 打印结果
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## 删除水印注释

请尝试使用以下代码片段从 PDF 文档中删除水印注释。

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // 加载 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // 使用 AnnotationSelector 筛选注释
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // 删除注释
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```
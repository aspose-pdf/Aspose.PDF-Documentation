---
title: Convert PDF to Microsoft PowerPoint in C++
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF允许您使用C++将PDF转换为PowerPoint格式。可以将PDF转换为PPTX，并将幻灯片作为图像。
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

本文解释了如何**使用C++将PDF转换为PowerPoint格式**。它涵盖了以下主题。

_格式_: **PPTX**
- [C++ PDF到PPTX](#cpp-pdf-to-pptx)
- [C++转换PDF到PPTX](#cpp-pdf-to-pptx)
- [C++如何将PDF文件转换为PPTX](#cpp-pdf-to-pptx)

_格式_: **Microsoft PowerPoint PPTX格式**
- [C++ PDF到PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++转换PDF到PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++如何将PDF文件转换为PowerPoint](#cpp-pdf-to-powerpoint-pptx)

本文涵盖的其他主题。
- [另见](#see-also)

## C++ PDF到PowerPoint转换

**Aspose.PDF for C++**允许您跟踪PDF到PPTX转换的进度。

在PDF到<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>转换过程中，文本被渲染为可选择/更新的文本。请注意，为了将PDF文件转换为PPTX格式，Aspose.PDF提供了一个名为[`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options)的类。PptxSaveOptions类的对象作为第二个参数传递给[`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)方法。以下代码片段展示了将PDF文件转换为PPTX格式的过程。

## 使用Aspose.PDF for C++进行简单的PDF到PPTX转换

为了将PDF转换为PPTX，Aspose.PDF for C++建议使用以下代码步骤。

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>步骤：在C++中将PDF转换为PPTX</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>步骤：在C++中将PDF转换为PowerPoint PPTX格式</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 类的实例。
2. 创建一个 [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 类的实例。
3. 使用 **Document** 对象的 **Save** 方法 _将 PDF 保存为 PPTX_。

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名称的字符串
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 以 PPTX 格式保存输出
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 将 PDF 转换为 PPTX 并将幻灯片作为图像

如果您需要将可搜索的 PDF 转换为以图像而非可选文本形式的 PPTX，Aspose.PDF 提供了通过 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 类实现的功能。 要实现这一点，将 [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 类的属性 [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) 设置为 'true'，如下代码示例所示。

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名称字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名字符串
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // 以PPTX格式保存输出
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PPTX 转换的进度详情

Aspose.PDF for C++ 允许您跟踪 PDF 到 PPTX 转换的进度。 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 类提供了 [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) 属性，可以指定为自定义方法，用于跟踪转换进度，如以下代码示例所示。

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 路径名字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 文件名字符串
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //指定自定义进度处理程序
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // 以 PPTX 格式保存输出
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
以下是用于显示进度转换的自定义方法。

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 转换进度 : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 结果页面的 " << eventInfo->Value << " of " << eventInfo->MaxValue << " 布局已创建." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 结果页面的 " << eventInfo->Value << " of " << eventInfo->MaxValue << " 已导出." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 源页面 " << eventInfo->Value << " of " << eventInfo->MaxValue << " 已分析." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**尝试在线将PDF转换为PowerPoint**

Aspose.PDF for C++ 为您提供免费的在线应用程序 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## 另请参阅

本文还涵盖这些主题。代码与上面相同。

_格式_: **PowerPoint**
- [C++ PDF 转 PowerPoint 代码](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint 编程](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint 库](#cpp-pdf-to-powerpoint-pptx)
- [C++ 将 PDF 保存为 PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ 从 PDF 生成 PowerPoint](#cpp-pdf-to-powerpoint-pptx)
- [C++ 从 PDF 创建 PowerPoint](#cpp-pdf-to-powerpoint-pptx)

- [C++ PDF 转 PowerPoint 转换器](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX 格式**
- [C++ PDF 转 PowerPoint PPTX 代码](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint PPTX API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint PPTX 编程实现](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint PPTX 库](#cpp-pdf-to-powerpoint-pptx)
- [C++ 将 PDF 保存为 PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ 从 PDF 生成 PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ 从 PDF 创建 PowerPoint PPTX](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 转 PowerPoint PPTX 转换器](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF 转 PPTX 代码](#cpp-pdf-to-pptx)
- [C++ PDF 转 PPTX API](#cpp-pdf-to-pptx)
- [C++ PDF 转 PPTX 编程实现](#cpp-pdf-to-pptx)
- [C++ PDF 转 PPTX 库](#cpp-pdf-to-pptx)
- [C++ 将 PDF 保存为 PPTX](#cpp-pdf-to-pptx)
- [C++ 从 PDF 生成 PPTX](#cpp-pdf-to-pptx)
- [C++ 从 PDF 创建 PPTX](#cpp-pdf-to-pptx)
- [C++ PDF 转 PPTX 转换器](#cpp-pdf-to-pptx)
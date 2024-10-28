---
title: Optimize PDF using C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /cpp/optimize-pdf/
description: 优化PDF文件，缩小所有图像，减少PDF大小，取消嵌入字体，启用重用页面内容，删除或平面化注释与C++。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

首先，您所做的任何PDF优化都是为了用户。在PDF中，用户优化主要是通过减少PDF的大小来提高其加载速度。这是最受欢迎的任务。  
我们可以使用几种技术来优化PDF，但最基本的是：

- 为在线浏览优化页面内容
- 缩小或压缩所有图像
- 启用重用页面内容
- 合并重复的流
- 取消嵌入字体
- 删除未使用的对象
- 删除平面化表单字段
- 删除或平面化注释

## 为网络优化PDF文档

当您面临优化PDF文档内容以在搜索引擎中获得更好排名的任务时，Aspose.PDF for C++提供了解决方案。

1. 在一个 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象中打开输入文档。
1. 使用 [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda) 方法。
1. 使用 Save 方法保存优化后的文档。

以下代码片段展示了如何为网络优化 PDF 文档。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//为网络优化 PDF 文档
void OptimizeForWeb() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String outfilename("OptimizeDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>();

    // 进行一些操作（添加页面、图像等）
    // ...

    // 为网络优化
    document->Optimize();

    // 保存输出文档
    document->Save(_dataDir + outfilename);
}
```

## 减少 PDF 大小

[OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) 方法允许您通过清除不必要的信息来减少文档大小。 默认情况下，此方法的工作原理如下：

- 未在文档页面上使用的资源将被移除
- 相同的资源将合并为一个对象
- 未使用的对象将被删除

下面的代码片段是一个示例。但请注意，此方法不能保证文档缩小。

```cpp
void ReduceSizePDF() {

    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String outfilename("ShrinkDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>();
    // 进行一些操作（添加页面、图像等）
    // ...

    // 优化PDF文档。但请注意，此方法不能保证文档缩小
    document->OptimizeResources();

    // 保存输出文档
    document->Save(_dataDir + outfilename);
}
```

## 优化策略管理

我们还可以自定义优化策略。 目前，[OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) 方法使用了5种技术。这些技术可以通过使用 [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/) 参数的 OptimizeResources() 方法来应用。

### 缩小或压缩所有图像

要优化 PDF 文档中的图像，我们将使用 [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization)。
为了解决图像优化问题，我们有以下选项：降低图像质量和/或更改其分辨率。 在任何情况下，都应该应用[ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/)。在下面的例子中，我们通过将[ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e)减少到50来缩小图像。

```cpp
void CompressImage() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名称的字符串
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置CompressImages选项
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // 设置ImageQuality选项
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // 使用OptimizationOptions优化PDF文档
    document->OptimizeResources(optimizationOptions); 
    // 保存更新的文档
    document->Save(_dataDir + outfilename);
}
```
要将图像设置为较低分辨率，请将[ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6)设置为true，并将[MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e)设置为相应的值。

```cpp
void ResizeImagesWithLowerResolution() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置CompressImages选项
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // 设置ImageQuality选项
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // 设置ResizeImage选项
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // 设置MaxResolution选项
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // 使用OptimizationOptions优化PDF文档
    document->OptimizeResources(optimizationOptions);
    // 保存更新后的文档
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF for C++ 还为您提供了对运行时设置的控制。今天，我们可以使用两种算法 - 标准和快速。为了控制执行时间，我们应该设置一个 [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4) 属性。

以下代码片段演示了快速算法：

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化 OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置 CompressImages 选项
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // 设置 ImageQuality 选项
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // 设置 ResizeImage 选项
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // 将图像压缩版本设置为快速
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // 使用 OptimizationOptions 优化 PDF 文档
    document->OptimizeResources(optimizationOptions);
    // 保存更新的文档
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### 删除未使用的对象

有时，您可能需要从PDF文档中删除某些未使用的对象，这些对象在页面上没有被引用。例如，当一个页面从文档页面树中删除，但页面对象本身没有被删除时，就可能发生这种情况。删除这些对象不会使文档无效，而是会缩小文档的大小。请查看以下代码片段：

```cpp
void RemovingUnusedObject() { 
    // 路径名的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置RemoveUsedObject选项
    optimizationOptions->set_RemoveUnusedObjects(true);

    // 使用OptimizationOptions优化PDF文档
    document->OptimizeResources(optimizationOptions);

    // 保存更新后的文档
    document->Save(_dataDir + outfilename); 
}
```

### 删除未使用的流

有时文档包含未使用的资源流。这些流不是“未使用的对象”，因为它们是从页面资源字典中引用的。因此，它们不会通过“删除未使用对象”方法被删除。但这些流从未与页面内容一起使用。当某个图像已从页面中删除但未从页面资源中删除时，可能会发生这种情况。此外，当从文档中提取页面并且文档页面具有“公共”资源（即相同的资源对象）时，这种情况经常发生。分析页面内容以确定资源流是否被使用。未使用的流被删除。这有时会减少文档的大小。使用此技术与上一步类似：

```cpp
void RemovingUnusedStreams() { 
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set RemoveUsedStreams option
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename); 
}
```

### 链接重复的流

一些文档可能包含多个重复的资源流（例如图像）。这种情况可能发生在一个文档与自身连接时。输出文档包含相同资源流的两个独立副本。我们分析所有资源流并进行比较。如果流是重复的，它们将被合并，也就是说，只保留一个副本。引用会被适当地更改，并且对象的副本将被移除。在某些情况下，这有助于减少文档的大小。

```cpp
void LinkingDuplicateStreams() { 
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化优化选项
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置 LinkDuplcateStreams 选项
    optimizationOptions->set_LinkDuplcateStreams(true);

    // 使用优化选项优化 PDF 文档
    document->OptimizeResources(optimizationOptions);

    // 保存更新的文档
    document->Save(_dataDir + outfilename); 
}
```

另外，我们可以使用 [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8) 设置。如果此属性设置为 true，则在优化相同页面的文档时，页面内容将被重用。

```cpp
void AllowReusePageContent() { 
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 初始化 OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // 设置 AllowReusePageContent 选项
    optimizationOptions->set_AllowReusePageContent(true);

    // 使用 OptimizationOptions 优化 PDF 文档
    document->OptimizeResources(optimizationOptions);

    // 保存更新后的文档
    document->Save(_dataDir + outfilename); 
}
```

### 解除字体嵌入

当您创建个人设计文件的 PDF 版本时，所有必要字体的副本会被添加到 PDF 文件本身。这就是嵌入。无论在何处打开此 PDF，无论是在您的计算机上、朋友的计算机上还是在您的打印供应商的计算机上，所有的正确字体都会存在并正确呈现。

但是，如果文档使用了嵌入的字体，这意味着所有字体数据都存储在文档中。优点是无论用户的机器上是否安装了字体，该文档都可以查看。但是嵌入字体会使文档变大。解除嵌入字体的方法会移除所有嵌入的字体。因此，文档的大小会减少，但如果没有安装正确的字体，文档本身可能会变得不可读。

```cpp
void UnembedFonts() {
    // String for path name
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Initialize OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Set AllowReusePageContent option
    optimizationOptions->set_UnembedFonts(true);

    // Optimize PDF document using OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Save updated document
    document->Save(_dataDir + outfilename);
}
```

优化资源将这些方法应用于文档。如果应用了这些方法，文档大小很可能会减小。如果这些方法都没有应用，文档大小将不会改变，这是显而易见的。

## 其他减少 PDF 文档大小的方法

### 删除或扁平化注释

PDF 文档中存在的注释自然会增加其大小。当注释不必要时可以删除。当需要注释但不需要额外编辑时，可以将其扁平化。这两种技术都可以减少文件大小。

```cpp
void FlatteningAnnotation() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名称的字符串
    String infilename("OptimizeDocument.pdf");
    // 输出文件名称的字符串
    String outfilename("OptimizeDocument_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 扁平化注释
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // 保存更新的文档
    document->Save(_dataDir + outfilename);
}
```

### 删除表单字段

从您的 PDF 中删除表单也将优化您的文档。 如果 PDF 文档包含 AcroForms，我们可以通过展平表单字段来尝试减小文件大小。

```cpp
void FlatteningFormFields() {
    // 用于路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("OptimizeFormField.pdf");
    // 输出文件名的字符串
    String outfilename("OptimizeFormField_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 展平表单字段
    // 展平表单
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // 保存更新的文档
    document->Save(_dataDir + outfilename);
}
```

### 将 PDF 从 RGB 颜色空间转换为灰度

PDF 文件包含文本、图像、附件、注释、图形和其他对象。 您可能会遇到需要将 PDF 从 RGB 颜色空间转换为灰度的要求，以便在打印这些 PDF 文件时速度更快。此外，当文件转换为灰度时，文档大小也会减少，但这也可能导致文档质量下降。这个功能目前被 Adobe Acrobat 的预检功能支持，但在谈到 Office 自动化时，Aspose.PDF 是提供此类文档操作便利的终极解决方案。为了实现这个需求，可以使用以下代码片段。

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // 路径名称的字符串
    String _dataDir("C:\\Samples\\");

    // 输入文件名的字符串
    String infilename("OptimizeDocument.pdf");
    // 输出文件名的字符串
    String outfilename("Test-gray_out.pdf");

    // 打开文档
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // 获取 PDF 中特定页面的实例
        auto page = document->get_Pages()->idx_get(idxPage);
        // 将 RGB 颜色空间图像转换为灰度颜色空间
        strategy->Convert(page);
    }
    // 保存结果文件
    document->Save(_dataDir + outfilename); 
}
```
### FlateDecode 压缩

Aspose.PDF for C++ 提供了对 PDF 优化功能的 FlateDecode 压缩支持。
要使用 FlateDecode 压缩优化图像，请将优化选项设置为 Flate。
下面的代码片段演示了如何在优化中使用选项以 **FlateDecode** 压缩存储图像：

```cpp
void FlatDecodeCompression() {
 // 路径名称的字符串
 String _dataDir("C:\\Samples\\");

 // 输入文件名称的字符串
 String infilename("FlateDecodeCompression.pdf");
 // 输出文件名称的字符串
 String outfilename("FlateDecodeCompression_out.pdf");

 // 打开文档
 auto document = MakeObject<Document>(_dataDir + infilename);

 // 初始化 OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // 要使用 FlateDecode 压缩优化图像，请将优化选项设置为 Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // 使用 OptimizationOptions 优化 PDF 文档
 document->OptimizeResources(optimizationOptions);

 // 保存更新的文档
 document->Save(_dataDir + outfilename);
}
```

### **在 XImageCollection 中存储图像**

Aspose.PDF for C++ 提供了将新图像存储到 [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) 中并使用 FlateDecode 压缩的功能。要启用此选项，您可以使用 **ImageFilterType.Flate** 标志。
以下代码片段展示了如何使用此功能：

```cpp
void StoreImageInXImageCollection() {

 // 路径名称的字符串
 String _dataDir("C:\\Samples\\");

 // 输出文件名的字符串
 String outfilename("FlateDecodeCompression_out.pdf");

 // 打开文档
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // 设置坐标
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // 使用 ConcatenateMatrix（连接矩阵）操作符：定义图像如何放置
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```
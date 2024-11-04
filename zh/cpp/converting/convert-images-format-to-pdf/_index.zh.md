---
title: 将各种图像格式转换为PDF
linktitle: 将图像转换为PDF
type: docs
weight: 60
url: /cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: 本主题向您展示如何使用Aspose.PDF for C++库将各种图像格式转换为PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** 允许您将不同格式的图像转换为PDF文件。我们的库展示了将最流行的图像格式（如BMP、DICOM、EMF、JPG、PNG、SVG和TIFF格式）转换的代码片段。

## 将BMP转换为PDF

使用**Aspose.PDF for C++**库将BMP文件转换为PDF文档。

<abbr title="Bitmap Image File">BMP</abbr>图像是具有扩展名的文件。BMP表示位图图像文件，用于存储位图数字图像。这些图像独立于图形适配器，也称为设备独立位图（DIB）文件格式。您可以使用Aspose.PDF for C++ API将BMP转换为PDF文件。 因此，您可以按照以下步骤将 BMP 图像转换为 PDF：

1. 创建一个用于路径名和文件名的[String 类](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个新的 Document 对象实例。
1. 向此[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)添加一个新的[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. 创建一个新的 Aspose.Pdf BMP。
1. 使用输入文件初始化 Aspose.PDF BMP 对象。
1. 将 Aspose.PDF BMP 作为段落添加到页面。
1. 最后，保存输出 PDF 文件

因此，以下代码片段遵循这些步骤，并展示如何使用 C++ 将 BMP 转换为 PDF：

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.bmp");

    // String for input file name
    String outfilename("ImageToPDF-BMP.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将 BMP 转换为 PDF**

Aspose 为您提供免费的在线应用程序 ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 转换 BMP 为 PDF 使用免费应用程序](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## 转换 DICOM 至 PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 格式是医疗行业用于创建、存储、传输和可视化检查患者的数字医学图像和文档的标准。

**Aspose.PDF for C++** 允许您转换 DICOM 和 SVG 图像，但由于技术原因要添加图像，您需要指定要添加到 PDF 中的文件类型：

1. 创建一个 [String 类](https://reference.aspose.com/pdf/cpp/class/system.string) 用于路径名和文件名。
1. 实例化 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 对象。
1. 向文档的页面集合中添加一个 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)。
1. Aspose.PDF TDicom 被添加为页面的段落。
1. 加载并[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入图像文件。

以下代码片段展示了如何使用 Aspose.PDF 将 DICOM 文件转换为 PDF 格式。您应加载 DICOM 图像，将图像放置在 PDF 文件中的某一页，并将输出保存为 PDF。

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将 DICOM 转换为 PDF**

Aspose 为您提供在线免费应用程序 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，您可以在此尝试调查其功能和工作质量。

[![Aspose.PDF 转换 DICOM 到 PDF 使用免费应用程序](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## 将 EMF 转换为 PDF

<abbr title="增强型图元文件格式">EMF</abbr>EMF 以设备无关的方式存储图形图像。EMF 的元文件由按时间顺序排列的可变长度记录组成，可以在任何输出设备上解析后呈现存储的图像。此外，您可以使用以下步骤将 EMF 转换为 PDF 图像：

1. 为路径名和文件名创建一个[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个新的 Document 对象实例。
1. 向此 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 添加一个新页面。
1. A new Aspose.Pdf TIFF is created.  
1. 使用输入文件初始化Aspose.PDF TIFF对象。  
1. Aspose.PDF TIFF作为段落添加到页面中。  
1. 加载并[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)输入图像文件。

此外，以下代码片段展示了如何在代码片段中使用C++将EMF转换为PDF：

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将 EMF 转换为 PDF**

Aspose 为您提供免费的在线应用程序 ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 转换 EMF 为 PDF 使用免费应用](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## 将 JPG 转换为 PDF

不必再想如何将 JPG 转换为 PDF，因为 **Aspose.PDF for C++** 库有最好的解决方案。

您可以通过以下步骤非常轻松地使用 Aspose.PDF for C++ 将 JPG 图像转换为 PDF：

1. 为路径名和文件名创建一个 [String 类](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个新的 Document 对象实例。
1. 向此 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 添加一个新页面。
1. 创建一个新的 Aspose::Pdf::Image。
1. 使用输入文件初始化 Aspose.PDF Image 对象。
1. Aspose.PDF 图像以段落的形式添加到页面。
1. 加载并保存输入图像文件。

下面的代码片段展示了如何使用 C++ 将 JPG 图像转换为 PDF：

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // 路径名的字符串
    String _dataDir("C:\\Samples\\Conversion\\");

    // 输入文件名的字符串
    String infilename("sample.jpg");

    // 输入文件名的字符串
    String outfilename("ImageToPDF-JPEG.pdf");

    // 打开文档
    auto document = MakeObject<Document>();

    // 在空文档中添加空页面
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // 在页面上添加图像
    page->get_Paragraphs()->Add(image);

    // 保存输出文档
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

然后你可以看到如何将图像转换为与页面**相同高度和宽度的 PDF**。 我们将获取图像尺寸，并根据以下步骤设置PDF文档的页面尺寸：

1. 加载输入图像文件
1. 获取图像的高度和宽度
1. 设置页面的高度、宽度和边距
1. 保存输出PDF文件

以下代码片段展示了如何使用C++将图像转换为相同页面高度和宽度的PDF：

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**尝试在线将JPG转换为PDF**

Aspose为您提供在线免费应用程序["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将JPG转换为PDF](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## 将PNG转换为PDF

**Aspose.PDF for C++**支持将PNG图像转换为PDF格式。查看下一个代码片段以实现您的任务。

<abbr title="便携式网络图形">PNG</abbr>指的是一种使用无损压缩的光栅图像文件格式，这使其在用户中很受欢迎。

您可以使用以下步骤将PNG转换为PDF图像：

1. 为路径名和文件名创建一个[String类](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个新的Document对象的实例。
1. 在此[文档](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)中添加一个新页面。

1. 创建一个新的 Aspose.Pdf PNG。
1. 使用输入文件初始化 Aspose.PDF PNG 对象。
1. 将 Aspose.PDF PNG 作为段落添加到页面。
1. 加载并保存输入图像文件。

此外，下面的代码片段展示了如何在 C++ 应用程序中将 PNG 转换为 PDF：

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.png");

    // String for input file name
    String outfilename("ImageToPDF-PNG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}  
**尝试在线将 PNG 转换为 PDF**  

Aspose 向您提供在线免费应用程序 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，您可以在此尝试研究其功能和工作质量。  

[![Aspose.PDF 使用免费应用程序将 PNG 转换为 PDF](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)  
{{% /alert %}}  

## 将 SVG 转换为 PDF  

**Aspose.PDF for C++** 解释了如何将 SVG 图像转换为 PDF 格式以及如何获取源 <abbr title="可伸缩矢量图形">SVG</abbr> 文件的尺寸。  

可伸缩矢量图形 (SVG) 是基于 XML 的二维矢量图形文件格式的规格家族，既可以是静态的，也可以是动态的（交互或动画）。SVG 规范是一个开放标准，自 1999 年以来由万维网联盟 (W3C) 开发。  

SVG 图像及其行为在 XML 文本文件中定义。 这意味着它们可以被搜索、索引、脚本化，如果需要，还可以被压缩。作为XML文件，SVG图像可以用任何文本编辑器创建和编辑，但通常用像Inkscape这样的绘图程序创建它们更方便。

1. 为路径名和文件名创建一个[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 创建一个[`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options)类的实例。
1. 使用提到的源文件名和选项创建[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)类的实例。
1. 使用所需的文件名保存文档。

以下代码片段展示了使用Aspose.PDF for C++将SVG文件转换为PDF格式的过程。

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
考虑一个具有高级功能的示例：

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**尝试在线将SVG格式转换为PDF**

Aspose.PDF for C++ 为您提供在线免费应用程序["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 SVG 到 PDF 免费应用](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## 将 TIFF 转换为 PDF

**Aspose.PDF** 文件格式支持，无论是单帧还是多帧 <abbr title="Tag Image File Format">TIFF</abbr> 图像。这意味着您可以在 C++ 应用程序中将 TIFF 图像转换为 PDF。

TIFF 或 TIF，标记图像文件格式，代表用于各种符合此文件格式标准的设备上的光栅图像。TIFF 图像可以包含多个帧，每个帧具有不同的图像。Aspose.PDF 文件格式也支持，无论是单帧还是多帧 TIFF 图像。因此，您可以在 C++ 应用程序中将 TIFF 图像转换为 PDF。因此，我们将通过以下步骤考虑将多页 TIFF 图像转换为多页 PDF 文档的示例：

1. 为路径名和文件名创建一个[String 类](https://reference.aspose.com/pdf/cpp/class/system.string)。
1. 一个新的 Document 对象实例被创建。
1. 向此 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 添加一个新页面。
1. 创建一个新的 Aspose.Pdf TIFF。
1. 使用输入文件初始化 Aspose.PDF TIFF 对象。
1. 将 Aspose.PDF TIFF 作为段落添加到页面。
1. 加载并保存输入图像文件。

此外，以下代码片段展示了如何使用 C++ 将多页或多帧的 TIFF 图像转换为 PDF：

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```
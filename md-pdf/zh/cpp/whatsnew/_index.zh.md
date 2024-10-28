---
title: C++ 的新功能
linktitle: 新功能
type: docs
weight: 10
url: /cpp/whatsnew/
description: 本页介绍了最近发布的 Aspose.PDF for C++ 中引入的最受欢迎的新功能。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Aspose.PDF 24.8 中的新功能

能够向页面添加 SVG 图像。

## Aspose.PDF 24.4 中的新功能

修复了加载 SVG 图像的问题。

## Aspose.PDF 24.3 中的新功能

修复了在将 PDF 文档转换为其他格式时的内存泄漏。

## Aspose.PDF 24.2 中的新功能

自 24.2 起已实现：

- 提高了 JPXDecoder 的性能。

- 修复了读取结构损坏的文档的问题。

## Aspose.PDF 23.7 中的新功能

- 引入了将 PDF 文档保存为 EPUB 格式的功能：

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String for path name
        String _dataDir("C:\\Samples\\Conversion\\");

        // String for input file name
        String infilename("sample.pdf");
        // String for output file name
        String outfilename("PDFToEPUB_out.epub");

        // Open document
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Save PDF file into EPUB format
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- 已实现加载 PCL 格式文件：

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Error: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Error: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Aspose.PDF 23.1 的新功能

从 23.1 开始，添加了对 Dicom 格式图像的支持：

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Aspose.PDF 22.11 中的新功能

从 22.11 宣布了第一个 **Aspose.PDF for C++ macOS** 的公开发布。

我们很高兴地宣布 Aspose.PDF for C++ macOS 的第一个公开版本。Aspose.PDF for C++ macOS 是一个专有的 C++ 库，允许开发人员在不使用 Adobe Acrobat 的情况下创建和操作 PDF 文档。Aspose.PDF for C++ macOS 允许开发人员创建表单、添加/编辑文本、操作 PDF 页面、添加注释、处理自定义字体等。

## Aspose.PDF 22.5 中的新功能

PDF 文档中实现了对 XFA 表单的支持。

## Aspose.PDF 22.4 中的新功能

新的 Aspose.PDF for C++ 版本具有 Aspose.PDF for .Net 22.4 和 Aspose.Imaging 22.4 的代码库。

- 实现了 System::Drawing::GetThumbnailImage() 方法；
- 优化了 RegionDataNodeRect 构造函数；
- 修复了每像素 1 位黑白图像的加载。

## Aspose.PDF 22.3 中的新功能

方法重载已添加到多个类中。 这些支持ArrayView类型的参数，而之前仅支持ArrayPtr。

## Aspose.PDF 22.1中的新功能

新的Aspose.PDF for C++版本具有Aspose.PDF for .Net 22.1的代码库：

- 提供了System::Xml的新实现。以前，我们有基于libxml2和libxslt库的自定义实现。新版本基于移植的CoreFX代码

- double-conversion库升级到3.1.7版本

- Dll文件使用Aspose证书签名

## Aspose.PDF 21.10中的新功能

### Aspose.PDF for C++支持将SVG转换为PDF格式的功能

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
        String infilename("Aspose.svg");
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

## Aspose.PDF 21.4 中的新功能

### 已实现将PDF文档保存为HTML格式

Aspose.PDF for C++支持将PDF文件转换为HTML的功能。

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```
---
title: 在 Qt 中处理 PDF 文档
type: docs
weight: 130
url: /zh/cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt 是一个跨平台应用程序开发框架，允许创建各种桌面、移动、Web 和嵌入式系统应用程序。本文将介绍如何集成我们的 C++ PDF 库以在您的 Qt 应用程序中处理 PDF 文档。

## 在 Qt 中使用 Aspose.PDF for C++

为了在 Windows 操作系统上的 Qt 应用程序中使用 Aspose.PDF for C++，请从[下载](https://downloads.aspose.com/pdf/cpp)部分下载最新版本的 API。一旦 API 下载完成，您可以使用以下任意选项将其与 Qt 一起使用。

- 使用 Qt Creator
- 使用 Visual Studio

这里，我们将演示如何在 Qt Creator 中的 Qt 控制台应用程序中集成和使用 Aspose.PDF for C++。

### 创建 Qt 控制台应用程序

{{% alert color="primary" %}}

本文假设您已正确安装 Qt 开发环境和 Qt Creator。

{{% /alert %}}

- 打开 Qt Creator 并创建一个新的*Qt 控制台应用程序*。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- 从*Build System*下拉菜单中选择 QMake 选项。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- 选择合适的 kit 并完成向导。

此时，您应该拥有一个可执行的 Qt 控制台应用程序，并且应该能够顺利编译。

### 将 Aspose.PDF for C++ API 集成到 Qt 中

- 解压您之前下载的 Aspose.PDF for C++ 压缩包
- 将解压后 Aspose.PDF for C++ 包中的*Aspose.Pdf.Cpp*和*CodePorting.Native.Cs2Cpp_vc14_20.4*文件夹复制到项目的根目录。您的项目应如下图所示。

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- 为了添加 lib 和 include 文件夹的路径，右键点击 LHS 面板中的项目并选择*Add Library*。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- 选择外部库选项，并逐一浏览路径以包含和库文件夹。

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- 完成后，您的.pro项目文件将包含以下条目：

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- 构建应用程序，集成完成。

### 在Qt中创建PDF文档

现在Aspose.PDF for C++已经与Qt集成，我们准备创建一个包含一些文本的PDF文档并将其保存到磁盘。为此：

- 在main.cpp中包含以下头文件

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- 在主函数中插入以下代码以生成PDF文档并保存到磁盘

```cpp

    使用命名空间 System;
    使用命名空间 Aspose::Pdf;
    使用命名空间 Aspose::Pdf::Text;
    
    QString text = "你好，世界";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```
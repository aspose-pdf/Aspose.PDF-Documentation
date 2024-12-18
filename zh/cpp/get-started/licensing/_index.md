---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /zh/cpp/licensing/
description: Aspose. PDF for C++ 邀请客户获取经典许可证和计量许可证。 以及使用有限的许可证来更好地探索产品。
lastmod: "2021-11-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 评估版本限制

我们希望客户在购买之前彻底测试我们的组件，因此评估版本允许您像平常一样使用它。然而，在使用评估版本的 API 时会有以下限制：

**PDF 带有评估水印**
Aspose.PDF for C++ 的评估版本提供完整的产品功能，但生成的 PDF 文档的所有页面顶部都会带有“仅限评估。使用 Aspose.PDF 创建。版权 2002-2017 Aspose Pty Ltd”的水印。

**可处理的集合项目数量限制**

在评估版本中，只能处理集合中的四个项目（例如，仅四页、四个表单字段等）。

## 使用文件或流对象应用许可证

许可证可以从文件或流对象中加载。Aspose.PDF for C++ 将尝试在以下位置查找许可证：

1. 明确的路径。
1. 包含 Aspose.PDF.dll 的文件夹。
1. 调用 Aspose.PDF.dll 的程序集所在的文件夹。
1. 包含入口程序集（您的 .exe）的文件夹。
1. 调用 Aspose.PDF.dll 的程序集中的嵌入资源。

设置许可证的最简单方法是将许可证文件与 Aspose.PDF.dll 文件放在同一文件夹中，并指定文件名，而无需路径，如下面的示例所示。

### 从文件加载许可证

应用许可证的最简单方法是将许可证文件与 Aspose.PDF.dll 文件放在同一文件夹中，并仅指定不带路径的文件名。

{{% alert color="primary" %}}

当您调用 SetLicense 方法时，您传递的许可证名称应该是许可证文件的名称。 例如，如果您将许可证文件名更改为 "Aspose.PDF.lic.xml"，请将该文件名传递给 Pdf->SetLicense(…) 方法。

{{% /alert %}}

```cpp
auto lic = MakeObject<Aspose::Pdf::License>();
lic->SetLicense(L"Aspose.PDF.Cpp.lic");
```

### 从流对象加载许可证

以下示例展示了如何从流中加载许可证。

```cpp
intrusive_ptr<License>license = new License();
intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.PDF.Cpp.lic"), FileMode_Open);

license->SetLicense(myStream);
```

## 计量许可证

Aspose.PDF 允许开发人员应用计量密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。那些希望根据 API 功能使用情况进行计费的客户可以使用计量许可。有关更多详细信息，请参阅计量许可常见问题部分。

引入了一个新的类 Metered 用于应用计量密钥。 以下是演示如何设置计量公共和私有密钥的示例代码。

有关更多详细信息，请参阅 [Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered) 部分。
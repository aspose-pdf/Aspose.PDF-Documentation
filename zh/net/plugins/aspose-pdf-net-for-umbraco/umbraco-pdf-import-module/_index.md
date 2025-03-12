---
title: Umbraco PDF 导入模块
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/umbraco-pdf-import-module/
description: 学习如何安装和使用 Umbraco PDF 导入模块
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "Umbraco PDF 导入模块允许开发人员无缝地将 PDF 内容导入他们的 Umbraco 网站，而无需额外的软件。这个强大的开源附加组件通过提供用户友好的界面来即时获取和显示 PDF 内容，从而简化文档处理，提高 .NET 应用程序中的内容管理效率。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 介绍

**Aspose.PDF for .NET** 是一个 PDF 文档创建和处理组件，使您的 .NET 应用程序能够读取、写入和处理现有的 PDF 文档，而无需使用 Adobe Acrobat。它还允许您创建表单并管理嵌入在 PDF 文档中的表单字段。

**Aspose.PDF for .NET** 价格合理，提供丰富的功能，包括 PDF 压缩选项；表格创建和处理；对图形对象的支持；广泛的超链接功能；扩展的安全控制；自定义字体处理；与数据源的集成；添加或删除书签；创建目录；添加、更新、删除附件和注释；导入或导出 PDF 表单数据；添加、替换或删除文本和图像；拆分、连接、提取或插入页面；将页面转换为图像；打印 PDF 文档等等。

### **模块特性**

Umbraco PDF 导入是来自 [Aspose](http://www.aspose.com/) 的开源附加组件，允许开发人员在不需要任何其他软件的情况下获取/读取任何 PDF 文档的内容。这个附加组件展示了 [Aspose.PDF](https://products.aspose.com/pdf/net/) 提供的强大导入功能。它在添加附加组件的页面上添加了一个简单的文件浏览器控件和 **从 PDF 导入** 按钮。点击该按钮后，文档内容将从文件中获取并立即显示在屏幕上。

## 系统要求和支持的平台

### **系统要求**

为了设置 Aspose .NET Pdf 导入 Umbraco 模块，您需要满足以下要求：

- Umbraco 6.0+。

如果您希望在其他版本的 Umbraco 上安装此模块，请随时与我们联系。

### **支持的平台**

该模块支持所有版本的

- 在 ASP.NET 4.0 上运行的 Umbraco。

## 下载

您可以从以下位置之一下载 Aspose .NET Pdf 导入 Umbraco：

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)。
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)。
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/)。

## 安装

下载后，请按照以下步骤将此包安装到您的 Umbraco 网站中：

1. 登录到 Umbraco **开发者** 部分，例如 <http://www.myblog.com/umbraco/>。
1. 从树中展开 **包** 文件夹。
   从这里有两种方式安装包：选择 **安装本地包** 或浏览 **Umbraco 包存储库**。
1. 如果您安装 **本地包**，请不要解压包，而是将 zip 文件加载到 Umbraco 中。
1. 按照屏幕上的说明进行操作。

**注意：** 安装时您可能会遇到“最大请求长度超出”错误。您可以通过更新 Umbraco web.config 文件中的 ‘maxRequestLength’ 值轻松解决此问题。

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## 使用

安装宏后，在您的网站上开始使用它非常简单：

1. 确保您已登录到 Umbraco **开发者** 部分，例如 <http://www.myblog.com/umbraco/>。
1. 点击屏幕左下角的 **设置**。
1. 展开 **模板** 节点并选择您想要添加宏的模板，例如博客文章。
1. 选择您希望按钮出现在所选模板中的位置。
1. 点击顶部功能区上的 **插入宏**。
1. 从 **选择宏** 中，选择已安装的宏并点击 **确定**。

您已成功添加模板。一个名为 **从 PDF 导入** 的按钮现在出现在使用此模板创建的所有页面上。任何人都可以简单地点击该按钮并导入 PDF 文档的内容。

## 视频演示

请查看下面的 [视频](https://www.youtube.com/watch?v=zmZTJ86B25E)，以查看模块的实际操作。

## 支持、扩展和贡献

### 支持

从 Aspose 的第一天起，我们就知道仅仅提供好的产品是不够的。我们还需要提供良好的服务。我们自己也是开发人员，理解当技术问题或软件中的小故障阻止您完成所需工作时的沮丧。我们在这里解决问题，而不是制造问题。

这就是为什么我们提供免费支持。任何使用我们产品的人，无论是购买了还是使用评估版，都值得我们全力关注和尊重。

您可以通过以下任何平台记录与 Aspose.PDF .NET for Umbraco 模块相关的问题或建议：

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)。
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)。

### 扩展和贡献

Aspose .NET PDF 导入 Umbraco 是开源的，其源代码可在以下主要社交编码网站上获得。鼓励开发人员下载源代码并根据自己的需求扩展功能。

#### 源代码

您可以从以下位置之一获取最新的源代码：

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)。
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)。

#### 如何配置源代码

您需要安装以下内容才能打开和扩展源代码：

- Visual Studio 2010 或更高版本。

请按照以下简单步骤开始：

1. 下载/克隆源代码。
1. 打开 Visual Studio 2010，选择 **文件** > **打开项目**。
1. 浏览到您下载的最新源代码并打开 **Aspose.Import from PDF.sln**。
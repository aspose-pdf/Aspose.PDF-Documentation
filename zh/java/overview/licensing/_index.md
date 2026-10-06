---
title: Aspose PDF 许可证
linktitle: 授权和限制
type: docs
weight: 50
url: /zh/java/licensing/
description: Aspose.PDF for Python 邀请其客户获取经典许可证。同时使用受限许可证以更好地探索产品。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java 的授权
Abstract: 本文讨论了 Aspose.PDF for Python 的限制和许可选项。它指出，评估版允许完整功能测试，但会在生成的 PDF 上添加水印，显示“Evaluation Only”以及版权信息。对于希望在不受这些限制的情况下进行测试的用户，提供为期 30 天的临时许可。文章进一步解释了如何通过从文件或流加载来实现经典许可，建议将许可文件放置在与 Aspose.PDF.dll 文件相同的目录中，并使用 `Aspose.Pdf.License` 类设置许可。提供了代码片段以演示许可过程。
---
## 评估版的限制

我们希望客户在购买前彻底测试我们的组件，因此评估版允许您像平常一样使用它。

- **PDF 创建了评估水印。** Aspose.PDF for Java 的评估版提供完整的产品功能，但生成的 PDF 文档的所有页面顶部均会加上水印，内容为 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd"。

- **可处理的集合项目数量限制。**
在评估版中，对于任何集合，您只能处理四个元素（例如，仅 4 页，4 个表单字段等）。

您可以从以下位置下载 **Aspose.PDF** for Java 的评估版 [Aspose 仓库](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). 评估版提供与产品授权版完全相同的功能。更进一步，当您购买授权并添加几行代码应用授权时，评估版会直接转为授权版。

一旦您对 **Aspose.PDF** 的评估满意，即可在 Aspose 网站上 [购买许可证](https://purchase.aspose.com/)。熟悉所提供的不同订阅类型。如果您有任何疑问，请随时联系 Aspose 销售团队。

每个 Aspose 许可证都包含为期一年且免费升级到此期间发布的所有新版本或修复的订阅。技术支持免费且无限制，且对许可证用户和试用用户均提供。

>如果您想在不受评估版限制的情况下测试 Aspose.PDF for Java，您也可以请求 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象加载。设置许可证最简单的方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并且仅指定文件名而不带路径，如下例所示。

许可证是一个纯文本 XML 文件，包含产品名称、授权给的开发者人数、订阅到期日期等详细信息。该文件已进行数字签名，请勿修改文件；即使不经意地在文件中添加额外的换行也会使其失效。

在对文档执行任何操作之前，您需要设置许可证。每个应用程序或进程只需设置一次许可证。

许可证可以从流或文件中加载，位置如下：

1. 显式路径。
1. 包含 aspose-pdf-xx.x.jar 的文件夹。

使用 License.setLicense 方法对组件进行授权。最简单的授权方式通常是将许可证文件放在与 Aspose.PDF.jar 同一文件夹中，并如下面示例所示仅指定文件名而不带路径：

{{% alert color="primary" %}}

从 Aspose.PDF for Java 4.2.0 开始，您需要调用以下代码行来初始化许可证。

{{% /alert %}}

### 从文件加载许可证

在本示例中，**Aspose.PDF** 将尝试在包含您应用程序 JAR 的文件夹中查找许可证文件。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### 从流对象加载许可证

以下示例展示了如何从流加载许可证。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### 验证许可证

可以验证许可证是否已正确设置。Document 类具有 isLicensed 方法，如果许可证已正确设置，它将返回 true。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 计量许可

Aspose.PDF 允许开发人员使用计量密钥。这是一种新的授权机制。新的授权机制将与现有的授权方法一起使用。希望根据 API 功能使用情况计费的客户可以使用计量授权。\u0412\u00A0 有关更多详情，请参阅\u0412 [计量授权 FAQ](https://purchase.aspose.com/faqs/licensing/metered)В 章节。

一个新类В [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В 已被引入以应用计量密钥。以下是示例代码，演示如何设置计量公钥和私钥。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## 使用多个 Aspose 产品

如果在应用程序中使用多个 Aspose 产品，例如 Aspose.PDF 和 Aspose.Words，以下是一些有用的提示。

- **为每个 Aspose 产品单独设置许可证。** 即使您拥有一个用于所有组件的单一许可证文件，例如 'Aspose.Total.lic'，仍然需要为应用程序中使用的每个 Aspose 产品单独调用 **License.SetLicense**。
- **使用完全限定的许可证类名。** 每个 Aspose 产品在其命名空间中都有一个 **License** 类。例如，Aspose.PDF 有 **com.aspose.pdf.License**，而 Aspose.Words 有 **com.aspose.words.License** 类。使用完全限定的类名可以避免对哪个许可证应用于哪个产品产生任何混淆。

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```

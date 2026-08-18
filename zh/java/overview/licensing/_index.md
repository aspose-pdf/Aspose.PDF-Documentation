---
title: Aspose PDF 许可证
linktitle: 许可和限制
type: docs
weight: 50
url: /java/licensing/
description: Aspose.PDF for Python 邀请其客户获得经典许可证。以及使用有限许可证来更好地探索该产品。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java 的许可
Abstract: 本文讨论了 Aspose.PDF for Python 的限制和许可选项。它强调评估版本允许完整的功能测试，但会在生成的 PDF 中添加水印，注明“仅限评估”以及版权信息。对于希望不受这些限制进行测试的用户，可以使用 30 天的临时许可证。本文进一步解释了如何通过从文件或流加载来实现经典许可证，建议将许可证文件放置在与 Aspose.PDF.dll 文件相同的目录中，并使用 `Aspose.Pdf.License` 类设置许可证。提供代码片段来说明许可过程。
---
## 评估版本的限制

我们希望客户在购买之前彻底测试我们的组件，因此评估版本允许您像平常一样使用它。

- **使用评估水印创建的 PDF。** Aspose.PDF for Java 的评估版本提供了完整的产品功能，但生成的 PDF 文档中的所有页面均在顶部标有“仅评估。使用 Aspose.PDF 创建。版权所有 2002-2020 Aspose Pty Ltd”水印。

- **可处理的收藏品数量限制。**
在任何集合的评估版本中，您只能处理四个元素（例如，仅 4 个页面、4 个表单字段等）。

您可以从 [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf) 下载 Java 版 **Aspose.PDF** 的评估版本。评估版本提供与产品的许可版本完全相同的功能。此外，当您购买许可证并添加几行代码来应用许可证时，评估版就会获得许可。

一旦您对 **Aspose.PDF** 的评估感到满意，您可以在 Aspose 网站上[购买许可证](https://purchase.aspose.com/)。让自己熟悉所提供的不同订阅类型。如果您有任何疑问，请随时联系 Aspose 销售团队。

每个 Aspose 许可证都包含一年期订阅，可免费升级到在此期间发布的任何新版本或修复程序。技术支持是免费且不受限制的，并且向许可用户和评估用户提供。

>如果您想在不受评估版限制的情况下测试 Aspose.PDF for Java，您还可以申请 30 天的临时许可证。请参阅[如何获得临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

可以从文件或流对象加载许可证。设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并指定不带路径的文件名，如下例所示。

该许可证是一个纯文本 XML 文件，其中包含产品名称、许可的开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此请勿修改该文件；即使无意中在文件中添加了额外的换行符也会使其失效。

在对文档进行任何操作之前，您需要设置许可证。您只需为每个应用程序或进程设置一次许可证。

可以从以下位置的流或文件加载许可证：

1. 显式路径。
1. 包含 aspose-pdf-xx.x.jar 的文件夹。

使用 License.setLicense 方法来许可组件。通常，设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.jar 相同的文件夹中，并仅指定文件名而不指定路径，如下例所示：

{{% alert color="primary" %}}

从Aspose.PDF for Java 4.2.0开始，您需要调用以下代码行来初始化许可证。

{{% /alert %}}

### 从文件加载许可证

在此示例中，**Aspose.PDF** 将尝试在包含应用程序 JAR 的文件夹中查找许可证文件。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### 从流对象加载许可证

以下示例显示如何从流加载许可证。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### 验证许可证

可以验证许可证是否已正确设置。 Document 类具有 isLicensed 方法，如果已正确设置许可证，该方法将返回 true。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 计量许可证

Aspose.PDF允许开发人员应用计量密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。想要根据 API 功能的使用情况进行计费的客户可以使用计量许可。有关更多详细信息，请参阅[计量许可常见问题解答](https://purchase.aspose.com/faqs/licensing/metered)部分。

引入了一个新类[计量](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)来应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

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

## 使用 Aspose 的多种产品

如果您在应用程序中使用多个 Aspose 产品，例如 Aspose.PDF 和 Aspose.Words，这里有一些有用的提示。

- **单独为每个 Aspose 产品设置许可证。** 即使您对所有组件都有一个许可证文件（例如“Aspose.Total.lic”），您仍然需要为应用程序中使用的每个 Aspose 产品单独调用 **License.SetLicense**。
- **使用完全限定的许可证类名称。** 每个 Aspose 产品在其命名空间中都有一个 **License** 类。例如，Aspose.PDF具有**com.aspose.pdf.License**，Aspose.Words具有**com.aspose.words.License**类。使用完全限定的类名可以避免对哪个许可证应用于哪个产品产生任何混淆。

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

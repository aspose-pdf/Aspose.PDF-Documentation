---
title: 许可和限制
linktitle: 许可和限制
type: docs
weight: 50
url: /zh/androidjava/licensing/
description: Aspose.PDF for Android via Java 邀请其客户获取 Classic 许可证和 Metered 许可证。同时使用受限许可证以更好地探索产品。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 评估版的限制

我们希望客户在购买前彻底测试我们的组件，因此评估版允许您像平常一样使用它。

- **PDF 带有评估水印。** Aspose.PDF for Android via Java 的评估版提供完整的产品功能，但生成的 PDF 文档的所有页面顶部都会加上 "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" 水印。

- **可处理的集合项目数量限制。**
在评估版中，任何集合只能处理四个元素（例如，仅 4 页、4 个表单字段等）。

您可以从以下位置下载 Aspose.PDF for Android via Java 的评估版。 [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). 评估版提供与产品的授权版完全相同的功能。此外，评估版在您购买许可证并添加几行代码以应用许可证后，就会变为授权版。

一旦您对 **Aspose.PDF** 的评估满意，您可以 [购买许可证](https://purchase.aspose.com/) 在 Aspose 网站上。熟悉所提供的不同订阅类型。如果您有任何疑问，请随时联系 Aspose 销售团队。

每个 Aspose 许可证都包含一年期的订阅，可在此期间免费升级到任何新版本或修复。技术支持免费且无限制，提供给已授权用户和评估用户。

>如果您想在不受评估版限制的情况下通过 Java 测试 Aspose.PDF for Android，您也可以申请 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象加载。设置许可证的最简方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并仅指定文件名而不带路径，如下面的示例所示。

许可证是一个纯文本的 XML 文件，包含产品名称、授权的开发者人数、订阅到期日期等信息。该文件已进行数字签名，请勿修改文件；即使不经意地在文件中添加额外的换行也会导致其失效。

在对文档执行任何操作之前，您需要设置许可证。每个应用程序或进程只需设置一次许可证。

许可证可以从流或文件中加载，位置如下：

1. 显式路径。
1. 包含 aspose-pdf-xx.x.jar 的文件夹。

使用 License.setLicense 方法来为组件授权。最简单的授权方式通常是将许可证文件放置在与 Aspose.PDF.jar 相同的文件夹中，并仅指定文件名（不带路径），如下示例所示：

{{% alert color="primary" %}}

从 Aspose.PDF for Java 4.2.0 开始，您需要调用以下代码行来初始化许可证。

{{% /alert %}}

### 从文件加载许可证

在此示例中，**Aspose.PDF** 将尝试在包含您应用程序的 JAR 文件的文件夹中查找许可证文件。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### 从流对象加载许可证

以下示例展示如何从流中加载许可证。

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### 在 2005/01/22 之前购买的许可证设置

**Aspose.PDF** for Java 不再支持旧许可证，请联系我们的 [销售团队](https://company.aspose.com/contact) 以获取新许可证文件。

### 验证许可证

可以验证许可证是否已正确设置。Document 类具有 isLicensed 方法，如果许可证已正确设置，则返回 true。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 计量许可

Aspose.PDF 允许开发者使用计量密钥。这是一种全新的许可机制。该许可机制将与现有的许可方式一起使用。希望根据 API 功能使用情况计费的客户可以使用计量许可。 欲了解详细信息，请参阅 [计量许可常见问题](https://purchase.aspose.com/faqs/licensing/metered) 章节。

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
## 使用来自 Aspose 的多个产品

如果在您的应用程序中使用多个 Aspose 产品，例如 Aspose.PDF 和 Aspose.Words，以下是一些有用的提示。

- **为每个 Aspose 产品单独设置许可证。** 即使您为所有组件拥有单个许可证文件，例如 'Aspose.Total.lic'，仍需为应用程序中使用的每个 Aspose 产品单独调用 **License.SetLicense**。
- **使用完全限定的许可证类名。** 每个 Aspose 产品在其命名空间中都有一个 **License** 类。例如，Aspose.PDF 的 **com.aspose.pdf.License**，Aspose.Words 的 **com.aspose.words.License** 类。使用完全限定的类名可以避免对哪个许可证适用于哪个产品产生混淆。

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

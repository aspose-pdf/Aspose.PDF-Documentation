---
title: 授权和限制
linktitle: 授权和限制
type: docs
weight: 90
url: /php-java/licensing/
description: Aspose.PDF for PHP via Java 邀请客户获取经典许可证和计量许可证。也可以使用有限许可证更好地探索产品。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 评估版本的限制

我们希望客户在购买前彻底测试我们的组件，因此评估版本允许您像正常使用一样使用它。

- **带有评估水印的PDF创建。** Aspose.PDF for PHP via Java 的评估版本提供完整的产品功能，但生成的PDF文档中的所有页面顶部都带有“仅供评估。由Aspose.PDF创建。版权2002-2020 Aspose Pty Ltd”的水印。

- **可处理的集合项数量限制。**

在评估版本中，从任何集合中，您只能处理四个元素（例如，仅4页，4个表单字段等）。

您可以从[Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf)下载**Aspose.PDF** for Java的评估版本。评估版本提供的功能与产品的授权版本完全相同。此外，当您购买许可证并添加几行代码以应用许可证时，评估版本就会变为授权版本。

一旦您对**Aspose.PDF**的评估感到满意，您可以在Aspose网站上[购买许可证](https://purchase.aspose.com/)。请熟悉提供的不同订阅类型。如果您有任何问题，请随时联系Aspose销售团队。

每个Aspose许可证都附带一年免费升级的订阅，以获取在此期间发布的任何新版本或修复。技术支持是免费的、无限的，并且提供给授权用户和评估用户。

>如果您想在没有评估版本限制的情况下测试Java版的Aspose.PDF for PHP，您还可以申请30天的临时许可证。
 请参考[如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象中加载。设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并指定不带路径的文件名，如下面的示例所示。

许可证是一个纯文本 XML 文件，其中包含产品名称、授权开发人员数量、订阅到期日期等详细信息。该文件经过数字签名，因此不要修改文件；即使是不小心多加一个换行符也会使其失效。

在对文档执行任何操作之前，您需要设置许可证。每个应用程序或进程只需设置一次许可证。

许可证可以从以下位置的流或文件中加载：

1. 显式路径。
1. 包含 aspose-pdf-xx.x.jar 的文件夹。

使用 License.setLicense 方法对组件进行授权。 通常，设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.jar 相同的文件夹中，并仅指定不带路径的文件名，如以下示例所示：

{{% alert color="primary" %}}

从 Aspose.PDF for PHP via Java 4.2.0 开始，您需要调用以下代码行来初始化许可证。

{{% /alert %}}

### 从文件加载许可证

在此示例中，**Aspose.PDF** 将尝试在包含应用程序 JAR 的文件夹中找到许可证文件。

```java
// 初始化许可证实例
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 调用 setLicense 方法设置许可证
license.setLicense("Aspose.Pdf.Java.lic");
```
### 从流对象加载许可证

以下示例显示了如何从流加载许可证。

```java
// 初始化许可证实例
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 从流中设置许可证
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### 设置在 2005/01/22 之前购买的许可证**Aspose.PDF** for Java 不再支持旧许可证，因此请联系我们的[销售团队](https://company.aspose.com/contact)获取新许可证文件。

### 验证许可证

可以验证许可证是否已正确设置。Document 类具有 isLicensed 方法，如果许可证已正确设置，该方法将返回 true。

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// 检查许可证是否已验证
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## 计量许可证

Aspose.PDF 允许开发人员应用计量密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。那些希望根据 API 功能的使用情况计费的客户可以使用计量许可。有关更多详细信息，请参阅[计量许可常见问题](https://purchase.aspose.com/faqs/licensing/metered)部分。

引入了一个新的类 [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) 来应用计量密钥。
 以下是演示如何设置计量公钥和私钥的示例代码。

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// 可选地，如果已应用有效的许可证，以下两行返回 true；
// 如果组件在评估模式下运行，则返回 false。
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## 使用多个 Aspose 产品

如果您在应用程序中使用多个 Aspose 产品，例如 Aspose.PDF 和 Aspose.Words，这里有一些有用的提示。

- **分别为每个 Aspose 产品设置许可证。** 即使您拥有一个用于所有组件的单一许可证文件，例如 'Aspose.Total.lic'，您仍然需要为您在应用程序中使用的每个 Aspose 产品分别调用 **License.SetLicense**。
- **使用完全限定的许可证类名称。** 每个 Aspose 产品在其命名空间中都有一个 **License** 类。 例如，Aspose.PDF 有 **com.aspose.pdf.License** 和 Aspose.Words 有 **com.aspose.words.License** 类。使用完全限定类名可以避免对哪个许可证应用于哪个产品的混淆。

```java
// 实例化 Aspose.Pdf 的 License 类
com.aspose.pdf.License license = new com.aspose.pdf.License();
// 设置许可证
license.setLicense("Aspose.Total.Java.lic");

// 为 Java 的 Aspose.Words 设置许可证

// 实例化 Aspose.Words 的 License 类
com.aspose.words.License licenseaw = new com.aspose.words.License();
// 设置许可证
licenseaw.setLicense("Aspose.Total.Java.lic");
```
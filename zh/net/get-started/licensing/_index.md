---
title: Aspose PDF 许可证
linktitle: 许可与限制
type: docs
weight: 90
url: /zh/net/licensing/
description: Aspose. PDF for .NET 邀请其客户获取经典许可证和计量许可证。以及使用有限许可证更好地探索产品。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 评估版本的限制

我们希望我们的客户在购买前彻底测试我们的组件，因此评估版本允许您正常使用它。

- **创建带有评估水印的 PDF。** Aspose.PDF for .NET 的评估版本提供完整的产品功能，但生成的 PDF 文档中的所有页面顶部都带有“仅限评估。由 Aspose.PDF 创建。版权所有 2002-2020 Aspose Pty Ltd”的水印。

- **可处理的集合项数量的限制。**
在评估版本中，您只能处理任何集合中的四个元素（例如，仅 4 页，4 个表单字段等）。
在任何集合的评估版本中，您只能处理四个元素（例如，只有 4 页、4 个表单字段等）。

>如果您想在没有评估版本限制的情况下测试 Aspose.HTML for .NET，您也可以申请一个 30 天的临时许可证。请参阅[如何获得临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象加载。设置许可证的最简单方法是将许可文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并指定文件名而不包括路径，如下例所示。

如果您使用 Aspose.PDF for .NET 以外的任何其他 Aspose for .NET 组件，请为 License 指定命名空间，如 [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license)。

### 从文件加载许可证

应用许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并仅指定文件名而不包括路径。

当您调用 [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 方法时，您传递的许可证名称应该是您的许可证文件的名称。
当您调用 [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 方法时，您传递的许可证名称应该是您的许可证文件的名称。

```csharp
public static void SetLicenseExample()
{
    // 初始化许可证对象
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // 设置许可证
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // 出了些问题
        throw;
    }
    Console.WriteLine("许可证设置成功。");
}
```
### 从流对象加载许可证

以下示例展示了如何从流中加载许可证。

```csharp
public static void SetLicenseFromStream()
{
    // 初始化许可证对象
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // 从文件流加载许可证
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // 设置许可证
    license.SetLicense(myStream);
    Console.WriteLine("许可证设置成功。");
}
```
## 计量许可

Aspose.PDF 允许开发者应用计量密钥。这是一种新的许可机制。新的许可机制将与现有的许可方法一起使用。那些希望根据 API 功能的使用情况来计费的客户可以使用计量许可。有关更多详细信息，请参阅计量许可常见问题解答部分。

已引入新类 Metered 以应用计量密钥。以下是演示如何设置计量公钥和私钥的示例代码。

有关更多详细信息，请参阅 [计量许可常见问题解答](https://purchase.aspose.com/faqs/licensing/metered) 部分。

```csharp
public static void SetMeteredLicense()
{
    // 设置计量公钥和私钥
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // 访问 setMeteredKey 属性并传递公钥和私钥作为参数
    metered.SetMeteredKey(
        "<在此处输入公钥>",
        "<在此处输入私钥>");

    // 从磁盘加载文档。
    Document doc = new Document("input.pdf");
    // 获取文档的页数
    Console.WriteLine(doc.Pages.Count);
}
```
请注意，使用 **Aspose.PDF for .NET** 的COM应用程序也应使用License类。

需要考虑的一点：
请注意，嵌入式资源是按添加的方式包含在程序集中的，即如果您将文本文件作为嵌入式资源添加到应用程序中，并在记事本中打开生成的EXE，您将看到文本文件的确切内容。因此，当使用许可证文件作为嵌入式资源时，任何人都可以在一些简单的文本编辑器中打开exe文件并查看/提取许可证内容。

因此，为了在嵌入应用程序许可证时增加额外的安全层，您可以压缩/加密许可证，之后您可以将其嵌入到程序集中。假设我们有Aspose.PDF.lic许可证文件，那么让我们用密码test创建Aspose.PDF.zip并将此zip文件嵌入解决方案中。以下代码片段可用于初始化许可证：

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            // 获取文档的页数
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### 应用2005年1月22日前购买的许可证

Aspose.PDF for .NET 不再支持旧式许可证。如果您持有2005年1月22日之前的许可证，并且您已更新到更近版本的Aspose.PDF，请联系我们的销售团队以获取新的许可证文件。

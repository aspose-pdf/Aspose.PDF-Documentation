---
title: Aspose PDF 许可证
linktitle: 许可和限制
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /zh/net/licensing/
description: Aspose.PDF for .NET 邀请客户获取经典许可证和计量许可证。以及使用有限许可证以更好地探索产品。
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF for .NET 引入了一个强大的许可框架，包括经典和计量许可证，允许用户在固定定价和基于使用的计费选项之间进行选择。经典许可证可以轻松地从文件或流中加载，而创新的计量许可证提供基于 API 使用的灵活计量，满足不同用户的需求。这种双重许可策略增强了开发人员对 PDF 解决方案的可访问性和可扩展性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
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
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 评估版本的限制

我们希望客户在购买之前充分测试我们的组件，因此评估版本允许您像往常一样使用它。

- **带有评估水印的 PDF。** Aspose.PDF for .NET 的评估版本提供完整的产品功能，但生成的 PDF 文档中的所有页面都带有文本“仅供评估。由 Aspose.PDF 创建。版权 2002-2025 Aspose Pty Ltd。”的水印。

- **限制可以处理的页面数量。**
在评估版本中，您只能处理文档的前四页。

>如果您想在没有评估版本限制的情况下测试 Aspose.PDF for .NET，您还可以申请 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

## 经典许可证

许可证可以从文件或流对象中加载。设置许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并指定文件名而不带路径，如下面的示例所示。

如果您与 Aspose.PDF for .NET 一起使用任何其他 Aspose for .NET 组件，请指定许可证的命名空间，如 [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license)。

### 从文件加载许可证

应用许可证的最简单方法是将许可证文件放在与 Aspose.PDF.dll 文件相同的文件夹中，并仅指定文件名而不带路径。

当您调用 [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index) 方法时，您传递的许可证名称应为您的许可证文件的名称。例如，如果您将许可证文件名更改为“Aspose.PDF.lic.xml”，则将该文件名传递给 Pdf.SetLicense(…) 方法。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### 从流对象加载许可证

以下示例演示如何从流中加载许可证。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## 计量许可证

Aspose.PDF 允许开发人员应用计量密钥。计量许可机制将与现有的许可方法一起使用。希望根据 API 功能的使用情况进行计费的客户可以使用计量许可。有关更多详细信息，请参阅计量许可常见问题解答部分。
本指南提供了平稳实施的最佳实践，并防止由于许可状态变化而导致的中断。

类“Metered”用于应用计量密钥。以下是演示如何设置计量公共和私有密钥的示例代码。

有关更多详细信息，请参阅 [计量许可常见问题解答](https://purchase.aspose.com/faqs/licensing/metered) 部分。

__计量许可方法__

应用计量许可证使用 `SetMeteredKey` 方法通过提供您的公共和私有密钥来激活计量许可证。这应在应用程序初始化期间执行一次，以确保正确的许可。

示例：

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
检查许可证状态使用 `IsMeteredLicensed()` 验证计量许可证是否处于活动状态。

示例：

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
方法 `Metered.GetConsumptionCredit()` 用于获取有关消费信用的信息。
方法 `Metered.GetConsumptionQuantity()` 用于获取有关消费文件大小的信息。

示例：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
       // Add five pages
       AddPages(document, 5);
       // Save the document
       document.Save(dataDir + "output.pdf")
    }
}

private static void AddPages(Document document, int n)
{
    for(int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}   
```

__计量许可的最佳实践__

✅ 推荐方法：单例模式
为了确保稳定的许可设置：

- 在应用程序启动时应用许可证。
- 使用单例模式（或类似方法）创建和重用计量许可证实例。
- 定期使用 `IsMeteredLicensed()` 检查许可证状态。仅在许可证变为无效时重新应用许可证。
- 如果正确实施，即使许可证服务器暂时不可用，许可证在 24 小时内仍然有效。

示例：单例实现

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ 常见错误：

- 频繁申请许可证
- 不要为每个操作创建新的计量许可证实例。
- 如果在初始化期间许可证服务器无法访问，许可证可能会恢复为评估模式。
- 不要为每个操作重复申请许可证。
- 频繁申请许可证可能会导致在许可证服务器暂时不可用时回退到试用模式。

__总结：__

✅ 在应用程序启动时设置计量许可证一次。
✅ 使用单例模式管理单个实例。
✅ 定期检查并在需要时重新应用许可证。
❌ 避免频繁申请许可证以防止回退到试用模式。
通过遵循这些最佳实践，您确保平稳和不间断地使用带有计量许可的 Aspose.PDF。

如果许可证已初始化，则只要该对象“存在”，即使由于某种原因与许可证服务器的连接丢失，许可证在接下来的 7 天内仍将被视为有效。如果您在需要做某事时初始化许可证，并且在初始化时与服务器没有连接，则许可证将进入评估模式。
还应强调的是，如果用户已初始化许可证，则只要该对象“存在”，即使由于某种原因与许可证服务器的连接丢失，许可证在接下来的 24 小时内仍将被视为有效。如果您在需要做某事时初始化许可证，并且在初始化时与服务器没有连接，则许可证将进入评估模式。

请注意，使用 **Aspose.PDF for .NET** 的 COM 应用程序也应使用许可证类。

需要考虑的一点：
请注意，嵌入的资源以添加的方式包含在程序集内，即如果您将文本文件作为嵌入资源添加到应用程序中，并在记事本中打开生成的 EXE，您将看到文本文件的确切内容。因此，在将许可证文件作为嵌入资源使用时，任何人都可以在某些简单的文本编辑器中打开 exe 文件并查看/提取嵌入许可证的内容。

因此，为了在将许可证与应用程序嵌入时增加额外的安全层，您可以压缩/加密许可证，然后将其嵌入到程序集内。假设我们有 Aspose.PDF.lic 许可证文件，那么我们可以制作带有密码 test 的 Aspose.PDF.zip，并将此 zip 文件嵌入到解决方案中。以下代码片段可用于初始化许可证：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
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
```
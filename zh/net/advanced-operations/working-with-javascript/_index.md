---
title: 使用 JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /zh/net/working-with-javascript/
description: 学习如何在 PDF 文档中使用 Aspose.PDF for .NET 添加、修改和执行 JavaScript。增强交互性和自动化。
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "发现通过 Aspose.PDF for .NET 将 JavaScript 集成到 PDF 文档中的增强功能。此新功能允许开发人员在文档和页面级别添加和管理 JavaScript 操作，从而实现面向改善用户参与和功能的交互式和动态 PDF 体验。释放 JavaScript 的潜力，创建模仿 Web 行为的复杂 PDF 表单，提高文档生成工作流程",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 添加 JavaScript (DOM)

### 什么是 Acrobat JavaScript？

Acrobat JavaScript 是一种基于 ISO-16262 的 JavaScript 版本 1.5 的语言，前称 ECMAScript，是由 Netscape Communications 开发的面向对象的脚本语言。JavaScript 的创建旨在将 Web 页面处理从服务器转移到 Web 应用程序中的客户端。Acrobat JavaScript 在 JavaScript 语言中实现了扩展，以新的对象及其附带的方法和属性的形式。这些 Acrobat 特定的对象使开发人员能够管理文档安全性、与数据库通信、处理文件附件、操作 PDF 文件使其表现得像一个交互式的、支持 Web 的表单，等等。由于 Acrobat 特定的对象是在核心 JavaScript 之上添加的，因此您仍然可以访问其标准类，包括 Math、String、Date、Array 和 RegExp。

### Acrobat JavaScript 与 HTML (Web) JavaScript 的区别

PDF 文档具有很大的灵活性，因为它们可以在 Acrobat 软件和 Web 浏览器中显示。因此，了解 Acrobat JavaScript 和在 Web 浏览器中使用的 JavaScript（也称为 HTML JavaScript）之间的区别非常重要：

- Acrobat JavaScript 无法访问 HTML 页面中的对象。同样，HTML JavaScript 也无法访问 PDF 文件中的对象。
- HTML JavaScript 能够操作诸如 Window 的对象。Acrobat JavaScript 无法访问此特定对象，但可以操作 PDF 特定的对象。

您可以在文档和页面级别添加 JavaScript，使用 [Aspose.PDF for .NET](/pdf/zh/net/)。要添加 JavaScript：

### 将 JavaScript 添加到文档或页面操作

1. 声明并实例化一个 JavascriptAction 对象，将所需的 JavaScript 语句作为构造函数参数。
1. 将 JavascriptAction 对象分配给 PDF 文档或页面的所需操作。

下面的示例将 OpenAction 应用到特定文档。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 在文档级别添加/删除 JavaScript

在 Document 类中添加了一个名为 JavaScript 的新属性，该属性具有 JavaScript 集合类型，并通过其键提供对 JavaScript 场景的访问。此属性用于添加文档级 JavaScript。JavaScript 集合具有以下属性和方法：

- string this(string key)– 通过名称获取或设置 JavaScript。
- IList Keys – 提供 JavaScript 集合中现有键的列表。
- bool Remove(string key) – 通过键删除 JavaScript。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### 使用 JavaScript 操作设置 PDF 文档的到期日期

Aspose.PDF 允许您通过嵌入 JavaScript 操作为 PDF 文档设置到期日期。此功能确保 PDF 在指定的日期和时间后变得不可访问，从而增强文档的安全性和控制。通过利用 JavaScript 操作，您可以定义精确的到期条件，确保文档的可访问性受到严格控制。

**您可以通过以下步骤实现此功能**

1. **初始化文档：** 创建一个新的 PDF 文档并添加一个空白页面或打开一个现有的 PDF 文档。
2. **定义到期日期和时间：** 设置文档到期的日期和时间。
3. **准备 JavaScript 代码：** 
    - 获取当前日期和时间。
    - 定义确切的到期日期和时间，考虑到 JavaScript 中的月份是从零开始的。
    - 将当前日期和时间与到期日期和时间进行比较。
    - 如果当前日期和时间超过到期日期和时间，则显示警报并关闭文档。
4. **设置打开操作：** 将 JavaScript 操作与文档的打开操作关联。
5. **保存文档：** 保存带有嵌入 JavaScript 的 PDF，该 JavaScript 强制执行到期条件。

以下是演示此功能的 C# (.NET) 和 Java 的代码片段。

以下 C# 代码片段演示如何使用 JavaScript 操作为 PDF 文档设置到期日期和时间：

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **JavaScript 日期对象：** 在 JavaScript 中，月份索引从 `0` 开始（1 月）到 `11` 结束（12 月）。确保在设置到期日期和时间时相应调整月份值。
  
- **安全考虑：** 虽然 JavaScript 操作可以控制 PDF 文档的行为，但它们依赖于 PDF 查看器对 JavaScript 的支持。并非所有 PDF 查看器都可能遵循这些脚本，用户可能出于安全原因禁用 JavaScript 执行。

- **自定义：** 修改 JavaScript 代码以在到期时执行其他操作，例如禁用某些功能、重定向到特定页面或记录事件。此外，如果需要，您可以仅检查到期日期而不指定时间。

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
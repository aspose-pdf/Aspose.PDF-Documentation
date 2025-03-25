---
title: PDF AI 副驾驶
linktitle: PDF AI 副驾驶
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 150
url: /zh/net/ai-copilot/
description: 本文描述了如何使用 Aspose.PDF 库处理 PDF 文档的 AI Copilot。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-10-23"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF AI Copilot",
    "alternativeHeadline": "Seamlessly Integrate AI with PDF Document Processing",
    "abstract": "PDF AI Copilot 功能利用先进的 AI 技术，通过文档摘要、与 PDF 内容的互动聊天能力以及从文档生成图像描述等功能来增强文档处理。这个创新的 API 简化了用户与 PDF 文档的互动和洞察提取，使其成为提高生产力和用户参与度的必备工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF AI Copilot, Aspose.PDF API, document summary, chat with documents, OpenAI Summary, OpenAI Chat, image descriptions, Llama Chat, AI document processing",
    "wordcount": "1047",
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
    "url": "/net/ai-copilot/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/ai-copilot/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}
**Aspose.PDF AI Copilot API** 旨在允许用户使用来自不同提供商的 LLM 处理 PDF 文档。这个 [API](https://reference.aspose.com/pdf/net/aspose.pdf.ai/) 将帮助用户构建聊天机器人应用程序并将 PDF 解决方案与 LLM 集成。
{{% /alert %}}

## 主要特性

* 文档摘要。
* 与文档聊天。
* 从文档中获取图像并提供描述。

## 示例

目前，以下 copilots 可用：

[**OpenAI Summary**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaisummarycopilot/) 允许用户从文档生成摘要。它提供了一种方便的方式，通过配置选项如模型、温度、令牌数量、模型指令、文档附件等来创建摘要。该 copilot 可以异步生成文本、文档格式的摘要，并将摘要保存为各种格式。提供的演示代码展示了如何创建 OpenAI 客户端、配置 copilot 选项以及使用 SummaryCopilot 生成和保存摘要。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task GetSummary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using (var openAiClient = Aspose.Pdf.AI.OpenAIClient
               .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
               //.WithProject("proj_123") // Configure optional parameters
               .Build())
    {
        // Create copilot options
        var options = Aspose.Pdf.AI.OpenAISummaryCopilotOptions
            .Create() // Create options like this, or...
            //.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate
            .WithTemperature(0.5) // Configure other optional parameters
            .WithDocument("SampleDocument.pdf"); // .WithDocument methods allows to add text, pdf and paths to documents
            //.WithDocuments(new List<Aspose.Pdf.AI.TextDocument> { new Aspose.Pdf.AI.TextDocument() }); // .WithDocuments methods allows to add text, pdf and path collections

        // Create summary copilot
        Aspose.Pdf.AI.ISummaryCopilot summaryCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateSummaryCopilot(openAiClient, options);

        // Get summary text
        string summaryText = await summaryCopilot.GetSummaryAsync();

        // Get summary document
        Aspose.Pdf.Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

        // Get summary document with page info
        Aspose.Pdf.Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new Aspose.Pdf.PageInfo());

        // Save PDF document
        await summaryCopilot.SaveSummaryAsync(dataDir + "Summary_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task GetSummary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using var openAiClient = Aspose.Pdf.AI.OpenAIClient
        .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
        //.WithProject("proj_123") // Configure optional parameters
        .Build();

    // Create copilot options
    var options = Aspose.Pdf.AI.OpenAISummaryCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate
        .WithTemperature(0.5) // Configure other optional parameters
        .WithDocument("SampleDocument.pdf"); // .WithDocument methods allows to add text, pdf and paths to documents
        //.WithDocuments(new List<Aspose.Pdf.AI.TextDocument> { new Aspose.Pdf.AI.TextDocument() }); // .WithDocuments methods allows to add text, pdf and path collections

    // Create summary copilot
    Aspose.Pdf.AI.ISummaryCopilot summaryCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateSummaryCopilot(openAiClient, options);

    // Get summary text
    string summaryText = await summaryCopilot.GetSummaryAsync();

    // Get summary document
    Aspose.Pdf.Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

    // Get summary document with page info
    Aspose.Pdf.Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new Aspose.Pdf.PageInfo());

    // Save PDF document
    await summaryCopilot.SaveSummaryAsync(dataDir + "Summary_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

[**OpenAI Chat**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaichatcopilot/) 是一个设计用于与文档进行聊天交互的 AI copilot。它促进了对用户查询的响应生成和上下文管理。用户可以配置 copilot 选项，如模型、温度、令牌数量、模型指令、文档附件等。该 copilot 可以对单个或多个查询提供响应，保存响应为各种格式，保存和删除上下文。

提供的代码演示了如何创建 OpenAI 客户端、配置 ChatCopilot 选项以及使用 ChatCopilot 与用户查询进行交互和管理上下文。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ChatWithDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using (var openAiClient = Aspose.Pdf.AI.OpenAIClient
                .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
                //.WithProject("proj_123") // Configure optional parameters
                //.WithOrganization("org_123")
                .Build()) // Build
    {
        // Create copilot options
        var options = Aspose.Pdf.AI.OpenAIChatCopilotOptions
            .Create() // Create options like this, or...
            //.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate
            .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt35Turbo) // Configure other optional parameters
            .WithTemperature(0.5)
            .WithTopP(1)
            //.WithContextBackupJsonPath("ContextBackup.json") // Supply context backup to resume the conversation session
            //.WithRestoreContextFromBackup(true) // If set to true, the context will be restored
            .WithDocument(dataDir + "SampleDocument.pdf"); // Attach documents using .WithDocument(s) methods allows to add text, pdf and paths to documents

        // Create summary copilot
        Aspose.Pdf.AI.IChatCopilot chatCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateChatCopilot(openAiClient, options);

        // Get response on a user query
        string copilotResponse1 = await chatCopilot.GetResponseAsync("Summarize this document.");

        // Get response on a list of queries
        string copilotResponse2 = await chatCopilot.GetResponseAsync(new List<string>
        {
            "What is the subject of this document?",
            "How many words in it?"
        });

        // Save PDF document
        await chatCopilot.SaveResponseAsync("Summarize this document.", dataDir + "ResponseDocument1_out.pdf");

        // Save PDF document
        await chatCopilot.SaveResponseAsync(new List<string>
            {
                "What is the subject of this document?",
                "How many words in it?"
            },
            dataDir + "ResponseDocument2_out.pdf");

        // Save context (ids of assistant, thread, documents)
        await chatCopilot.SaveContextAsync(dataDir + "ContextBackup.json");

        // Deletes the context
        await chatCopilot.DeleteContextAsync();
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ChatWithDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using var openAiClient = Aspose.Pdf.AI.OpenAIClient
        .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
        //.WithProject("proj_123") // Configure optional parameters
        //.WithOrganization("org_123")
        .Build(); // Build

    // Create copilot options
    var options = Aspose.Pdf.AI.OpenAIChatCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate
        .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt35Turbo) // Configure other optional parameters
        .WithTemperature(0.5)
        .WithTopP(1)
        //.WithContextBackupJsonPath("ContextBackup.json") // Supply context backup to resume the conversation session
        //.WithRestoreContextFromBackup(true) // If set to true, the context will be restored
        .WithDocument(dataDir + "SampleDocument.pdf"); // Attach documents using .WithDocument(s) methods allows to add text, pdf and paths to documents

    // Create summary copilot
    Aspose.Pdf.AI.IChatCopilot chatCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateChatCopilot(openAiClient, options);

    // Get response on a user query
    string copilotResponse1 = await chatCopilot.GetResponseAsync("Summarize this document.");

    // Get response on a list of queries
    string copilotResponse2 = await chatCopilot.GetResponseAsync(new List<string>
    {
        "What is the subject of this document?",
        "How many words in it?"
    });

    // Save summary as PDF document
    await chatCopilot.SaveResponseAsync("Summarize this document.", dataDir + "ResponseDocument1_out.pdf");

    // Save summary as PDF document
    await chatCopilot.SaveResponseAsync(new List<string>
        {
            "What is the subject of this document?",
            "How many words in it?"
        },
        dataDir + "ResponseDocument2_out.pdf");

    // Save context (ids of assistant, thread, documents)
    await chatCopilot.SaveContextAsync(dataDir +"ContextBackup.json");

    // Deletes the context
    await chatCopilot.DeleteContextAsync();
}
```
{{< /tab >}}
{{< /tabs >}}

[**OpenAI Image Description**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaiimagedescriptioncopilot/) 是一个设计用于生成 PDF 文档内图像以及单独图像文件的图像描述的 AI copilot。用户可以配置 copilot 选项，如模型、温度、令牌数量、模型指令、文档附件等。该 copilot 提供了一次获取所有附加文档的图像描述的能力。

提供的代码片段演示了如何创建 OpenAI 客户端、配置 ImageDescriptionCopilot 选项以及使用 copilot 获取附加文档的图像描述。此外，还有一个扩展方法，允许将图像描述添加到附加文档中的图像，并在提供的目录中保存新文档。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task CreateImageDescriptions()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using (var openAiClient = Aspose.Pdf.AI.OpenAIClient
        .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
        //.WithProject("proj_123") // Configure optional parameters
        //.WithOrganization("org_123")
        .Build()) // Build
    {
        // Create copilot options
        var options = Aspose.Pdf.AI.OpenAIImageDescriptionCopilotOptions
            .Create() // Create options like this, or...
            //.Create(options => { options.Model = OpenAIModels.Gpt4Turbo; }) // ...create using delegate
            .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt4Turbo) // The model should have vision capabilities
            .WithTemperature(0.5)
            .WithTopP(1)
            .WithDocument(new Aspose.Pdf.AI.PdfDocument // Attach documents
            {
                Name = "Another_Pdf_with_images",
                Document = new Aspose.Pdf.Document(dataDir + "Pdf_with_images.pdf")
            })
            .WithDocument(dataDir + "Mona_liza.jpg"); // Attach images
            //.WithDocument("Pdf_with_images.pdf"); // Attach document paths

        // Create copilot
        var copilot = Aspose.Pdf.AI.AICopilotFactory.CreateImageDescriptionCopilot(openAiClient, options);

        // Get Image descriptions
        List<Aspose.Pdf.AI.ImageDescriptionResult> imageDescriptions = await copilot.GetImageDescriptionsAsync();

        // Use extension method to add image descriptions to attached documents
        await copilot.AddPdfImageDescriptionsAsync(dataDir);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task CreateImageDescriptions()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    // Create AI client
    using var openAiClient = Aspose.Pdf.AI.OpenAIClient
        .CreateWithApiKey(ApiKey) // Create OpenAI client with the API key
        //.WithProject("proj_123") // Configure optional parameters
        //.WithOrganization("org_123")
        .Build(); // Build

    // Create copilot options
    var options = Aspose.Pdf.AI.OpenAIImageDescriptionCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = OpenAIModels.Gpt4Turbo; }) // ...create using delegate
        .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt4Turbo) // The model should have vision capabilities
        .WithTemperature(0.5)
        .WithTopP(1)
        .WithDocument(new Aspose.Pdf.AI.PdfDocument // Attach documents
        {
            Name = "Another_Pdf_with_images",
            Document = new Aspose.Pdf.Document(dataDir + "Pdf_with_images.pdf")
        })
        .WithDocument(dataDir + "Mona_liza.jpg"); // Attach images
        //.WithDocument(dataDir + "Pdf_with_images.pdf"); // Attach document paths

    // Create copilot
    var copilot = Aspose.Pdf.AI.AICopilotFactory.CreateImageDescriptionCopilot(openAiClient, options);

    // Get Image descriptions
    List<Aspose.Pdf.AI.ImageDescriptionResult> imageDescriptions = await copilot.GetImageDescriptionsAsync();

    // Use extension method to add image descriptions to attached documents
    await copilot.AddPdfImageDescriptionsAsync(dataDir);
}
```
{{< /tab >}}
{{< /tabs >}}

[**Llama Chat**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/llamaclient/) 允许创建一个客户端以向 Llama 聊天完成 API 发送请求。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ChatWithLlama()
{
    using (var llamaClient = Aspose.Pdf.AI.LlamaClient
        .CreateWithApiKey(ApiKey) // Create Llama client with the API key
        .Build())
    {
        var result = await llamaClient.CreateCompletionAsync(new Aspose.Pdf.AI.LlamaChatCompletionRequest
        {
            Messages = new List<Aspose.Pdf.AI.ChatMessage>
            {
                Aspose.Pdf.AI.ChatMessage.FromUser("Hello!")
            }
        });

        var response = result.Choices[0].Message.Content; // Hello! How can I assist you today?
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ChatWithLlama()
{
    using var llamaClient = Aspose.Pdf.AI.LlamaClient
        .CreateWithApiKey(ApiKey) // Create Llama client with the API key
        .Build();

    var result = await llamaClient.CreateCompletionAsync(new Aspose.Pdf.AI.LlamaChatCompletionRequest
    {
        Messages = new List<Aspose.Pdf.AI.ChatMessage>
        {
            Aspose.Pdf.AI.ChatMessage.FromUser("Hello!")
        }
    });

    var response = result.Choices[0].Message.Content; // Hello! How can I assist you today?
}
```
{{< /tab >}}
{{< /tabs >}}

[**Llama Summary**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/llamaclient/) 允许客户端用于创建 Summary Copilot。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task GenerateSummary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    using (var llamaClient = Aspose.Pdf.AI.LlamaClient
        .CreateWithApiKey(ApiKey) // Create Llama client with the API key
        .Build())
    {
        // Create copilot options
        var options = Aspose.Pdf.AI.LlamaSummaryCopilotOptions
            .Create() // Create options like this, or...
            //.Create(options => { options.Model = LlamaModels.Llama13BChat; }) // ...create using delegate
            .WithTemperature(0.5) // Configure other optional parameters
            .WithDocument(dataDir + "SampleDocument.pdf"); // .WithDocument methods allow to add text, pdf, and paths to documents
            //.WithDocuments(new List<Aspose.Pdf.AI.TextDocument> { new Aspose.Pdf.AI.TextDocument() }); // .WithDocuments methods allow to add text, pdf and path collections

        // Create summary copilot
        var summaryCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateSummaryCopilot(llamaClient, options);

        // Get summary text
        string summaryText = await summaryCopilot.GetSummaryAsync();

        // Get summary document
        Aspose.Pdf.Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

        // Get the summary document with page info
        Aspose.Pdf.Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new Aspose.Pdf.PageInfo());

        // Save the summary as a PDF document
        await summaryCopilot.SaveSummaryAsync(dataDir + "Llama_out.pdf");

        // Save summary with specified format
        await summaryCopilot.SaveSummaryAsync(dataDir + "Llama_out.docx", Aspose.Pdf.SaveFormat.DocX);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task GenerateSummary()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_AI();

    using var llamaClient = Aspose.Pdf.AI.LlamaClient
        .CreateWithApiKey(ApiKey) // Create Llama client with the API key
        .Build();

    // Create copilot options
    var options = Aspose.Pdf.AI.LlamaSummaryCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = LlamaModels.Llama13BChat; }) // ...create using delegate
        .WithTemperature(0.5) // Configure other optional parameters
        .WithDocument(dataDir + "SampleDocument.pdf"); // .WithDocument methods allow to add text, pdf, and paths to documents
        //.WithDocuments(new List<Aspose.Pdf.AI.TextDocument> { new Aspose.Pdf.AI.TextDocument() }); // .WithDocuments methods allow to add text, pdf and path collections

    // Create summary copilot
    var summaryCopilot = Aspose.Pdf.AI.AICopilotFactory.CreateSummaryCopilot(llamaClient, options);

    // Get summary text
    string summaryText = await summaryCopilot.GetSummaryAsync();

    // Get summary document
    Aspose.Pdf.Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

    // Get the summary document with page info
    Aspose.Pdf.Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new Aspose.Pdf.PageInfo());

    // Save the summary as a PDF document
    await summaryCopilot.SaveSummaryAsync(dataDir + "Llama_out.pdf");

    // Save summary with specified format
    await summaryCopilot.SaveSummaryAsync(dataDir + "Llama_out.docx", Aspose.Pdf.SaveFormat.DocX);
}
```
{{< /tab >}}
{{< /tabs >}}
---
title: PDF AI 코파일럿
linktitle: PDF AI 코파일럿
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 150
url: /ko/net/ai-copilot/
description: 이 문서에서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서를 처리하는 데 AI Copilot을 사용하는 방법을 설명합니다.
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
    "abstract": "PDF AI Copilot 기능은 문서 요약, PDF 콘텐츠와의 대화형 채팅 기능, 문서에서 이미지 설명 생성과 같은 기능을 통해 문서 처리를 향상시키기 위해 고급 AI 기술을 활용합니다. 이 혁신적인 API는 사용자가 PDF 문서와 상호작용하고 통찰력을 추출하는 방식을 간소화하여 생산성과 사용자 참여를 향상시키는 필수 도구입니다.",
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
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}
**Aspose.PDF AI Copilot API**는 사용자가 다양한 공급자의 LLM을 사용하여 PDF 문서를 처리할 수 있도록 설계되었습니다. 이 [API](https://reference.aspose.com/pdf/net/aspose.pdf.ai/)는 사용자가 챗봇 애플리케이션을 구축하고 PDF 솔루션을 LLM과 통합하는 데 도움을 줄 것입니다.
{{% /alert %}}

## 주요 기능

* 문서 요약.
* 문서와의 채팅.
* 문서에서 이미지를 가져오고 설명 제공.

## 예제

현재 사용할 수 있는 다음의 코파일럿이 있습니다:

[**OpenAI Summary**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaisummarycopilot/)는 사용자가 문서에서 요약을 생성할 수 있도록 합니다. 모델, 온도, 토큰 수, 모델 지침, 문서 첨부 파일 등과 같은 옵션을 구성하여 요약을 생성하는 편리한 방법을 제공합니다. 코파일럿은 비동기적으로 텍스트, 문서로 요약을 생성하고 다양한 형식으로 요약을 저장할 수 있습니다. 제공된 데모 코드는 OpenAI 클라이언트 생성, 코파일럿 옵션 구성 및 SummaryCopilot을 사용하여 요약을 생성하고 저장하는 방법을 보여줍니다.

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

[**OpenAI Chat**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaichatcopilot/)는 문서와의 채팅 상호작용을 위해 설계된 AI 코파일럿입니다. 사용자 쿼리에 대한 응답을 생성하고 컨텍스트를 관리하는 데 도움을 줍니다. 사용자는 모델, 온도, 토큰 수, 모델 지침, 문서 첨부 파일 등과 같은 코파일럿 옵션을 구성할 수 있습니다. 코파일럿은 단일 또는 여러 쿼리에 대한 응답을 제공하고, 다양한 형식으로 응답을 저장하며, 컨텍스트를 저장하고 삭제할 수 있습니다.

제공된 코드는 OpenAI 클라이언트 생성, ChatCopilot 옵션 구성 및 ChatCopilot을 사용하여 사용자 쿼리와 상호작용하고 컨텍스트를 관리하는 방법을 보여줍니다.

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

[**OpenAI Image Description**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/openaiimagedescriptioncopilot/)는 PDF 문서 내의 이미지 및 별도의 이미지 파일에 대한 이미지 설명을 생성하기 위해 설계된 AI 코파일럿입니다. 사용자는 모델, 온도, 토큰 수, 모델 지침, 문서 첨부 파일 등과 같은 코파일럿 옵션을 구성할 수 있습니다. 코파일럿은 모든 첨부 문서에 대한 이미지 설명을 한 번에 가져올 수 있는 기능을 제공합니다.

제공된 코드 조각은 OpenAI 클라이언트 생성, ImageDescriptionCopilot 옵션 구성 및 첨부 문서에 대한 이미지 설명을 얻기 위해 코파일럿을 사용하는 방법을 보여줍니다. 또한, 첨부 문서의 이미지에 이미지 설명을 추가하고 제공된 디렉토리에 새 문서를 저장할 수 있는 확장 메서드가 있습니다.

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

[**Llama Chat**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/llamaclient/)는 Llama 채팅 완료 API에 요청을 보내기 위한 클라이언트를 생성할 수 있습니다.

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

[**Llama Summary**](https://reference.aspose.com/pdf/net/aspose.pdf.ai/llamaclient/)는 Summary Copilot을 생성하는 데 사용할 수 있는 클라이언트를 제공합니다.

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
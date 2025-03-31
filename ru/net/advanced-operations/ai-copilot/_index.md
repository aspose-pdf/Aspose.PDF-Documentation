---
title: PDF AI Copilot» — «Копия помощника на базе ИИ в формате PDF
linktitle: PDF AI Copilot» — «Копия помощника на базе ИИ в формате PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 150
url: /ru/net/ai-copilot/
description: Эта статья описывает, как AI Copilot может быть использован для обработки PDF-документов с помощью библиотеки Aspose.PDF.
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
    "abstract": "Функция PDF AI Copilot использует передовые технологии ИИ для улучшения обработки документов через такие функции, как резюмирование документов, интерактивные возможности чата с содержимым PDF и генерация описаний изображений из документов. Этот инновационный API упрощает взаимодействие пользователей с PDF-документами и извлечение из них информации, что делает его незаменимым инструментом для повышения продуктивности и вовлеченности пользователей.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

{{% alert color="primary" %}}
**Aspose.PDF AI Copilot API** предназначен для того, чтобы позволить пользователям обрабатывать PDF-документы с использованием LLM от различных поставщиков. Этот [API](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/) поможет пользователям в создании приложений чат-ботов и интеграции PDF-решений с LLM.
{{% /alert %}}

## Ключевые особенности

* Резюме документов.
* Чат с документами.
* Получение изображений из документов и предоставление описаний.

## Примеры

В настоящее время доступны следующие копилоты:

[**OpenAI Summary**](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/openaisummarycopilot/) позволяет пользователям генерировать резюме из документов. Он предоставляет удобный способ создания резюме, настраивая такие параметры, как модель, температура, количество токенов, инструкции модели, вложения документов и другие. Копилот может асинхронно генерировать резюме в виде текста, документов и сохранять резюме в различных форматах. Предоставленный демонстрационный код демонстрирует создание клиента OpenAI, настройку параметров копилота и использование SummaryCopilot для генерации и сохранения резюме.

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

[**OpenAI Chat**](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/openaichatcopilot/) — это ИИ копилот, предназначенный для взаимодействия с документами в чате. Он облегчает генерацию ответов на запросы пользователей и управление контекстом. Пользователи могут настраивать параметры копилота, такие как модель, температура, количество токенов, инструкции модели, вложения документов и другие. Копилот может предоставлять ответы на один или несколько запросов, сохранять ответы в различных форматах, сохранять и удалять контекст.

Предоставленный код демонстрирует создание клиента OpenAI, настройку параметров ChatCopilot и использование ChatCopilot для взаимодействия с запросами пользователей и управления контекстом.

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

[**OpenAI Image Description**](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/openaiimagedescriptioncopilot/) — это ИИ копилот, предназначенный для генерации описаний изображений изображений внутри PDF-документов, а также отдельных файлов изображений. Пользователи могут настраивать параметры копилота, такие как модель, температура, количество токенов, инструкции модели, вложения документов и другие. Копилот предоставляет возможность получать описания изображений для всех прикрепленных документов сразу.

Предоставленный фрагмент кода демонстрирует создание клиента OpenAI, настройку параметров ImageDescriptionCopilot и использование копилота для получения описаний изображений для прикрепленных документов. Кроме того, есть метод расширения, который позволяет добавлять описания изображений к изображениям в прикрепленных документах и сохранять новые документы в указанной директории.

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

[**Llama Chat**](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/llamaclient/) позволяет создать клиента для отправки запросов к API завершения чата Llama.

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

[**Llama Summary**](https://reference.aspose.com/pdf/ru/net/aspose.pdf.ai/llamaclient/) позволяет клиенту использоваться для создания Summary Copilot.

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
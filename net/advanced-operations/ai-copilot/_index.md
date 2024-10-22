---
title: Working with PDF Documents using AI Copilot
linktitle: Working with PDF Documents using AI Copilot
type: docs
weight: 10
url: /net/ai-copilot/
description: This article describes how AI Copilot can be used to process the PDF document with Aspose.PDF library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-10-22"
---

**Aspose.PDF AI Copilot API** designed to allows users to process PDF documents using LLMs from different providers. This [API](https://reference.aspose.com/pdf/net/aspose.pdf/) will help users in building chatbot applications and integrating PDF solutions with LLMs.

## Key Features:

* Document summary.
* Chat with documents.
* Get images from documents and provide descriptions.

## Examples:

Currently, the following copilots available:

**OpenAI Summary** allows users to generate summaries from documents. It provides a convenient way to create summaries by configuring options such as the model, temperature, number of tokens, model instructions, document attachments, and others. The copilot can asynchronously generate summaries as text, as documents, and save the summaries in various formats.The provided demo code showcases the creation of an OpenAI client, the configuration of copilot options, and the usage of the SummaryCopilot to generate and save summaries.

```cs
// Create AI client.
var openAiClient = OpenAIClient
.CreateWithApiKey(ApiKey) // Create OpenAI client with the API key.
.WithProject("proj_123") // Configure optional parameters.
.Build();

// Create copilot options.
var options = OpenAISummaryCopilotOptions
.Create() // Create options like this, or...
//.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate.
.WithTemperature(0.5) // Configure other optional parameters.
.WithDocument("DocumentInputPath") // .WithDocument methods allows to add text, pdf and paths to documents.
.WithDocuments(new List<TextDocument>()); // .WithDocuments methods allows to add text, pdf and path collections.

// Create summary copilot.
var summaryCopilot = AICopilotFactory.CreateSummaryCopilot(openAiClient, options);

// Get summary text.
string summaryText = await summaryCopilot.GetSummaryAsync();

// Get summary document.
Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

// Get summary document with page info.
Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new PageInfo());

// Save summary as PDF document.
await summaryCopilot.SaveSummaryAsync("outputPath");
```

**OpenAI Chat** is an AI copilot designed for chat interactions with documents. It facilitates generating responses to user queries and managing context. Users can configure the copilot options, such as the model, temperature, number of tokens, model instructions, document attachments, and others. The copilot can provide responses to single or multiple queries, save responses in various formats, save and delete the context.

The provided code demonstrates the creation of an OpenAI client, configuration of ChatCopilot options, and usage of the ChatCopilot to interact with user queries and manage context.

```cs
// Create AI client.
var openAiClient = OpenAIClient
.CreateWithApiKey(ApiKey) // Create OpenAI client with the API key.
.WithProject("proj_123") // Configure optional parameters.
.WithOrganization("org_123")
.Build(); // Build.

// Create copilot options.
var options = OpenAIChatCopilotOptions
.Create() // Create options like this, or...
//.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate.
.WithModel(OpenAIModels.Gpt35Turbo) // Configure other optional parameters.
.WithTemperature(0.5)
.WithTopP(1)
.WithDocument("DocumentInputPath") // Attach documents using .WithDocument(s) methods allows to add text, pdf and paths to documents.
.WithContextBackupJsonPath("PathToContextBackup") // Supply context backup to resume the conversation session.
.WithRestoreContextFromBackup(true); // If set to true, the context

// Create summary copilot.
var chatCopilot = AICopilotFactory.CreateChatCopilot(openAiClient, options);

// Get response on a user query.
string copilotResponse1 = await chatCopilot.GetResponseAsync("user message");

// Get response on a list of queries.
string copilotResponse2 = await chatCopilot.GetResponseAsync(new List<string>
{
"message1",
"message2"
});

// Save summary as PDF document.
await chatCopilot.SaveResponseAsync("message1", "outputPath");

// Save summary as PDF document.
await chatCopilot.SaveResponseAsync(new List<string>
{
"message1",
"message2"
}, "outputPath");
```

**OpenAI Image Description** is an AI copilot designed for generating image descriptions of images inside PDF documents as well as separate image files. Users can configure the copilot options, such as the model, temperature, number of tokens, model instructions, document attachments, and others. The copilot provides the ability to get image descriptions for all attached documents at once.

The provided code snippet demonstrates the creation of an OpenAI client, configuration of ImageDescriptionCopilot options, and usage of the copilot to obtain image descriptions for attached documents. Additionally, there is an extension method that allows adding image descriptions to images in the attached documents and saving new documents in the provided directory.

```cs
// Create AI client.
var openAiClient = OpenAIClient
.CreateWithApiKey(ApiKey) // Create OpenAI client with the API key.
.WithProject("proj_123") // Configure optional parameters.
.WithOrganization("org_123")
.Build(); // Build.

// Create copilot options.
var options = OpenAIImageDescriptionCopilotOptions
.Create() // Create options like this, or...
//.Create(options => { options.Model = OpenAIModels.Gpt35Turbo; }) // ...create using delegate.
.WithModel(OpenAIModels.Gpt35Turbo) // Configure other optional parameters.
.WithTemperature(0.5)
.WithTopP(1)
.WithDocument(new PdfDocument // Attach documents.
{
Name = "Another_Pdf_with_images",
Document = new Document(GetInputPath("Pdf_with_images_low_res_bw.pdf"))
})
.WithDocument(GetInputPath("Mona_liza.jpg")) // Attach images
.WithDocument(GetInputPath("Pdf_with_images.pdf")); // Attach document paths.

// Create copilot.
var copilot = AICopilotFactory.CreateImageDescriptionCopilot(openAiClient, options);

// Get Image descriptions.
List<ImageDescriptionResult> imageDescriptions = await copilot.GetImageDescriptionsAsync();

// Use extension method to add image descriptions to attached documents.
await copilot.AddPdfImageDescriptionsAsync("DocumentsOutputDirectory");
```

**Llama Chat** allows the creation of a client to send requests to the Llama chat completion API.

```cs
    var llamaClient = LlamaClient
        .CreateWithApiKey(ApiKey)
        .Build();

    var result = await llamaClient.CreateCompletionAsync(new LlamaChatCompletionRequest
    {
        Messages = new List<ChatMessage>
        {
            ChatMessage.FromUser("Hello!")
        }
    });

    var response = result.Choices[0].Message.Content; // Hello! How can I assist you today?
```

**Llama Summary** allows client can be used to create the Summary Copilot.

```cs
    var llamaClient = LlamaClient
        .CreateWithApiKey(ApiKey) // Create Llama client with the API key.
        .Build();
    
    // Create copilot options.
    var options = LlamaSummaryCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = LlamaModels.Llama13BChat; }) // ...create using delegate.
        .WithTemperature(0.5) // Configure other optional parameters.
        .WithDocument("DocumentInputPath") // .WithDocument methods allow to add text, pdf, and paths to documents.
        .WithDocuments(new List<TextDocument>()); // .WithDocuments methods allow to add text, pdf and path collections.

    // Create summary copilot.
    var summaryCopilot = AICopilotFactory.CreateSummaryCopilot(llamaClient, options);

    // Get summary text.
    string summaryText = await summaryCopilot.GetSummaryAsync();

    // Get summary document.
    Document summaryDocument = await summaryCopilot.GetSummaryDocumentAsync();

    // Get the summary document with page info.
    Document summaryDocumentWithPageInfo = await summaryCopilot.GetSummaryDocumentAsync(new PageInfo());

    // Save the summary as a PDF document.
    await summaryCopilot.SaveSummaryAsync("outputPath");

    // Save summary with specified format.
    await summaryCopilot.SaveSummaryAsync("outputPath", SaveFormat.DocX);
```
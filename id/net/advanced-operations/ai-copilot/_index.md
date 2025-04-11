---
title: PDF AI Copilot
linktitle: PDF AI Copilot
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 150
url: /id/net/ai-copilot/
description: Artikel ini menjelaskan bagaimana AI Copilot dapat digunakan untuk memproses dokumen PDF dengan pustaka Aspose.PDF.
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
    "abstract": "Fitur PDF AI Copilot memanfaatkan teknologi AI canggih untuk meningkatkan pemrosesan dokumen melalui fungsionalitas seperti ringkasan dokumen, kemampuan obrolan interaktif dengan konten PDF, dan menghasilkan deskripsi gambar dari dokumen. API inovatif ini menyederhanakan cara pengguna berinteraksi dengan dan mengekstrak wawasan dari dokumen PDF, menjadikannya alat penting untuk meningkatkan produktivitas dan keterlibatan pengguna.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2604",
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
    "dateModified": "2025-04-08",
    "description": "Fitur PDF AI Copilot memberdayakan pengguna untuk meningkatkan pemrosesan dokumen PDF dengan mengintegrasikan kemampuan AI canggih, termasuk ringkasan dokumen, fungsionalitas obrolan interaktif, dan generasi deskripsi gambar, menyederhanakan alur kerja dan meningkatkan produktivitas. API inovatif ini memfasilitasi interaksi yang mulus dengan konten PDF, menjadikannya alat penting bagi pengembang dan bisnis yang ingin mengoptimalkan manajemen dokumen."
}
</script>

{{% alert color="primary" %}}
**Aspose.PDF AI Copilot API** dirancang untuk memungkinkan pengguna memproses dokumen PDF menggunakan LLM dari berbagai penyedia. [API](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/) ini akan membantu pengguna dalam membangun aplikasi chatbot dan mengintegrasikan solusi PDF dengan LLM.
{{% /alert %}}

## Fitur Utama

* Ringkasan dokumen.
* Obrolan dengan dokumen.
* Dapatkan gambar dari dokumen dan berikan deskripsi.

## Contoh

Saat ini, copilots berikut tersedia:

[**OpenAI Summary**](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/openaisummarycopilot/) memungkinkan pengguna untuk menghasilkan ringkasan dari dokumen. Ini menyediakan cara yang nyaman untuk membuat ringkasan dengan mengonfigurasi opsi seperti model, suhu, jumlah token, instruksi model, lampiran dokumen, dan lainnya. Copilot dapat secara asinkron menghasilkan ringkasan sebagai teks, dokumen, dan menyimpan ringkasan dalam berbagai format. Kode demo yang disediakan menunjukkan pembuatan klien OpenAI, konfigurasi opsi copilot, dan penggunaan SummaryCopilot untuk menghasilkan dan menyimpan ringkasan.

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

[**OpenAI Chat**](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/openaichatcopilot/) adalah copilot AI yang dirancang untuk interaksi obrolan dengan dokumen. Ini memfasilitasi pembuatan respons terhadap pertanyaan pengguna dan pengelolaan konteks. Pengguna dapat mengonfigurasi opsi copilot, seperti model, suhu, jumlah token, instruksi model, lampiran dokumen, dan lainnya. Copilot dapat memberikan respons terhadap satu atau beberapa pertanyaan, menyimpan respons dalam berbagai format, menyimpan dan menghapus konteks.

Kode yang disediakan menunjukkan pembuatan klien OpenAI, konfigurasi opsi ChatCopilot, dan penggunaan ChatCopilot untuk berinteraksi dengan pertanyaan pengguna dan mengelola konteks.

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

[**OpenAI Image Description**](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/openaiimagedescriptioncopilot/) adalah copilot AI yang dirancang untuk menghasilkan deskripsi gambar dari gambar di dalam dokumen PDF serta file gambar terpisah. Pengguna dapat mengonfigurasi opsi copilot, seperti model, suhu, jumlah token, instruksi model, lampiran dokumen, dan lainnya. Copilot memberikan kemampuan untuk mendapatkan deskripsi gambar untuk semua dokumen yang dilampirkan sekaligus.

Potongan kode yang disediakan menunjukkan pembuatan klien OpenAI, konfigurasi opsi ImageDescriptionCopilot, dan penggunaan copilot untuk memperoleh deskripsi gambar untuk dokumen yang dilampirkan. Selain itu, ada metode ekstensi yang memungkinkan menambahkan deskripsi gambar ke gambar dalam dokumen yang dilampirkan dan menyimpan dokumen baru di direktori yang disediakan.

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

**OpenAI OCR** adalah copilot AI yang dirancang untuk mengekstrak teks dari dokumen dan gambar yang dipindai. Pengguna dapat mengonfigurasi opsi copilot, seperti model, suhu, jumlah token, instruksi model, lampiran dokumen, dan lainnya.

Potongan kode yang disediakan menunjukkan pembuatan klien OpenAI, konfigurasi opsi ```OpenAIOcrCopilotOptions```, dan penggunaan copilot untuk memperoleh teks dari dokumen dan gambar yang dipindai.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ExtractText()
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
        var options = Aspose.Pdf.AI.OpenAIOcrCopilotOptions
            .Create() // Create options like this, or...
            //.Create(options => { options.Model = OpenAIModels.Gpt4OMini; }) // ...create using delegate
            .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt4OMini) // The model should have vision capabilities
            .WithDocument(dataDir + "ScannedDocument.pdf") // Attach document paths
            .WithDocument(dataDir + "ImageWithText.jpg"); // Attach images

        // Create copilot
        Aspose.Pdf.AI.IOcrCopilot copilot = Aspose.Pdf.AI.AICopilotFactory.CreateOcrCopilot(openAiClient, options);

        // Get text recognitions
        List<Aspose.Pdf.AI.TextRecognitionResult> textRecognitions = await copilot.GetTextRecognitionResultAsync();

        // Access to the extracted text
        string text = textRecognitions[0].OcrDetails[0].ExtractedText;
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static async Task ExtractText()
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
    var options = Aspose.Pdf.AI.OpenAIOcrCopilotOptions
        .Create() // Create options like this, or...
        //.Create(options => { options.Model = OpenAIModels.Gpt4OMini; }) // ...create using delegate
        .WithModel(Aspose.Pdf.AI.OpenAIModels.Gpt4OMini) // The model should have vision capabilities
        .WithDocument(dataDir + "ScannedDocument.pdf") // Attach document paths
        .WithDocument(dataDir + "ImageWithText.jpg"); // Attach images

    // Create copilot
    Aspose.Pdf.AI.IOcrCopilot copilot = Aspose.Pdf.AI.AICopilotFactory.CreateOcrCopilot(openAiClient, options);

    // Get text recognitions
    List<Aspose.Pdf.AI.TextRecognitionResult> textRecognitions = await copilot.GetTextRecognitionResultAsync();

    // Access to the extracted text
    string text = textRecognitions[0].OcrDetails[0].ExtractedText;
}
```
{{< /tab >}}
{{< /tabs >}}

[**Llama Chat**](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/llamaclient/) memungkinkan pembuatan klien untuk mengirim permintaan ke API penyelesaian obrolan Llama.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

[**Llama Summary**](https://reference.aspose.com/pdf/id/net/aspose.pdf.ai/llamaclient/) memungkinkan klien digunakan untuk membuat Summary Copilot.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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
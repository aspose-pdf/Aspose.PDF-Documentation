---
title: Using Aspose.PDF ChatGPT for .NET plugin
type: docs
weight: 10
url: /net/plugins/chatGPT/
description: You should work with Aspose.PDF for .NET with Coldfusion using PdfFileInfo Class
lastmod: "2024-01-24"
draft: true
---

{{% alert color="primary" %}}

In this article, we will explain how to use Aspose.PDF for .NET with Coldfusion. It’ll help you understand the details of Aspose.PDF for .Net and Coldfusion integration. With the help of a simple example, I’ll show you the process of incorporating the functionality of Aspose.PDF for .Net into your Coldfusion applications.

{{% /alert %}}

```csharp
    var options = new PdfChatGptRequestOptions();
    options.AddInput(new FileDataSource("sample.pdf"));
    options.AddOutput(new FileDataSource("chat_results.pdf"));
    options.ApiKey = "Your API key.";
    options.MaxTokens = 1000;
    options.Query = "What are the best keywords for this text?";
    var plugin = new PdfChatGpt();
    var result = await plugin.ProcessAsync(options);
    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion;
    await Console.Out.WriteLineAsync(fileResultPath.ToString());
    await Console.Out.WriteLineAsync(chatCompletionObject?.ToString());
```
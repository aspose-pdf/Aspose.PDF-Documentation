---
title: ASP.NET without using Visual Studio
type: docs
weight: 60
url: /net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) can be used to develop ASP.NET pages or applications without using Visual Studio. In this example, we’ll write HTML and the C# or VB.NET code in a single .aspx file; this is commonly known as Instant ASP.NET.

{{% /alert %}}

## Implementation details

{{% alert color="primary" %}}

Create a sample web application and copy Aspose.PDF.dll into a directory named "Bin" in your website directory ( *if bin folder does not exist, create one* ). Then create your .aspx page and copy the following code into it.
This example shows how to use [Aspose.PDF for .NET](/pdf/net/) with inline code in an ASP.NET page in order to create a simple PDF document with some sample text inside it.
{{% /alert %}}

```cs
<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> using Aspose.PDF for .NET with Inline ASP.NET</title>
    </head>
    <body>
        <h3>creation of simple PDF document while using Aspose.PDF for .NET with Inline ASP.NET</h3>
<%
    // set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Initialize document object
    Document document = new Document();
    // Add page
    Page page = document.Pages.Add();
    // Add text to new page
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
    // Save updated PDF
    var outputFileName = dataDir + "HelloWorld_out.pdf";
    document.Save(outputFileName);
%>

    </body>
</html>
```

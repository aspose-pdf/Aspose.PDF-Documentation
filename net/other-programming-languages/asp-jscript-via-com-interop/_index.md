---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

This is a simple ASP application that shows you how to add simple text string to PDF file using [Aspose.PDF for .NET](/pdf/net/) and JScript via COM Interop.

{{% /alert %}}

Example:

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> using Aspose.PDF for .NET in classical ASP sample</title>
    </head>
    <body>
        <h3>creation of sample PDF document while using Aspose.PDF for .NET with classical ASP and JScript</h3>
<%
// set license
var lic = Server.CreateObject("Aspose.Pdf.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instantiate Pdf instance by calling its empty constructor
var pdf = Server.CreateObject("Aspose.Pdf.Document");

// Create a new Page in the PDF object
var pdfpage = pdf.Pages.Add();

// Create Text Fragment object
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Assign some content to the Fragment
sampleText.Text =  = "HelloWorld using ASP and JScript";

// Add Text paragraph to paragraphs collection of a section
pdfpage.Paragraphs.Add(SampleText);

// Save the PDF document
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```

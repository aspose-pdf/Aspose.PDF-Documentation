---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Sometimes you might wish to export text in textboxes with formatting. Unfortunately, Reporting Services does not support this. However, you still can implement it using Aspose.PDF for Reporting Services. Just enable a special mode in which all text in textboxes is treated as HTML and put the necessary HTML tags to format the text in the output document. For example, to have normal, bold and italic text in the same textbox, enter the following textbox value:

Some of this text is ```<b>bold</b>``` and other text is ```<i>italic</i>```.

When exported, the text will look like as some of this text is **bold** and other text is *italic*.

Please note that this approach has some limitations

{{% /alert %}}

{{% alert color="primary" %}}

- The formatting isn’t visible in design time (in the Report Builder, Reporting Services web portal etc.). Instead, you will see the HTML text in form of plain text with tags.
- Aspose.PDF for Reporting Services rendering extension recognizes and properly formats HTML code in textboxes. The default PDF renderer of Reporting Services will export this markup as plain text.

**Parameter Name**: IsHtmlTagSupported  
**Date Type**: Boolean  
**Values supported**: True, False (default)   

**Example**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

If you want to add this parameter in the Report Designer, use the 'Boolean' data type.

 
Currently Aspose.Pdf for Reporting Services supports a subset of all the HTML tags. You may find more information in the Aspose.PDF [Documentation](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

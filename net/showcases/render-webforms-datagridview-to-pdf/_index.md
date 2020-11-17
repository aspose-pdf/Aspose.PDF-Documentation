---
title: Render WebForms DataGridView to PDF
type: docs
weight: 20
url: /net/render-webforms-datagridview-to-pdf/
---
# How to export WebForm to PDF using Aspose.PDF/Aspose.HTML

## Introduction

Generally, to convert WebForm to PDF document uses additional tools. This sample shows how to use Aspose.PDF library to render WebForm to PDF. The Aspose Export GridView To Pdf Control is also included in this sample to show how to render _GridView control to PDF document._

## How to render WebForm to PDF

The original idea for render WebForm to PDF is to create helper class, which inherited from [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), and overriding a Render method.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

There are two Aspose tools can be used for render HTML to PDF:

- Aspose.PDF for .NET
- Aspose Export GridView control (based on Aspose.PDF)

## Source Files
In this sample we have 2 demo reports.

- _Default.aspx_ demonstrate export to PDF using Aspose.PDF
- _Report2.aspx_ demonstrate export to PDF using Aspose Export GridView control (based on Aspose.PDF)

## Additional files
`Helpers\PdfPage.cs` - contains a helper class, which shows how to use Aspose.PDF API.</em>

The Aspose.Pdf.GridViewExport project contains extened GridView control for demonstration in `Report2.aspx`

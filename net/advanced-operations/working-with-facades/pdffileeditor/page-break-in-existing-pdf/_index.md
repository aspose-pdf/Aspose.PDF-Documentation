---
title: Page Break in existing PDF
type: docs
weight: 70
url: /net/page-break-in-existing-pdf/
description: This section explains how to break pages in an existing PDF using PdfFileEditor class.
lastmod: "2021-01-18"
draft: false
---

As a default layout, the contents inside PDF files are added in Top-Left to Bottom-Right layout. Once the contents exceed beyond page bottom margin, the page break occurs. However you may come across a requirement to insert page break depending upon requirement. A method named AddPageBreak(...) method is added in [PdfFileEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class to accomplish this requirement.

1. public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)
1. public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)
1. public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)

- src is source document/path to document/stream with source document;
- dest is destination document/path where document will be saved/stream where document will be saved.;
- PageBreak is array of page break objects. It have two properties: index of page where page break must be placed and vertical position of the page break on the page.

### **Example-1**


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Working-Document-PageBreak-PageBreak.cs" >}}
### **Example-2**


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Working-Document-PageBreak-PageBreakWithDestPath.cs" >}}
### **Example-3**


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Working-Document-PageBreak-PageBreakWithStream.cs" >}}

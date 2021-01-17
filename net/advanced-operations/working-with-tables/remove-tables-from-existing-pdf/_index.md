---
title: Remove Tables from existing PDF
type: docs
weight: 20
url: /net/remove-tables-from-existing-pdf/
lastmod: "2021-01-16"
---

{{% alert color="primary" %}}

Aspose.PDF for NET offers the capabilities to insert/create Table inside PDF document while its being generated from scratch or you can also add the table object in any existing PDF document. However you may have a requirement to [Manipulate Tables in existing PDF](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) where you can update the contents in existing table cells. However you may come across a requirement to remove table objects from existing PDF document.

{{% /alert %}}

In order to remove the tables, we need to use [TableAbsorber](https://apireference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) class to get hold of tables in existing PDF and then call [Remove](https://apireference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

```csharp
public static void Remove_Table()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-Java
    PdfAnnotationEditor editor = new PdfAnnotationEditor();
    editor.BindPdf("table2.pdf");
    // Create TableAbsorber object to find tables
    TableAbsorber absorber = new TableAbsorber();
    // Visit first page with absorber
    absorber.Visit(editor.Document.Pages[1]);
    // Remove first table 
    absorber.Remove(absorber.TableList[0]);            
}
```

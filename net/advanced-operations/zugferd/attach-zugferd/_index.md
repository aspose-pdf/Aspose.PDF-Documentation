---
title: Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#
linktitle: Attach ZUGFeRD to PDF
type: docs
weight: 10
url: /net/attach-zugferd/
description: Learn how to generate a PDF document with ZUGFeRD in Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Attach ZUGFeRD to PDF

The next code snippet also works with a new graphical [Aspose.Drawing](/pdf/net/drawing/) interface.

We recommend following steps to attach ZUGFeRD to PDF:

* Define a path variable that points to a folder where the input and output PDF files are located.
* Create a document object by loading an existing PDF file (e.g. "ZUGFeRD-test.pdf") from the path.
* Create a [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) object by providing the path and description of another file named "factur-x.xml", which contains invoice metadata conforming to the ZUGFeRD standard.
* Add properties to the file specification object, such as the description, MIME type, and AF relationship. The AF relationship indicates how the embedded file is related to the PDF document. In this case, it is set to "Alternative", meaning the embedded file is an alternative representation of the PDF content.
* Add the file specification object to the document's embedded files collection. File name should be specified to ZUGFeRD standard, e.g. "factur-x.xml".
* Convert the document to PDF/A-3U format, a subset of PDF that ensures the long-term preservation of electronic documents. PDF/A-3U allows embedding files of any format in PDF documents.
* Save the converted document as a new PDF file (e.g. "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Setup new file to be added as attachment
var description = "Invoice metadata conforming to ZUGFeRD standard";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Add attachment to document's attachment collection
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```

The convert method takes a stream, a PDF format, and a convert error action as parameters. The stream parameter can be used to save the conversion log. The convert error action parameter specifies what to do if any errors occur during the conversion. In this case, it is set to "Delete", which means that any elements that are not compliant with the PDF/A-3U format will be deleted from the document.

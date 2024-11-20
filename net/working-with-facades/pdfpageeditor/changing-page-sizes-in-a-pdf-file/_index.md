---
title: Changing page sizes in PDF file
type: docs
weight: 30
url: /net/changing-page-sizes-in-a-pdf-file/
description: Try to learn how to change page sizes in a PDF file using PdfPageEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Implementation details

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class in [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) contains a property named [PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) which can be used to change the page size of an individual page or multiple pages at once. The Pages property can be used to assign the numbers of the pages on which the new page size needs to be applied. PageSize class contains a list of different page sizes as its members. Any of the members of this class can be assigned to PageSize property of the [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class. You can also get page size of any page using GetPageSize method and passing the page number.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangePageSizes-ChangePageSizes.cs" >}}

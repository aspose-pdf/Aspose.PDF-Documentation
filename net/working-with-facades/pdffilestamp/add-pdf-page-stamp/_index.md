---
title: Add PDF Page Stamp
type: docs
weight: 10
url: /net/add-pdf-page-stamp/
description: This section explains how to work with Aspose.PDF Facades using PdfFileStamp Class.
lastmod: "2021-01-20"
draft: false
---

## Add PDF Page Stamp on All Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add PDF page stamp on all the pages of a PDF file. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the PDF page stamp using [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)  method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add PDF page stamp on all pages in a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddPageStampAll-AddPageStampAll.cs" >}}

## Add PDF Page Stamp on Particular Pages in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add PDF page stamp on particular pages of a PDF file. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) classes. You also need to create the PDF page stamp using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method of [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) object as well. As you want to add PDF page stamp on particular pages of the PDF file, you also need to set the [Pages](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://apireference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add PDF page stamp on particular pages in a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddPageStampPage-AddPageStampPage.cs" >}}

## Add Page Number in a PDF File

[PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class allows you to add page numbers in a PDF file. In order to add page numbers, you first need to create object of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class. In order to get the current page number you can use **#** sign in your text anywhere you like. You can format the page number text using [FormattedText](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. If you want to start the page numbering from a specific number then you can set [StartingNumber](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) property. Once you’re ready to add page number in the file, you need to call [AddPageNumber](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add page number in a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddPageNumber-AddPageNumber.cs" >}}

### Custom Numbering style

The PdfFileStamp class offers the feature to add Page Number information as stamp object inside PDF document. Prior to this release, the class only supported 1,2,3,4 as page numbering style. However, there has been a requirement from some customers to use custom numbering style when placing page number stamp inside PDF document. In order to accomplish this requirement, [NumberingStyle](https://apireference.aspose.com/pdf/net/aspose.pdf/numberingstyle) property has been introduced, which accepts the values from [NumberingStyle](https://apireference.aspose.com/pdf/net/aspose.pdf/numberingstyle) enumeration. Specified below are values offered in this enumeration.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-AddPageNumber-CustomNumberStyle.cs" >}}

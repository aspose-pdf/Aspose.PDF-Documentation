---
title: Convert PDF Pages
type: docs
weight: 20
url: /net/convert-pdf-pages/
---

## Convert PDF Pages to Different Image Formats (Facades)

In order to convert PDF pages to different image formats, you need to create **PdfConverter** object and open the PDF file using **BindPdf** method. After that, you need to call **DoConvert** method for initialization tasks. Then, you can loop through all the pages using **HasNextImage** and **GetNextImage** methods. The **GetNextImage** method allows you to create image of a particular page. You also need to pass ImageFormat to this method in order to create an image of specific type i.e. JPEG, GIF or PNG etc. Finally, call the **Close** method of the **PdfConverter** class. The following code snippet shows you how to convert PDF pages to images.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Images-ConvertPDFPages-ConvertPDFPages.cs" >}}
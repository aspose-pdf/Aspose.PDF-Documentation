---
title: Working with Facades
type: docs
weight: 112
url: /java/working-with-facades/
description: This section explains how to work with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-05-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---


## <ins>**Extract Images from the Whole PDF to Files (facades)**
[PdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class allows you to extract images from a PDF file. First off, you need to create an object of [PdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractImage--) class and bind input PDF file using bindPdf method. After that, call [extractImage](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/pdfextractor/methods/extractImage\(\)/) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Images-ExtractImagesFromTheWholePDFToFiles-.java" >}}
## <ins>**Extract Chart objects from PDF document (facades)**
The PDF allow to group page content into elements named as **Marked Content**. Adobe Acrobat shows them as "containers". The Chart objects are placed in such objects. We have introduced a new method extractMarkedContentAsImages() in PdfExtractor class to extract these object. This method render every **Marked Content** into a separate image. Please note all the charts are not fully placed into one container. Because of this some charts will be saved into separate images by parts.

Please note that the correct grouping of content into containers is the responsibility of a PDF document designer. If you want to get charts with header or other objects you should either edit/create the PDF document where whole chart is placed in one container.

**Java**

{{< highlight java >}}

 //Open document

Document document = new Document("sample.pdf");

//instantiate PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extract Chart objects as image in a folder

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();

{{< /highlight >}}



## <ins>**Extract Text from the Whole PDF File (facades)**
[pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class allows you to extract text from the whole PDF file. You need to create an object of [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class and bind the input PDF file using [**bindPdf**](http://www.aspose.com/api/java/pdf/com.aspose.pdf.facades/classes/pdfextractor/methods/bindPdf\(java.lang.String\)/) method. [extractText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractText--) method helps you extract all the text into the memory. However, in order to get the text, you need to use getText method. The following code snippet shows you how to extract text from the whole PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromTheWholePDFFile-.java" >}}
## <ins>**Extract Text from a Range of Pages (facades)**
You can use [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class to extract text from a range of pages. First of all, you need to create a [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) object and bind the PDF file using [**bindPdf**](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) method. After that, you need to set setStartPage and setEndPage properties to specify the range from which the text needs to be extracted. Finally, you need to extract all the text into memory using [extractText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#extractText-java.nio.charset.Charset-) method and then get the extracted text using getText method.

The following code snippet shows you how to extract text from a range of pages of a PDF file



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromARangeOfPages-.java" >}}
## <ins>**Extract Text from Individual Pages of a PDF (facades)**
In order to extract text from individual pages, you can use [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class. This class provides two methods hasNextPageText and [getNextPageText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#getNextPageText-java.io.OutputStream-) which help retrieve the text from individual pages. First, you need to create an object of [pdfExtractor](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using method. After that, you need to extract the text into memory using extractText method. Finally, you have to navigate through all the pages using HasNextPageText method and get the text of individual pages using [getNextPageText](https://apireference.aspose.com/java/pdf/com.aspose.pdf.facades/PdfExtractor#getNextPageText-java.io.OutputStream-) method. The following code snippet shows you how to extract text from individual pages of a PDF file.



{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Text-ExtractTextFromIndividualPagesOfAPDF-.java" >}}
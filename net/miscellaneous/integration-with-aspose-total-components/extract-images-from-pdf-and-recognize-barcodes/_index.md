---
title: Extract Images from PDF and recognize BarCodes
type: docs
weight: 20
url: /net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

The PDF documents are usually comprised of Text, Image, Table, Attachments, Graph, Annotation and other related objects. There are cases when Barcodes are embedded inside PDF file and some customers have the requirement to identify the Barcodes present inside the PDF file. The following article explains the steps on how to extract images from PDF pages and identify the Barcodes inside them.

{{% /alert %}}

According to Document Object Model of Aspose.PDF for .NET, a PDF file contains one or more pages where each page contains collection of Images, Forms and Fonts in Resources object. So in order to extract images from PDF file, we will traverse through individual pages of PDF file, get the collection of Images from particular page and save them in MemoryStream object for further processing with BarCodeReader class of Aspose.BarCodeRecognition.

**C#**

```csharp
// Open document
Aspose.PDF.Document document = new Aspose.PDF.Document("source.pdf");

// Traverse through individual pages of PDF file
for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
{
    // Traverse through each image extracted from PDF pages
    foreach (XImage xImage in document.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            // Save output image
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // Set the stream position to the begining of Stream
            imageStream.Position = 0;
   
            // Instantiate BarCodeReader object
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // Get BarCode text from BarCode image
                string code = barcodeReader.GetCodeText();
   
                // Write the BarCode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }
   
            // Close BarCodeReader object to release the Image file
   
            barcodeReader.Close();
        }
    }
}

```

For further details on topics covered in this article, please visit the following links

- [Extract Images from the PDF File](/net/extract-images-from-the-pdf-file/)
- [Read Barcodes](https://docs.aspose.com/barcode/net/read-barcodes/)

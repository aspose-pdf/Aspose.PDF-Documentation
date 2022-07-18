---
title: Add Page Number to PDF with C++
linktitle: Add Page Number
type: docs
weight: 100
url: /cpp/add-page-number/
description: Aspose.PDF for C++ allows you to add Page Number Stamp to your PDF file using PageNumber Stamp class.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to Add Page Numbers to an Existing PDF

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.
**Aspose.PDF for C++** allows you to add page numbers with PageNumberStamp.

The following steps and sample code illustrate how to add page numbering labels to an existing PDF document using the [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) page element to automatically add page numbers to a PDF.

Steps for Adding Page Numbers to an Existing PDF Document:

In order to add page number stamp, you need to create a [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and a [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) object using required properties.

After that, you can call [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) method of the [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) to add the stamp in the PDF.

You can also set the font attributes of the page number stamp.

The following code snippet shows you how to add page numbers in a PDF file.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create page number stamp
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Whether the stamp is background
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Set text properties
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Add stamp to particular page
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Save output document
    document->Save(_dataDir+ outputFileName);
}
```

## Live Example

[Add PDF page numbers](https://products.aspose.app/pdf/page-number) is an online free web application that allows you to investigate how adding page numbers functionality works.

[![How to add page number in pdf using C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Add/Remove Bates numbering

**Bates numbering** (also known as Bates stamping) is used in the legal, medical, and business fields to place identifying numbers and/or date/time-marks on images and documents as they are scanned or processed, for example, during the discovery stage of preparations for trial or identifying business receipts. This process provides identification, protection, and automatic consecutive numbering of the images or documents.

Aspose.PDF has limited support for Bates Numbering for now. This functionality will be updated according to customers' requests.

### How to remove Bates nubmering

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Save output document
    document->Save(_dataDir + outputFileName);
}
```

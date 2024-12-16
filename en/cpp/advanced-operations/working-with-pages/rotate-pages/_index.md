---
title: Rotate PDF Pages Using C++
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with C++.

## Change Page Orientation

Aspose.PDF for C++ allows you to change the page orientation from landscape to portrait and vice versa. To change the page orientation, set the page's MediaBox using the following code snippet. You can also change page orientation by setting rotation angle using Rotate() method.

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        //  We must to move page upper in order to compensate changing page size
        // (lower edge of the page is 0,0 and information is usually placed from the
        //  Top of the page. That's why we move lover edge upper on difference between
        //  Old and new height.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // Sometimes we also need to set CropBox (if it was set in original file)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Setting Rotation angle of page
        page->set_Rotate(Rotation::on90);
    }

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```

## Fitting the Page Content to the New Page Orientation

Please note that when using the above code snippet, some of the document's content might be cut because the page height is decreased. To avoid this, increase width proportionally and leave the height intact. Example of calculations:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // New height the same
        double newHeight = r->get_Height();
        // New width is expanded proportionally to make orientation landscape
        // (we assume that previous orientation is portrait)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Besides the above approach, consider using the PdfPageEditor facade which can apply zoom to the page contents.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Get rectangular region of first page of PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Instantiate PdfPageEditor instance
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Bind source PDF
    ppe->BindPdf(_dataDir + inputFileName);
    // Set zoom coefficient
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Update page size
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Save output file
    document->Save(_dataDir + outputFileName);
}
```
```
---
title: PDFから画像を抽出する
linktitle: PDFから画像を抽出する
type: docs
weight: 20
url: /ja/cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for C++を使用してPDFから画像の一部を抽出する方法。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

また、PDFドキュメントを扱う際に要求されるタスクとして、PDFファイルから画像を抽出することがあります。例えば、多くの素晴らしい画像が含まれたPDFメールを受け取り、それらを個別のファイルとして抽出したい場合があります。

Aspose.PDFライブラリを使用すると、次のコードスニペットでPDFから画像を抽出できます：

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extract a particular image
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Save output image
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```
```
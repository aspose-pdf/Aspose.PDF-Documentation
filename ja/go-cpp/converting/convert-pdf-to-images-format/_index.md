---
title: GoでPDFを画像形式に変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /ja/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: このトピックでは、Aspose.PDF for Go を使用して PDF をさまざまな画像形式（例: TIFF、BMP、JPEG、PNG、SVG）に数行のコードで変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Aspose.PDF for Go を使用した PDF の画像形式への変換ツール
Abstract: Aspose.PDF for Go via C++ は、PDF ドキュメントを JPEG、PNG、BMP、TIFF などのさまざまな画像形式へシームレスに変換できるようにします。この機能により、開発者は元のドキュメントの内容、レイアウト、解像度を保持しながら、高品質な画像をレンダリングできます。このライブラリは、解像度、画像品質、カラーデプスなどの出力設定に対して柔軟なオプションを提供します。ドキュメントには、開発者が PDF から画像への変換をアプリケーションに効率的に統合できるよう、ステップバイステップの手順とコードサンプルが用意されています。
SoftwareApplication: go-cpp
---

## GoでPDFを画像に変換

この記事では、PDFを画像形式に変換するオプションをご紹介します。

以前にスキャンした文書は多くの場合 PDF ファイル形式で保存されています。しかし、画像形式でさらに編集したり送信したりする必要がありますか？ PDF を画像に変換するための汎用ツールとして **Aspose.PDF for Go via C++** をご用意しました。
最も一般的なタスクは、PDF ドキュメント全体またはドキュメントの特定のページを画像セットとして保存する必要がある場合です。**Aspose.PDF for Go via C++** は、PDF を JPG および PNG フォーマットに変換でき、特定の PDF ファイルから画像を取得するために必要な手順を簡素化します。

**Aspose.PDF for Go via C++** は様々な PDF から画像形式への変換をサポートしています。セクションをご確認ください。 [Aspose.PDF がサポートするファイル形式](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## PDF を JPEG に変換する

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをJPEG画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. ページをJPEGに変換するには [ページをJPGに変換](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF を JPEG にオンラインで変換してみよう**

Aspose.PDF for Go はオンラインの無料アプリケーションをご提供します [PDF を JPEG に変換](https://products.aspose.app/pdf/conversion/pdf-to-jpg), そこで、機能と品質がどのように動作するかを調べてみることができます。

[![Aspose.PDF 変換：PDF を JPEG に、無料アプリで](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## PDF を TIFF に変換

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをTIFF画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. ページを TIFF に変換するには [ページをTiffに変換](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF を TIFF にオンラインで変換してみよう**

Aspose.PDF for Go はオンラインの無料アプリケーションをご提供します ["PDF を TIFF に"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), そこで、機能と品質がどのように動作するかを調べてみることができます。

[![Aspose.PDF で PDF を TIFF に変換（無料アプリ）](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## PDFをPNGに変換

提供された Go コードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントの最初のページを PNG 画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. ページを PNG に変換するには [ページをPNGに変換](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで PNG に変換してみてください**

私たちの無料アプリケーションの動作例として、次の機能をご確認ください。

Aspose.PDF for Go はオンラインの無料アプリケーションをご提供します ["PDFからPNGへ"](https://products.aspose.app/pdf/conversion/pdf-to-png), そこで、機能と品質がどのように動作するかを調べてみることができます。

[![無料アプリでPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** は、XML ベースのファイル形式に基づく二次元ベクターグラフィックス（静的および動的（インタラクティブまたはアニメーション））のための仕様群です。SVG 仕様は、1999 年から World Wide Web Consortium（W3C）によって開発が進められているオープンスタンダードです。

## PDF を SVG に変換

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをSVG画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. ページを SVG に変換するには [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで SVG に変換してみましょう**

Aspose.PDF for Go はオンラインの無料アプリケーションをご提供します [PDFからSVGへ](https://products.aspose.app/pdf/conversion/pdf-to-svg), そこで、機能と品質がどのように動作するかを調べてみることができます。

[![Aspose.PDF 無料アプリで PDF を SVG に変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## PDFをDICOMに変換する

提供された Go コードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントの最初のページを DICOM 画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. ページを DICOM に変換するには [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## PDF を BMP に変換

提供されたGoコードスニペットは、Aspose.PDF ライブラリを使用して PDF ドキュメントの最初のページを BMP 画像に変換する方法を示しています。

1. PDFドキュメントを開く。
1. ページを BMP に変換する [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) 関数。
1. PDF ドキュメントを閉じ、割り当てられたリソースを解放してください。

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
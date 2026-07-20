---
title: RustでPDFを画像フォーマットに変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /ja/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: このトピックでは、Aspose.PDF for Rust を使用して、PDF を TIFF、BMP、JPEG、PNG、SVG などのさまざまな画像形式に数行のコードで変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Aspose.PDF for Rust を使用した PDF を画像形式に変換するツール
Abstract: Aspose.PDF for Rust via C++ は、PDF ドキュメントを JPEG、PNG、BMP、TIFF などのさまざまな画像形式にシームレスに変換できる機能を提供します。この機能により、開発者は元のドキュメントのコンテンツ、レイアウト、解像度を保持しながら高品質な画像をレンダリングできます。ライブラリは、解像度、画像品質、カラーデプスなどの出力設定に柔軟なオプションを提供します。ドキュメントには、開発者が PDF から画像への変換をアプリケーションに効率的に統合できるよう、ステップバイステップの手順とコードサンプルが用意されています。
SoftwareApplication: rust-cpp
---

## PDFを画像に変換する

この記事では、PDF を画像形式に変換するオプションをご紹介します。

以前にスキャンされたドキュメントは、PDF ファイル形式で保存されていることが多いです。しかし、グラフィックエディタで編集したり、画像形式でさらに送信する必要がありますか？**Aspose.PDF for Rust via C++** を使用して PDF を画像に変換する汎用ツールをご用意しています。
最も一般的なタスクは、PDFドキュメント全体またはドキュメントの特定のページを画像のセットとして保存する必要がある場合です。**Aspose.PDF for Rust via C++** を使用すると、PDFをJPGおよびPNG形式に変換でき、特定のPDFファイルから画像を取得するために必要な手順を簡素化できます。

**Aspose.PDF for Rust via C++** はさまざまな PDF から画像への形式変換をサポートしています。セクションを確認してください。 [Aspose.PDF 対応ファイル形式](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### PDF を JPEG に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをJPEG画像に変換する方法を示しています:

1. PDFドキュメントを開く。
1. ページをJPEGに変換するには [ページ_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF を JPEG にオンラインで変換してみてください**

Aspose.PDF for Rust は、オンラインの無料アプリケーションをご提供します ["PDFをJPEGに変換"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), そこでは、機能と品質がどのように機能するかを調査しようとすることができます。

[![Aspose.PDF 変換 PDF から JPEG へ 無料アプリで](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### PDF を TIFF に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをTIFF画像に変換する方法を示しています:

1. PDFドキュメントを開く。
1. ページをTIFFに変換するには [ページ_to_TIFF](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF を TIFF にオンラインで変換してみましょう**

Aspose.PDF for Rust は、オンラインの無料アプリケーションをご提供します ["PDF から TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), そこでは、機能と品質がどのように機能するかを調査しようとすることができます。

[![Aspose.PDF 変換 PDF を TIFF に フリー アプリで](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF を PNG に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをPNG画像に変換する方法を示しています:

1. PDFドキュメントを開く。
1. ページをPNGに変換するには [page_to_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF をオンラインで PNG に変換してみて**

無料アプリケーションがどのように動作するかの例として、次の機能をご確認ください。

Aspose.PDF for Rust は、オンラインの無料アプリケーションをご提供します ["PDFからPNGへ"](https://products.aspose.app/pdf/conversion/pdf-to-png), そこでは、機能と品質がどのように機能するかを調査しようとすることができます。

[![無料アプリを使用して PDF を PNG に変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** は、2 次元ベクター グラフィックス用の XML ベースのファイル形式に関する仕様群であり、静的および動的（インタラクティブまたはアニメーション）なものです。SVG 仕様は、1999 年から World Wide Web Consortium (W3C) によって開発が進められているオープンスタンダードです。

### PDF を SVG に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをSVG画像に変換する方法を示しています:

1. PDFドキュメントを開く。
1. Pageを使用してSVGに変換する [page_to_svg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**PDF を SVG にオンラインで変換してみてください**

Aspose.PDF for Rust は、オンラインの無料アプリケーションをご提供します [PDFからSVGへ](https://products.aspose.app/pdf/conversion/pdf-to-svg), そこでは、機能と品質がどのように機能するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリで PDF を SVG に変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### PDF を SVG ZIP アーカイブに変換

以下の例は PDF ドキュメントを SVG アーカイブに変換し、各ページを ZIP コンテナ内の個別の SVG ファイルとして保存します。

1. ソース PDF ドキュメントを開く。
1. ドキュメントをSVGファイルを含むZIPアーカイブとして保存します。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### PDF を DICOM に変換

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをDICOM画像に変換する方法を示しています：

1. PDFドキュメントを開く。
1. Page を DICOM に変換する [page_to_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### PDF を BMP に変換する

提供されたRustコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをBMP画像に変換する方法を示しています。

1. PDFドキュメントを開く。
1. ページを BMP に変換するには [page_to_bmp](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) 関数。

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```
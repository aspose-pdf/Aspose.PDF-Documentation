---
title: GoでPDFをEPUB、TeX、Text、XPSに変換
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: /ja/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: このトピックでは、Go を使用して PDF ファイルを EPUB、LaTeX、テキスト、XPS などの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF を EPUB、TeX、テキスト、XPS に変換するための Golang ツール
Abstract: Aspose.PDF for Go via C++ は、PDF ドキュメントを DOCX、PPTX、HTML、EPUB、SVG などのさまざまなファイル形式に変換する強力な機能を提供します。この機能により、開発者は PDF コンテンツをシームレスに抽出および再利用でき、異なる出力形式間で書式、構造、品質を維持します。ライブラリは、特定の要件に合わせて変換プロセスをカスタマイズできる柔軟なオプションを提供します。ドキュメントには、開発者がアプリケーション内で PDF をファイルに変換する機能を効率的に実装するための包括的なガイドラインとコードサンプルが含まれています。
SoftwareApplication: go-cpp
---

## PDF を EPUB に変換

**<abbr title="Electronic Publication">EPUB</abbr>** は International Digital Publishing Forum (IDPF) の無料でオープンな e‑book 標準です。ファイルの拡張子は .epub です。
EPUBはリフロー可能コンテンツ用に設計されており、EPUBリーダーが特定の表示デバイス向けにテキストを最適化できることを意味します。EPUBは固定レイアウトコンテンツもサポートしています。このフォーマットは、出版社や変換ハウスが社内で使用できる単一のフォーマットであると同時に、配布や販売にも利用できるよう意図されています。Open eBook標準に取って代わります。

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをEPUBに変換する方法を示しています:

1. PDFドキュメントを開く。
1. PDFファイルをEPUBに変換するには [SaveEpub](https://reference.aspose.com/pdf/go-cpp/convert/saveepub/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースをすべて解放します。

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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで EPUB に変換してみてください**

Aspose.PDF for Go はオンラインで無料のアプリケーションを提供します ["PDF を EPUB に"](https://products.aspose.app/pdf/conversion/pdf-to-epub)、そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリでPDFからEPUBへの変換](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## PDFをTeXに変換する

**Aspose.PDF for Go** は PDF を TeX に変換することをサポートしています。
LaTeXファイル形式は、特別なマークアップを備えたテキストファイル形式であり、高品質な組版のためのTeXベースの文書作成システムで使用されます。

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをTeXに変換する方法を示しています：

1. PDFドキュメントを開く。
1. PDF ファイルを TeX に変換するには [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースをすべて解放します。

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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF をオンラインで LaTeX/TeX に変換してみよう**

Aspose.PDF for Go はオンラインで無料のアプリケーションを提供します ["PDFからLaTeXへ"](https://products.aspose.app/pdf/conversion/pdf-to-tex)、そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリでPDFからLaTeX/TeXへの変換](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF を TXT に変換

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをTXTに変換する方法を示しています：

1. PDFドキュメントを開く。
1. PDF ファイルを TXT に変換するには [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースをすべて解放します。

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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**オンラインで PDF をテキストに変換してみてください**

Aspose.PDF for Go はオンラインで無料のアプリケーションを提供します ["PDF をテキストへ"](https://products.aspose.app/pdf/conversion/pdf-to-txt)、そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF 無料アプリでPDFからテキストへの変換](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF を XPS に変換

XPS ファイルタイプは主に Microsoft Corporation の XML Paper Specification に関連付けられています。XML Paper Specification (XPS) は、かつて Metro というコードネームで、Next Generation Print Path (NGPP) のマーケティングコンセプトを包含していた、Microsoft が文書の作成と閲覧を Windows オペレーティングシステムに統合するための取り組みです。

**Aspose.PDF for Go** は PDF ファイルを変換する可能性を提供します <abbr title="XML Paper Specification">XPS</abbr> フォーマット。提示されたコードスニペットを使用して、GoでPDFファイルをXPSフォーマットに変換してみましょう。

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントをXPSに変換する方法を示しています:

1. PDFドキュメントを開く。
1. PDF ファイルを XPS に変換するには [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースをすべて解放します。

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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**PDF を XPS にオンラインで変換してみてください**

Aspose.PDF for Go はオンラインで無料のアプリケーションを提供します ["PDFからXPSへ"](https://products.aspose.app/pdf/conversion/pdf-to-xps)、そこで、機能と品質がどのように動作するかを調査しようとすることができます。

[![Aspose.PDF を使用した PDF から XPS への変換（無料アプリ）](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## PDFをグレースケールPDFに変換

提供されたGoコードスニペットは、Aspose.PDFライブラリを使用してPDFドキュメントの最初のページをグレースケールPDFに変換する方法を示しています：

1. PDFドキュメントを開く。
1. PDFページをグレースケールPDFに変換するには [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) 関数。
1. PDFドキュメントを閉じ、割り当てられたリソースをすべて解放します。

この例では、PDF の特定のページをグレースケールに変換します:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

この例では、PDF ドキュメント全体をグレースケールに変換します:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
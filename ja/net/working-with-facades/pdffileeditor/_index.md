---
title: PdfFileEditor クラス
type: docs
weight: 10
url: ja/net/pdffileeditor-class/
description: このセクションでは、PdfFileEditor クラスを使用して Aspose.PDF Facades を操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF ドキュメントの操作にはさまざまな機能があります。PDF ファイルのページを管理することは、この作業の重要な部分です。Aspose.PDF.Facades はこの目的のために `PdfFileEditor` クラスを提供します。

PdfFileEditor クラスには、個々のページを操作するのに役立つメソッドが含まれています。このクラスはページの内容を編集または操作しません。新しいページを挿入したり、既存のページを削除したり、ページを分割したり、PdfFileEditor を使用してページの配置を指定したりできます。

このクラスが提供する機能は、ファイル編集、PDF 配置、および分割の3つの主要カテゴリに分けることができます。以下でこれらのセクションについて詳しく説明します:

## ファイル編集

このセクションに含めることができる機能には、挿入、追加、削除、連結、抽出があります。 You can insert a new page at a specified location using Insert method, or append the pages at the end of the file. You can also delete any number of pages from the file using Delete method, by specifying an integer array containing the numbers of pages to be deleted. Concatenate method helps you to join pages from multiple PDF files. You can extract any number of pages using Extract method, and save these pages into another PDF file or memory stream.

このセクションでは、このクラスの機能を探り、そのメソッドの目的を説明します。

- [PDF ドキュメントの連結](/pdf/net/concatenate-pdf-documents/)
- [PDF ページの抽出](/pdf/net/extract-pdf-pages/)
- [PDF ページの挿入](/pdf/net/insert-pdf-pages/)
- [PDF ページの削除](/pdf/net/delete-pdf-pages/)

## ページブレークの使用

ページブレークは、ドキュメントの再流れを可能にする特別な機能です。

- [既存のPDFでのページブレーク](/pdf/net/page-break-in-existing-pdf/)

## PDF 面付け

面付けは、印刷前にページを正しく配置するプロセスです。 `PdfFileEditor`は、この目的のために2つのメソッド、すなわち`MakeBooklet`と`MakeNUp`を提供します。MakeBookletメソッドは、印刷後に折りたたんだり製本したりしやすくするためにページを配置するのに役立ちますが、MakeNUpメソッドはPDFファイルの1ページに複数のページを印刷することを可能にします。

- [PDFのブックレットを作成する](/pdf/net/make-booklet-of-pdf/)
- [PDFファイルのNUpを作成する](/pdf/net/make-nup-of-pdf-files/)

## 分割

分割機能により、既存のPDFファイルを異なる部分に分割できます。PDFファイルの前部または後部を分割することができます。PdfFileEditorは分割のためのさまざまなメソッドを提供しているため、ファイルを個々のページや複数ページのセットに分割することも可能です。

- [PDFページを分割する](/pdf/net/split-pdf-pages/)
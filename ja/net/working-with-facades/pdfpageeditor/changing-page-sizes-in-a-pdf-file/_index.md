---
title: PDFファイルのページサイズを変更する
type: docs
weight: 30
url: ja/net/changing-page-sizes-in-a-pdf-file/
description: PdfPageEditorクラスを使用してPDFファイルのページサイズを変更する方法を学びましょう。
lastmod: "2021-06-05"
draft: false
---

## 詳細

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor)クラスは、[Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)にあり、[PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize)という名前のプロパティを含んでいます。このプロパティを使用すると、個々のページまたは複数のページのページサイズを一度に変更できます。 Pages プロパティは、新しいページサイズを適用する必要があるページの番号を割り当てるために使用できます。PageSize クラスには、そのメンバーとしてさまざまなページサイズのリストが含まれています。このクラスのメンバーのいずれかを [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスの PageSize プロパティに割り当てることができます。また、GetPageSize メソッドを使用してページ番号を渡すことで、任意のページのページサイズを取得することもできます。



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ChangePageSizes-ChangePageSizes.cs" >}}
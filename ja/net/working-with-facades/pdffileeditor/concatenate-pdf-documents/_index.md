---
title: C#でPDFドキュメントを結合する
linktitle: PDFドキュメントを結合する
type: docs
weight: 20
url: ja/net/concatenate-pdf-documents/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDF FacadesでPDFドキュメントを結合する方法を説明します。
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

## **概要**

この記事では、異なるPDFファイルを1つのPDFにマージ、結合、または連結する方法をC#で説明します。以下のトピックをカバーしています。

- [C#でPDFファイルをマージする](#concatenate-pdf-files-using-file-paths)
- [C#でPDFファイルを結合する](#concatenate-pdf-files-using-file-paths)

- [C#で複数のPDFファイルを1つのPDFにマージする](#concatenate-array-of-pdf-files-using-file-paths)
- [C# 複数のPDFファイルを1つのPDFに結合](#concatenate-array-of-pdf-files-using-file-paths)
- [C# フォルダ内のすべてのPDFファイルを結合](#concatenating-all-pdf-files-in-particular-folder)
- [C# フォルダ内のすべてのPDFファイルを結合](#concatenating-all-pdf-files-in-particular-folder)
- [C# ファイルパスを使用してPDFファイルを結合](#concatenate-pdf-files-using-file-paths)
- [C# ストリームを使用してPDFファイルを結合](#concatenate-array-of-pdf-files-using-streams)
- [C# フォルダ内のすべてのPDFファイルを連結](#concatenate-pdf-files-in-folder)

## ファイルパスを使用してPDFファイルを連結

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)は、複数のPDFファイルを連結することを可能にする[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)内のクラスです。 ファイルを FileStreams を使用して連結するだけでなく、MemoryStreams を使用して連結することもできます。この記事では、MemoryStreams を使用してファイルを連結するプロセスについて説明し、コードスニペットを使用して示します。

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスの [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) メソッドを使用して、2 つの PDF ファイルを連結することができます。[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) メソッドでは、3 つのパラメータを渡すことができます: 最初の入力 PDF、2 番目の入力 PDF、および出力 PDF。最終的な出力 PDF には、両方の入力 PDF ファイルが含まれます。

次の C# コードスニペットは、ファイルパスを使用して PDF ファイルを連結する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

場合によっては、アウトラインが多い場合、ユーザーは CopyOutlines を false に設定してアウトラインを無効にし、連結のパフォーマンスを向上させることがあります。
{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## MemoryStreamを使用して複数のPDFファイルを結合する

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスの [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) メソッドは、ソースPDFファイルと宛先PDFファイルをパラメータとして受け取ります。これらのパラメータはディスク上のPDFファイルへのパスであるか、またはMemoryStreamである可能性があります。この例では、最初にディスクからPDFファイルを読み取るための2つのファイルストリームを作成します。そして、これらのファイルをバイト配列に変換します。PDFファイルのこれらのバイト配列はMemoryStreamに変換されます。PDFファイルからMemoryStreamを取得したら、それらを結合メソッドに渡して1つの出力ファイルにマージできるようになります。

以下のC#コードスニペットは、MemoryStreamを使用して複数のPDFファイルを結合する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## ファイルパスを使用してPDFファイルの配列を連結する

複数のPDFファイルを連結したい場合は、PDFファイルの配列を渡すことができる[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドのオーバーロードを使用できます。最終的な出力は、配列内のすべてのファイルから作成されたマージファイルとして保存されます。次のC#コードスニペットは、ファイルパスを使用してPDFファイルの配列を連結する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## ストリームを使用してPDFファイルの配列を連結する

PDFファイルの配列を連結することは、ディスク上に存在するファイルに限定されません。 配列のPDFファイルをストリームから連結することもできます。複数のPDFファイルを連結したい場合は、[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドの適切なオーバーロードを使用できます。まず、入力ストリームの配列と出力PDF用のストリームを作成し、次に[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index)メソッドを呼び出します。出力は出力ストリームに保存されます。以下のC#コードスニペットは、ストリームを使用してPDFファイルの配列を連結する方法を示しています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## 特定のフォルダー内のすべてのPdfファイルを連結する

実行時に特定のフォルダー内のすべてのPdfファイルを読み取り、ファイル名を知らなくてもそれらを連結することができます。 ディレクトリのパスを指定してください。そこには、結合したいPDFドキュメントが含まれています。

この機能を達成するために、次のC#コードスニペットを試してみてください。

## PDFフォームを結合し、フィールド名をユニークに保つ

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) の [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) クラスは、PDFファイルを結合する機能を提供します。 Now, if the Pdf files which are to be concatenated have form fields with similar field names, Aspose.PDF provides the feature to keep the fields in the resultant Pdf file as unique and also you can specify the suffix to make the field names unique. [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) プロパティの [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) を true に設定すると、Pdf フォームを連結する際にフィールド名がユニークになります。また、PdfFileEditor の [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) プロパティを使用して、フォームを連結する際にフィールド名をユニークにするために追加されるサフィックスのユーザー定義フォーマットを指定できます。この文字列には `%NUM%` サブストリングを含める必要があり、結果ファイルで数字に置き換えられます。

この機能を実現するための簡単なコードスニペットを以下に示します。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}
## PDFファイルを連結して目次を作成

## PDFファイルを連結

PDFファイルをマージする方法については、次のコードスニペットをご覧ください。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### 空白ページを挿入

PDFファイルがマージされた後、文書の先頭に空白ページを挿入し、そこに目次を作成することができます。この要件を達成するために、マージされたファイルを**Document**オブジェクトにロードし、Page.Insert(...)メソッドを呼び出して空白ページを挿入する必要があります。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### テキストスタンプを追加

目次を作成するために、[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)と[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp)オブジェクトを使用して、最初のページにテキストスタンプを追加する必要があります。 Stamp クラスは [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) を追加するための `BindLogo(...)` メソッドを提供しており、`SetOrigin(..)` メソッドを使用してこれらのテキストスタンプを追加する場所を指定することもできます。この記事では、2 つの PDF ファイルを連結しているため、これらの個々のドキュメントを指す 2 つのテキストスタンプオブジェクトを作成する必要があります。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### ローカルリンクの作成

次に、連結されたファイル内のページへのリンクを追加する必要があります。この要件を達成するために、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスの `CreateLocalLink(..)` メソッドを使用することができます。次のコードスニペットでは、4 番目の引数として Transparent を渡して、リンクの周囲の長方形が見えないようにしています。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}
### 完全なコード

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}


## フォルダ内のPDFファイルを連結する

Aspose.Pdf.Facades名前空間の[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor)クラスは、PDFファイルを連結する機能を提供します。特定のフォルダ内のすべてのPDFファイルを実行時に読み込んで連結することができ、ファイル名を知る必要もありません。連結したいPDFドキュメントを含むディレクトリのパスを指定するだけです。

この機能をAspose.PDFで実現するために、次のC#コードスニペットを使用してみてください：

```csharp
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// 特定のディレクトリ内のすべてのPdfファイルの名前を取得
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// 現在のシステム日付を取得し、そのフォーマットを設定
string date = DateTime.Now.ToString("MM-dd-yyyy");
// 現在のシステム時間を取得し、そのフォーマットを設定
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// 最終的な結果のPdfドキュメントの値を設定
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// PdfFileEditorオブジェクトをインスタンス化
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// PdfFileEditorオブジェクトのConcatenateメソッドを呼び出し、すべての入力ファイルを単一の出力ファイルに連結
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```
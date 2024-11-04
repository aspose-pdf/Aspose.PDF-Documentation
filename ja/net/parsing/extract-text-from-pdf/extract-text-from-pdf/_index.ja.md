---
title: PDFからテキストを抽出するC#
linktitle: PDFからテキストを抽出する
type: docs
weight: 10
url: /net/extract-text-from-all-pdf/
description: この記事では、Aspose.PDFを使用してC#でPDFドキュメントからテキストを抽出するさまざまな方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントの全ページからテキストを抽出する

PDFドキュメントからテキストを抽出することは一般的な要件です。この例では、Aspose.PDF for .NETがPDFドキュメントの全ページからテキストを抽出する方法を示します。**TextAbsorber**クラスのオブジェクトを作成する必要があります。その後、**Document**クラスを使用してPDFを開き、**Pages**コレクションの**Accept**メソッドを呼び出します。**TextAbsorber**クラスはドキュメントからテキストを吸収し、**Text**プロパティで返します。次のコードスニペットは、PDFドキュメントの全ページからテキストを抽出する方法を示しています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリとも機能します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// テキストを抽出するTextAbsorberオブジェクトを作成
TextAbsorber textAbsorber = new TextAbsorber();
// すべてのページについて吸収器を受け入れる
pdfDocument.Pages.Accept(textAbsorber);
// 抽出されたテキストを取得
string extractedText = textAbsorber.Text;
// ライターを作成し、ファイルを開く
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// ファイルにテキストの行を書き込む
tw.WriteLine(extractedText);
// ストリームを閉じる
tw.Close();
```
ドキュメントオブジェクトの特定のページで**Accept**メソッドを呼び出します。インデックスはテキストを抽出する必要がある特定のページ番号です。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも機能します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// テキストを抽出するためのTextAbsorberオブジェクトを作成します
TextAbsorber textAbsorber = new TextAbsorber();

// 特定のページに対して吸収器を受け入れます
pdfDocument.Pages[1].Accept(textAbsorber);

// 抽出されたテキストを取得します
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// ライターを作成し、ファイルを開きます
TextWriter tw = new StreamWriter(dataDir);

// ファイルにテキスト行を書き込みます
tw.WriteLine(extractedText);

// ストリームを閉じます
tw.Close();
```
## ページからテキストを抽出するための Text Device の使用

**TextDevice** クラスを使用して、PDFファイルからテキストを抽出できます。TextDeviceはその実装でTextAbsorberを使用しているため、実際には同じことを行いますが、TextDeviceはページ ImageDevice, PageDeviceなどから何でも抽出するための "Device" アプローチを統一するために実装されました。TextAbsorberはページ、PDF全体、またはXFormからテキストを抽出できるため、このTextAbsorberはより汎用性があります。

### 全ページからテキストを抽出する

以下の手順とコードスニペットは、テキストデバイスを使用してPDFからテキストを抽出する方法を示しています。

1. 入力PDFファイルを指定してDocumentクラスのオブジェクトを作成する
1. TextDeviceクラスのオブジェクトを作成する
1. 抽出オプションを指定するためにTextExtractOptionsクラスのオブジェクトを使用する
1. TextDeviceクラスのProcessメソッドを使用して内容をテキストに変換する
1. テキストを出力ファイルに保存する

以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// 抽出されたテキストを保持するための文字列
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // テキストデバイスを作成する
        TextDevice textDevice = new TextDevice();

        // テキスト抽出オプションを設定 - テキスト抽出モードを設定する（RawまたはPure）
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // 特定のページを変換してテキストをストリームに保存する
        textDevice.Process(pdfPage, textStream);
        // 特定のページを変換してテキストをストリームに保存する
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // メモリストリームを閉じる
        textStream.Close();

        // メモリストリームからテキストを取得する
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// 抽出したテキストをテキストファイルに保存する
File.WriteAllText(dataDir, builder.ToString());
```
## 特定のページ領域からテキストを抽出する

**TextAbsorber** クラスは、PDFドキュメントの特定のページまたは全ページからテキストを抽出する機能を提供します。このクラスは抽出したテキストを **Text** プロパティで返します。しかし、特定のページ領域からテキストを抽出する必要がある場合は、**TextSearchOptions** の **Rectangle** プロパティを使用できます。Rectangle プロパティは Rectangle オブジェクトを値として取り、このプロパティを使用してテキストを抽出する必要があるページの領域を指定できます。

ページの **Accept** メソッドがテキストを抽出するために呼び出されます。**Document** および **TextAbsorber** クラスのオブジェクトを作成します。**Document** オブジェクトの個々のページに対して **Accept** メソッドを呼び出します。**Index** はテキストを抽出する特定のページ番号です。**TextAbsorber** クラスの **Text** プロパティからテキストを取得できます。次のコードスニペットは、個々のページからテキストを抽出する方法を示しています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。
以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// テキストを抽出するためのTextAbsorberオブジェクトを作成する
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// 最初のページに対してabsorberを受け入れる
pdfDocument.Pages[1].Accept(absorber);

// 抽出されたテキストを取得する
string extractedText = absorber.Text;
// ライターを作成し、ファイルを開く
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// ファイルにテキストの行を書き込む
tw.WriteLine(extractedText);
// ストリームを閉じる
tw.Close();
```

## 列に基づいてテキストを抽出する

PDFファイルは、テキスト、イメージ、アノテーション、添付ファイル、グラフなどの要素で構成されている場合があり、Aspose.PDF for .NETはこれらの要素を追加および操作する機能を提供します。
PDFファイルにはテキスト、画像、注釈、添付ファイル、グラフなどの要素が含まれている場合があり、Aspose.PDF for .NETはこれらの要素を追加および操作する機能を提供します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // フォントサイズを少なくとも70%減らす必要があります
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### 第二のアプローチ - ScaleFactorの使用

この新しいリリースでは、TextAbsorberおよび内部テキストフォーマットメカニズムのいくつかの改善も導入されました。したがって、今では「Pure」モードを使用してテキストを抽出する際に、ScaleFactorオプションを指定でき、これは上記のアプローチに加えて、マルチカラムPDFドキュメントからテキストを抽出する別のアプローチとなるかもしれません。このスケールファクターは、テキスト抽出中の内部テキストフォーマットメカニズムに使用されるグリッドを調整するために設定されるかもしれません。ScaleFactorの値を1から0.1（0.1を含む）の間で指定すると、フォントサイズの縮小と同じ効果があります。

ScaleFactorの値を0.1から-0.1の間で指定すると、ゼロ値として扱われますが、テキストを抽出する際に必要なスケールファクターを自動的に計算するようにアルゴリズムを作動させます。
ScaleFactorの値を0.1から-0.1の間で指定すると、ゼロ値として扱われますが、テキストを自動的に抽出する際に必要なスケールファクターを計算するようにアルゴリズムに指示します。

大量のPDFファイルをテキスト内容抽出に処理する際は、自動スケーリング（ScaleFactor = 0）の使用を提案します。または、グリッド幅の冗長な削減を手動で設定します（約ScaleFactor = 0.5）。ただし、具体的な文書にスケーリングが必要かどうかを判断してはいけません。文書に不必要なグリッド幅の冗長な削減を設定すると（それが必要でない場合）、抽出されるテキスト内容は完全に適切です。次のコードスニペットをご覧ください。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// 文書ディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 文書を開く
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// 多くの文書で列を分割するには、スケールファクターを0.5に設定するだけで十分です
// ゼロの設定では、アルゴリズムが自動的にスケールファクターを選択できます
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}
新しいScaleFactorと古い手動フォント縮小係数の間に直接対応はありません。ただし、デフォルトのアルゴリズムは、何らかの内部理由により既に縮小されているフォントサイズの値を考慮しています。たとえば、フォントサイズを10から7に縮小することは、スケールファクターを5/8（= 0.625）に設定するのと同じ効果があります。
{{% /alert %}}

## PDFドキュメントから強調表示されたテキストを抽出する

PDFドキュメントからテキストを抽出するさまざまなシナリオで、PDFドキュメントから強調表示されたテキストのみを抽出する要件が発生することがあります。この機能を実装するために、APIにはTextMarkupAnnotation.GetMarkedText()メソッドとTextMarkupAnnotation.GetMarkedTextFragments()メソッドが追加されました。TextMarkupAnnotationをフィルタリングして、上記のメソッドを使用してPDFドキュメントから強調表示されたテキストを抽出できます。次のコードスニペットは、PDFドキュメントから強調表示されたテキストを抽出する方法を示しています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリとも連携します。
次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// すべてのアノテーションをループ処理します
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // TextMarkupAnnotationをフィルタリングします
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // 強調表示されたテキストフラグメントを取得します
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // 強調表示されたテキストを表示します
            Console.WriteLine(tf.Text);
        }
    }
}
```

## XMLからテキストフラグメントとセグメント要素にアクセスする

時々、XMLから生成されたPDFドキュメントを処理する際に、TextFragementまたはTextSegment項目にアクセスする必要があります。
時々、XMLから生成されたPDFドキュメントを処理する際に、TextFragementまたはTextSegmentアイテムにアクセスする必要があります。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```

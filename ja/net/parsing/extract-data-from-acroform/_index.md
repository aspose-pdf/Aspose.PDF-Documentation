---
title:  C#を使用してAcroFormからデータを抽出する
linktitle:  AcroFormからデータを抽出する
type: docs
weight: 50
url: ja/net/extract-data-from-acroform/
description: Aspose.PDFを使用すると、PDFファイルからフォームフィールドデータを簡単に抽出できます。AcroFormsからデータを抽出し、JSON、XML、またはFDF形式で保存する方法を学びましょう。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントからフォームフィールドを抽出する

Aspose.PDF for .NETは、フォームフィールドを生成したり、フォームフィールドに入力したりすることを可能にするだけでなく、PDFファイルからフォームフィールドデータやフォームフィールドに関する情報を抽出するのも簡単です。

以下のサンプルコードでは、PDF内のすべてのAcroFormおよびフォームフィールド値についての情報を抽出するために、PDFの各ページを反復処理する方法を示しています。このサンプルコードは、事前にフォームフィールドの名前を知らないという前提で作成されています。

次のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Get values from all fields
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Field Name : {0} ", formField.PartialName);
        Console.WriteLine("Value : {0} ", formField.Value);
    }
}
```
フォームフィールドの名前がわかっている場合は、Documents.Form コレクションのインデクサを使用して、このデータをすばやく取得できます。この記事の最後にその機能を使用する方法のサンプルコードをご覧ください。

## タイトルでフォームフィールドの値を取得する

フォームフィールドの Value プロパティを使用して、特定のフィールドの値を取得できます。値を取得するには、Document オブジェクトの Form コレクションからフォームフィールドを取得します。この例では、TextBoxField を選択して Value プロパティを使用してその値を取得します。

## PDFドキュメントからフォームフィールドをJSONに抽出する

次のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## PDFファイルからXMLへデータ抽出

Formクラスを使用すると、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートできます。XMLにデータをエクスポートするには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXmlメソッドを呼び出す必要があります。最後に、FileStreamオブジェクトを閉じてFormオブジェクトを破棄します。次のコードスニペットは、XMLファイルにデータをエクスポートする方法を示しています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// ドキュメントを開く
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// xmlファイルを作成。
System.IO.FileStream xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create);
// データをエクスポート
form.ExportXml(xmlOutputStream);
// ファイルストリームを閉じる
xmlOutputStream.Close();

// ドキュメントを閉じる
form.Dispose();
```
## PDFファイルからFDFへデータをエクスポートする

Formクラスを使用して、PDFファイルからFDFファイルにデータをエクスポートすることができます。FDFにデータをエクスポートするためには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportFdfメソッドを呼び出す必要があります。最後に、FormクラスのSaveメソッドを使用してPDFファイルを保存します。以下のコードスニペットは、FDFファイルにデータをエクスポートする方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// ドキュメントを開く
form.BindPdf(dataDir + "input.pdf");

// fdfファイルを作成する。
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// データをエクスポート
form.ExportFdf(fdfOutputStream);

// ファイルストリームを閉じる
fdfOutputStream.Close();

// 更新されたドキュメントを保存
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## PDFファイルからXFDFへデータをエクスポート

Formクラスを使用して、PDFファイルからXFDFファイルへデータをエクスポートすることができます。XFDFへデータをエクスポートするには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXfdfメソッドを呼び出す必要があります。最後に、FormクラスのSaveメソッドを使用してPDFファイルを保存できます。以下のコードスニペットは、XFDFファイルへデータをエクスポートする方法を示しています。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリとも動作します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// ドキュメントを開く
form.BindPdf(dataDir + "input.pdf");

// xfdfファイルを作成。
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// データをエクスポート
form.ExportXfdf(xfdfOutputStream);

// ファイルストリームを閉じる
xfdfOutputStream.Close();

// 更新されたドキュメントを保存
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```


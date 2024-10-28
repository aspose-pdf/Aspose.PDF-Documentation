---
title: PDF文書を連結する
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: このセクションでは、PdfFileEditorクラスを使用してcom.aspose.pdf.facadesでPDF文書を連結する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ファイルパスを使用してPDFファイルを連結する (Facades)

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスのconcatenateメソッドは、2つのPDFファイルを連結するために使用できます。concatenateメソッドでは、3つのパラメータを渡すことができます：最初の入力PDF、2番目の入力PDF、および出力PDFです。最終的な出力PDFには、両方の入力PDFファイルが含まれます。

次のコードスニペットは、ファイルパスを使用してPDFファイルを連結する方法を示しています。

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // ファイルを連結
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


いくつかのケースでは、アウトラインが多い場合、ユーザーは**CopyOutlines**をfalseに設定して、結合のパフォーマンスを向上させることができます。

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // ファイルを結合
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## MemoryStreamsを使用して複数のPDFファイルを結合

[Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) メソッドは、[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスのメソッドで、ソースPDFファイルと宛先PDFファイルをパラメータとして受け取ります。
 これらのパラメータは、ディスク上のPDFファイルへのパスであるか、またはMemoryStreamsである可能性があります。さて、この例では、まずディスクからPDFファイルを読み取るための2つのファイルストリームを作成します。それから、これらのファイルをバイト配列に変換します。PDFファイルのこれらのバイト配列は、MemoryStreamsに変換されます。一旦PDFファイルからMemoryStreamsを取得すると、それらを連結メソッドに渡して単一の出力ファイルにマージすることができます。

次のコードスニペットは、MemoryStreamsを使用して複数のPDFファイルを連結する方法を示しています。

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // PDFファイルを読み取るための2つのファイルストリームを作成
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // PDFファイルの内容を保持するバイト配列を作成
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // PDFファイルの内容をバイト配列に読み込む
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // バイト配列をMemoryStreamsに変換し、それらのストリームを連結
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // ストリームを連結するためにPdfFileEditorクラスのインスタンスを作成
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // 両方の入力MemoryStreamsを連結して出力MemoryStreamに保存
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // MemoryStreamをバイト配列に戻す
                        byte[] data = pdfStream.ToArray();
                        // 出力PDFファイルを保存するためのFileStreamを作成
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // 出力ファイルストリームにバイト配列内容を書き込む
                        output.Write(data, 0, data.Length);
                        // 出力ファイルを閉じる
                        output.Close();
                    }
                }
            }
            // 入力ファイルを閉じる
            fs1.Close();
            fs2.Close();
        }
```

## ファイルパスを使用してPDFファイルの配列を連結する (ファサード)

複数のPDFファイルを連結したい場合、ファイルパスの配列を渡すことができる連結メソッドのオーバーロードを使用できます。最終的な出力は、配列内のすべてのファイルから作成されたマージファイルとして保存されます。

以下のコードスニペットは、ファイルパスを使用してPDFファイルの配列を連結する方法を示しています。

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // ファイルの配列
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // ファイルを連結
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## ストリームを使用してPDFファイルの配列を連結する (ファサード)

PDFファイルの配列を連結することは、ディスク上に存在するファイルに限られません。
 配列のPDFファイルをストリームから連結することもできます。複数のPDFファイルを連結したい場合は、Concatenateメソッドの適切なオーバーロードを使用できます。まず、入力ストリームの配列と出力PDF用の1つのストリームを作成し、次にConcatenateメソッドを呼び出します。出力は出力ストリームに保存されます。

以下のコードスニペットは、ストリームを使用してPDFファイルの配列を連結する方法を示しています。

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // ストリームの配列
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // 出力ストリーム
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // ファイルを連結
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## PDFフォームを連結してフィールド名を一意に保つ

[com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) 名前空間の [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) クラスは、PDFファイルを連結する機能を提供します。
 現在、連結されるPdfファイルに同じフィールド名のフォームフィールドがある場合、Aspose.PDFは、結果のPdfファイルのフィールドを一意に保つ機能を提供しており、フィールド名を一意にするためのサフィックスを指定することもできます。PdfFileEditorの[KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--)メソッドをtrueに設定すると、Pdfフォームが連結されたときにフィールド名が一意になります。また、PdfFileEditorの[UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--)メソッドを使用して、フォームが連結されたときにフィールド名を一意にするために追加されるサフィックスのユーザー定義形式を指定できます。この文字列には、結果のファイル内で数値に置き換えられる%NUM%サブストリングを含める必要があります。

この機能を実現するための簡単なコードスニペットをご覧ください。

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // 入力ファイルと出力ファイルのパスを設定

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // PdfFileEditorオブジェクトをインスタンス化
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // すべてのフィールドに一意のフィールドIdを保持するため
                KeepFieldsUnique = true,
                // フォームが連結されたときにフィールド名を一意にするために追加されるサフィックスの形式
                UniqueSuffix = "_%NUM%"
            };

            // ファイルを連結して結果のPdfファイルにする
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## 結合 挿入 空白ページ

PDFファイルが結合された後、ドキュメントの最初に空白ページを挿入することができ、このページに目次を作成することができます。この要件を達成するために、結合されたファイルをDocumentオブジェクトにロードし、Page.Insert(…)メソッドを呼び出して空白ページを挿入する必要があります。

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // PdfFileEditorオブジェクトを作成
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // ファイルを結合
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```
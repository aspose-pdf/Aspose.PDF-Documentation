---
title: PDF印刷の操作 - ファサード
type: docs
weight: 10
url: /ja/net/working-with-pdf-printing-facades/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDFファサードでPDFファイルを印刷する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## プリンターとページ設定を使用してPDFファイルをデフォルトプリンターに印刷する

まず、ドキュメントが画像に変換され、プリンターに印刷されます。[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer)クラスのインスタンスを作成し、BindPdfメソッドを使用してドキュメントをそれにバインドし、特定の設定を行います。例では、A4フォーマット、縦方向を使用しています。printerSettingsでは、まず最初に印刷するプリンターの名前を指定します。そうでなければ、デフォルトプリンターに印刷されます。次に、必要なコピー数を設定します。

```csharp
 public static void PrintingPDFFile()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation
            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // Set printer name
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // Set PageSize (if required)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Set PageMargins (if required)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Print document using printer and page settings
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Close the PDF file after printing
            viewer.Close();
        }
```

ドキュメントの印刷ダイアログを表示するには、次のコードスニペットを試してください:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // PdfViewer オブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力 PDF ファイルを開く
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 印刷のための属性を設定
            viewer.AutoResize = true;         // サイズを調整してファイルを印刷
            viewer.AutoRotate = true;         // 回転を調整してファイルを印刷

            // プリンタとページ設定および PrintDocument のオブジェクトを作成

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // PageSize を設定 (必要に応じて)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // PageMargins を設定 (必要に応じて)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // ドキュメント印刷コードをここに記述
                // プリンタとページ設定を使用してドキュメントを印刷
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // 印刷後に PDF ファイルを閉じる
            viewer.Close();
        }
```

## PDFをソフトプリンターに印刷

ファイルに印刷するプリンターがあります。仮想プリンターの名前を設定し、前の例と同様に設定を行います。

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // PdfViewerオブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力PDFファイルを開く
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 印刷の属性を設定
            viewer.AutoResize = true;         // サイズを調整してファイルを印刷
            viewer.AutoRotate = true;         // 回転を調整してファイルを印刷
            viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

            viewer.PrintAsImage = false;

            // プリンターとページ設定、およびPrintDocumentのオブジェクトを作成
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // プリンター名を設定
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // またはPDFプリンターを設定
            //ps.PrinterName = "Adobe PDF";

            // ページサイズを設定（必要な場合）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // ページの余白を設定（必要な場合）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // プリンターとページ設定を使用してドキュメントを印刷
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 印刷後にPDFファイルを閉じる
            viewer.Close();
        }
```

## 印刷ダイアログを隠す

Aspose.PDF for .NETを使用すると、印刷ダイアログを隠すことができます。このためには、[PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog)メソッドを使用します。

以下のコードスニペットは、印刷ダイアログを隠す方法を示しています。

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // PdfViewerオブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力PDFファイルを開く
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 印刷の属性を設定
            viewer.AutoResize = true;         // 調整されたサイズでファイルを印刷
            viewer.AutoRotate = true;         // 調整された回転でファイルを印刷

            viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

            // プリンタとページ設定およびPrintDocumentのオブジェクトを作成
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDFプリンタ名を設定
            ps.PrinterName = "OneNote for Windows 10";

            // ページサイズを設定（必要に応じて）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // ページマージンを設定（必要に応じて）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // プリンタとページ設定を使用してドキュメントを印刷
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 印刷後にPDFファイルを閉じる
            viewer.Close();
        }
```

## カラーファイルのPDFをグレースケールでXPSファイルに印刷

カラーファイルのPDFドキュメントは、[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer)を使用して、グレースケールでXPSプリンタに印刷することができます。それを実現するためには、PdfViewer.PrintAsGrayscaleプロパティを使用し、それを*true*に設定する必要があります。次のコードスニペットは、PdfViewer.PrintAsGrayscaleプロパティの実装を示しています。

```csharp
public static void PrintingPDFasGrayscale()
        {
            // PdfViewerオブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力PDFファイルを開く
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 印刷のための属性を設定
            viewer.AutoResize = true;         // 調整されたサイズでファイルを印刷
            viewer.AutoRotate = true;         // 調整された回転でファイルを印刷

            viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない
            viewer.PrintAsGrayscale = false;

            // プリンタとページ設定のオブジェクトとPrintDocumentを作成
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDFプリンタ名を設定
            ps.PrinterName = "OneNote for Windows 10";

            // ページサイズを設定（必要に応じて）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // ページ余白を設定（必要に応じて）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // プリンタとページ設定を使用して文書を印刷
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 印刷後にPDFファイルを閉じる
            viewer.Close();
        }
```

## PDFからPostScriptへの変換

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) クラスはPDF文書を印刷する機能を提供し、このクラスを使用してPDFファイルをPostScript形式に変換することもできます。PDFファイルをPostScriptに変換するには、最初に任意のPSプリンターをインストールし、PdfViewerを使用してファイルに印刷するだけです。

次のコードスニペットは、PDFをPostScript形式に印刷および変換する方法を示しています。

```csharp
public static void PrintingPDFToPostScript()
        {
            // PdfViewerオブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力PDFファイルを開く
            viewer.BindPdf(_dataDir + "sample.pdf");

            // 印刷のための属性を設定
            viewer.AutoResize = true;         // サイズを調整してファイルを印刷
            viewer.AutoRotate = true;         // 回転を調整してファイルを印刷
            viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

            viewer.PrintAsImage = false;

            // プリンターとページ設定およびPrintDocumentのオブジェクトを作成
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDFプリンター名を設定
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 出力ファイル名とPrintToFile属性を設定
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // PageSizeを設定（必要な場合）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // PageMarginsを設定（必要な場合）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // プリンターとページ設定を使用して文書を印刷
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 印刷後にPDFファイルを閉じる
            viewer.Close();
        }
```

## 印刷ジョブのステータスを確認する

PDFファイルは、印刷ダイアログを表示せずに、物理プリンタおよびMicrosoft XPS Document Writerに印刷することができます。[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) クラスを使用します。大きなPDFファイルを印刷する場合、プロセスに時間がかかることがあり、印刷プロセスが完了したか、問題が発生したかをユーザーが確認できない場合があります。印刷ジョブのステータスを確認するには、PrintStatusプロパティを使用します。以下のコードスニペットは、PDFファイルをXPSファイルに印刷し、印刷ステータスを取得する方法を示しています。

```csharp
public static void CheckingPrintJobStatus()
        {
            // PdfViewerオブジェクトを作成
            PdfViewer viewer = new PdfViewer();

            // 入力PDFファイルを開く
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // 印刷の属性を設定
            viewer.AutoResize = true;         // 調整されたサイズでファイルを印刷
            viewer.AutoRotate = true;         // 調整された回転でファイルを印刷
            viewer.PrintPageDialog = false;   // 印刷時にページ番号ダイアログを表示しない

            viewer.PrintAsImage = false;

            // プリンタとページ設定、およびPrintDocumentのオブジェクトを作成
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // XPS/PDFプリンタ名を設定
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // 出力ファイル名とPrintToFile属性を設定
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // PageSizeを設定（必要に応じて）
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // PageMarginsを設定（必要に応じて）
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // プリンタとページ設定を使用してドキュメントを印刷
            viewer.PrintDocumentWithSettings(pgs, ps);

            // 印刷ステータスを確認
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // エラーが見つかりませんでした。印刷作業は問題なく完了しました
                Console.WriteLine("印刷が問題なく完了しました。");
            }

            // 印刷後にPDFファイルを閉じる
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## SimplexモードとDuplexモードでのページの印刷

特定の印刷ジョブでは、PDFドキュメントのページをDuplexモードまたはSimplexモードで印刷することができますが、1つの印刷ジョブ内で一部のページをsimplexとして、他のページをduplexとして印刷することはできません。しかし、要件を達成するために、異なるページ範囲とPrintingJobSettingsオブジェクトを使用することができます。以下のコードスニペットは、PDFファイルの一部のページをSimplexモードで、一部のページをDuplexモードで印刷する方法を示しています。
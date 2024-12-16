---
title: PDF印刷の操作
type: docs
weight: 10
url: /ja/java/print-pdf-file/
description: このセクションでは、PdfViewerクラスを使用してAspose.PDF FacadesでPDFファイルを印刷する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## プリンターとページ設定を使用してPDFファイルをデフォルトプリンターに印刷する

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) クラスを使用すると、PDFファイルをデフォルトのプリンターに印刷できます。そのためには、[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) オブジェクトを作成し、openPdfFile(..) メソッドを使用してPDFを開く必要があります。

printDocument(..) メソッドを呼び出して、PDFをデフォルトプリンターに印刷します。

次のコードスニペットは、プリンターとページ設定を使用してPDFをデフォルトプリンターに印刷する方法を示しています。

```java
 public static void PrintingPDFFile() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // サイズ調整してファイルを印刷
        viewer.setAutoRotate(true); // 回転を調整してファイルを印刷
        viewer.setPrintPageDialog(false); // 印刷時にページ番号ダイアログを表示しない

        // プリンターとページ設定、およびPrintDocumentのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // プリンター名を設定
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // PageSizeを設定（必要な場合）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMarginsを設定（必要な場合）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンターとページ設定を使用して文書を印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


以下のコードスニペットを使用して、印刷ダイアログを表示してみてください:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // 調整されたサイズでファイルを印刷
        viewer.setAutoRotate(true); // 調整された回転でファイルを印刷
        viewer.setPrintPageDialog(true);

        // プリンタとページ設定、PrintDocumentのためのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // PageSizeを設定（必要に応じて）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMarginsを設定（必要に応じて）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // プリンタとページ設定を使用してドキュメントを印刷
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


## ソフトプリンターへのPDF印刷

ファイルに印刷するプリンターがあります。仮想プリンターの名前を設定し、前の例に倣って設定を行います。

```java
public static void PrintingPDFToSoftPrinter() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷の属性を設定
        viewer.setAutoResize(true); // 調整されたサイズでファイルを印刷
        viewer.setAutoRotate(true); // 調整された回転でファイルを印刷
        viewer.setPrintPageDialog(false); // 印刷時にページ番号のダイアログを表示しない

        // プリンターとページ設定、PrintDocumentのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Microsoftソフトプリンターを設定
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // またはAdobe
        // printerSettings.setPrinterName("Adobe PDF");

        // PageSizeを設定（必要な場合）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMarginsを設定（必要な場合）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンターとページ設定を使用してドキュメントを印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


## 印刷ダイアログを非表示にする

Aspose.PDF for Javaを使用すると、印刷ダイアログを非表示にすることができます。このためには、[getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--) メソッドを使用します。

次のコードスニペットは、印刷ダイアログを非表示にする方法を示しています。

```java
public static void PrintingPDFHidePrintDialog() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // 調整されたサイズでファイルを印刷
        viewer.setAutoRotate(true); // 調整された回転でファイルを印刷

        viewer.setPrintPageDialog(false); // 印刷時にページ番号ダイアログを表示しない

        // プリンタとページ設定およびPrintDocumentのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // プリンタをMicrosoft Soft Printerに設定
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // PageSizeを設定（必要なら）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMarginsを設定（必要なら）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンタとページ設定を使用してドキュメントを印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


## カラーファイルをグレースケールで印刷する

カラーファイルをグレースケールで印刷するには、[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) を使用してXPSプリンターに印刷できます。そのためには、プロパティ PdfViewer.PrintAsGrayscale を使用し、*true* に設定する必要があります。

以下のコードスニペットは、PdfViewer.PrintAsGrayscale プロパティの実装を示しています。

```java
 public static void PrintingPDFasGrayscale() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // サイズを調整してファイルを印刷
        viewer.setAutoRotate(true); // 回転を調整してファイルを印刷

        viewer.setPrintAsGrayscale(true);

        // プリンターとページ設定用のオブジェクトを作成し、PrintDocumentを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // プリンターをMicrosoft Soft Printerに設定
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // ページサイズを設定（必要な場合）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // ページマージンを設定（必要な場合）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンターとページ設定を使用してドキュメントを印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


## PDFをPostScriptに変換

[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer)クラスは、PDFドキュメントを印刷する機能を提供し、このクラスを使用してPDFファイルをPostScript形式に変換することもできます。PDFファイルをPostScriptに変換するには、まずPSプリンタをインストールし、PdfViewerを使ってファイルに印刷します。

次のコードスニペットは、PDFを印刷してPostScript形式に変換する方法を示しています。

```java
public static void PrintingPDFToPostScript() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // サイズを調整してファイルを印刷
        viewer.setAutoRotate(true); // 回転を調整してファイルを印刷

        viewer.setPrintAsGrayscale(true);
        

        // プリンタとページ設定、およびPrintDocumentのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // PostScriptプリンタを設定
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // ページサイズを設定（必要に応じて）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // ページマージンを設定（必要に応じて）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンタとページ設定を使用してドキュメントを印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```


## 印刷ジョブステータスの確認

PDFファイルは、印刷ダイアログを表示せずに、物理プリンターやMicrosoft XPS Document Writerに印刷することができます。[PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer)クラスを使用します。大きなPDFファイルを印刷する場合、プロセスが長時間かかることがあり、ユーザーは印刷プロセスが完了したのか問題が発生したのかを確信できないかもしれません。印刷ジョブのステータスを確認するには、PrintStatusプロパティを使用します。次のコードスニペットは、PDFファイルをXPSファイルに印刷し、印刷ステータスを取得する方法を示しています。

```java
public static void CheckingPrintJobStatus() {
        // PdfViewerオブジェクトを作成
        PdfViewer viewer = new PdfViewer();

        // 入力PDFファイルを開く
        viewer.bindPdf(_dataDir + "sample.pdf");

        // 印刷のための属性を設定
        viewer.setAutoResize(true); // 調整されたサイズでファイルを印刷
        viewer.setAutoRotate(true); // 調整された回転でファイルを印刷

        viewer.setPrintAsGrayscale(true);

        // プリンターおよびページ設定、PrintDocumentのオブジェクトを作成
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // プリンターをMicrosoft Soft Printerに設定
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // PageSizeを設定（必要な場合）
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // PageMarginsを設定（必要な場合）
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // プリンターとページ設定を使用してドキュメントを印刷
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // 印刷ステータスを確認
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // エラーは見つかりませんでした。印刷ジョブは正常に完了しました
            System.out.println("Everything went OK!");
        }
        // 印刷後にPDFファイルを閉じる
        viewer.close();
    }
```
---
title: PDFからPostScriptへの変換
linktitle: PDFからPostScriptへの変換
type: docs
weight: 30
url: /ja/net/pdf-to-postscript-conversion/
description: PDFからPostScriptへの変換のためのソリューションがあります。このタスクには印刷とPdfViewerクラスを使用します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFからPostScriptへの変換",
    "alternativeHeadline": "PDFをPostScriptに変換",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "PDFからPostScriptへの変換のためのソリューションがあります。このタスクには印刷とPdfViewerクラスを使用します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリとも連携します。

## **C#でPDFをポストスクリプトに変換**

PdfViewerクラスはPDFドキュメントの印刷機能を提供し、このクラスを利用してPDFファイルをPostScript形式に変換することができます。PDFファイルをPostScriptに変換するには、まず任意のPSプリンタをインストールし、PdfViewerを使用してファイルに印刷します。ハワイ大学の指示に従ってPSプリンタをインストールする方法が記載されています。以下のコードスニペットは、PDFを印刷してPostScript形式に変換する方法を示しています。

```csharp
public static void PrintToPostscriptFile()
{
    // ドキュメントディレクトリへのパス。
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // PrinterSettingsとPageSettingsを設定
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // PSプリンタを設定、このドライバーはWindowsにプリインストールされているプリンタードライバーのリストで見つけることができます
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // 出力ファイル名とPrintToFile属性を設定
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // 印刷ページダイアログを無効にする
    viewer.PrintPageDialog = false;
    // プリンタ設定オブジェクトをメソッドに渡す
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## 印刷ジョブのステータスを確認する

PDFファイルは、印刷ダイアログを表示せずに、物理プリンターやMicrosoft XPS Document Writerに印刷することができます。これはPdfViewerクラスを使用して行います。大きなPDFファイルを印刷する場合、プロセスに時間がかかることがあるため、ユーザーは印刷プロセスが完了したか、問題に遭遇したかどうかがわからないことがあります。印刷ジョブのステータスを決定するには、PrintStatusプロパティを使用します。次のコードスニペットは、PDFファイルをXPSファイルに印刷し、印刷ステータスを取得する方法を示しています。

```csharp
public static void CheckingPrintJobStatus()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // The path to the documents directory.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // PdfViewerオブジェクトをインスタンス化
    PdfViewer viewer = new PdfViewer();

    // ソースPDFファイルをバインド
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // 印刷ダイアログを非表示
    viewer.PrintPageDialog = false;

    // Printer Settingsオブジェクトを作成
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // プリンター名を指定
    ps.PrinterName = "Microsoft XPS Document Writer";

    // 結果の印刷物名
    ps.PrintFileName = "ResultantPrintout.xps";

    // 出力をファイルに印刷
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // 印刷物のページサイズを指定
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // 上記の設定でドキュメントを印刷
    viewer.PrintDocumentWithSettings(pgs, ps);

    // 印刷ステータスをチェック
    if (viewer.PrintStatus != null)
    {
        // 例外が投げられた
        if (viewer.PrintStatus is Exception ex)
        {
            // 例外メッセージを取得
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // エラーは見つかりませんでした。印刷ジョブは正常に完了しました
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## 印刷ジョブの所有者名の取得/設定

最近、印刷ジョブの所有者名（実際にWebページの印刷ボタンを押したユーザー）を取得/設定する要件を受けました。この情報はPDFファイルを印刷する際に必要です。この要件を達成するために、PrinterJobNameというプロパティを使用できます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// ソースPDFファイルをバインド
viewer.BindPdf(dataDir + "input.pdf");
// 印刷ジョブの名前を指定
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください。
private static string GetCurrentUserCredentials()
{
    // 実行中のアプリケーションのタイプ（ASP.NET、Windowsフォームなど）によって実装が異なります。
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## インパーソネーションの使用

印刷ジョブの所有者名を取得する別のアプローチは、インパーソネーション（別のユーザーコンテキストで印刷ルーチンを実行する）を使用することです。また、ユーザーはSetJobルーチンを使用して直接所有者名を変更することができます。

Aspose.PDFの印刷APIを使用して所有者値を設定することは、セキュリティ上の理由から不可能であることに注意してください。プロパティPrinterJobNameは、スプーラー印刷アプリケーションのドキュメント名列の値を設定するために使用できます。上に共有されたコードスニペットは、ユーザーがドキュメント名列にユーザー名を組み込む方法を示しています（例えばUserName\documentNameの構文を使用して）。しかし、所有者列の設定は次の方法でユーザーによって直接実装できます：

1) インパーソネーション。所有者列の値には印刷コードを実行するユーザーの値が含まれているため、別のユーザーコンテキスト内でAspose.PDF印刷APIを呼び出す方法があります。例として、ここに説明されているソリューションをご覧ください。このクラスを使用することで、ユーザーは目標を達成できます：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// 印刷時にページ番号ダイアログを生成しない
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserNameはスプーラーアプリのOwner列の値です
    viewer.Close();
}
```
2) Spooler APIとSetJobルーチンの使用

以下のコードスニペットは、PDFファイルの一部のページをシンプレックスモード、一部のページをデュプレックスモードで印刷する方法を示しています。

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// 完全な例やデータファイルについては、https://github.com/aspose-pdf/Aspose.Pdf-for-.NET をご覧ください。
// 文書ディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
ps.PrintToFile = true;
ps.FromPage = printingJobs[printingJobIndex].FromPage;
ps.ToPage = printingJobs[printingJobIndex].ToPage;
ps.Duplex = printingJobs[printingJobIndex].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++printingJobIndex < printingJobs.Count)
    {
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```



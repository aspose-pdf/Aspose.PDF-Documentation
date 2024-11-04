---
title: PDFをMicrosoft PowerPointに変換する
linktitle: PDFをPowerPointに変換する
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDFを使用すると、Javaを利用してPDFをPowerPoint形式に変換できます。PDFをPPTXにスライドを画像として変換することが可能です。
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Java**は、PDFからPPTXへの変換の進行状況を追跡できます。  
Aspose.SlidesというAPIがあり、PPT/PPTXプレゼンテーションを作成および操作する機能を提供しています。このAPIは、PPT/PPTXファイルをPDF形式に変換する機能も提供しています。Aspose.PDF for Javaでは、PDFドキュメントをPPTX形式に変換する機能を導入しました。この変換中に、PDFファイルの個々のページがPPTXファイル内の別々のスライドに変換されます。

PDFからPPTXへの変換中に、テキストは選択/更新可能なテキストとしてレンダリングされ、画像としてレンダリングされるのではありません。
 PDFファイルをPPTX形式に変換するために、Aspose.PDFはPptxSaveOptionsというクラスを提供します。 [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) クラスのオブジェクトは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) メソッドの第二引数として渡されます。

次のコードスニペットを確認して、PDFをPowerPoint形式に変換するタスクを解決してください:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // PDFドキュメントを読み込む
        Document document = new Document(documentFileName);

        // PptxSaveOptionsインスタンスを生成
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // 出力をPPTX形式で保存
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## PDFをスライドとして画像形式でPPTXに変換する

検索可能なPDFを選択可能なテキストとしてではなく、画像としてPPTXに変換する必要がある場合、Aspose.PDFは[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions)クラスを通じてその機能を提供します。これを達成するには、以下のコードサンプルに示すように、[PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions)クラスのプロパティSlidesAsImagesを'true'に設定します。

以下のコードスニペットは、PDFファイルをスライドとして画像形式のPPTXに変換するプロセスを示しています。

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // PDFドキュメントをロード
    Document document = new Document(documentFileName);
    // PptxSaveOptionsインスタンスを初期化
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // 出力をPPTX形式で保存
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## コンソールで進捗を表示する Aspose.PDF for Java の例は次のようになります:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDFをPPTXに変換します。
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // PDFドキュメントを読み込む
        Document document = new Document(documentFileName);

        // PptxSaveOptionsインスタンスを生成する
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // カスタム進捗ハンドラーを指定する
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // 出力をPPTX形式で保存する
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## PPTX変換の進捗詳細

Aspose.PDF for Javaを使用すると、PDFからPPTXへの変換の進捗を追跡できます。[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions)クラスは、変換の進捗を追跡するためのカスタムメソッドを指定できる[CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions)プロパティを提供します。以下のコードサンプルに示されています。

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - 変換の進捗 : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - 結果ページの%s/%dレイアウトが作成されました。", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - 結果ページ%d/%dがエクスポートされました。", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - ソースページ%d/%dが分析されました。", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**PDFをPowerPointにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、そこで機能や品質を試して調査することができます。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
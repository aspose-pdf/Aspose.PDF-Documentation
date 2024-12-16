---
title: PDFドキュメントを保存する
linktitle: 保存
type: docs
weight: 30
url: /ja/java/save-pdf-document/
description: Aspose.PDF for Javaライブラリを使用してPDFファイルを保存する方法を学びます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントをファイルシステムに保存する

作成または操作したPDFドキュメントをファイルシステムに保存するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのSaveメソッドを使用します。 フォーマットタイプ（オプション）を指定しない場合、ドキュメントはAspose.PDF v.1.7 (*.pdf)形式で保存されます。

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // いくつかの操作を行う、例として新しい空のページを追加
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## ストリームにPDF文書を保存

作成したPDF文書や編集したPDF文書を、Saveメソッドのオーバーロードを使用してストリームに保存することもできます。

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // いくつかの操作を行う、例えば新しい空のページを追加
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## WebアプリケーションでPDF文書を保存

Webアプリケーションで文書を保存するには、上記で提案された方法を使用できます。さらに、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスにはオーバーロードされたメソッドSaveがあります。
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // ファイルをInputStreamとして取得
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // responseのOutputStreamにコピー
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("ファイルを出力ストリームに書き込む際のエラー。ファイル名は '{}'", fileName, ex);
    //         throw new RuntimeException("出力ストリームにファイルを書き込む際のIOError");
    //     }
    // }
```


詳細な説明については、[Showcase]()セクションを参照してください。

## PDF/AまたはPDF/X形式で保存する

PDF/Aは、電子文書のアーカイブと長期保存に使用されるポータブルドキュメントフォーマット（PDF）のISO標準化バージョンです。PDF/Aは、フォントリンク（フォント埋め込みとは対照的）や暗号化など、長期アーカイブに適さない機能を禁止している点でPDFと異なります。PDF/Aビューアに対するISOの要件には、カラーマネジメントガイドライン、埋め込みフォントのサポート、埋め込み注釈を読むためのユーザーインターフェイスが含まれます。

PDF/XはPDF ISO標準のサブセットです。PDF/Xの目的はグラフィック交換を容易にすることであり、そのため標準のPDFファイルには適用されない印刷関連の要件があります。

両方の場合において、Saveメソッドは文書を保存するために使用されますが、文書はConvertメソッドを使用して準備する必要があります。

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```
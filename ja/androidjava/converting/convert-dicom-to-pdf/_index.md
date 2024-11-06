---
title: DICOMをPDFに変換
linktitle: DICOMをPDFに変換
type: docs
weight: 250
url: ja/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Javaを使用してDICOM形式で保存された医用画像をPDFファイルに変換します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>は、医療画像の処理、保存、印刷、送信に関する標準です。ファイル形式の定義とネットワーク通信プロトコルが含まれています。

Aspose.PDF for Javaを使用すると、DICOMファイルをPDF形式に変換できます。次のコードスニペットを確認してください：

1. イメージをストリームに読み込む
1. [`Documentオブジェクト`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) を初期化する
1. サンプルDICOM画像ファイルを読み込む
1. 出力PDFドキュメントを保存する

```java
//    DICOMをPDFに変換
    public void convertDICOMtoPDF () {
        // ドキュメントオブジェクトを初期化
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // サンプルBMP画像ファイルを読み込む
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // 出力ドキュメントを保存
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
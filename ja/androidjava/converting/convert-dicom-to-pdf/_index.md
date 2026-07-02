---
title: DICOM を PDF に変換
linktitle: DICOM を PDF に変換
type: docs
weight: 250
url: /ja/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java を使用して、DICOM 形式で保存された医療画像を PDF ファイルに変換します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 医療画像における情報の取り扱い、保存、印刷、送信のための標準です。ファイル形式の定義とネットワーク通信プロトコルが含まれています。

Aspsoe.PDF for Java を使用すると、DICOM ファイルを PDF 形式に変換できます。次のコードスニペットをご確認ください：

1. 画像をストリームにロード
1. 初期化 [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. サンプル DICOM 画像ファイルをロード
1. 出力 PDF ドキュメントを保存

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
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

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


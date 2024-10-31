---
title: PDFからフォントを抽出する
linktitle: フォントを抽出する
type: docs
weight: 30
url: /php-java/extract-fonts-from-pdf/
description: Aspose.PDF for PHPを使用してPDFからフォントを抽出する方法
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFドキュメントからすべてのフォントを取得したい場合は、Documentクラスで提供されている[Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--)メソッドを使用できます。既存のPDFドキュメントからすべてのフォントを取得するための以下のコードスニペットを確認してください:

```php

    // Licenseクラスの新しいインスタンスを作成し、ライセンスファイルを設定します。
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // PDFドキュメントを含むディレクトリのパスと、抽出されたフォントの出力ディレクトリを設定します。
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // レスポンスデータ変数を初期化します。
    $responseData = "";

    try {
        // PDFドキュメントを読み込みます。
        $document = new Document($inputFile);

        // PDFドキュメントで使用されているすべてのフォントを取得します。
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // 各フォントを反復処理し、TrueTypeフォントファイルとして保存します。
        foreach ($fonts as $font) {
            // フォントファイルの出力ファイルパスを設定します。
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // フォントファイルを書き込むためのFileOutputStreamオブジェクトを作成します。
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // フォントをTrueTypeフォントファイルとして保存します。
            $font->save($fontStream);

            // フォントストリームを閉じます。
            $fontStream->close();

            // フォント名をレスポンスデータに追加します。
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // PDFドキュメントを閉じます。
        $document->close();
    }
```
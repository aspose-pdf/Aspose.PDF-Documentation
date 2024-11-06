---
title: AcroFormからデータを抽出する
linktitle: AcroFormからデータを抽出する
type: docs
weight: 50
url: ja/php-java/extract-data-from-acroform/
description: AcroFormsは多くのPDFドキュメントに存在します。この記事は、PHPとAspose.PDFを使用してAcroFormsからデータを抽出する方法を理解するのに役立ちます。
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントからフォームフィールドを抽出する

Aspose.PDF for PHPは、フォームフィールドを作成して入力するだけでなく、PDFファイルからフォームフィールドデータやフォームフィールド情報を簡単に抽出することもできます。

フォームフィールドの名前を事前に知らないと仮定します。その場合、PDFの各ページを反復して、PDF内のすべてのAcroFormsの情報およびフォームフィールドの値を抽出する必要があります。フォームにアクセスするには、[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) メソッドを使用する必要があります。

```php

    // Licenseクラスの新しいインスタンスを作成し、ライセンスファイルを設定します
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // PDFドキュメントを含むディレクトリへのパスを設定します
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // 入力PDFファイルへのパスを設定します
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // 応答がJSON形式であることを示すために応答ヘッダーを設定します
    header('Content-Type: application/json; charset=utf-8');

    // 応答データ変数を初期化します
    $responseData = "";

    try {
        // Documentクラスの新しいインスタンスを作成し、入力PDFファイルをロードします
        $document = new Document($inputFile);

        // ドキュメントからフォームフィールドを取得し、PHP値に変換します
        $fields = java_values($document->getForm()->getFields());

        // 各フォームフィールドをループして、フィールド名と値を抽出します
        foreach ($fields as $formField) {
            // フィールド名と値を応答データに連結します
            $responseData = $responseData . "(Field Name: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Value: " . $formField->getValue() . "),";
        }

        // ドキュメントを閉じます
        $document->close();
    }
```


フォームフィールドの名前を知っている場合、Documents.Formコレクションのインデクサーを使用して、このデータを迅速に取得することができます。

## PDFファイルからXMLへのデータ抽出

Formクラスを使用すると、ExportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートすることができます。データをXMLにエクスポートするためには、Formクラスのオブジェクトを作成し、FileStreamオブジェクトを使用してExportXmlメソッドを呼び出す必要があります。最後に、FileStreamオブジェクトを閉じて、Formオブジェクトを破棄します。以下のコードスニペットは、XMLファイルにデータをエクスポートする方法を示しています。

```php

    // ドキュメントを開く
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // フォントファイルを書き込むためのFileOutputStreamオブジェクトを作成
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // データをエクスポート
    $form->exportXml($xmlOutputStream);

    // ファイルストリームを閉じる
    $xmlOutputStream->close();

    // ドキュメントを閉じる
    $form->close();
```

## PDFファイルからFDFへのデータエクスポート

PDFフォームのデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-)メソッドを使用できます。

このクラスは、`com.aspose.pdf.facades`からのものです。似た名前ですが、このクラスは少し異なる目的を持っています。

データをFDFにエクスポートするには、`Form`クラスのオブジェクトを作成し、`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。以下のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```php

    // ドキュメントを開く
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // フォントファイルを書き込むためのFileOutputStreamオブジェクトを作成する。
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // データをエクスポート
    $form->exportFdf($xmlOutputStream);

    // ファイルストリームを閉じる
    $xmlOutputStream->close();

    // ドキュメントを閉じる
    $form->close();
```

## PDFファイルからXFDFにデータをエクスポートする

PDFフォームデータをXFDFファイルにエクスポートするには、[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form)クラスの[exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-)メソッドを使用できます。

データをXFDFにエクスポートするには、`Form`クラスのオブジェクトを作成し、その後`OutputStream`オブジェクトを使用して`exportXfdf`メソッドを呼び出す必要があります。
次のコードスニペットは、データをXFDFファイルにエクスポートする方法を示しています。

```php

    // ドキュメントを開く
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // フォントファイルを書き込むためのFileOutputStreamオブジェクトを作成する。
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // データをエクスポートする
    $form->exportXfdf($xmlOutputStream);

    // ファイルストリームを閉じる
    $xmlOutputStream->close();

    // ドキュメントを閉じる
    $form->close();
```
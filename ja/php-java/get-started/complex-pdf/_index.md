---
title: 複雑なPDFの作成 
linktitle: 複雑なPDFの作成
type: docs
weight: 60
url: ja/php-java/complex-pdf-example/
description: Aspose.PDF for PHP via Javaを使用すると、画像、テキストフラグメント、テーブルを含むより複雑なドキュメントを作成できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/php-java/hello-world-example/)の例では、Aspose.PDFを使用してPDFドキュメントを作成する簡単な手順を示しました。この記事では、Aspose.PDF for PHP via Javaを使用してより複雑なドキュメントを作成する方法を見ていきます。例として、旅客フェリーサービスを運営する架空の会社のドキュメントを取り上げます。

ドキュメントをゼロから作成する場合、特定の手順に従う必要があります：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) オブジェクトをインスタンス化します。このステップでは、メタデータを含むがページのない空のPDFドキュメントを作成します。

1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)を追加します。これで、ドキュメントには1ページが追加されます。
1. [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image)を追加します。これは、PDFオペレーターを使った低レベルの操作に基づく複雑な操作です。
    - ストリームから画像を読み込む
    - 画像をページリソースのImagesコレクションに追加する
    - GSaveオペレーターを使用: このオペレーターは現在のグラフィックス状態を保存します。
    - [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/)オブジェクトを作成する
    - ConcatenateMatrixオペレーターを使用: 画像の配置方法を定義します。
    - Doオペレーターを使用: このオペレーターは画像を描画します。
    - GRestoreオペレーターを使用: このオペレーターはグラフィックス状態を復元します。
1. ヘッダー用の[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を作成します。ヘッダーには、フォントサイズ24ptのArialフォントと中央揃えを使用します。

1. ページにヘッダーを追加します。[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)。
1. 説明用の[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)を作成します。説明にはArialフォント、フォントサイズ24pt、中央揃えを使用します。
1. ページの段落に(説明)を追加します。
1. テーブルを作成し、テーブルプロパティを追加します。
1. ページの[Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)に(テーブル)を追加します。
1. ドキュメントを "Complex.pdf" として保存します。

```php

    $document = new Document();
    // ページを追加
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // 画像を追加
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // ヘッダーを追加
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("New ferry routes in Fall 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // 説明を追加
    $descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // テーブルを追加
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Departs City");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Departs Island");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```
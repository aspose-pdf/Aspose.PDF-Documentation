---
title: Optimize, Compress or Reduce PDF Size in PHP
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /ja/php-java/optimize-pdf/
description: PDFファイルを最適化し、すべての画像を縮小し、PDFのサイズを減らし、フォントの埋め込みを解除し、未使用のオブジェクトをPHPで削除します。
lastmod: "2024-06-05"
---

PDFドキュメントには、時々追加のデータが含まれることがあります。PDFファイルのサイズを減らすことで、ネットワーク転送とストレージを最適化するのに役立ちます。これは、ウェブページ上での公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージへのアーカイブに特に便利です。PDFを最適化するためにいくつかの技術を使用できます：

- オンライン閲覧用にページコンテンツを最適化
- すべての画像を縮小または圧縮
- ページコンテンツの再利用を有効にする
- 重複するストリームを結合
- フォントの埋め込みを解除
- 未使用のオブジェクトを削除
- フォームフィールドをフラット化して削除
- 注釈を削除またはフラット化

## ウェブ用にPDFドキュメントを最適化

最適化または直線化とは、PDFファイルをウェブブラウザを使用してオンライン閲覧に適したものにするプロセスを指します。
 Aspose.PDFはこのプロセスをサポートしています。

PDFをウェブ表示用に最適化するには：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトで入力ドキュメントを開きます。
1. [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--) メソッドを使用します。
1. save(..) メソッドを使用して最適化されたドキュメントを保存します。

以下のコードスニペットは、PDFドキュメントをウェブ用に最適化する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ウェブ用に最適化
    $document->optimize();

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## PDFファイルサイズの削減

このトピックでは、PDFファイルのサイズを最適化/削減する手順を説明します。 Aspose.PDF APIは、不要なオブジェクトを削除し、画像を含むPDFファイルを圧縮することにより、出力PDFを最適化する柔軟性を提供する[OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions)クラスを提供します。これらのオプションは、以下のセクションで詳しく説明されています。

### 不要なオブジェクトを削除

重複しているオブジェクトや未使用のオブジェクトを削除することで、PDFドキュメントのサイズを最適化することができます。以下のコードスニペットは、その方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // PDFドキュメントを最適化します。ただし、このメソッドは
    // ドキュメントを確実に縮小することを保証するものではありません
    $document->optimizeResources();

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();

```

## すべての画像を縮小または圧縮

ソースPDFファイルに画像が含まれている場合、画像を圧縮し、その品質を設定することを検討してください。 画像圧縮を有効にするには、setCompressImages(..) メソッドに true を引数として渡します。ドキュメント内のすべての画像が再圧縮されます。圧縮は、setImageQuality(..) メソッドによって定義され、品質の値はパーセントで表されます。100% は品質と画像サイズが変更されないことを意味します。画像サイズを小さくするには、setImageQuality(..) メソッドに 100 未満の引数を渡します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化する
    $optimizationOptions = new OptimizationOptions();

    // CompressImagesオプションを設定する
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // ImageQualityオプションを設定する
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // OptimizationOptionsを使用してPDFドキュメントを最適化する
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```

別の方法としては、低解像度で画像をリサイズすることです。 この場合、ResizeImagesをtrueに設定し、MaxResolutionを適切な値に設定する必要があります。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化
    $optimizationOptions = new OptimizationOptions();

    // CompressImagesオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // ImageQualityオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // ResizeImageオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // MaxResolutionオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

もう一つの重要な問題は実行時間です。 しかし、再び、この設定も管理することができます。現在、標準と高速の2つのアルゴリズムを使用できます。実行時間を制御するためには、Versionプロパティを設定する必要があります。以下のスニペットは、高速アルゴリズムを示しています。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化
    $optimizationOptions = new optimization_OptimizationOptions();

    // CompressImagesオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // ImageQualityオプションを設定
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // 画像圧縮バージョンを高速に設定
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## 未使用オブジェクトの削除

PDFドキュメントには、ドキュメント内の他のオブジェクトから参照されていないPDFオブジェクトが含まれている場合があります。これは例えば、ページがドキュメントページツリーから削除されても、ページオブジェクト自体が削除されない場合に発生することがあります。これらのオブジェクトを削除することは、ドキュメントを無効にするのではなく、むしろそれを縮小します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## 未使用ストリームの削除

時々、ドキュメントには未使用のリソースストリームが含まれています。
 これらのストリームは、ページのリソース辞書から参照されているため、「未使用のオブジェクト」ではありません。これは、画像がページから削除されたが、ページリソースからは削除されていない場合に発生することがあります。また、この状況は、ドキュメントからページが抽出され、ドキュメントページが「共通」のリソース、つまり同じリソースオブジェクトを持っている場合によく発生します。リソースストリームが使用されているかどうかを判断するために、ページコンテンツが分析されます。未使用のストリームは削除されます。これにより、ドキュメントのサイズが小さくなることがあります。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## 重複ストリームのリンク

時々、ドキュメントにはいくつかの同一のリソースストリーム（例えば画像）が含まれています。 これは、例えばドキュメントがそれ自体と連結された場合に発生する可能性があります。出力ドキュメントには、同じリソースストリームの2つの独立したコピーが含まれています。すべてのリソースストリームを分析し、それらを比較します。ストリームが重複している場合、それらはマージされます。つまり、1つのコピーのみが残され、参照が適切に変更され、オブジェクトのコピーが削除されます。これにより、ドキュメントサイズが小さくなることがあります。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化する
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // OptimizationOptionsを使用してPDFドキュメントを最適化する
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```

さらに、AllowReusePageContent設定を使用することができます。このプロパティがtrueに設定されている場合、同一のページに対してドキュメントを最適化する際にページコンテンツが再利用されます。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化する
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化する
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```

## フォントの埋め込み解除

ドキュメントが埋め込みフォントを使用している場合、すべてのフォントデータがドキュメントに配置されていることを意味します。利点は、ユーザーのマシンにフォントがインストールされているかどうかに関係なく、ドキュメントが表示可能であることです。しかし、フォントを埋め込むとドキュメントが大きくなります。フォントの埋め込み解除メソッドは、すべての埋め込みフォントを削除します。これによりドキュメントサイズが減少しますが、正しいフォントがインストールされていない場合、ドキュメントが読めなくなる可能性があります。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // OptimizationOptionsを初期化
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化
    $document->optimizeResources($optimizationOptions);

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## 注釈の削除またはフラット化

注釈は不要な場合に削除することができます。
 必要な場合でも追加の編集が不要な場合は、フラット化することができます。これらの技術はどちらもファイルサイズを削減します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## フォームフィールドの削除

PDFドキュメントにAcroFormsが含まれている場合、フォームフィールドをフラット化することでファイルサイズを削減することができます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // フォームをフラット化
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

## PDFをRGBカラースペースからグレースケールに変換する

PDFファイルは、テキスト、画像、添付ファイル、注釈、グラフ、その他のオブジェクトで構成されています。PDFをRGBカラースペースからグレースケールに変換する必要があるかもしれません。これは、そのPDFファイルを印刷する際により高速になるためです。また、ファイルがグレースケールに変換されると、ドキュメントのサイズも縮小されますが、この変更により、ドキュメントの品質が低下する可能性があります。現在、この機能はAdobe Acrobatのプリフライト機能でサポートされていますが、オフィスの自動化について言えば、Aspose.PDFはドキュメント操作のための最終的なソリューションを提供します。

この要件を達成するために、次のコードスニペットを使用できます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```


## FlateDecode 圧縮

Aspose.PDF for PHP via Javaは、PDF最適化機能のためのFlateDecode圧縮のサポートを提供します。以下のコードスニペットは、FlateDecode圧縮で画像を保存するために最適化オプションを使用する方法を示しています：

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // OptimizationOptionsを初期化する
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // OptimizationOptionsを使用してPDFドキュメントを最適化する
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```

## XImageCollectionに画像を保存する

Aspose.PDF for PHP via Javaは、FlateDecode圧縮で新しい画像を[XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection)に保存する機能を提供します。
 このオプションを有効にするには、ImageFilterType.Flate フラグを使用できます。次のコードスニペットは、この機能を使用する方法を示しています。

```php
    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントを初期化
    $page = $document->getPages()->get_Item(1);

    // イメージをストリームに読み込む
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // 座標を設定
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // ConcatenateMatrix（行列の連結）オペレーターを使用：イメージの配置方法を定義
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();
```
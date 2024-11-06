---
title: ページプロパティの取得と設定
type: docs
weight: 30
url: ja/php-java/get-and-set-page-properties/
description: 本トピックでは、Aspose.PDF for PHP via Java を使用して PDF ファイル内のページ数を取得し、ページプロパティを取得し、ページ色を判定する方法について説明します。
lastmod: "2024-06-05"
---

Aspose.PDF for PHP via Java を使用すると、Java アプリケーション内で PDF ファイルのページプロパティを読み取り、設定することができます。このセクションでは、PDF ファイル内のページ数を取得し、色などの PDF ページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。

## PDF ファイルのページ数を取得する

ドキュメントを扱う際には、しばしばそれらが何ページ含んでいるか知りたいことがあります。Aspose.PDF を使用すると、これには2行のコードしか必要ありません。

PDF ファイルのページ数を取得するには:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用して PDF ファイルを開きます。
1. 次に、ドキュメントのページが取得されます。取得したページからページ数を取得しようとします。

以下のコードスニペットは、PDF ファイルのページ数を取得する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // ページ数を取得
    $responseData = $responseData . "Page Count : " + $pages->size();
```

### ドキュメントを保存せずにページ数を取得

PDFファイルが保存され、すべての要素が実際にPDFファイル内に配置されるまでは、特定のドキュメントのページ数を取得することはできません（すべての要素が収まるページ数を確実にすることができないため）。しかし、Aspose.PDF for PHP via Javaのリリース以降、[processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--)という名前のメソッドを導入し、ファイルを保存せずにPDFドキュメントのページ数を取得する機能を提供しています。したがって、ページ数情報をその場で取得できます。この要件を達成するために、次のコードスニペットを試してください。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);      

    // PDFファイルのページコレクションにページを追加
    $page = $document->getPages()->add();
    
    // 300個のTextFragmentインスタンスを追加するループを作成
    for ($i=0; $i < 300; $i++) { 
       // PDFの最初のページの段落コレクションにTextFragmentを追加
       $page->getParagraphs()->add(new TextFragment("Pages count test"));
    }
    
    // 段落を処理してページ数情報を取得
    $document->processParagraphs();

    $pages = $document->getPages();

    // ページ数を取得
    $responseData = $responseData . "Page Count : " + $pages->size();
```


## ページプロパティを取得する

PDFファイル内の各ページには、幅、高さ、裁ち落とし、裁断、仕上げボックスなど、多くのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

### **ページプロパティの理解: Artbox、BleedBox、CropBox、MediaBox、TrimBox、Rectプロパティの違い**

- **メディアボックス**: メディアボックスは、最も大きなページボックスです。これは、PostScriptまたはPDFに印刷される際に選択されたページサイズ（例えば、A4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷される媒体の物理サイズを決定します。
- **裁ち落としボックス**: ドキュメントに裁ち落としがある場合、PDFには裁ち落としボックスも含まれます。
 Bleedは、ページの端を越えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカットされる（「トリム」される）際に、インクがページの端まで届くようにするために使用されます。たとえページがトリムマークから少しずれてカットされても、ページに白い縁が現れることはありません。
- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれるボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートする際に使用されます。
- **Crop box**: クロップボックスは、Adobe Acrobatで表示されるPDFドキュメントの「ページ」サイズです。通常の表示では、Adobe Acrobatに表示されるのはクロップボックスの内容のみです。
  これらのプロパティの詳細な説明については、Adobe.Pdf仕様、特に10.10.1ページ境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交差部分（一般的に見える矩形）。 以下の図はこれらのプロパティを示しています。

詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

### ページプロパティへのアクセス

次のコードスニペットは、ドキュメント内の特定のページに対して、ArtBox、BleedBox、CropBox、MediaBox、TrimBox、Rect、ページ番号、および回転などのプロパティを取得します。そして、抽出されたデータを別々の変数に格納し、それらを連結してレスポンス文字列にします。

1. $inputFile変数を使用して新しいDocumentオブジェクトを作成します。
1. getPages()メソッドを使用して、ドキュメントからページのコレクションを取得します。
1. get_Item()メソッドを使用して、ページコレクションから特定のページを取得します。
1. 特定のページオブジェクトからさまざまなプロパティ（ArtBox、BleedBox、CropBox、MediaBox、TrimBox、Rect、ページ番号、回転）を抽出し、それらを別々の変数に格納します。
1. コードは、抽出されたプロパティ値を別々のレスポンス文字列（$responseData1、$responseData2など）に連結します。
1. 次に、$pages オブジェクトの size() メソッドを使用してページ数を取得しようとしますが、$pages 変数は定義されていません。

以下のコードスニペットは、ページのプロパティを取得する方法を示しています。

```php

   // ドキュメントを開く
    $document = new Document($inputFile);

    // ページコレクションを取得
    $pageCollection = $document->getPages();

    // 特定のページを取得
    $page = $pageCollection->get_Item(1);

    // ページのプロパティを取得
    $responseData1 = "ArtBox : Height = " . $page->getArtBox()->getHeight()
        . ", Width = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Height = " . $page->getBleedBox()->getHeight() . ", Width = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Height = " . $page->getCropBox()->getHeight() . ", Width = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Height = " . $page->getMediaBox()->getHeight() . ", Width = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Height = " . $page->getTrimBox()->getHeight() . ", Width = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Height = " . $page->getRect()->getHeight() . ", Width = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Page Number :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotate :-" . $page->getRotate() . PHP_EOL;

    // ページ数を取得
    $responseData8 = $responseData8 . "Page Count : " . $pages->size();
```


## ページカラーの判定

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスは、PDF ドキュメント内の特定のページに関連するプロパティを提供し、ページが使用する色の種類 - RGB、白黒、グレースケール、または未定義 - を含みます。

PDF ファイルのすべてのページは [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) コレクションによって含まれています。[ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) プロパティは、ページ上の要素の色を指定します。特定の PDF ページの色情報を取得または判定するには、[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) クラスオブジェクトの [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) プロパティを使用します。

次のコードスニペットは、PDF ファイルの各ページを反復して色情報を取得する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // PDF ファイルのすべてのページを反復処理する
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // 特定の PDF ページの色タイプ情報を取得する
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="ページ # -" . $pageCount . " は白黒です..";
                break;
            case 1:
                $responseData ="ページ # -" . $pageCount . " はグレースケールです...";
                break;
            case 0:
                $responseData ="ページ # -" . $pageCount . " はRGBです..";
                break;
            case 3:
                $responseData ="ページ # -" . $pageCount . " の色は未定義です..";
                break;
        }
    }
```
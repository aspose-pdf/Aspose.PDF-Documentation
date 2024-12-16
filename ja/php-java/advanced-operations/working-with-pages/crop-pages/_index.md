---
title: PHPを使用してPDFページをトリミングする
linktitle: ページをトリミング
type: docs
weight: 80
url: /ja/php-java/crop-pages/
description: Aspose.PDF for PHP via Javaを使用して、幅、高さ、裁ち落とし、トリム、トリムボックスなどのページプロパティを取得できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ページプロパティを取得

PDFファイルの各ページには、幅、高さ、裁ち落とし、トリム、トリムボックスなど、いくつかのプロパティがあります。Aspose.PDF for PHP via Javaを使用すると、これらのプロパティにアクセスできます。

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、PostScriptまたはPDFに印刷されたときに選択されたページサイズ（例：A4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的なサイズを決定します。
- **裁ち落としボックス**: ドキュメントに裁ち落としがある場合、PDFにも裁ち落としボックスがあります。
 ブリードは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカットされる（「トリミング」）際に、インクがページの端まで到達することを保証するために使用されます。たとえページがトリムマークからわずかにずれてカットされても、ページに白い縁が現れることはありません。

- **トリムボックス**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **アートボックス**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートする際に使用されます。
- **クロップボックス**: クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常のビューでは、Adobe Acrobatでクロップボックスの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdf仕様書、特に10.10.1ページの境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交差（一般に見える矩形）。 以下の図はこれらの特性を示しています。 詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

以下のスニペットはページをクロップする方法を示しています：

```php

    // ドキュメントを開く
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // 新しいボックス矩形を作成
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

この例では、サンプルファイルを使用しました [here](crop_page.pdf)。 Initially our page looks like shown on the Figure 1.  
最初に、私たちのページは図1に示されているように見えます。  
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.  
変更後、ページは図2のように見えます。  
![Figure 2. Cropped Page](crop_page2.png)
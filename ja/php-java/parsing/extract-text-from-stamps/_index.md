---
title: スタンプからテキストを抽出する
type: docs
weight: 60
url: ja/php-java/extract-text-from-stamps/
---

## スタンプ注釈からテキストを抽出する

Aspose.PDF for PHP via Javaを使用すると、スタンプ注釈からテキストを抽出できます。PDFのスタンプ注釈からテキストを抽出するために、以下の手順を使用できます。

1. PDFドキュメントを読み込む
1. ドキュメントの目的のページを取得する
1. StampAnnotationクラスの新しいインスタンスを作成する
1. AnnotationSelectorクラスの新しいインスタンスを作成し、スタンプ注釈を渡す
1. ページで注釈セレクタを受け入れる
1. 選択されたスタンプ注釈を取得する
1. TextAbsorberクラスの新しいインスタンスを作成する
1. 最初のスタンプ注釈を取得する
1. スタンプ注釈の通常の外観を取得する
1. テキストアブソーバーを使用して外観を訪れる
1. テキストアブソーバーから抽出されたテキストを取得する
1. ドキュメントを閉じる

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```
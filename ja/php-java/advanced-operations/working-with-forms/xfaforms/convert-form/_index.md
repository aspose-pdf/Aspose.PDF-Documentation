---
title: XFAフォームをAcroFormに変換
linktitle: XFAフォームを変換
type: docs
weight: 10
url: ja/php-java/convert-form/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してXFAフォームをAcroFormに変換する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 動的XFAフォームを標準AcroFormに変換

動的フォームは、XFA（XML Forms Architecture）として知られるXML仕様に基づいています。動的XFAフォームを標準AcroFormに変換することもできます。フォームに関する情報（PDFに関して）は非常に曖昧で、フィールドが存在し、プロパティやJavaScriptイベントがあることを指定しますが、レンダリングについては指定しません。XFAフォームのオブジェクトは、ドキュメントを読み込む際に描画されます。

現在、PDFはデータとPDFフォームを統合するための2つの異なる方法をサポートしています：

- AcroForms（Acrobatフォームとも呼ばれます）は、PDF 1.2フォーマット仕様で導入され、含まれています。

- Adobe XML Forms Architecture (XFA) フォームは、PDF 1.5 フォーマット仕様でオプション機能として導入されました。(XFA 仕様は PDF 仕様には含まれておらず、参照のみされています。)

XFA フォームのページを抽出または操作することはできません。なぜなら、フォームの内容は、XFA フォームの表示中にアプリケーション内で表示またはレンダリングしようとする際に、実行時に生成されるためです。Aspose.PDF には、開発者が XFA フォームを標準の AcroForms に変換できる機能があります。

```php

        // XFA フォームを読み込む
        $document = new Document($inputFile);
        
        // フォームフィールドのタイプを標準の AcroForm に設定
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // 更新されたドキュメントを保存
        $document->save($outputFile);
        
        // 修正された PDF を保存    
        $document->close();
```
---
title: JavaScript 経由で C++ を使用した高度な操作
linktitle: 高度な操作
type: docs
weight: 60
url: /ja/javascript-cpp/advanced-operations/
description: Aspose.PDF for JavaScript via C++ は、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーおよび開発者向けの情報を確認してください。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**高度な操作** は、既存の PDF ファイルをプログラムで処理する方法についてのセクションです。これは、[基本操作](/pdf/ja/javascript-cpp/basic-operations/)で説明されているように Aspose.PDF で作成されたドキュメントや、Adobe Acrobat、Google Docs、Microsoft Office、Open Office など他の PDF 作成ツールで作成された PDF にも該当します。

## Web Workers の使用

バージョン 23.6 で Web Workers を使用する機能が追加されました：

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

JavaScript 経由で C++ から Web Workers を使用することで、インターフェイスをブロックせずに、別のワーカースレッドで操作を実行することができます。

Web Workersは、スクリプトをバックグラウンドで実行するためのシンプルなツールです。これにより、ユーザーインターフェースに干渉することなく、別のワーカースレッドでタスクを実行できます。

さまざまな方法を学びます：

- [ドキュメントの操作](/pdf/ja/javascript-cpp/working-with-documents/) - ドキュメントを圧縮、分割、結合し、ドキュメント全体に対して他の操作を行います。
- [ページの操作](/pdf/ja/javascript-cpp/working-with-pages/) - ページを追加、移動、削除、トリミング、スタンプを行います。
- [PDFのメタデータ](/pdf/ja/javascript-cpp/pdf-file-metadata/) - ドキュメントのメタデータを取得または設定します。
- [画像の操作](/pdf/ja/javascript-cpp/working-with-images/) - ドキュメントに画像を挿入、削除、抽出します。
- [ナビゲーションとインタラクション](/pdf/ja/javascript-cpp/navigation-and-interaction/) - アクション、ブックマークを扱い、ページをナビゲートします。
- [注釈](/pdf/ja/javascript-cpp/annotations/) - 注釈により、ユーザーはPDFページにカスタムコンテンツを追加できます。PDFドキュメントから注釈を追加、削除、変更できます。

- [セキュリティと署名](/pdf/ja/javascript-cpp/securing-and-signing/) - プログラムでPDFドキュメントを保護および署名します。
- [Attachments](/pdf/ja/javascript-cpp/attachments/) - PDFドキュメントにはファイルの添付が含まれている場合があります。これらの添付ファイルは、他のPDFドキュメントや、オーディオファイル、Microsoft Officeドキュメントなど、あらゆる種類のファイルである可能性があります。PDFに添付ファイルを追加する方法、添付ファイルの情報を取得してファイルに保存する方法、JavaScriptを使用してPDFから添付ファイルをプログラムで削除する方法を学びます。
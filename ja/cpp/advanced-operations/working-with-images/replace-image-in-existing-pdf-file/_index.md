---
title: 既存のPDFファイルの画像をC++で置換
linktitle: 画像を置換
type: docs
weight: 70
url: ja/cpp/replace-image-in-existing-pdf-file/
description: このセクションでは、++ライブラリを使用して既存のPDFファイル内の画像を置換する方法について説明します。
lastmod: "2021-12-18"
---

ImagesコレクションのReplaceメソッドを使用すると、既存のPDFファイル内の画像を置換することができます。

Imagesコレクションは、ページのResourcesコレクションにあります。画像を置換するには：

1. Documentオブジェクトを使用してPDFファイルを開きます。
2. 特定の画像を置換し、DocumentオブジェクトのSaveメソッドを使用して更新されたPDFファイルを保存します。

以下のコードスニペットは、PDFファイル内の画像を置換する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // 特定の画像を置換
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // 更新されたPDFファイルを保存
    document->Save(_dataDir + u"output.pdf");
}
```
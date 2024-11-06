---
title: PDFファイルから画像を削除するC++の使用
linktitle: 画像を削除
type: docs
weight: 20
url: ja/cpp/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for C++を使用してPDFファイルから画像を削除する方法を説明します。
lastmod: "2021-12-18"
---

PDFファイルから画像を削除するには：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトを作成し、入力PDFファイルを開きます。
1. Documentオブジェクトの[Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)から画像を保持しているページを取得します。
1. 画像は、ページのResourcesコレクションにあるImagesコレクションに保持されます。
1. ImagesコレクションのDeleteメソッドで画像を削除します。
1. DocumentオブジェクトのSaveメソッドを使用して出力を保存します。

次のコードスニペットは、PDFファイルから画像を削除する方法を示しています。

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Delete a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Save updated PDF file
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```
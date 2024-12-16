---
title: PDFドキュメントからサムネイル画像を生成
linktitle: サムネイル画像を生成
type: docs
weight: 100
url: /ja/java/generate-thumbnail-images-from-pdf-documents/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFドキュメントからサムネイル画像を生成する方法について説明します。
lastmod: "2021-06-05"
---

## Aspose.PDF for Javaのアプローチ

Aspose.PDF for Javaは、PDFドキュメントを扱うための広範なサポートを提供します。また、PDFドキュメントのページをさまざまな画像形式に変換する機能もサポートしています。上記の機能は、Aspose.PDF for Javaを使用して簡単に実現できます。

Aspose.PDFには明確な利点があります：

- PDFファイルを操作するために、システムにAdobe Acrobatをインストールする必要はありません。
- Aspose.PDF for Javaの使用は、Acrobat Automationと比較して簡単で理解しやすいです。

PDFページをJPEGに変換する必要がある場合、[com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) 名前空間は、PDFページをJPEG画像にレンダリングするためのクラス [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) を提供します。
 以下のコードスニペットをご覧ください。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // 特定のディレクトリ内のすべてのPDFファイルの名前を取得する
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // ディレクトリの読み取り中にエラーが発生しました
        }

        // 配列内のすべてのファイルエントリを反復処理する
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // ドキュメントを開く
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // 解像度オブジェクトを作成する
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // 特定のページを変換し、画像をストリームに保存する
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // ストリームを閉じる
                imageStream.close();
            }
        }

    }
}
```
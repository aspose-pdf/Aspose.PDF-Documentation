---
title: デフォルトフォント名の設定
linktitle: デフォルトフォント名の設定
type: docs
weight: 90
url: ja/java/set-default-font-name/
description: このセクションでは、Aspose.PDF for Javaライブラリを使用してデフォルトフォント名を設定する方法について説明します。
lastmod: "2021-06-05"
---

**Aspose.PDF for Java** APIを使用すると、ドキュメント内にフォントがない場合にデフォルトフォント名を設定できます。デフォルトフォント名を設定するには、[RenderingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions) クラスの [setDefaultFontName](https://reference.aspose.com/pdf/java/com.aspose.pdf/RenderingOptions#setDefaultFontName-java.lang.String-) メソッドを使用します。setDefaultFontNameがnullに設定されている場合、**Times New Roman** フォントが使用されます。

次のコードスニペットは、PDFを画像として保存するときにデフォルトフォント名を設定する方法を示しています：

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import com.aspose.pdf.*;
import com.aspose.pdf.devices.PngDevice;
import com.aspose.pdf.devices.Resolution;

public class ExampleSetDefaultFontName {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void SetDefaultFontName() {
        
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        FileOutputStream imageStream = null;;
        try {
            imageStream = new FileOutputStream(_dataDir + "SetDefaultFontName.png");
        } catch (FileNotFoundException e) {
            // TODO 自動生成されたキャッチブロック
            e.printStackTrace();
        }

        Resolution resolution = new Resolution(300);
        PngDevice pngDevice = new PngDevice(resolution);
        RenderingOptions ro = new RenderingOptions();
        ro.setDefaultFontName ("Arial");
        pngDevice.setRenderingOptions(ro);
        pngDevice.process(pdfDocument.getPages().get_Item(1), imageStream);
    }    
}
```
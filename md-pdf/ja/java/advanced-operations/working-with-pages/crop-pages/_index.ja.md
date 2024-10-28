---
title: PDFページをプログラムでトリミング 
linktitle: ページをトリミング
type: docs
weight: 80
url: /java/crop-pages/
description: Aspose.PDF for Javaを使用して、幅、高さ、断裁、トリムボックスなどのページプロパティを取得できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ページプロパティを取得する

PDFファイル内の各ページには、幅、高さ、断裁、トリムボックスなどのプロパティがあります。Aspose.PDF for Javaを使用すると、これらのプロパティにアクセスできます。

- **メディアボックス**: メディアボックスは最も大きなページボックスです。これは、PostScriptまたはPDFに印刷されたときに選択されたページサイズ（例えばA4、A5、USレターなど）に対応します。言い換えれば、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理的なサイズを決定します。
- **ブリードボックス**: ドキュメントにブリードがある場合、PDFにもブリードボックスがあります。
 Bleedは、ページの端を超えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズにカットされたとき（「トリミング」）、インクがページの端まで届くようにするために使用されます。ページが誤ってトリミングされた場合でも（トリムマークからわずかにずれてカットされた場合）、ページに白い端が表示されることはありません。

- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートするときに使用されます。
- **Crop box**: クロップボックスは、Adobe Acrobatで表示されるPDFドキュメントの「ページ」サイズです。通常のビューでは、Adobe Acrobatでクロップボックスの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdf仕様、特に10.10.1ページ境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交差点（一般的に見える矩形）。 以下の図はこれらのプロパティを示しています。
詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

以下のスニペットはページをクロップする方法を示しています：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // 新しいボックス矩形を作成
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // 出力ドキュメントを保存
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
この例では、サンプルファイルを[ここ](crop_page.pdf)で使用しました。最初に、私たちのページは図1に示すように見えます。  
![Figure 1. Cropped Page](crop_page.png)

After the change, the page will look like Figure 2.  
変更後、ページは図2のように見えます。  
![Figure 2. Cropped Page](crop_page2.png)
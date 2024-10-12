---
title: PDF ページをプログラムでクロップ C++
linktitle: ページをクロップ
type: docs
weight: 80
url: /cpp/crop-pages/
description: Aspose.PDF for C++を使用して、幅、高さ、裁ち切り、クロップ、トリムボックスなどのページプロパティを取得できます。
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ページプロパティを取得する

PDF ファイルの各ページには、幅、高さ、裁ち切り、クロップ、トリムボックスなどのプロパティがあります。Aspose.PDFを使用すると、これらのプロパティにアクセスできます。

- **メディアボックス**: メディアボックスは最大のページボックスです。これは、PostScriptやPDFに印刷されたときに選択されたページサイズ（例：A4、A5、USレターなど）に対応します。言い換えると、メディアボックスはPDFドキュメントが表示または印刷されるメディアの物理サイズを決定します。
- **裁ち切りボックス**: ドキュメントに裁ち切りがある場合、PDFにも裁ち切りボックスがあります。 Bleedは、ページの端を越えて広がる色（またはアートワーク）の量です。これは、ドキュメントが印刷されてサイズに合わせてカットされたとき（「トリミング」）、インクがページの端まで届くようにするために使用されます。ページがミストリムされている場合でも - トリムマークからわずかにずれて切られた場合でも - ページに白い端が表示されることはありません。
- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメント内のページの実際の内容の周りに描かれたボックスです。このページボックスは、他のアプリケーションでPDFドキュメントをインポートするときに使用されます。
- **Crop box**: クロップボックスは、Adobe AcrobatでPDFドキュメントが表示される「ページ」サイズです。通常のビューでは、Adobe Acrobatでクロップボックスの内容のみが表示されます。これらのプロパティの詳細な説明については、Adobe.Pdf仕様、特に10.10.1ページ境界を参照してください。
- **Page.Rect**: MediaBoxとDropBoxの交差点（一般に見える長方形）。 以下の図はこれらのプロパティを示しています。  
詳細については、[このページ](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)をご覧ください。

以下のスニペットはページをトリミングする方法を示しています:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Open source document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Create new Box Rectagle
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

この例では、サンプルファイル[こちら](crop_page.pdf)を使用しました。最初にページは図1のように表示されます。  
![図1. 切り取られたページ](crop_page.png)

After the change, the page will look like Figure 2.  
![Figure 2. Cropped Page](crop_page2.png)

変更後、ページは図2のように表示されます。  
![図2. 切り取られたページ](crop_page2.png)
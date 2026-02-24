---
title: Python を使用したページプロパティの取得と設定
linktitle: ページプロパティの取得と設定
type: docs
weight: 90
url: /ja/python-net/get-and-set-page-properties/
description: このセクションでは、PDF ファイルのページ数を取得し、色などの PDF ページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用したページプロパティの取得と設定方法
Abstract: この記事では、Aspose.PDF for Python via .NET の機能について、Python を使用して PDF ファイルのページプロパティの読み取りと設定に焦点を当てて説明します。この記事は、PDF のページ数の決定、ページプロパティへのアクセスと変更、カラー情報の取り扱いなど、さまざまな機能をカバーします。ページ数を取得するには `Document` クラスと `PageCollection` コレクションを使用し、ドキュメントを保存せずにページ数を取得するコードスニペットを示します。この記事では、MediaBox、BleedBox、TrimBox、ArtBox、CropBox などの異なるページプロパティを説明し、これらのプロパティにアクセスするコード例を提供します。さらに、PDF から特定のページを取得して別ドキュメントとして保存する方法や、各ページのカラータイプを判定する方法についても取り上げています。例はすべて Python で実装されており、これらの機能の実用的な応用を示しています。
---

Aspose.PDF for Python via .NET を使用すると、Python アプリケーション内で PDF ファイルのページプロパティを読み取りおよび設定できます。このセクションでは、PDF ファイルのページ数を取得し、色などの PDF ページプロパティに関する情報を取得し、ページプロパティを設定する方法を示します。例では [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) と [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API を使用し、Python で記述されています。

## PDF ファイルのページ数を取得する

文書を扱う際、ページ数を知りたいことがよくあります。Aspose.PDF を使用すれば、コードは 2 行以内で済みます。

PDF ファイルのページ数を取得するには：

1. [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスを使用して PDF ファイルを開きます。
1. 次に、[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションの Count プロパティ（Document オブジェクトから）を使用して、ドキュメントの総ページ数を取得します。

以下のコードスニペットは、PDF ファイルのページ数を取得する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### ドキュメントを保存せずにページ数を取得する

PDF ファイルをオンザフライで生成する際、PDF 作成中に（目次作成など）システムやストリームに保存せずにページ数を取得する必要が生じることがあります。この要件に対応するため、Document クラスにメソッド [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) が導入されました。以下のコードスニペットをご覧いただき、ドキュメントを保存せずにページ数を取得する手順を確認してください。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## ページプロパティを取得する

PDF ファイルの各ページには、幅や高さ、BleedBox、CropBox、TrimBox など複数のプロパティがあります。Aspose.PDF を使用すると、これらのプロパティにアクセスできます。

### ページプロパティの理解：ArtBox、BleedBox、CropBox、MediaBox、TrimBox、Rect プロパティの違い

- **Media box**: メディアボックスは最大のページボックスです。これは、ドキュメントが PostScript や PDF に印刷されたときに選択されたページサイズ（例：A4、A5、US Letter など）に対応します。言い換えれば、メディアボックスは PDF ドキュメントが表示または印刷される媒体の物理的なサイズを決定します。
- **Bleed box**: ドキュメントにブリードがある場合、PDF にもブリードボックスが設定されます。ブリードはページの端を超えて広がるカラー（またはアートワーク）の量で、印刷後にサイズをカット（「トリム」）したときにインクがページの端まで届くようにするために使用されます。たとえページがトリムラインから少し外れてカットされても、ページに白い縁が現れません。
- **Trim box**: トリムボックスは、印刷およびトリミング後のドキュメントの最終サイズを示します。
- **Art box**: アートボックスは、ドキュメントのページ内の実際のコンテンツを囲むボックスです。このページボックスは、他のアプリケーションで PDF ドキュメントをインポートする際に使用されます。
- **Crop box**: クロップボックスは、Adobe Acrobat で PDF ドキュメントが表示される「ページ」サイズです。通常ビューでは、Adobe Acrobat ではクロップボックスの内容のみが表示されます。
これらのプロパティの詳細な説明については、Adobe.Pdf 仕様書、特に 10.10.1 ページ境界を参照してください。
-- **Page.Rect**: MediaBox と DropBox（`Page.rect`）の交差部分（一般的に可視矩形）です。矩形プロパティについては [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 型をご覧ください。下の図がこれらのプロパティを示しています。

詳細については、[this page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html) をご覧ください。

### ページプロパティへのアクセス

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、特定の PDF ページに関連するすべてのプロパティを提供します。PDF ファイルのすべてのページは、[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトの [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションに格納されています。

ここから、インデックスを使用して個々の `Page` オブジェクトにアクセスするか、コレクションをループしてすべてのページを取得することができます。個々のページにアクセスすると、そのプロパティを取得できます。以下のコードスニペットは、ページプロパティ（`Page` API）を取得する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## ページのカラーを判定する

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) クラスは、PDF ドキュメント内の特定のページに関連するプロパティを提供し、ページが使用するカラータイプ（RGB、白黒、グレースケール、または未定義）を含みます。

PDF ファイルのすべてのページは、[PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) コレクションに格納されています。[color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) プロパティはページ上の要素の色を指定します。特定の PDF ページのカラー情報を取得または判定するには、[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) オブジェクトの [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) プロパティを使用します。

以下のコードスニペットは、PDF ファイルの個々のページを反復処理してカラー情報を取得する方法を示しています。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```



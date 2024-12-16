---
title: PDFでの見出しの操作
type: docs
weight: 70
url: /ja/java/working-with-headings/
lastmod: "2021-06-05"
description: JavaでPDFドキュメントの見出しに番号を付けます。Aspose.PDF for Javaはさまざまな種類の番号スタイルを提供します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 見出しに番号スタイルを適用する

見出しはドキュメントの重要な部分です。著者は常に見出しを読者にとってより顕著で意味のあるものにしようとします。ドキュメントに複数の見出しがある場合、著者はこれらの見出しを整理するためのいくつかのオプションがあります。見出しを整理するための最も一般的なアプローチの1つは、見出しを番号スタイルで記述することです。

Aspose.PDF for Javaは、多くの事前定義された番号スタイルを提供します。これらの事前定義された番号スタイルは、列挙型NumberingStyleに格納されています。NumberingStyle列挙型の事前定義された値とその説明は以下の通りです:

|**見出しタイプ**|**説明**|
| :- | :- |
|NumeralsArabic|アラビア型、例えば、1,1.1,...|

|NumeralsRomanUppercase|ローマ数字大文字タイプ、例えば、I,I.II,...|
|NumeralsRomanLowercase|ローマ数字小文字タイプ、例えば、i,i.ii, ...|
|LettersUppercase|英語大文字タイプ、例えば、A,A.B, ...|
|LettersLowercase|英語小文字タイプ、例えば、a,a.b, ...|
[com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading)クラスの[setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading)プロパティは、見出しの番号スタイルを設定するために使用されます。

上の図に示されている出力を得るためのソースコードは、以下の例に示されています。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // ドキュメントディレクトリへのパス。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("リスト 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("リスト 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("計画の発効日における、各許可された計画に基づいて配布される財産の価値");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```
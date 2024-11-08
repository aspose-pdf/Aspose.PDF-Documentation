title: PDFでの見出しの操作
type: docs
weight: 70
url: /ja/php-java/working-with-headings/
lastmod: "2024-06-05"
description: PHPを使用してPDF文書内の見出しに番号を付ける。Aspose.PDF for PHP via Javaはさまざまな種類の番号スタイルを提供します。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 見出しに番号スタイルを適用する

見出しは、どの文書においても重要な部分です。作家は常に見出しを読者にとってより目立ち、意味のあるものにしようとします。文書に複数の見出しがある場合、作家はこれらの見出しを整理するためのいくつかのオプションを持っています。見出しを整理する最も一般的なアプローチの1つは、見出しを番号スタイルで書くことです。

Aspose.PDF for PHP via Javaは、多くの事前定義された番号スタイルを提供します。これらの事前定義された番号スタイルは、列挙型であるNumberingStyleに格納されています。NumberingStyle列挙型の事前定義された値とその説明は以下の通りです：

|**見出しの種類**|**説明**|
| :- | :- |

|NumeralsArabic|アラビアタイプ、例えば、1,1.1,...|
|NumeralsRomanUppercase|ローマ数字大文字タイプ、例えば、I,I.II, ...|
|NumeralsRomanLowercase|ローマ数字小文字タイプ、例えば、i,i.ii, ...|
|LettersUppercase|英語大文字タイプ、例えば、A,A.B, ...|
|LettersLowercase|英語小文字タイプ、例えば、a,a.b, ...|
[com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) クラスの [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) プロパティは、見出しの番号スタイルを設定するために使用されます。

上記の図に示されている出力を得るためのソースコードは、以下の例に示されています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $document->getPageInfo()->setWidth(612.0);
    $document->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $page = $document->getPages()->add();
    $page->getPageInfo()->setWidth(612.0);
    $page->getPageInfo()->setHeight(792.0);
    $document->getPageInfo()->setMargin(new MarginInfo());
    $document->getPageInfo()->getMargin()->setLeft(72);
    $document->getPageInfo()->getMargin()->setRight(72);
    $document->getPageInfo()->getMargin()->setTop(72);
    $document->getPageInfo()->getMargin()->setBottom(72);

    $floatBox = new FloatingBox();
    $floatBox->setMargin($page->getPageInfo()->getMargin());

    $page->getParagraphs()->add($floatBox);

    $heading = new Heading(1);
    $heading->setInList(true);
    $heading->setStartNumber(1);
    $heading->setText("リスト 1");
    $heading->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading);
    $heading2 = new Heading(1);
    $heading2->setInList(true);
    $heading2->setStartNumber(13);
    $heading2->setText("リスト 2");
    $heading2->setStyle(NumberingStyle::$NumeralsRomanLowercase);
    $heading2->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading2);

    $heading3 = new Heading(2);
    $heading3->setInList(true);
    $heading3->setStartNumber(1);
    $heading3->setText("各許容されたものに対して計画に基づいて配分される財産の、計画の発効日現在の価値");
    $heading3->setStyle (NumberingStyle::$LettersLowercase);
    $heading3->setAutoSequence(true);

    $floatBox->getParagraphs()->add($heading3);
    
    $document->save($outputFile);
    $document->close();
```
---
title: 高度な機能
linktitle: 高度な機能
type: docs
weight: 120
url: /ja/java/advanced-features/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFドキュメントにLaTeXタグを使用する方法を示します。
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Latexタグのサポート

このツールは、科学論文の作成、書籍の執筆、および他の多くの出版物の形態に全般的に使用されます。美しくデザインされたドキュメントを作成するだけでなく、数式、表、参考文献、書誌目録など、印刷セットの複雑な要素を非常に迅速に実装することができ、すべてのセクションで一貫したマークアップを得ることができます。

Latexタグを使用したコードスニペットでの数学演習の例を確認しましょう。

Aspose.PDF for Java 19.9以降のバージョンでは、\begin \end \qedhere Latexタグのサポートが提供されています。これには、以下のコードサンプルで示されているように、LaTeXテキストをドキュメント環境に囲む必要があります。

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} 証明は次のとおりです: " +
              "\\begin{align}" +
              "(x+y)^3&=(x+y)(x+y)^2" +
              "(x+y)(x^2+2xy+y^2)\\\\" +
              "&=x^3+3x^2y+3xy^3+x^3.\\qedhere" +
              "\\end{align}" +
              "\\end{proof}" +
              "\\end{document}";

Document doc = new Document();
Page page = doc.getPages().add();

LatexFragment latex = new LatexFragment(s);

page.getParagraphs().add(latex);
      
doc.save(dataDir + "Script_out.pdf");
```
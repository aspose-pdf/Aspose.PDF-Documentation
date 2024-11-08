---
title: 高级功能
linktitle: 高级功能
type: docs
weight: 120
url: /zh/java/advanced-features/
description: 本节展示如何使用 Aspose.PDF for Java 在 PDF 文档中使用 LaTeX 标签。
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 支持 LaTeX 标签

该工具通常用于创建科学论文、撰写书籍和许多其他形式的出版物。它不仅允许创建设计精美的文档，还允许用户非常快速地实现打印集中的复杂元素，如数学表达式、表格、引用和书目，从而在所有部分获得一致的标记。

让我们来看一个使用 LaTeX 标签的代码片段中的数学练习示例。

从 Aspose.PDF for Java 19.9 版本开始，API 提供对 \begin \end \qedhere LaTeX 标签的支持。这需要您将 LaTeX 文本封装在文档环境中，如以下代码示例所示。

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} 证明如下: " +
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
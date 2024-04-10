---
title: Advanced Features
linktitle: Advanced Features
type: docs
weight: 120
url: /java/advanced-features/
description: This section shows how you can use LaTeX Tags in PDF document with Aspose.PDF for Java.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Support for Latex Tags

This tool is used overall for creating scientific papers, writing books, and many other forms of publication. It allows not only to create beautifully designed documents, but also allows users to very quickly implement such complex elements of the printed set as math expressions, tables, references and bibliographies, getting consistent markup across all sections.

Let's check out an example of a math exercise in a code snippet using Latex tags.

From version Aspose.PDF for Java 19.9 API provides support for \begin \end \qedhere Latex tags. This requires you to enclose the LaTeX text into document environment as shown in the following code sample.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";		
		
String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} The proof is a follows: " +
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

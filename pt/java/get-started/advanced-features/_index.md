---
title: Funcionalidades Avançadas
linktitle: Funcionalidades Avançadas
type: docs
weight: 120
url: /pt/java/advanced-features/
description: Esta seção mostra como você pode usar Tags LaTeX em documentos PDF com Aspose.PDF para Java.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Suporte para Tags LaTeX

Esta ferramenta é utilizada principalmente para criar artigos científicos, escrever livros e muitas outras formas de publicação. Ela permite não apenas criar documentos lindamente projetados, mas também permite aos usuários implementar rapidamente elementos complexos do conjunto impresso, como expressões matemáticas, tabelas, referências e bibliografias, obtendo uma marcação consistente em todas as seções.

Vamos conferir um exemplo de um exercício matemático em um trecho de código usando tags LaTeX.

A partir da versão Aspose.PDF para Java 19.9, a API fornece suporte para as tags LaTeX \begin \end \qedhere. Isso requer que você envolva o texto LaTeX no ambiente do documento, conforme mostrado no exemplo de código a seguir.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} A prova é a seguinte: " +
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
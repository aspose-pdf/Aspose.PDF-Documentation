---
title: Продвинутые функции
linktitle: Продвинутые функции
type: docs
weight: 120
url: /ru/java/advanced-features/
description: Этот раздел показывает, как можно использовать теги LaTeX в PDF-документе с помощью Aspose.PDF для Java.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Поддержка тегов Latex

Этот инструмент используется для создания научных статей, написания книг и многих других форм публикаций. Он позволяет не только создавать красиво оформленные документы, но и позволяет пользователям очень быстро реализовать такие сложные элементы набора, как математические выражения, таблицы, ссылки и библиографии, получая единообразную разметку во всех разделах.

Давайте рассмотрим пример математического упражнения в кодовом фрагменте с использованием тегов Latex.

Начиная с версии Aspose.PDF для Java 19.9 API обеспечивает поддержку тегов \begin \end \qedhere Latex. Это требует заключения текста LaTeX в среду документа, как показано в следующем примере кода.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} Доказательство следующее: " +
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
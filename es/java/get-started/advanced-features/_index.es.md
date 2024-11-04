---
title: Funciones Avanzadas
linktitle: Funciones Avanzadas
type: docs
weight: 120
url: /java/advanced-features/
description: Esta sección muestra cómo puedes usar etiquetas LaTeX en documentos PDF con Aspose.PDF para Java.
lastmod: "2022-01-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Soporte para Etiquetas Latex

Esta herramienta se utiliza en general para crear artículos científicos, escribir libros y muchas otras formas de publicación. No solo permite crear documentos bellamente diseñados, sino que también permite a los usuarios implementar muy rápidamente elementos tan complejos del conjunto impreso como expresiones matemáticas, tablas, referencias y bibliografías, obteniendo un marcado consistente en todas las secciones.

Veamos un ejemplo de un ejercicio matemático en un fragmento de código usando etiquetas Latex.

A partir de la versión Aspose.PDF para Java 19.9, la API proporciona soporte para las etiquetas Latex \begin \end \qedhere. Esto requiere que encierres el texto de LaTeX en un entorno de documento como se muestra en el siguiente ejemplo de código.

```java
String dataDir = Utils.getSharedDataDir(UseLatexScript3.class) + "Text/";





String s =
              "\\usepackage{amsmath,amsthm}" +
              "\\begin{document}" +
              "\\begin{proof} La demostración es la siguiente: " +
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
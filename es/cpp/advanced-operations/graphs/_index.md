---
title: Trabajando con Gráficas en PDF
linktitle: Trabajando con Gráficas
type: docs
weight: 70
url: /es/cpp/graphs/
description: Este artículo explica qué es un Gráfico, cómo crear un objeto de rectángulo relleno, cómo agregar texto dentro de un objeto gráfico, cómo agregar un objeto línea al PDF, etc.
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Qué es un Gráfico

Agregar gráficos a documentos PDF es una tarea muy común para los desarrolladores mientras trabajan con Adobe Acrobat Writer u otras aplicaciones de procesamiento de PDF. Hay muchos tipos de gráficos que se pueden usar en aplicaciones PDF.
[Aspose.PDF for C++](/pdf/es/cpp/) también admite la adición de gráficos a documentos PDF. Para este propósito, se proporciona la clase Graph. Graph es un elemento a nivel de párrafo y se puede agregar a la colección de Paragraphs en una instancia de Page. Una instancia de Graph contiene una colección de Shapes.

Los siguientes tipos de formas son compatibles con la clase [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph):


- [Arc](/pdf/es/cpp/add-arc/) - a veces también llamado bandera es un par ordenado de vértices adyacentes, pero a veces también llamado línea dirigida.
- [Circle](/pdf/es/cpp/add-circle/) - muestra datos utilizando un círculo dividido en sectores. Usamos un gráfico circular (también llamado gráfico de pastel) para mostrar cómo los datos representan partes de un todo o un grupo.
- [Curve](/pdf/es/cpp/add-curve/) - es una unión conectada de líneas proyectivas, cada línea encontrando a otras tres en puntos dobles ordinarios.
- [Line](/pdf/es/cpp/add-line) - los gráficos de líneas se utilizan para mostrar datos continuos y pueden ser útiles para predecir eventos futuros cuando muestran tendencias a lo largo del tiempo.
- [Rectangle](/pdf/es/cpp/add-rectangle/) - es una de las muchas formas fundamentales que verás en los gráficos, puede ser muy útil para ayudarte a resolver un problema.
- [Ellipse](/pdf/es/cpp/add-ellipse/) - es un conjunto de puntos en un plano, creando una forma ovalada y curva.

Los detalles anteriores también se representan en las figuras a continuación:

![Figures in Graphs](graph.png)
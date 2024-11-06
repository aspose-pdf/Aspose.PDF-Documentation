---
title: Trabajando con Gráficos 
linktitle: Trabajando con Gráficos
type: docs
weight: 70
url: es/java/graphs/
description: Este artículo explica qué es un Gráfico, cómo crear un objeto de rectángulo lleno, cómo agregar texto dentro de un objeto gráfico, cómo agregar un objeto de línea al PDF, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Qué es un Gráfico

El propósito principal del gráfico es mostrar hechos numéricos en forma visual para que puedan ser comprendidos rápidamente, fácilmente y claramente. Así, los gráficos son representaciones visuales de datos recopilados. Los datos también pueden presentarse en forma de tabla; sin embargo, una presentación gráfica es más fácil de entender. Esto es especialmente cierto cuando hay una tendencia o comparación que se debe mostrar.

Agregar gráficos a documentos PDF es una tarea muy común para los desarrolladores al trabajar con Adobe Acrobat Writer u otras aplicaciones de procesamiento de PDF.
 Hay muchos tipos de gráficos que se pueden utilizar en aplicaciones PDF. Los operadores gráficos utilizados en los flujos de contenido PDF describen la apariencia de las páginas que se van a reproducir en un dispositivo de salida rasterizado.

[Aspose.PDF para Java](/pdf/java/) también admite la adición de gráficos a documentos PDF. Para este propósito, se proporciona la clase Graph. Graph es un elemento a nivel de párrafo y se puede agregar a la colección de Paragraphs en una instancia de Page. Una instancia de Graph contiene una colección de Shapes.

Los siguientes tipos de formas son compatibles con la clase [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph):

- [Arc](/pdf/java/add-arc/) - a veces también llamado bandera es un par ordenado de vértices adyacentes, pero a veces también llamado línea dirigida.
- [Circle](/pdf/java/add-circle/) - muestra datos usando un círculo dividido en sectores. Usamos un gráfico circular (también llamado gráfico de pastel) para mostrar cómo los datos representan porciones de un todo o un grupo.

- [Curve](/pdf/java/add-curve/) - es una unión conectada de líneas proyectivas, cada línea encontrándose con otras tres en puntos dobles ordinarios.- [Line](/pdf/java/add-line) - los gráficos de líneas se utilizan para mostrar datos continuos y pueden ser útiles para predecir eventos futuros cuando muestran tendencias a lo largo del tiempo.
- [Rectangle](/pdf/java/add-rectangle/) - es una de las muchas formas fundamentales que verás en los gráficos, puede ser muy útil para ayudarte a resolver un problema.
- [Ellipse](/pdf/java/add-ellipse/) - es un conjunto de puntos en un plano, creando una forma ovalada y curva.

Los detalles anteriores también se representan en las figuras a continuación:

![Figures in Graphs](graph.png)
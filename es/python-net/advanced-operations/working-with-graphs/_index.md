---
title: Trabajando con gráficos en PDF usando Python
linktitle: Trabajando con gráficos
type: docs
weight: 70
url: /es/python-net/working-with-graphs/
description: Este artículo explica qué es un grafo, cómo crear un objeto rectángulo relleno y otras funciones
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Añadiendo gráficos a PDF usando Python
Abstract: El artículo discute la integración de gráficos en documentos PDF, un requisito común para los desarrolladores que utilizan Adobe Acrobat Writer u otras herramientas de procesamiento de PDF. Presenta la clase Graph en Aspose.PDF for Python via .NET, que facilita esta tarea al permitir la adición de varios tipos de formas a los documentos PDF. La clase Graph es un elemento a nivel de párrafo que puede añadirse a la colección Paragraphs en una instancia de Page y admite una colección de formas, incluyendo Arc, Circle, Curve, Line, Rectangle y Ellipse. Cada forma cumple un propósito único, como los Arcs que representan adyacencia, los Circles que ilustran porciones de datos, los Curves que representan líneas conectadas, los Lines que muestran tendencias continuas de datos, los Rectangles que resuelven problemas espaciales y los Ellipses que forman formas ovaladas. El artículo también proporciona representaciones visuales de estas formas para facilitar la comprensión.
---

## Qué es un grafo

Agregar gráficos a documentos PDF es una tarea muy común para los desarrolladores al trabajar con Adobe Acrobat Writer u otras aplicaciones de procesamiento de PDF. Hay muchos tipos de gráficos que pueden usarse en aplicaciones PDF.
[Aspose.PDF for Python via .NET](/pdf/python-net/) también admite la inserción de gráficos en documentos PDF. Para este fin, se proporciona la clase Graph. Graph es un elemento a nivel de párrafo y puede añadirse a la colección Paragraphs en una instancia de Page. Una instancia de Graph contiene una colección de Shapes.

Los siguientes tipos de formas son compatibles con la clase [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/):

- [Arc](/pdf/python-net/add-arc/) - a veces también llamado una bandera, es un par ordenado de vértices adyacentes, pero a veces también llamado una línea dirigida.
- [Circle](/pdf/python-net/add-circle/) - muestra datos usando un círculo dividido en sectores. Utilizamos un gráfico circular (también llamado diagrama de pastel) para mostrar cómo los datos representan porciones de un todo o de un grupo.
- [Curve](/pdf/python-net/add-curve/) - es una unión conectada de líneas proyectivas, cada línea intersecta a otras tres en puntos dobles ordinarios.
- [Line](/pdf/python-net/add-line) - los gráficos de líneas se utilizan para mostrar datos continuos y pueden ser útiles para predecir eventos futuros cuando muestran tendencias a lo largo del tiempo.
- [Rectangle](/pdf/python-net/add-rectangle/) - es una de las muchas formas fundamentales que verás en los gráficos; puede ser muy útil para ayudarte a resolver un problema.
- [Ellipse](/pdf/python-net/add-ellipse/) - es un conjunto de puntos en un plano que forma una forma ovalada y curva.

Los detalles anteriores también se representan en las figuras siguientes:

![Figuras en gráficos](graphs.png)



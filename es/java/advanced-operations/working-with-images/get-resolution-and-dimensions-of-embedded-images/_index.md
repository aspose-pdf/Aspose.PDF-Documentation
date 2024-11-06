---
title: Obtener Resolución y Dimensiones de Imágenes Integradas
linktitle: Obtener Resolución y Dimensiones
type: docs
weight: 40
url: es/java/get-resolution-and-dimensions-of-embedded-images/
description: Esta sección muestra detalles para obtener la resolución y dimensiones de imágenes integradas
lastmod: "2021-06-05"
---

Este tema explica cómo usar las clases de operador en el espacio de nombres Aspose.PDF que proporcionan la capacidad de obtener información de resolución y dimensión sobre imágenes sin tener que extraerlas.

Hay diferentes maneras de lograr esto. Este artículo explica cómo usar un `arraylist` y [clases de colocación de imágenes](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. Primero, cargue el archivo PDF de origen (con imágenes).
1. Luego cree un objeto ArrayList para mantener los nombres de cualquier imagen en el documento.
1. Obtenga las imágenes usando la propiedad Page.Resources.Images.
1. Cree un objeto de pila para mantener el estado gráfico de la imagen y úselo para realizar un seguimiento de diferentes estados de imagen.

1. Crea un objeto ConcatenateMatrix que defina la transformación actual. También admite escalar, rotar e inclinar cualquier contenido. Concatena la nueva matriz con la anterior. Tenga en cuenta que no podemos definir la transformación desde cero, sino solo modificar la transformación existente.
1. Debido a que podemos modificar la matriz con ConcatenateMatrix, también puede ser necesario volver al estado original de la imagen. Use los operadores GSave y GRestore. Estos operadores están emparejados, por lo que deben ser llamados juntos. Por ejemplo, si realiza algún trabajo gráfico con transformaciones complejas y finalmente devuelve las transformaciones al estado inicial, el enfoque será algo como esto:

```java
// Dibuja algún texto
GSave

ConcatenateMatrix  // rota los contenidos después del operador

// Algún trabajo gráfico

ConcatenateMatrix // escala (con la rotación previa) los contenidos después del operador

// Algún otro trabajo gráfico

GRestore

// Dibuja algún texto
```

Como resultado, el texto se dibuja en forma regular, pero se realizan algunas transformaciones entre los operadores de texto.
 Para mostrar la imagen o dibujar objetos de formulario e imágenes, necesitamos usar el operador Do.

También tenemos una clase llamada XImage que proporciona dos propiedades, Ancho y Alto, que se pueden usar para obtener las dimensiones de la imagen.

1. Realizar algunos cálculos para calcular la resolución de la imagen.
2. Mostrar la información en un Command Prompt junto con el nombre de la imagen.

El siguiente fragmento de código te muestra cómo obtener las dimensiones y la resolución de una imagen sin extraer la imagen del documento PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Cargar el archivo PDF de origen
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Definir la resolución predeterminada para la imagen
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Definir objeto de lista de arrays que contendrá los nombres de las imágenes
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Insertar un objeto en la pila
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Obtener todos los operadores en la primera página del documento
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Usar operadores GSave/GRestore para revertir las transformaciones a las previamente establecidas
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Instanciar objeto ConcatenateMatrix ya que define la matriz de transformación actual.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Crear operador Do que dibuja objetos de recursos. Dibuja objetos de Formulario y objetos de Imagen
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Guardar estado anterior y empujar el estado actual a la parte superior de la pila
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Descartar el estado actual y restaurar el anterior
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // Multiplicar la matriz actual con la matriz de estado
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // En caso de que este sea un operador de dibujo de imagen
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Crear objeto XImage para contener imágenes de la primera página del pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Obtener dimensiones de la imagen
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Obtener información de Alto y Ancho de la imagen
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Calcular la resolución basada en la información anterior
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Mostrar la información de Dimensión y Resolución de cada imagen
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Guardar documento de salida
                doc.save(_dataDir);
            }
        }
    }
}
```
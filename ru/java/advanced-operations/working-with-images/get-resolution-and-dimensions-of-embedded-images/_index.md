---
title: Получение разрешения и размеров встроенных изображений
linktitle: Получение разрешения и размеров
type: docs
weight: 40
url: /ru/java/get-resolution-and-dimensions-of-embedded-images/
description: Этот раздел показывает детали получения разрешения и размеров встроенных изображений
lastmod: "2021-06-05"
---

Эта тема объясняет, как использовать классы операторов в пространстве имен Aspose.PDF, которые предоставляют возможность получать информацию о разрешении и размерах изображений, без необходимости извлекать их.

Существует несколько способов достижения этой цели. В этой статье объясняется, как использовать `arraylist` и [классы размещения изображений](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. Сначала загрузите исходный PDF файл (с изображениями).
1. Затем создайте объект ArrayList для хранения имен любых изображений в документе.
1. Получите изображения, используя свойство Page.Resources.Images.
1. Создайте объект стека для хранения графического состояния изображения и используйте его для отслеживания различных состояний изображений.

1. Создайте объект ConcatenateMatrix, который определяет текущее преобразование. Он также поддерживает масштабирование, вращение и искажение любого содержимого. Он объединяет новую матрицу с предыдущей. Обратите внимание, что мы не можем определить преобразование с нуля, а можем только изменить существующее преобразование.
1. Поскольку мы можем изменить матрицу с помощью ConcatenateMatrix, нам также может понадобиться вернуть изображение в исходное состояние. Используйте операторы GSave и GRestore. Эти операторы идут парой, поэтому их следует вызывать вместе. Например, если вы выполняете графическую работу со сложными преобразованиями и в конечном итоге возвращаете преобразования в начальное состояние, подход будет следующим:

```java
// Нарисовать текст
GSave

ConcatenateMatrix  // повернуть содержимое после оператора

// Некоторая графическая работа

ConcatenateMatrix // масштабировать (с предыдущим вращением) содержимое после оператора

// Другая графическая работа

GRestore

// Нарисовать текст
```

В результате текст рисуется в обычной форме, но между операторами текста выполняются некоторые преобразования.
 Для отображения изображения или рисования объектов форм и изображений, нам нужно использовать оператор Do.

У нас также есть класс под названием XImage, который предоставляет два свойства, Ширина и Высота, которые можно использовать для получения размеров изображения.

1. Выполните некоторые вычисления для вычисления разрешения изображения.
2. Отобразите информацию в командной строке вместе с именем изображения.

Следующий фрагмент кода показывает, как получить размеры и разрешение изображения без извлечения изображения из PDF-документа.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Загрузите исходный PDF файл
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Определите разрешение по умолчанию для изображения
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Определите объект списка массивов, который будет содержать имена изображений
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Вставьте объект в стек
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Получите всех операторов на первой странице документа
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Используйте оператор GSave/GRestore для возврата трансформаций к ранее установленным
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Создайте объект ConcatenateMatrix, так как он определяет текущую матрицу преобразования.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Создайте оператор Do, который рисует объекты из ресурсов. Он рисует объекты формы и изображения
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Сохраните предыдущее состояние и поместите текущее состояние на вершину стека
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Удалите текущее состояние и восстановите предыдущее
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

                // Умножьте текущую матрицу на матрицу состояния
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // В случае, если это оператор рисования изображения
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Создайте объект XImage для хранения изображений первой страницы pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Получите размеры изображения
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Получите информацию о высоте и ширине изображения
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Вычислите разрешение на основе вышеуказанной информации
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Отобразите информацию о размерах и разрешении каждого изображения
                    System.out.printf(_dataDir + "image %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Сохраните выходной документ
                doc.save(_dataDir);
            }
        }
    }
}
```
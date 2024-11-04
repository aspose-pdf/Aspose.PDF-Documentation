---
title: Работа с Операторами
linktitle: Работа с Операторами
type: docs
weight: 170
url: /java/operators/
description: Эта тема объясняет, как использовать операторы с Aspose.PDF. Классы операторов предоставляют отличные возможности для манипуляции с PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Введение в Операторы PDF и их Использование

Оператор — это ключевое слово PDF, указывающее на действие, которое должно быть выполнено, например, отрисовка графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа косой черты (2Fh). Операторы имеют смысл только внутри потока содержимого.

Поток содержимого — это объект потока PDF, чьи данные состоят из инструкций, описывающих графические элементы, которые будут нарисованы на странице. Более подробную информацию об операторах PDF можно найти в [спецификации PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Подробности Реализации

Эта тема объясняет, как использовать операторы с Aspose.PDF.
 The selected example adds an image into a PDF file to illustrate the concept. To add an image in a PDF file, different operators are needed. This example uses [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), and [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- The [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) operator saves the PDF's current graphical state.
- The This topic explains how to use operators with Aspose.PDF. Выбранный пример добавляет изображение в PDF-файл для иллюстрации концепции. Для добавления изображения в PDF-файл требуются разные операторы. Этот пример использует [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) и [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- Оператор (concatenate matrix) используется для определения того, как изображение должно быть размещено на странице PDF.
- Оператор [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) рисует изображение на странице.
- Оператор [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) восстанавливает графическое состояние.

Чтобы добавить изображение в PDF-файл:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и откройте входной PDF-документ.
1. Получите конкретную страницу, на которую будет добавлено изображение.
1. Добавьте изображение в коллекцию ресурсов страницы.
1. Используйте операторы для размещения изображения на странице:
   - Сначала используйте оператор [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) для сохранения текущего графического состояния.
   - Затем используйте оператор [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) для указания, где должно быть размещено изображение.
   - Используйте оператор [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) для отрисовки изображения на странице.
1. Наконец, используйте оператор [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) для сохранения обновленного графического состояния.

Следующий фрагмент кода показывает, как использовать операторы PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // Создайте новый PDF документ
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Получите страницу, на которую нужно добавить изображение
        Page page = pdfDocument.getPages().get_Item(1);

        // Установите координаты
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Загрузите изображение в поток
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Блок для обработки исключения
            e.printStackTrace();
        }

        // Добавьте изображение в коллекцию изображений ресурсов страницы
        page.getResources().getImages().add(imageStream);

        // Использование оператора GSave: этот оператор сохраняет текущее графическое состояние
        page.getContents().add(new GSave());
        // Создайте объекты Rectangle и Matrix
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Использование оператора ConcatenateMatrix (конкатенация матрицы): определяет, как должно быть размещено изображение
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Использование оператора Do: этот оператор рисует изображение
        page.getContents().add(new Do(ximage.getName()));
        // Использование оператора GRestore: этот оператор восстанавливает графическое состояние
        page.getContents().add(new GRestore());

        // Сохраните обновленный документ
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## Нарисовать XForm на странице, используя операторы

Эта тема демонстрирует, как использовать операторы GSave/GRestore, оператор ContatenateMatrix для позиционирования xForm и оператор Do для рисования xForm на странице.

Код ниже обертывает существующее содержимое PDF-файла парой операторов GSave/GRestore. Этот подход помогает получить начальное состояние графики в конце существующего содержимого. Без этого подхода в конце цепочки существующих операторов могут оставаться нежелательные преобразования.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // Пример демонстрирует
        // Использование операторов GSave/GRestore
        // Использование оператора ContatenateMatrix для позиционирования xForm
        // Использование оператора Do для рисования xForm на странице

        // Обернуть существующее содержимое парой операторов GSave/GRestore
        // это необходимо для получения начального состояния графики в конце существующего содержимого
        // иначе в конце цепочки существующих операторов могут оставаться нежелательные преобразования
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Добавить оператор сохранения состояния графики для правильного очистки состояния графики после
        // новых команд
        pageContents.add(new GSave());

        // Создать xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Определить ширину и высоту изображения
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Загрузить изображение в поток
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        // Добавить изображение в коллекцию изображений ресурсов XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Используя оператор Do: этот оператор рисует изображение
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Разместить форму в координатах x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Нарисовать форму с помощью оператора Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Разместить форму в координатах x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Нарисовать форму с помощью оператора Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // // Восстановить состояние графики с помощью GRestore после GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## Удаление графических объектов с использованием операторных классов

Операторные классы предоставляют отличные возможности для манипуляции с PDF. Когда PDF файл содержит графику, которую невозможно удалить с помощью метода [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) класса [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), операторные классы могут быть использованы для её удаления.

Следующий фрагмент кода показывает, как удалить графику. Обратите внимание, что если PDF файл содержит текстовые метки для графики, они могут сохраниться в PDF файле, используя этот подход. Поэтому ищите графические операторы для альтернативного метода удаления таких изображений.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // Используемые операторы рисования путей
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## Изменение цветового пространства PDF документа

{{% alert color="primary" %}}

Aspose.PDF для Java 9.0.0 поддерживает изменение цветового пространства PDF документа. Возможность изменения цвета RGB на CMYK и наоборот.

{{% /alert %}}

Следующие методы были реализованы в классе [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) для изменения цветового пространства. Используйте их для изменения некоторых конкретных цветов RGB/CMYK в цветовое пространство CMYK/RGB, сохраняя остальную часть PDF документа без изменений.

{{% alert color="primary" %}}
**Изменения в публичном API**
Реализованы следующие методы:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

Следующий фрагмент кода демонстрирует, как изменить цветовое пространство с использованием Aspose.PDF для Java.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("Значения операторов цвета RGB в pdf-документе");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // Преобразование RGB в цвет CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("Неподдерживаемая команда");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// Проверка результата
System.out.println("Значения преобразованных операторов цвета CMYK в результирующем pdf-документе");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```
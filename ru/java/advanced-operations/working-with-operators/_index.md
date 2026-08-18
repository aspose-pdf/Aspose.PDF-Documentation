---
title: Работа с операторами PDF в Java
linktitle: Работа с операторами
type: docs
weight: 90
url: /java/working-with-operators/
description: Узнайте, как использовать низкоуровневые операторы PDF в Java для манипулирования потоками контента, размещения изображений, повторного использования XForm и очистки графики.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Используйте низкоуровневые операторы PDF для управления потоком контента в Java.
Abstract: В этой статье объясняется, как работать с низкоуровневыми операторами PDF в Aspose.PDF для Java. Узнайте, как точно размещать изображения, рисовать многоразовое содержимое XForm и удалять графические операторы со страниц PDF.
---
## Введение в операторы PDF и их использование

Оператор — это ключевое слово PDF, определяющее какое-либо действие, которое должно быть выполнено, например рисование графической фигуры на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа косой черты (2Fh). Операторы имеют смысл только внутри потока контента.

Поток контента — это объект потока PDF, данные которого состоят из инструкций, описывающих графические элементы, которые должны быть нарисованы на странице. Более подробную информацию об операторах PDF можно найти в [спецификации PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Используйте эту страницу, когда вам нужен прямой контроль над потоком содержимого PDF в Java, например, размещение изображения с явной матричной математикой, многократное использование одной и той же графики через XForm или удаление низкоуровневых инструкций по рисованию со страницы.

## Добавьте изображение с помощью операторов PDF

Используйте операторы низкого уровня, когда размещение изображения должно контролироваться точно на уровне потока контента, а не с помощью API-интерфейсов макета более высокого уровня.

1. Откройте исходный PDF-файл с помощью [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Добавьте поток входного изображения к ресурсам страницы и сохраните возвращаемое имя ресурса.
1. Создайте [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), который определяет целевую область, и постройте [Матрицу](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) на основе ее границ.
1. Используйте [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) для сохранения текущего состояния графики, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) для позиционирования изображения, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) для его рисования и [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) для восстановления предыдущего состояния.
1. Сохраните обновленный PDF-документ.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## Нарисуйте многоразовое содержимое XForm на странице.

Используйте этот подход, когда одно и то же изображение или графику необходимо визуализировать более одного раза без дублирования ресурса в PDF-файле.

1. Откройте исходный PDF-файл с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), получите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и получите доступ к ее [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Оберните существующее содержимое страницы с помощью [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) и [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/), чтобы последующие преобразования не просочились в исходный поток содержимого.
1. Создайте ресурс [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/), добавьте изображение в ресурсы формы и используйте [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) плюс [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/), чтобы нарисовать изображение внутри формы.
1. Разместите одну и ту же форму по координатам нескольких страниц, добавив матрицу перевода и выполнив имя формы с помощью оператора `Do`.
1. Восстановите состояние графики и сохраните выходной PDF-файл.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## Удаление графических операторов со страницы

Используйте этот пример, если страница содержит операторы векторного рисования, которые необходимо удалить непосредственно из потока контента.

1. Откройте исходный PDF-файл с помощью [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Перебирайте операторы содержимого страницы и собирайте экземпляры [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) и [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Удалите собранные операторы из содержимого страницы и сохраните обновленный PDF-файл.

Этот метод удаляет только целевые инструкции по рисованию. Если страница также содержит связанные текстовые метки или другие неграфические операторы, эти элементы остаются в потоке контента и, возможно, потребуется отдельный этап очистки.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## Связанные темы

- [Расширенные операции с PDF в Java](/pdf/java/advanced-operations/)
- [Работа с изображениями в PDF с помощью Java](/pdf/java/working-with-images/)
- [Работа со страницами PDF в Java](/pdf/java/working-with-pages/)
- [Работа с векторной графикой в ​​Java](/pdf/java/working-with-vector-graphics/)

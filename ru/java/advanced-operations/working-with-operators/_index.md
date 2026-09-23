---
title: Работа с PDF-операторами в Java
linktitle: Работа с операторами
type: docs
weight: 90
url: /ru/java/working-with-operators/
description: Узнайте, как использовать низкоуровневые PDF-операторы в Java для манипулирования потоками содержимого, размещения изображений, повторного использования XForm и очистки графики.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Используйте низкоуровневые PDF-операторы для управления потоками содержимого в Java
Abstract: В этой статье объясняется, как работать с низкоуровневыми PDF‑операторами в Aspose.PDF for Java. Узнайте, как точно размещать изображения, рисовать переиспользуемый контент XForm и удалять графические операторы со страниц PDF.
---
## Введение в PDF‑операторы и их использование

Оператор — это PDF‑ключевое слово, указывающее действие, которое должно быть выполнено, например, отрисовка графической формы на странице. Ключевое слово оператора отличается от именованного объекта отсутствием начального символа косой черты (2Fh). Операторы имеют смысл только внутри контент‑потока.

Контент‑поток — это объект PDF‑потока, данные которого состоят из инструкций, описывающих графические элементы, которые необходимо отрисовать на странице. Более подробная информация о PDF‑операторах доступна в [Спецификация PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Используйте эту страницу, когда вам требуется прямой контроль над потоком содержимого PDF в Java, например, размещение изображения с явными матричными вычислениями, повторное использование одной и той же графики несколько раз через XForm или удаление низкоуровневых инструкций рисования со страницы.

## Добавление изображения с помощью PDF-операторов

Используйте низкоуровневые операторы, когда размещение изображения должно контролироваться точно на уровне потока содержимого, а не через API более высокого уровня для макета.

1. Откройте исходный PDF с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите целевой [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Добавьте поток входного изображения к ресурсам страницы и сохраните возвращённое имя ресурса.
1. Создайте [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), который определяет целевую область, и постройте [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) по его границам.
1. Используйте [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) для сохранения текущего графического состояния, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) для позиционирования изображения, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) для его отрисовки и [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) для восстановления предыдущего состояния.
1. Сохраните обновлённый PDF‑документ.

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

## Отрисовка переиспользуемого XForm‑контента на странице

Используйте этот подход, когда одно и то же изображение или графика должны отображаться более одного раза без дублирования ресурса в файле PDF.

1. Откройте исходный PDF с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), выберите нужную страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и получите доступ к её [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Заключите существующее содержимое страницы между [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) и [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/), чтобы последующие преобразования не повлияли на исходный поток содержимого.
1. Создайте ресурс [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/), добавьте изображение в ресурсы формы и используйте [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) и [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/), чтобы нарисовать изображение внутри формы.
1. Разместите одну и ту же форму в нескольких точках страницы, добавив матрицу переноса и вызвав оператор `Do` с именем формы.
1. Восстановите состояние графики и сохраните PDF‑вывод.

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

Используйте этот пример, когда страница содержит операторы векторного рисования, которые следует удалить непосредственно из потока содержимого.

1. Откройте исходный PDF с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите целевой [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Переберите операторы содержимого страницы и соберите экземпляры [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) и [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Удалите собранные операторы из содержимого страниц и сохраните обновлённый PDF.

Эта техника удаляет только целевые инструкции рисования. Если на странице также содержатся связанные текстовые подписи или другие не графические операторы, эти элементы остаются в потоке содержимого и могут потребовать отдельного прохода очистки.

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

- [Продвинутые операции с PDF в Java](/pdf/ru/java/advanced-operations/)
- [Работа с изображениями в PDF с помощью Java](/pdf/ru/java/working-with-images/)
- [Работа со страницами PDF в Java](/pdf/ru/java/working-with-pages/)
- [Работа с векторной графикой на Java](/pdf/ru/java/working-with-vector-graphics/)



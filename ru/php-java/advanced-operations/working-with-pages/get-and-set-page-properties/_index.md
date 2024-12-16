---
title: Получение и Установка Свойств Страницы
type: docs
weight: 30
url: /ru/php-java/get-and-set-page-properties/
description: Эта тема объясняет, как получить номера в PDF-файле, получить свойства страницы и определить цвет страницы с использованием Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
---

Aspose.PDF для PHP через Java позволяет читать и устанавливать свойства страниц в PDF-файле в ваших Java-приложениях. Этот раздел показывает, как получить количество страниц в PDF-файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страницы.

## Получение Количества Страниц в PDF-Файле

При работе с документами вы часто хотите знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF-файле:

1. Откройте PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Затем страницы документа извлекаются. Пытается получить количество страниц из извлеченных страниц.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

```php

    // Открыть документ
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Получить количество страниц
    $responseData = $responseData . "Количество страниц : " + $pages->size();
```

### Получить количество страниц без сохранения документа

Пока PDF файл не сохранён и все элементы фактически не размещены внутри PDF файла, мы не можем получить количество страниц для конкретного документа (потому что мы не можем быть уверены в количестве страниц, на которых будут размещены все элементы). Однако начиная с выпуска Aspose.PDF для PHP через Java, мы представили метод под названием [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--), который предоставляет возможность получить количество страниц для PDF документа, не сохраняя файл. Таким образом, мы можем получить информацию о количестве страниц на лету. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```php

    // Открыть документ
    $document = new Document($inputFile);      

    // добавить страницу в коллекцию страниц PDF файла
    $page = $document->getPages()->add();
    
    // создать цикл для добавления 300 экземпляров TextFragment
    for ($i=0; $i < 300; $i++) { 
       // добавить TextFragment в коллекцию параграфов первой страницы PDF
       $page->getParagraphs()->add(new TextFragment("Тест количества страниц"));
    }
    
    // обработать параграфы для получения информации о количестве страниц
    $document->processParagraphs();

    $pages = $document->getPages();

    // Получить количество страниц
    $responseData = $responseData . "Количество страниц : " + $pages->size();
```


## Получение Свойств Страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF позволяет вам получить доступ к этим свойствам.

### **Понимание Свойств Страницы: Различия между Artbox, BleedBox, CropBox, MediaBox, TrimBox и Rect свойством**

- **Медиабокс**: Медиабокс - это самый большой блок страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Другими словами, медиабокс определяет физический размер носителя, на котором отображается или печатается PDF-документ.
- **Блид-бокс**: Если документ имеет вылет, PDF также будет иметь блид-бокс.
 Bleed - это количество цвета (или графики), которое выходит за край страницы. Оно используется для того, чтобы при печати и обрезке документа до нужного размера ("подрезке") краска доходила до самого края страницы. Даже если страница неправильно обрезана - слегка отклонена от меток обрезки - на странице не появятся белые края.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box - это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box - это размер "страницы", при котором ваш PDF-документ отображается в Adobe Acrobat. В обычном режиме отображаются только содержимое Crop box в Adobe Acrobat.
  Для подробного описания этих свойств прочтите спецификацию Adobe.Pdf, особенно раздел 10.10.1 "Границы страницы".
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Изображение ниже иллюстрирует эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Доступ к свойствам страницы

Следующий фрагмент кода получает такие свойства, как ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Номер страницы и Поворот для конкретной страницы в документе. Затем он сохраняет извлеченные данные в отдельные переменные и объединяет их в строку ответа.

1. Создайте новый объект Document, используя переменную $inputFile.
1. Получите коллекцию страниц из документа, используя метод getPages().
1. Получите конкретную страницу из коллекции страниц, используя метод get_Item().
1. Извлеките различные свойства (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Номер страницы, Поворот) из объекта конкретной страницы и сохраните их в отдельные переменные.
1. Код объединяет извлеченные значения свойств в отдельные строки ответа ($responseData1, $responseData2 и т.д.).
1. Далее он пытается получить количество страниц, используя метод size() на объекте $pages, но переменная $pages не определена.

Следующий фрагмент кода показывает, как получить свойства страницы.

```php

   // Открыть документ
    $document = new Document($inputFile);

    // Получить коллекцию страниц
    $pageCollection = $document->getPages();

    // Получить конкретную страницу
    $page = $pageCollection->get_Item(1);

    // Получить свойства страницы
    $responseData1 = "ArtBox : Высота = " . $page->getArtBox()->getHeight()
        . ", Ширина = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Высота = " . $page->getBleedBox()->getHeight() . ", Ширина = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Высота = " . $page->getCropBox()->getHeight() . ", Ширина = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Высота = " . $page->getMediaBox()->getHeight() . ", Ширина = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Высота = " . $page->getTrimBox()->getHeight() . ", Ширина = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Высота = " . $page->getRect()->getHeight() . ", Ширина = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Номер страницы :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Поворот :-" . $page->getRotate() . PHP_EOL;

    // Получить количество страниц
    $responseData8 = $responseData8 . "Количество страниц : " . $pages->size();
```


## Определение цвета страницы

Класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) предоставляет свойства, связанные с конкретной страницей в PDF-документе, включая тип цвета - RGB, черно-белый, градации серого или неопределенный - который используется на странице.

Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). Свойство [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) указывает цвет элементов на странице. Чтобы получить или определить информацию о цвете для конкретной страницы PDF, используйте свойство [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) объекта класса [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

Следующий фрагмент кода показывает, как перебрать каждую страницу PDF-файла, чтобы получить информацию о цвете.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Перебрать все страницы PDF-файла
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Получить информацию о типе цвета для конкретной страницы PDF
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Страница # -" . $pageCount . " - черно-белая..";
                break;
            case 1:
                $responseData ="Страница # -" . $pageCount . " - градации серого...";
                break;
            case 0:
                $responseData ="Страница # -" . $pageCount . " - RGB..";
                break;
            case 3:
                $responseData ="Страница # -" . $pageCount . " - цвет не определен..";
                break;
        }
    }
```
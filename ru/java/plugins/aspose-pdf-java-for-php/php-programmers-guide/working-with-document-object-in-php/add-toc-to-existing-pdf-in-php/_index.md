---
title: Добавить Оглавление в Существующий PDF на PHP
type: docs
weight: 20
url: ru/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавить Оглавление

Чтобы добавить оглавление в PDF документ, используя **Aspose.PDF Java для PHP**, просто вызовите класс **AddToc**.

PHP Код

```php

# Открыть PDF документ.
$doc = new Document($dataDir . "input1.pdf");

# Получить доступ к первой странице PDF файла
$toc_page = $doc->getPages()->insert(1);

# Создать объект для представления информации об оглавлении
$toc_info = new TocInfo();
$title = new TextFragment("Содержание");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Установить заголовок для оглавления
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Создать строковые объекты, которые будут использоваться как элементы оглавления
$titles = array("Первая страница", "Вторая страница");

$i = 0;
while ($i < 2){

    # Создать объект Заголовок
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Указать страницу назначения для объекта заголовка
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Страница назначения
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Координата назначения
    $segment2->setText($titles[$i]);

    # Добавить заголовок на страницу, содержащую оглавление
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Сохранить PDF документ
$doc->save($dataDir . "TOC.pdf");

print "Оглавление успешно добавлено, пожалуйста, проверьте выходной файл.";

```


**Скачать Запускаемый Код**

Скачайте **Add TOC (Aspose.PDF)** с любого из ниже перечисленных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)
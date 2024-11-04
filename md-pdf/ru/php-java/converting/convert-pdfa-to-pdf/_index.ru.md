---
title: Преобразование PDF/A в формат PDF
linktitle: Преобразование PDF/A в формат PDF
type: docs
weight: 110
url: /php-java/convert-pdfa-to-pdf/
lastmod: "2024-05-20"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовать файл PDF/A в документ PDF с помощью библиотеки PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование документа PDF/A в PDF

Преобразование документа PDF/A в PDF означает удаление ограничений <abbr title="Архив формата портативных документов">PDF/A</abbr> из оригинального документа. Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) имеет метод removePdfaCompliance(..) для удаления информации о соответствии PDF из входного/исходного файла.

```php
// Создайте новый экземпляр класса Document с входным файлом
$document = new Document($inputFile);

// Удалите соответствие PDF/A из документа
$document->removePdfaCompliance();

// Сохраните измененный документ в выходной файл
$document->save($outputFile);
```

Эта информация также будет удалена, если вы внесете любые изменения в документ (например,
 add pages). В следующем примере выходной документ теряет соответствие PDF/A после добавления страницы.

```php
// Создать новый экземпляр класса Document с входным файлом
$document = new Document($inputFile);

// Удалить соответствие PDF/A из документа
$document->getPages()->add();

// Сохранить измененный документ в выходной файл
$document->save($outputFile);
```
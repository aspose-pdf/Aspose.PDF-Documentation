---
title: Изменение AcroForms
linktitle: Изменение AcroForms
type: docs
weight: 40
url: ru/java/modifing-form/
description: В этом разделе объясняется, как изменять формы в вашем PDF документе с помощью Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Установка пользовательского шрифта для поля формы

Поля формы в файлах Adobe PDF могут быть настроены для использования определенных шрифтов по умолчанию. Aspose.PDF позволяет разработчикам применять любой шрифт в качестве шрифта по умолчанию для поля, будь то один из 14 основных шрифтов или пользовательский шрифт.
Чтобы установить и обновить шрифт по умолчанию, используемый для полей формы, Aspose.PDF имеет класс DefaultAppearance (Font font, double size, Color color). Этот класс может быть доступен с использованием com.aspose.pdf.DefaultAppearance. Чтобы использовать этот объект, используйте метод setDefaultAppearance(..) класса Field.

Следующий фрагмент кода показывает, как установить шрифт по умолчанию для поля формы PDF.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить конкретное поле формы из документа
    $field = $document->getForm()->get("textbox1");

    // Создать объект шрифта
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Установить информацию о шрифте для поля формы
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Сохранить обновленный документ
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Get/Set FieldLimit

Этот код демонстрирует использование класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) для открытия документа, извлечения поля формы, установки его максимальной длины, извлечения максимальной длины с помощью методов 'setMaxLen' и 'getMaxLen'.

```php

    // Открытие документа
    $document = new Document($inputFile);

    // Получение конкретного поля формы из документа
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Получение максимального ограничения поля с использованием DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

Вы также можете получить то же значение, используя пространство имен Aspose.PDF.Facades, с помощью следующего фрагмента кода.

```php

    // Открытие документа
    $document = new Document($inputFile);

    // Получение конкретного поля формы из документа
    $field = $document->getForm()->get("textbox1");

    // Получение максимального ограничения поля с использованием DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```


Similarly, Aspose.PDF имеет метод, который получает ограничение поля, используя подход DOM. Следующий фрагмент кода показывает шаги.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить конкретное поле формы из документа
    $field = $document->getForm()->get("textbox1");

    // Удалить поле
    $field->delete();
    
    $document->close();
```
## Удаление конкретного поля формы из PDF-документа

Все поля формы содержатся в коллекции Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Эта коллекция предоставляет различные методы, которые управляют полями формы, включая метод удаления. Если вы хотите удалить конкретное поле, передайте имя поля в качестве параметра методу удаления, а затем сохраните обновленный PDF-документ.

Следующий фрагмент кода показывает, как удалить именованное поле из PDF-документа.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить конкретное поле формы из документа
    $field = $document->getForm()->get("textbox1");

    // Удалить поле
    $field->delete();
    
    $document->close();
```


## Изменение поля формы в PDF-документе

Коллекция Form объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) позволяет управлять полями формы в PDF-документе.

Чтобы изменить поле формы, получите поле из коллекции Form и установите его свойства. Затем сохраните обновленный PDF-документ.

Следующий фрагмент кода показывает, как изменить существующее поле формы в PDF-документе.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить конкретное поле формы из документа
    $field = $document->getForm()->get("textbox1");

    // Изменить значение поля
    $field->setValue("Обновленное значение");

    // Установить поле только для чтения
    $field->setReadOnly(true);

    // Сохранить обновленный документ
    $document->save($outputFile);        
    $document->close();
```

### Перемещение поля формы на новое место в PDF-файле

Если вы хотите переместить поле формы на новое место на странице PDF, сначала получите объект поля, а затем укажите новое значение для его метода setRect.
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) объект с новыми координатами назначается методу setRect(..). Затем сохраните обновленный PDF, используя метод save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает, как переместить поле формы в новое место.

```php

    // Открыть документ
    $document = new Document($inputFile);

    // Получить конкретное поле формы из документа
    $field = $document->getForm()->get("textbox1");

    // Изменить расположение поля
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Сохранить обновленный документ
    $document->save($outputFile);        
    $document->close();
```
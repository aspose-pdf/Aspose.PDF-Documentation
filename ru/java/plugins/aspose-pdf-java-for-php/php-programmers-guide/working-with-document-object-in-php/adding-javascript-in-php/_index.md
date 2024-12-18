---
title: Добавление JavaScript в PHP
type: docs
weight: 10
url: /ru/java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Добавление JavaScript

Чтобы добавить JavaScript в PDF-документ с использованием **Aspose.PDF Java for PHP**, просто вызовите класс **AddJavaScript**.

PHP Код

```php
# Открыть PDF-документ.
$doc = new Document($dataDir . "input1.pdf");

# Добавление JavaScript на уровне документа
# Создание объекта JavascriptAction с желаемым JavaScript выражением
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Назначение объекта JavascriptAction для желаемого действия документа
$doc->setOpenAction($javaScript);

# Добавление JavaScript на уровне страницы
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Сохранить PDF-документ
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScript успешно добавлен, пожалуйста, проверьте выходной файл.";
```


**Загрузка Исполняемого Кода**

Загрузите **Добавление JavaScript (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
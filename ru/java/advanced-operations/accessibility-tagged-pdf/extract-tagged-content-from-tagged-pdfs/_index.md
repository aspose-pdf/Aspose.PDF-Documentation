---
title: Извлечение содержимого с тегами из PDF
linktitle: Извлечение содержимого с тегами
type: docs
weight: 20
url: ru/java/extract-tagged-content-from-tagged-pdfs/
description: Эта статья объясняет, как извлечь содержимое с тегами из PDF-документа с использованием Aspose.PDF для Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение содержимого PDF с тегами

Для получения содержимого PDF-документа с текстом с тегами, Aspose.PDF предоставляет метод [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Приведенный ниже фрагмент кода показывает, как получить содержимое PDF-документа с текстом с тегами:

```java
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории документов.
String path = "pathTodir";

// Создать PDF-документ
Document document = new Document();

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Работа с содержимым Tagged Pdf
//

// Установить заголовок и язык для документа
taggedContent.setTitle("Простой документ с тегами PDF");
taggedContent.setLanguage("en-US");

// Сохранить документ с тегами PDF
document.save(path + "TaggedPDFContent.pdf");
```


## Получение корневой структуры

Для получения корневой структуры помеченного PDF-документа Aspose.PDF предлагает методы [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) и **getStructureElement()** интерфейса [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Следующий фрагмент кода показывает, как получить корневую структуру помеченного PDF-документа:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Путь к директории с документами.
String path = "pathTodir";
// Создание PDF документа
Document document = new Document();

// Получение контента для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Установка заголовка и языка для документа
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Свойства StructTreeRootElement и RootElement используются для доступа к
// объекту StructTreeRoot PDF документа и к корневому элементу структуры (элемент структуры документа).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## Доступ к дочерним элементам

Для доступа к дочерним элементам Tagged PDF документа, Aspose.PDF предлагает класс **ElementList**. Следующий фрагмент кода показывает, как получить доступ к дочерним элементам Tagged PDF документа:

```java
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Открыть PDF документ
Document document = new Document( path +"StructureElements.pdf");

// Получить содержимое для работы с TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Доступ к корневому элементу(ам)
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Получить свойства
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Доступ к дочерним элементам первого элемента в корневом элементе
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Установить свойства
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Сохранить Tagged PDF документ
document.save( path +"AccessChildrenElements.pdf");
```
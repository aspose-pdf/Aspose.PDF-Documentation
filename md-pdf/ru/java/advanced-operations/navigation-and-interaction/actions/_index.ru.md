---
title: Работа с Действиями
linktitle: Действия
type: docs
weight: 20
url: /java/actions/
description: Этот раздел объясняет, как программно добавлять действия в документ и поля формы с помощью Java. Узнайте, как добавить, создать и получить гиперссылку в PDF-файле.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF-файл может содержать встроенные вложения, и часто необходимо создавать гиперссылки на эти документы. Вы можете направить читателей из основного PDF-документа к вложению PDF, создав ссылку в основном документе, которая указывает на вложение.

## Добавление Гиперссылки в PDF-Файл

Можно добавлять гиперссылки в PDF-файлы, либо чтобы позволить читателям перейти к другой части PDF, либо к внешнему контенту.

Для того, чтобы добавить веб-гиперссылки в PDF-документы:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Получите класс [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), к которому вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) с использованием объектов Page и [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle). Объект Rectangle используется для указания места на странице, где должна быть добавлена ссылка.
1. Установите метод getAction в объект [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction), который указывает расположение удаленного URI.
1. Чтобы отобразить текст гиперссылки, добавьте строку текста в место, аналогичное тому, где расположен объект [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation).
1. Чтобы добавить свободный текст:

- Создайте экземпляр объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation).
 Он также принимает объекты Page и Rectangle в качестве аргументов, поэтому возможно предоставить те же значения, что и указанные в конструкторе LinkAnnotation.
- Используя свойство Contents объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation), укажите строку, которая должна отображаться в выходном PDF.
- При необходимости установите ширину границы объектов [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) и FreeTextAnnotation в 0, чтобы они не отображались в PDF-документе.
- После того как объекты [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) и [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) были определены, добавьте эти ссылки в коллекцию аннотаций объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

- Наконец, сохраните обновленный PDF, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
The following code snippet shows you how to add a hyperlink to a PDF file.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Открыть документ
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Создать ссылку
        Page page = document.getPages().get_Item(1);
        // Создать объект аннотации ссылки
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Создать объект границы для LinkAnnotation
        Border border = new Border(link);
        // Установить значение ширины границы как 0
        border.setWidth(0);
        // Установить границу для LinkAnnotation
        link.setBorder(border);
        // Указать тип ссылки как удаленный URI
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Добавить аннотацию ссылки в коллекцию аннотаций первой страницы PDF файла
        page.getAnnotations().add(link);

        // Создать аннотацию свободного текста
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // Строка, которая будет добавлена как свободный текст
        textAnnotation.setContents("Ссылка на сайт Aspose");
        // Установить границу для аннотации свободного текста
        textAnnotation.setBorder(border);
        // Добавить аннотацию свободного текста в коллекцию аннотаций первой страницы документа
        page.getAnnotations().add(textAnnotation);

        // Сохранить обновленный документ
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```


## Создание гиперссылки на страницы в том же PDF

Aspose.PDF для Java предоставляет отличные возможности для создания PDF, а также его манипуляции. Он также предлагает возможность добавлять ссылки на страницы PDF, и ссылка может направлять либо на страницы в другом PDF файле, веб-URL, запускать приложение или даже ссылаться на страницы в том же PDF файле.

Для того чтобы добавить локальную гиперссылку, нам нужно создать TextFragment, чтобы ссылка могла быть связана с TextFragment. Класс [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) имеет метод под названием [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--), который используется для связывания экземпляра LocalHyperlink. Следующий фрагмент кода показывает шаги для выполнения этого требования.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Создать экземпляр Document
        Document document = new Document();

        // Добавить страницу в коллекцию страниц PDF файла
        Page page = document.getPages().add();

        // Создать экземпляр Text Fragment
        TextFragment text = new TextFragment("link page number test to page 2");

        // Создать экземпляр локальной гиперссылки
        LocalHyperlink link = new LocalHyperlink();

        // Установить целевую страницу для экземпляра ссылки
        link.setTargetPageNumber(2);

        // Установить гиперссылку для TextFragment
        text.setHyperlink(link);

        // Добавить текст в коллекцию абзацев страницы
        page.getParagraphs().add(text);

        // Создать новый экземпляр TextFragment
        text = new TextFragment("link page number test to page 1");

        // TextFragment должен быть добавлен на новую страницу
        text.setInNewPage(true);

        // Создать другой экземпляр локальной гиперссылки
        link = new LocalHyperlink();

        // Установить целевую страницу для второй гиперссылки
        link.setTargetPageNumber(1);

        // Установить ссылку для второго TextFragment
        text.setHyperlink(link);

        // Добавить текст в коллекцию абзацев объекта страницы
        page.getParagraphs().add(text);

        // Сохранить обновленный документ
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```


## Получить URL назначения гиперссылки в PDF

Ссылки представлены в виде аннотаций в PDF-файле, и их можно добавлять, обновлять или удалять. Aspose.PDF для Java также поддерживает получение назначения (URL) гиперссылки в PDF-файле.

Чтобы получить URL ссылки:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Получите [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), с которой вы хотите извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector), чтобы извлечь все объекты [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) с указанной страницы.
1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) методу Accept объекта [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

1. Получите все выбранные аннотации ссылок в объект IList, используя свойство Selected объекта [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector).
2. Наконец, извлеките действие LinkAnnotation как GoToURIAction.

Следующий фрагмент кода показывает, как получить назначения гиперссылок (URL) из PDF-файла.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Извлечение действий
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Перебор индивидуальных элементов внутри списка
        if (list.size() == 0)
            System.out.println("Гиперссылки не найдены..");
        else {
            // Перебор всех закладок
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Вывод URL назначения
                    System.out.println("Назначение: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // конец else
    }
```


## Получение текста гиперссылки

Гиперссылка состоит из двух частей: текста, который отображается в документе, и URL-адреса назначения. В некоторых случаях нам нужен именно текст, а не URL.

Текст и аннотации/действия в PDF-файле представлены разными сущностями. Текст на странице — это просто набор слов и символов, в то время как аннотации придают некоторую интерактивность, такую как та, что присуща гиперссылке.

Чтобы найти содержимое URL, вам нужно работать как с аннотацией, так и с текстом. Объект [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) сам по себе не содержит текста, но располагается под текстом на странице. Таким образом, чтобы получить текст, аннотация дает границы URL, в то время как объект Text предоставляет содержимое URL. Пожалуйста, смотрите следующий фрагмент кода.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Извлечение действий
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Печать URL каждого аннотации ссылки
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Печать текста, связанного с гиперссылкой
                System.out.println(extractedText);
            }
        }
    }
```


## Удаление действия открытия документа из PDF файла

[Как указать страницу PDF при просмотре документа](#how-to-specify-pdf-page-when-viewing-document) объясняет, как указать документу открываться на другой странице, а не на первой. При объединении нескольких документов, и если в одном или более из них установлено действие GoTo, возможно, вы захотите удалить его. Например, если вы объединяете два документа и второй имеет действие GoTo, которое ведет вас на вторую страницу, выходной документ откроется на второй странице второго документа вместо первой страницы объединенного документа. Чтобы избежать этого поведения, удалите команду открытия.

Чтобы удалить действие открытия:

1. Установите метод [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) в null.
1. Сохраните обновленный PDF, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как удалить действие открытия документа из PDF файла.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Открыть документ
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Удалить действие открытия документа
        document.setOpenAction(null);
        
        // Сохранить обновленный документ
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```


## Как указать страницу PDF при просмотре документа {#how-to-specify-pdf-page-when-viewing-document}

При просмотре PDF файлов в просмотрщике PDF, таком как Adobe Reader, файлы обычно открываются на первой странице. Однако можно настроить файл на открытие на другой странице.

Класс [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) позволяет указать страницу в PDF файле, которую вы хотите открыть. При передаче значения объекта GoToAction методу getOpenAction класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), документ открывается на странице, указанной в объекте XYZExplicitDestination. Следующий фрагмент кода показывает, как указать страницу в качестве действия открытия документа.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Загрузить PDF файл
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Получить экземпляр второй страницы документа
        Page page2 = document.getPages().get_Item(2);
        // Создать переменную для установки коэффициента масштабирования целевой страницы
        double zoom = 1;
        // Создать экземпляр GoToAction
        GoToAction action = new GoToAction(page2);
        // Перейти на 2 страницу
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Установить действие открытия документа
        document.setOpenAction (action);
        // Сохранить обновленный документ
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```
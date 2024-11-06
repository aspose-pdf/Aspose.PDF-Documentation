---
title: Обновление ссылок в PDF 
linktitle: Обновление ссылок
type: docs
weight: 20
url: ru/java/update-links/
description: Обновление ссылок в PDF программным способом. Это руководство о том, как обновить ссылки в PDF на языке Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Обновление ссылок в PDF файле

Как обсуждалось в разделе Добавление гиперссылки в PDF файл, класс [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) позволяет добавлять ссылки в PDF файл. Существует также аналогичный класс, используемый для получения существующих ссылок из PDF файлов. Используйте его, если вам нужно обновить существующую ссылку. Чтобы обновить существующую ссылку:

1. Загрузите PDF файл.
1. Перейдите на конкретную страницу в PDF файле.
1. Укажите назначение ссылки с помощью свойства Destination объекта [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. Целевая страница указывается с помощью конструктора [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### Установка цели ссылки на страницу в том же документе

Следующий фрагмент кода показывает, как обновить ссылку в PDF-файле и установить ее цель на вторую страницу документа.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Загрузить PDF-файл
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Получить первую аннотацию ссылки с первой страницы документа
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Изменение ссылки: изменить назначение ссылки
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Укажите место назначения для объекта ссылки
        // Представляет явное назначение, которое отображает страницу с координатами (left, top), расположенными в верхнем левом углу 
        // окна, и содержимое страницы увеличено в соответствии с коэффициентом увеличения.
        // Первый параметр - номер целевой страницы.
        // Второй - левая координата
        // Третий - верхняя координата
        // Четвертый аргумент - коэффициент увеличения при отображении соответствующей страницы. Использование 2 означает, что страница будет отображаться в 200% увеличении
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Сохраните документ с обновленной ссылкой
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Установить пункт назначения ссылки на веб-адрес

Чтобы обновить гиперссылку так, чтобы она указывала на веб-адрес, создайте объект [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) и передайте его в свойство Action объекта LinkAnnotation. Следующий фрагмент кода показывает, как обновить ссылку в PDF-файле и установить ее цель как веб-адрес.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Загрузить PDF-файл
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Получить первую аннотацию ссылки с первой страницы документа
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Изменение ссылки: изменение действия ссылки и установка цели как веб-адрес
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Сохранить документ с обновленной ссылкой
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### Установить цель ссылки на другой PDF файл

Следующий фрагмент кода показывает, как обновить ссылку в PDF файле и установить её цель на другой PDF файл.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Загрузить PDF файл
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // Следующая строка обновляет пункт назначения, не обновляя файл
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // Следующая строка обновляет файл
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Сохранить документ с обновленной ссылкой
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Обновить цвет текста LinkAnnotation

Аннотация ссылки не содержит текста.
 Вместо этого текст размещается в содержимом страницы под аннотацией. Поэтому, чтобы изменить цвет текста, измените цвет текста страницы, вместо того чтобы пытаться изменить цвет аннотации. Следующий фрагмент кода показывает, как обновить цвет аннотации ссылки в PDF файле.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Загрузите PDF файл
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Найдите текст под аннотацией
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Измените цвет текста.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Сохраните документ с обновленной ссылкой
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```
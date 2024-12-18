---
title: Извлечение ссылок из PDF-файла
linktitle: Извлечение ссылок
type: docs
weight: 30
url: /ru/java/extract-links/
description: Извлечение ссылок из PDF с помощью Java. Эта тема объясняет, как извлечь ссылки с помощью класса AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение ссылок из PDF-файла

Ссылки представлены как аннотации в PDF-файле, поэтому для извлечения ссылок извлеките все объекты [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Получите [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page), с которой вы хотите извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) для извлечения всех объектов [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) с указанной страницы.

1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) методу Accept объекта Page.
1. Получите все выбранные аннотации ссылок в объект IList, используя метод [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) объекта [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

Следующий фрагмент кода показывает, как извлечь ссылки из PDF-файла.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // Загрузите PDF-файл
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("Аннотация расположена: " + annot.getRect());
        }
                
        // Сохраните документ с обновленной ссылкой
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```
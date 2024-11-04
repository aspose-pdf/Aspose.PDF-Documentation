---
title: Пример Hello World на Java
linktitle: Пример Hello World
type: docs
weight: 40
url: /java/hello-world-example/
description: Эта страница показывает, как использовать простое программирование для создания PDF-документа, содержащего текст - Hello World с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Пример Hello World

Пример “Hello World” традиционно используется для ознакомления с возможностями языка программирования или программного обеспечения с простым случаем использования.

Aspose.PDF для Java API дает возможность разработчикам Java-приложений создавать, читать, редактировать и обрабатывать PDF-файлы в своих приложениях. Он позволяет читать и конвертировать несколько различных типов файлов в формат PDF и обратно. В этой статье Hello World показано, как создать PDF-файл на Java с использованием Aspose.PDF для Java API. После [установки Aspose.PDF для Java](/pdf/java/installation/) в вашей среде, вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает Aspose.PDF API.

Приведенный ниже фрагмент кода следует следующим шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Добавьте TextFragment в коллекцию [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) страницы
1. Сохраните полученный PDF-документ

Следующий фрагмент кода является программой Hello World, демонстрирующей работу Aspose.PDF для Java API.

```java
// Инициализация объекта документа
Document document = new Document();
 
// Добавить страницу
Page page = document.getPages().add();
 
// Добавить текст на новую страницу
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Сохранить обновленный PDF
document.save("HelloWorld_out.pdf");
```
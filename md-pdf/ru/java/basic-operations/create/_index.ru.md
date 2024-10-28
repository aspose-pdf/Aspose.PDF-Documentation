---
title: Создать PDF документ
linktitle: Создать
type: docs
weight: 10
url: /java/create-document/
description: Узнайте, как создать PDF файл в Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для Java** API позволяет разработчикам приложений на Java внедрять функциональность обработки PDF документов в свои приложения. Он может использоваться для создания и чтения PDF файлов без необходимости установки какого-либо другого программного обеспечения на исходной машине. Aspose.PDF для Java может использоваться в различных типах приложений Java, таких как настольные, JSP и JSF приложения.

## Как создать PDF файл с использованием Java

Чтобы создать PDF файл с использованием Java, можно следовать следующим шагам.

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)

1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) в коллекцию [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) страницы
2. Сохраните полученный PDF-документ

```java
// Инициализировать объект документа
Document document = new Document();
 
//Добавить страницу
Page page = document.getPages().add();
 
// Добавить текст на новую страницу
page.getParagraphs().add(new TextFragment("Привет, мир!"));
 
// Сохранить обновленный PDF
document.save("HelloWorld_out.pdf");
```
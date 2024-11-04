---
title: Создать PDF документ 
linktitle: Создать
type: docs
weight: 10
url: /php-java/create-document/
description: Узнайте, как создать PDF файл в Aspose.PDF для PHP через Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF для PHP через Java** API позволяет разработчикам внедрять функциональность обработки PDF документов в свои приложения. Он может использоваться для создания и чтения PDF файлов без необходимости установки какого-либо другого программного обеспечения на базовой машине. Aspose.PDF для PHP через Java можно использовать в различных типах приложений, таких как Desktop, JSP и JSF приложения.

## Как создать PDF файл, используя PHP через Java

Чтобы создать PDF файл, используя PHP через Java, можно использовать следующие шаги.

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) к объекту документа

1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) в коллекцию [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) на странице
1. Сохраните итоговый PDF документ

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```
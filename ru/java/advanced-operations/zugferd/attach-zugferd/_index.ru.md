---
title: Создание PDF, соответствующего PDF/3-A, и добавление счета ZUGFeRD в Java
linktitle: Присоединение ZUGFeRD к PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Узнайте, как создать PDF-документ с ZUGFeRD в Aspose.PDF для Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Присоединение ZUGFeRD к PDF

Мы рекомендуем следующие шаги для присоединения ZUGFeRD к PDF:

* Определите переменную пути, указывающую на папку, где находятся входные и выходные PDF-файлы.
* Определите строковую переменную path, которая хранит путь к PDF-файлу, который будет обработан. Используйте метод `Paths.get` для объединения частей полного пути.
* Создайте блок try-with-resources, который гарантирует, что объект Document, созданный из переменной пути, будет автоматически закрыт после завершения блока. Объект Document представляет PDF-документ, который будет изменен и сохранен.

* Создайте объект [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/), предоставив путь и описание другого файла, который содержит метаданные счета, соответствующие стандарту ZUGFeRD.
 * Добавьте свойства в объект спецификации файла, такие как описание, MIME-тип и AFrelationship. AFrelationship указывает, как встроенный файл соотносится с PDF-документом. В данном случае он установлен как "Alternative", что означает, что встроенный файл является альтернативным представлением содержимого PDF.
* Добавьте объект спецификации файла в коллекцию встроенных файлов документа. Имя файла должно соответствовать стандарту ZUGFeRD, например, "factor-x.xml".
* Преобразуйте документ в формат PDF/A-3U, подмножество PDF, которое обеспечивает долгосрочное сохранение электронных документов. PDF/A-3U позволяет встраивать файлы любого формата в PDF-документы.
* Сохраните преобразованный документ как новый PDF-файл (например, "ZUGFeRD-res.pdf").
* Закройте блок try-with-resources и освободите объект Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Метаданные счета, соответствующие стандарту ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Добавьте вложение в коллекцию вложений документа
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```
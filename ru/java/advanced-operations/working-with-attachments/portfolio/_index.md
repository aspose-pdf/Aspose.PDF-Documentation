---
title: Работа с портфолио в PDF-документах
linktitle: Портфолио
type: docs
weight: 40
url: ru/java/portfolio/
description: Как создать PDF-портфолио с помощью Java. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Сначала давайте разберемся, **Что такое формат файла PDF-портфолио?**

Например, возьмем файл PDF-портфолио, который содержит Word, Excel, презентации PowerPoint и т.д., в качестве вложений. Здесь каждый из вложенных файлов сохраняет свой исходный формат документа, но встроен или собран в один файл PDF-портфолио. Вы можете, конечно, открывать, читать или редактировать каждый отдельный файл PDF-портфолио так, как если бы он находился на диске или в папке. Кроме того, как и в обычном PDF-документе, вы также можете применять водяные знаки, устанавливать пароли и параметры безопасности, такие как возможность просмотра, печати или внесения изменений во вложения PDF-портфолио.

Мы можем разместить или собрать исходные файлы в их оригинальном виде или формате в качестве вложений в файл PDF-портфолио.

## Как создать PDF-портфолио

Aspose.PDF позволяет создавать PDF-портфолио с использованием класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Добавьте файл в объект Document.Collection после его получения с помощью класса [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Когда файлы добавлены, используйте метод Save класса Document, чтобы сохранить документ портфолио.

Следующий пример использует файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.

Код ниже приводит к созданию следующего портфолио.

### PDF-портфолио, созданное с помощью Aspose.PDF

![PDF-портфолио, созданное с помощью Aspose.PDF для Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Создать экземпляр объекта Document
        Document pdfDocument = new Document();

        // Создать экземпляр объекта Collection
        pdfDocument.setCollection(new Collection());

        // Получить файлы для добавления в портфолио
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // Указать описание файлов
        excel.setDescription ("Файл Excel");
        word.setDescription ("Файл Word");
        image.setDescription ("Файл изображения");

        // Добавить файлы в коллекцию документов
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // Сохранить документ портфолио
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## Извлечение файлов из PDF портфолио

PDF Портфолио позволяют собрать контент из различных источников (например, PDF, Word, Excel, JPEG файлы) в один унифицированный контейнер. Оригинальные файлы сохраняют свою индивидуальность, но собираются в файл PDF Портфолио. Пользователи могут открывать, читать, редактировать и форматировать каждый компонент файла независимо от других компонент файлов.

Aspose.PDF позволяет создавать документы PDF Портфолио, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Он также предоставляет возможность извлекать файлы из PDF портфолио.

Следующий пример кода показывает шаги для извлечения файлов из PDF портфолио.

![Извлечение файлов из PDF портфолио](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // Открыть документ
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // Получить коллекцию встроенных файлов
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // Итерировать через отдельные файлы портфолио
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## Удаление файлов из PDF портфолио

Чтобы удалить/удалить файлы из PDF портфолио, попробуйте использовать следующие строки кода.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // Загрузить исходное PDF портфолио
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```
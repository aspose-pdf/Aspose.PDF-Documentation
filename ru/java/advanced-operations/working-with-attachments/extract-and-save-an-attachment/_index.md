---
title: Извлечение и сохранение вложения
linktitle: Извлечение и сохранение вложения
type: docs
weight: 20
url: /ru/java/extract-and-save-an-attachment/
description: Aspose.PDF для Java позволяет получить все вложения из PDF-документа. Также вы можете получить отдельное вложение из вашего документа.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение вложений из PDF-документа

С помощью Aspose.PDF можно получить все вложения из PDF-документа. Это полезно, когда вы хотите сохранить документы отдельно от PDF или если вам нужно удалить вложения из PDF.

Следующие фрагменты кода показывают, как получить все вложения из PDF-документа.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Открыть документ
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Получить конкретный встроенный файл
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Получить свойства файла
  System.out.printf("Имя: - " + fileSpecification.getName());
  System.out.printf("\nОписание: - " + fileSpecification.getDescription());
  System.out.printf("\nТип Mime: - " + fileSpecification.getMIMEType());
  // Получить вложение из PDF-файла
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Создать путь для файла из pdf
   file.getParentFile().mkdirs();
   // Создать и извлечь файл из pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Закрыть объект InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Закрыть объект Document
  pdfDocument.dispose();
        
    }

```


## Получить информацию о вложении

Как упоминалось в разделе [Получение вложений из PDF-документа](/pdf/ru/java/get-attachments-from-a-pdf-document/), информация о вложении содержится в объекте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), собранном с другими вложениями в коллекции EmbeddedFiles объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Объект [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) предоставляет методы, которые получают информацию о вложении, например:

- getName() – получает имя файла.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – получает описание файла.
- getMIMEType() – получает MIME-тип файла.
- getParams() – информация о параметрах файла, например, CheckSum, CreationDate, ModDate и Size.

Чтобы получить эти параметры, сначала убедитесь, что метод getParams() не возвращает null.

Либо переберите все вложения в коллекции EmbeddedFiles, используя цикл for, либо получите отдельное вложение, указав его индексное значение.
 Следующий фрагмент кода показывает, как получить информацию о конкретном вложении.

```java
    public static void GetAttachmentInformation() {
  // Открыть документ
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Получить конкретный встроенный файл
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Получить свойства файла
  System.out.println("Имя:-" + fileSpecification.getName());
  System.out.println("Описание:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // Проверить, содержит ли объект параметров параметры
  if (fileSpecification.getParams() != null) {
   System.out.println("Контрольная сумма:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Дата создания:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Дата изменения:- " + fileSpecification.getParams().getModDate());
   System.out.println("Размер:- " + fileSpecification.getParams().getSize());
  } 
```
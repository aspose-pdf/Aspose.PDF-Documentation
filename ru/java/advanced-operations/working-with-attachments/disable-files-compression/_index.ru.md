---
title: Отключение сжатия файлов при добавлении в качестве встроенных ресурсов
linktitle: Отключение сжатия файлов
type: docs
weight: 40
url: /java/disable-files-compression-when-adding-as-embedded-resources/
description: В этой статье объясняется, как отключить сжатие файлов при добавлении в качестве встроенных ресурсов
lastmod: "2021-06-05"
---

Класс [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) позволяет разработчикам добавлять вложения к PDF-документам. По умолчанию вложения сжаты. Мы обновили API, чтобы позволить разработчикам отключать сжатие при добавлении файлов в качестве встроенного ресурса. Это дает разработчикам больше контроля над обработкой файлов.

Для того чтобы разработчики могли управлять сжатием файлов, в класс [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) был добавлен метод [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-).
 Это свойство определяет, какое кодирование будет использоваться для сжатия файла. Метод принимает значение из перечисления [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding). Возможные значения - это [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None и [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Если кодирование установлено на [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, то вложение не сжимается. Кодирование по умолчанию - [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Следующий фрагмент кода показывает, как добавить вложение в PDF-документ.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // получить ссылку на исходный/входной файл
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // прочитать все содержимое из исходного файла в ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // создать экземпляр объекта Stream из содержимого ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // создать экземпляр объекта Document из экземпляра потока
  Document pdfDocument = new Document(is);
  // настроить новый файл для добавления в качестве вложения
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Пример текстового файла");
  // указать свойство Encoding, установив его в FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // добавить вложение в коллекцию вложений документа
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // сохранить новый вывод
  pdfDocument.save("output.pdf");
    }
```
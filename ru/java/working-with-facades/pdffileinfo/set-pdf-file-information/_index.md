---
title: Установить информацию о PDF-файле - фасады
type: docs
weight: 20
url: ru/java/set-pdf-information/
description: Этот раздел объясняет, как установить информацию о PDF-файле с использованием Aspose.PDF Facades и класса PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) позволяет установить специфичную для файла информацию PDF-документа. Вам необходимо создать объект класса [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) и затем установить различные специфичные для файла свойства, такие как Автор, Заголовок, Ключевые слова и Создатель и так далее. Наконец, сохраните обновленный PDF-файл, используя метод [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) объекта [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

Следующий фрагмент кода показывает, как установить информацию о PDF-файле.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Установить информацию о PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // Сохранить обновленный файл
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## Установить Мета Информацию

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) метод позволяет добавить любую информацию. В нашем примере мы добавили поле. Проверьте следующий фрагмент кода:

```java
   public static void SetMetaInfo()
    {
        // Создаем экземпляр объекта PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Установить новый пользовательский атрибут как мета информацию
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // Сохранить обновленный файл
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```
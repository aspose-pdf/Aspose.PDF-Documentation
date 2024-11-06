---
title: Получение информации о PDF-файле - фасады
type: docs
weight: 10
url: ru/java/get-pdf-information/
description: Этот раздел объясняет, как получить информацию о PDF-файле с помощью Aspose.PDF Facades, используя класс PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Чтобы получить информацию, специфичную для PDF-файла, необходимо создать объект класса [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). После этого вы можете получить значения отдельных свойств, таких как Тема, Заголовок, Ключевые слова и Создатель и т.д.

Следующий фрагмент кода показывает, как получить информацию о PDF-файле.

```java
public static void GetPdfInfo()
    {
        // Открыть документ
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Получить информацию о PDF
        System.out.println("Тема: " + fileInfo.getSubject());
        System.out.println("Заголовок: " + fileInfo.getTitle());
        System.out.println("Ключевые слова: " + fileInfo.getKeywords());
        System.out.println("Создатель: " + fileInfo.getCreator());
        System.out.println("Дата создания: " + fileInfo.getCreationDate());
        System.out.println("Дата изменения: " + fileInfo.getModDate());
        // Узнать, является ли это допустимым PDF и зашифрован ли он
        System.out.println("Является ли допустимым PDF: " + fileInfo.isPdfFile());
        System.out.println("Зашифрован ли: " + fileInfo.isEncrypted());

        System.out.println("Ширина страницы:" +fileInfo.getPageWidth(1));
    }
```


## Получить Мета Информацию

Для получения информации мы используем метод [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). С помощью 'Hashtable' мы получаем все возможные значения.

```java
public static void GetMetaInfo()
    {        
        // Создаем экземпляр объекта PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Извлекаем все существующие пользовательские атрибуты
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // получить ключ
            String key = enumerator.nextElement();  
            // вывести ключ и значение, соответствующее этому ключу
            System.out.println(key + ": " + hTable.get(key));
        }

        // Извлечь один пользовательский атрибут
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```
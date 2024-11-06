---
title: Извлечение шрифтов из PDF
linktitle: Извлечение шрифтов
type: docs
weight: 30
url: ru/java/extract-fonts-from-pdf/
description: Как извлечь шрифт из PDF с использованием Aspose.PDF для Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод `Document.IDocumentFontUtilities.getAllFonts()`, предоставляемый в классе Document. Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы получить все шрифты из существующего PDF-документа:

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // Путь к директории с документами.
    String filePath = "<... введите имя файла ...>";
    
    // Загрузить PDF-документ
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```
---
title: Convert PDF to text 
linktitle: Convert PDF to text
type: docs
weight: 120
url: ru/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: С помощью Aspose.PDF для Android через Java вы можете конвертировать весь PDF-документ в текстовый файл или конвертировать только страницу PDF в текстовый файл.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Конвертировать страницу PDF в текстовый файл

Вы можете конвертировать PDF-документ в TXT файл с помощью Aspose.PDF для Android через Java. Вы должны использовать метод Visit класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) для решения этой задачи.

Следующий фрагмент кода объясняет, как извлечь текст с определённых страниц.

```java
public void convertPDFPagesToTXT() {
        // Открыть документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Сохранить извлеченный текст в текстовом файле
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
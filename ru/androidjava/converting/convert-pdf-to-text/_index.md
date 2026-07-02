---
title: Преобразовать PDF в текст
linktitle: Преобразовать PDF в текст
type: docs
weight: 120
url: /ru/androidjava/convert-pdf-to-txt/
lastmod: "2026-07-01"
description: С помощью Aspose.PDF for Android via Java вы можете преобразовать весь документ PDF в текстовый файл или преобразовать только страницу PDF в текстовый файл.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Преобразовать страницу PDF в текстовый файл

Вы можете преобразовать документ PDF в файл TXT с помощью Aspose.PDF for Android via Java. Вам следует использовать метод Visit [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) класс для решения этой задачи.

Следующий фрагмент кода объясняет, как извлечь текст с определённых страниц.

```java
public void convertPDFPagesToTXT() {
        // Open document
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

        // Save the extracted text in text file
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


---
title: Convert Text to PDF
linktitle: Convert Text to PDF
type: docs
weight: 300
url: /ru/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Java позволяет конвертировать простой текстовый файл в PDF или конвертировать предварительно форматированный текстовый файл в PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java** предоставляет возможность конвертировать текстовые файлы в формат PDF. В этой статье мы демонстрируем, как легко и эффективно мы можем конвертировать текстовый файл в PDF, используя Aspose.PDF.

Когда вам нужно конвертировать текстовый файл в PDF, сначала прочитайте исходный текстовый файл в некотором ридере.
 Мы использовали StringBuilder для чтения содержимого текстового файла. Создайте объект Document и добавьте новую страницу в коллекцию Pages. Создайте новый объект TextFragment и передайте объект StringBuilder в его конструктор. Добавьте новый параграф в коллекцию Paragraphs, используя объект TextFragment, и сохраните полученный PDF-файл, используя метод Save класса Document.

## Конвертировать текстовый файл в PDF

```java
public void convertTXTtoPDF_Simple () {
        // Инициализировать объект документа

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // Создать объект Document, вызвав его пустой конструктор
        document=new Document();

        // Добавить новую страницу в коллекцию Pages документа
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать экземпляр TextFragment и передать текст из объекта reader в его
        // конструктор в качестве аргумента
        TextFragment text=new TextFragment(stringBuilder.toString());

        // Добавить новый текстовый параграф в коллекцию параграфов и передать объект
        // TextFragment
        page.getParagraphs().add(text);

        // Сохранить полученный PDF-файл
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## Преобразование предварительно отформатированного текстового файла в PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // Читать текстовый файл как массив строк
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Создать экземпляр объекта Document, используя его пустой конструктор
        document=new Document();

        // Добавить новую страницу в коллекцию страниц документа
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // Установить левые и правые поля для лучшего представления
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // проверить, содержит ли строка символ "подача формы"
            // см. https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Создать экземпляр TextFragment и
                // передать строку его
                // конструктору как аргумент
                TextFragment text=new TextFragment(line);

                // Добавить новый текстовый абзац в коллекцию абзацев и передать объект TextFragment
                page.getParagraphs().add(text);
            }
        }
        // Сохранить полученный PDF файл
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```
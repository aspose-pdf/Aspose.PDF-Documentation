---
title: Конвертировать PDF в PowerPoint
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 110
url: /ru/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF позволяет конвертировать PDF в формат PowerPoint. Один из способов - это возможность конвертировать PDF в PPTX с слайдами в виде изображений.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

У нас есть API под названием Aspose.Slides, который предлагает возможность создавать и управлять презентациями PPT/PPTX. Этот API также предоставляет возможность конвертировать файлы PPT/PPTX в формат PDF. В Aspose.PDF для Java мы внедрили функцию преобразования PDF документов в формат PPTX. Во время этого преобразования отдельные страницы PDF файла конвертируются в отдельные слайды в файле PPTX.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

During PDF to PPTX conversion, the text is rendered as Text where you can select/update it, instead of its rendered as an image. Please note that in order to convert PDF files to PPTX format, Aspose.PDF provides a class named PptxSaveOptions. An object of the [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) class is passed as a second argument to the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) method.

Во время преобразования PDF в PPTX текст отображается как текст, который вы можете выбрать/обновить, а не в виде изображения. Обратите внимание, что для преобразования PDF файлов в формат PPTX Aspose.PDF предоставляет класс с именем PptxSaveOptions. Объект класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) передается в качестве второго аргумента методу [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Check next code snippet to resolve your tasks with conversion PDF to PowerPoint format:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        // Загрузить PDF документ
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        // Создать объект опции сохранения Excel
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        // Сохранить вывод в формате PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            // Сохранить файл в формате PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
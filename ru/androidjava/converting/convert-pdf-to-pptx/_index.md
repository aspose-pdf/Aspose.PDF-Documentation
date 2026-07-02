---
title: Конвертировать PDF в PowerPoint
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 110
url: /ru/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF позволяет конвертировать PDF в формат PowerPoint. Есть возможность конвертировать PDF в PPTX с слайдами в виде изображений.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

У нас есть API под названием Aspose.Slides, который предоставляет возможность создавать и редактировать презентации PPT/PPTX. Этот API также позволяет конвертировать файлы PPT/PPTX в формат PDF. В Aspose.PDF for Java мы внедрили функцию преобразования PDF‑документов в формат PPTX. При этой конвертации отдельные страницы PDF‑файла преобразуются в отдельные слайды в файле PPTX.

{{% alert color="primary" %}}

Попробуйте онлайн. Вы можете проверить качество конвертации Aspose.PDF и просмотреть результаты онлайн по этой ссылке [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Во время конвертации PDF в PPTX текст отображается как Text, который можно выделять/обновлять, вместо того чтобы он отображался как изображение. Обратите внимание, что для конвертации PDF‑файлов в формат PPTX Aspose.PDF предоставляет класс с именем PptxSaveOptions. Объект этого [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) класс передаётся в качестве второго аргумента [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) метод.

Посмотрите следующий фрагмент кода, чтобы решить ваши задачи по преобразованию PDF в формат PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


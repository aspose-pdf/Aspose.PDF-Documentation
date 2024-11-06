---
title: Преобразование DICOM в PDF
linktitle: Преобразование DICOM в PDF
type: docs
weight: 250
url: ru/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Преобразование медицинских изображений, сохраненных в формате DICOM, в PDF файл с использованием Aspose.PDF для Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Цифровая обработка и коммуникации в медицине">DICOM</abbr> — это стандарт для обработки, хранения, печати и передачи информации в медицинской визуализации. Он включает определение формата файла и протокол сетевой связи.

Aspose.PDF для Java позволяет преобразовывать файлы DICOM в формат PDF, ознакомьтесь со следующим фрагментом кода:

1. Загрузите изображение в поток
1. Инициализируйте [`объект Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Загрузите образец файла изображения DICOM
1. Сохраните выходной PDF документ

```java
//    Преобразование DICOM в PDF
    public void convertDICOMtoPDF () {
        // Инициализируйте объект документа
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Загрузите образец файла изображения BMP
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Сохраните выходной документ
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
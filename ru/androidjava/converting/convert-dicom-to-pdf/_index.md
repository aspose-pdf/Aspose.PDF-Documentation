---
title: Конвертировать DICOM в PDF
linktitle: Конвертировать DICOM в PDF
type: docs
weight: 250
url: /ru/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: Конвертировать медицинские изображения, сохранённые в формате DICOM, в файл PDF с использованием Aspose.PDF for Android через Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> является стандартом для обработки, хранения, печати и передачи информации в медицинской визуализации. Он включает определение формата файлов и сетевой протокол коммуникаций.

Aspsoe.PDF for Java позволяет конвертировать файлы DICOM в формат PDF, проверьте следующий фрагмент кода:

1. Загрузите изображение в поток
1. Инициализировать [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Загрузите пример файла изображения DICOM
1. Сохраните выходной PDF‑документ

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
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

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```



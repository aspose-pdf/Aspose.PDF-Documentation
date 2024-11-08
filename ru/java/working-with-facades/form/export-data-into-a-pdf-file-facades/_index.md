---
title: Экспорт данных в XML из PDF файла (Facades)
type: docs
weight: 20
url: /ru/java/export-data-into-a-pdf-file-facades/
description: Этот раздел объясняет, как экспортировать данные в XML из PDF файла с использованием Aspose.PDF Facades и класса Form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Класс [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) позволяет экспортировать данные в XML файл из PDF файла, используя метод exportXml. Чтобы экспортировать данные в XML, необходимо создать объект класса [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form), открыть исходную PDF форму, используя метод bindPDF, и затем вызвать метод exportXml, используя объект OutputStream. В конце вы можете закрыть объект OutputStream и освободить объект Form. Следующий фрагмент кода показывает, как экспортировать данные в XML файл.


{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}
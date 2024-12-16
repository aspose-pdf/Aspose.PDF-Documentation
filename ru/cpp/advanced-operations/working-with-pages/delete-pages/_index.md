---
title: Программное удаление страниц PDF
linktitle: Удаление страниц PDF
type: docs
weight: 30
url: /ru/cpp/delete-pages/
description: Вы можете удалить страницы из вашего PDF файла, используя библиотеку C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалить страницы из файла PDF, используя Aspose.PDF для C++. Чтобы удалить определенную страницу из коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## Удаление страницы из PDF файла

1. Вызовите метод [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) и укажите индекс страницы
1. Вызовите метод Save, чтобы сохранить обновленный PDF файл
Следующий фрагмент кода показывает, как удалить определенную страницу из файла PDF, используя C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Удалить определенную страницу
    document->get_Pages()->Delete(2);

    // Сохранить обновленный PDF
    document->Save(_dataDir + inputFileName);
}
```
---
title: Управление подписями
linktitle: Управление подписями
type: docs
weight: 80
url: /java/signature-management/
description: Узнайте, как удалить существующую подпись PDF в Java с помощью фасада PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить подписи PDF в Java
Abstract: Узнайте, как удалить подпись из подписанного PDF-файла с помощью Aspose.PDF для Java. Текущий набор примеров Java охватывает удаление существующей подписи по имени и сохранение обновленного документа. Он не включает отдельный образец для очистки связанного поля подписи.
---
## Удалите подпись

Используйте этот рабочий процесс, если из документа необходимо удалить существующую цифровую подпись.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите подписанный PDF-файл.
2. Прочтите коллекцию подписей и выберите имя подписи.
3. Позвоните `removeSignature` с этим именем.
4. Сохраните обновленный файл и закройте объект фасада.

### Пример Java

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

Текущий набор примеров Java не включает отдельный метод для удаления связанного поля подписи после удаления подписи.

---
title: Управление подписями
linktitle: Управление подписями
type: docs
weight: 80
url: /ru/java/signature-management/
description: Узнайте, как удалить существующую подпись PDF в Java с помощью фасада PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить подписи PDF в Java
Abstract: Узнайте, как удалить подпись из подписанного PDF с помощью Aspose.PDF for Java. Текущий набор примеров Java охватывает удаление существующей подписи по имени и сохранение обновленного документа. Он не включает отдельный пример для очистки связанного поля подписи.
---
## Удалите подпись

Используйте этот рабочий процесс, когда необходимо удалить существующую цифровую подпись из документа.

### Шаги

1. Создайте `PdfFileSignature` создать экземпляр и привязать подписанный PDF.
2. Прочитайте коллекцию подписей и выберите имя подписи.
3. Вызовите `removeSignature` с таким именем.
4. Сохраните обновлённый файл и закройте объект фасада.

### Пример на Java

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



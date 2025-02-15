---
title: Как создать PDF-портфолио
type: docs
weight: 10
url: /ru/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

PDF-портфолио позволяет объединить контент из различных источников (например, PDF, Word, Excel, JPEG файлы) в один единый контейнер. Оригинальные файлы сохраняют свою индивидуальность, но собираются в файл PDF-портфолио. Пользователи могут открывать, читать, редактировать и форматировать каждый компонентный файл независимо от других компонентных файлов.

Aspose.PDF для Java позволяет создавать PDF-портфолио, используя класс Document. Загрузите отдельный файл в объект FileSpecification и добавьте его в объект Document.Collection, используя метод add(...). После добавления файлов используйте метод save(..) класса Document для генерации документа портфолио.

{{% /alert %}}

## Пример кода

Следующий пример использует файл Microsoft XPS, документ Word, PDF и изображение для создания PDF-портфолио.


**PDF-портфолио, созданное с помощью Aspose.PDF**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "СоздатьPDFПортфолио.java" >}}
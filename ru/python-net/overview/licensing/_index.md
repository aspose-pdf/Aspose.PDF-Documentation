---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /ru/python-net/licensing/
description: Aspose. PDF для Python приглашает своих клиентов получить классическую лицензию. Также используйте ограниченную лицензию для более детального изучения продукта.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ограничения пробной версии

Мы хотим, чтобы наши клиенты тщательно протестировали наши компоненты перед покупкой, поэтому пробная версия позволяет использовать их, как обычно.

- **PDF, созданный с водяным знаком пробной версии.** Пробная версия Aspose.PDF для Python предоставляет полную функциональность продукта, но все страницы в сгенерированных PDF-документах помечены водяным знаком "Только для оценки. Создано с помощью Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" вверху.

>Если вы хотите протестировать Aspose.PDF без ограничений пробной версии, вы также можете запросить временную лицензию на 30 дней.
 Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Лицензию можно загрузить из файла или объекта потока. Самый простой способ установить лицензию — поместить файл лицензии в ту же папку, что и файл Aspose.PDF.dll, и указать имя файла без пути, как показано в примере ниже.

Если вы используете любой другой компонент Aspose для Python вместе с Aspose.PDF для Python, пожалуйста, укажите пространство имен для License, как [класс Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```